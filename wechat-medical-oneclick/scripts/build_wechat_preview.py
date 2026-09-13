#!/usr/bin/env python3
"""Build a standalone WeChat preview with inline-styled HTML and embedded images."""

from __future__ import annotations

import argparse
import base64
import html
import mimetypes
import re
from pathlib import Path


COLORS = {
    "brown": "#4A2A1A",
    "green": "#5F8F74",
    "light": "#DCEBD8",
    "cream": "#FFF9ED",
    "orange": "#EF8B45",
}


def strip_frontmatter(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---\n", 4)
    if end < 0:
        return {}, text
    meta: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            meta[key.strip()] = value.strip().strip('"\'')
    return meta, text[end + 5 :]


def inline_markup(text: str) -> str:
    tokens: list[str] = []

    def stash(value: str) -> str:
        tokens.append(value)
        return f"@@TOKEN{len(tokens)-1}@@"

    text = re.sub(
        r"\[([^\]]+)\]\((https?://[^)]+)\)",
        lambda m: stash(
            f'<a href="{html.escape(m.group(2), quote=True)}" '
            f'style="color:{COLORS["green"]};text-decoration:underline;">'
            f'{html.escape(m.group(1))}</a>'
        ),
        text,
    )
    escaped = html.escape(text)
    escaped = re.sub(
        r"\*\*(.+?)\*\*",
        rf'<strong style="color:{COLORS["orange"]};font-weight:700;">\1</strong>',
        escaped,
    )
    escaped = re.sub(r"`([^`]+)`", r"<code>\1</code>", escaped)
    for index, token in enumerate(tokens):
        escaped = escaped.replace(f"@@TOKEN{index}@@", token)
    return escaped


def embed_image(src: str, article_dir: Path) -> str:
    if src.startswith(("data:", "http://", "https://", "blob:", "file://")):
        if src.startswith("data:"):
            return src
        raise ValueError(f"图片必须是可内嵌的本地文件，发现不允许的地址：{src}")
    image_path = (article_dir / src).resolve()
    if not image_path.is_file():
        raise FileNotFoundError(f"图片不存在：{image_path}")
    mime = mimetypes.guess_type(image_path.name)[0] or "image/png"
    payload = base64.b64encode(image_path.read_bytes()).decode("ascii")
    return f"data:{mime};base64,{payload}"


def render_markdown(body: str, article_dir: Path) -> tuple[str, int, int]:
    lines = body.splitlines()
    output: list[str] = []
    paragraph: list[str] = []
    list_items: list[str] = []
    ordered = False
    image_count = 0
    part_count = 0

    def flush_paragraph() -> None:
        if paragraph:
            content = inline_markup(" ".join(item.strip() for item in paragraph))
            output.append(
                f'<p style="margin:0 0 1.05em;color:#3F352F;font-size:16px;line-height:1.9;letter-spacing:.02em;">{content}</p>'
            )
            paragraph.clear()

    def flush_list() -> None:
        nonlocal ordered
        if list_items:
            tag = "ol" if ordered else "ul"
            output.append(
                f'<{tag} style="margin:.2em 0 1.1em;padding-left:1.45em;color:#3F352F;font-size:16px;line-height:1.85;">'
                + "".join(f'<li style="margin:.35em 0;">{inline_markup(item)}</li>' for item in list_items)
                + f"</{tag}>"
            )
            list_items.clear()
            ordered = False

    for raw in lines + [""]:
        line = raw.rstrip()
        image_match = re.fullmatch(r"\s*!\[([^\]]*)\]\(([^)]+)\)\s*", line)
        heading = re.match(r"^(#{2,4})\s+(.+)$", line)
        bullet = re.match(r"^\s*[-*+]\s+(.+)$", line)
        number = re.match(r"^\s*\d+[.)]\s+(.+)$", line)
        if image_match:
            flush_paragraph(); flush_list()
            image_count += 1
            alt, src = image_match.groups()
            data_uri = embed_image(src.strip(), article_dir)
            output.append(
                f'<figure style="margin:1.35em 0;padding:10px;background:{COLORS["light"]};border-radius:18px;">'
                f'<img src="{data_uri}" alt="{html.escape(alt, quote=True)}" '
                'style="display:block;width:100%;height:auto;border-radius:12px;" /></figure>'
            )
        elif heading:
            flush_paragraph(); flush_list()
            level, label = len(heading.group(1)), inline_markup(heading.group(2))
            if level == 2:
                part_count += 1
                output.append(
                    f'<section style="margin:2.4em 0 1.15em;border-top:2px solid {COLORS["light"]};padding-top:1.25em;">'
                    f'<span style="display:inline-block;color:{COLORS["green"]};font-size:12px;font-weight:700;letter-spacing:.14em;">PART {part_count:02d}</span>'
                    f'<h2 style="margin:.35em 0 0;color:{COLORS["brown"]};font-size:24px;line-height:1.35;">{label}</h2></section>'
                )
            else:
                size = 20 if level == 3 else 17
                output.append(f'<h{level} style="margin:1.65em 0 .75em;color:{COLORS["brown"]};font-size:{size}px;line-height:1.45;">{label}</h{level}>')
        elif bullet or number:
            flush_paragraph()
            desired_ordered = bool(number)
            if list_items and desired_ordered != ordered:
                flush_list()
            ordered = desired_ordered
            list_items.append((number or bullet).group(1))
        elif line.startswith("> "):
            flush_paragraph(); flush_list()
            output.append(
                f'<blockquote style="margin:1em 0;padding:.9em 1em;border-left:4px solid {COLORS["green"]};background:{COLORS["cream"]};color:{COLORS["brown"]};line-height:1.8;">{inline_markup(line[2:])}</blockquote>'
            )
        elif not line.strip():
            flush_paragraph(); flush_list()
        elif line.strip() == "---":
            flush_paragraph(); flush_list()
            output.append(f'<hr style="border:0;border-top:1px solid {COLORS["light"]};margin:2em 0;" />')
        elif line.startswith("# "):
            # H1 is metadata/title in WeChat and is intentionally outside #output.
            continue
        else:
            paragraph.append(line)
    return "\n".join(output), image_count, part_count


def build(input_path: Path, output_path: Path) -> tuple[int, int]:
    meta, body = strip_frontmatter(input_path.read_text(encoding="utf-8"))
    rendered, image_count, part_count = render_markdown(body, input_path.parent)
    title = html.escape(meta.get("title", input_path.stem))
    doc = f'''<!doctype html>
<html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title></head>
<body style="margin:0;background:#F3F1EC;font-family:-apple-system,BlinkMacSystemFont,'PingFang SC','Microsoft YaHei',sans-serif;">
<div style="position:sticky;top:0;z-index:9;padding:12px;background:#F3F1EC;border-bottom:1px solid #DDD5C9;text-align:center;">
  <button id="copyButton" disabled style="border:0;border-radius:999px;padding:12px 20px;background:{COLORS['green']};color:white;font-size:15px;font-weight:700;cursor:pointer;">图片加载中…</button>
  <div id="copyStatus" style="margin-top:7px;color:#655A52;font-size:12px;">预期图片 {image_count} 张</div>
</div>
<main style="max-width:677px;margin:18px auto;padding:0 12px;">
<article id="output" style="box-sizing:border-box;background:white;padding:26px 22px 34px;box-shadow:0 8px 28px rgba(74,42,26,.08);">{rendered}</article>
</main>
<script>
const output = document.getElementById('output');
const button = document.getElementById('copyButton');
const status = document.getElementById('copyStatus');
const expected = {image_count};
async function ready() {{
  const imgs = [...output.querySelectorAll('img')];
  await Promise.all(imgs.map(img => img.complete ? Promise.resolve() : new Promise((resolve,reject) => {{ img.onload=resolve; img.onerror=reject; }})));
  const loaded = imgs.filter(img => img.complete && img.naturalWidth > 0).length;
  if (loaded !== expected) {{ status.textContent = `图片校验失败：${{loaded}}/${{expected}}`; return; }}
  button.disabled = false; button.textContent = '复制排版正文（含图片）';
  status.textContent = `已加载并内嵌 ${{loaded}} 张图片，可复制富文本`;
}}
async function copyRich() {{
  if (button.disabled) return;
  const selection = window.getSelection();
  const range = document.createRange(); range.selectNodeContents(output);
  selection.removeAllRanges(); selection.addRange(range);
  let ok = false;
  try {{ ok = document.execCommand('copy'); }} catch (_) {{}}
  selection.removeAllRanges();
  if (!ok && navigator.clipboard && window.ClipboardItem) {{
    const rich = '<meta charset="utf-8">' + output.outerHTML;
    await navigator.clipboard.write([new ClipboardItem({{
      'text/html': new Blob([rich], {{type:'text/html'}}),
      'text/plain': new Blob([output.innerText], {{type:'text/plain'}})
    }})]); ok = true;
  }}
  if (!ok) throw new Error('浏览器拒绝富文本剪贴板权限');
  button.textContent = '已复制（含图片）';
  status.textContent = `剪贴板已写入富文本，包含 ${{expected}} 个内嵌 <img>；粘贴后请核对图片数量再保存草稿`;
  setTimeout(() => button.textContent = '复制排版正文（含图片）', 2200);
}}
button.addEventListener('click', () => copyRich().catch(err => status.textContent = '复制失败：' + err.message));
ready().catch(() => status.textContent = '图片解码失败，不能复制');
</script></body></html>'''
    output_path.write_text(doc, encoding="utf-8")
    embedded = len(re.findall(r'<img\s[^>]*src="data:image/', doc))
    if embedded != image_count:
        raise RuntimeError(f"图片内嵌数量不一致：Markdown={image_count}, HTML={embedded}")
    return image_count, part_count


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    images, parts = build(args.input.resolve(), args.output.resolve())
    print(f"OK images={images} embedded={images} parts={parts} output={args.output.resolve()}")


if __name__ == "__main__":
    main()
