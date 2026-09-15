# Copy and local WeChat preview

## Caption standard

Write one caption immediately after each image passes quality checks.

- Length: `260–340` Chinese characters, aiming for about `300`.
- Heading: repeat the exact numbered page title.
- Opening: use one relatable patient concern or concise takeaway.
- Explanation: add useful context that complements the image instead of copying its cards word for word.
- Action: give 2–4 specific, safe things the reader can do.
- Closing: use a calm reminder, follow-up cue, or natural reader interaction question.
- Tone: warm, credible, plain-language, non-alarmist, suitable for a hospital or clinician-run WeChat account.
- Accuracy: keep thresholds, units, red flags, medication claims, and treatment advice aligned with the verified sources used for the image.
- Avoid hashtags, exaggerated promises, clickbait, sales language, individualized diagnosis, and instructions to change prescription treatment independently.

Count Chinese punctuation as characters only approximately; prioritize a natural `260–340`-character paragraph over an exact mechanical count.

## Article assembly

Create one Markdown file with this order:

```markdown
---
title: 系列主题
description: 80–120字系列摘要
---

# 系列主题

简短导语

## 01｜第一页标题

![01｜第一页标题](images/01.png)

约300字文案

... repeat through 06 ...
```

Save the package as:

```text
outputs/<topic-slug>-wechat-series/
├── article.md
├── wechat-preview.html
└── images/
    ├── 01.png
    ├── 02.png
    ├── 03.png
    ├── 04.png
    ├── 05.png
    └── 06.png
```

Use the first image as the visual cover when a cover is required. Keep the six captions intact in article mode; do not use WeChat's short image-text/贴图 mode because six captions of about 300 characters exceed its 1000-character content limit.

## Standalone rich-text preview

Treat “复制图文到公众号”, “一键复制公众号排版”, and similar wording as a request to build a local preview, not as authorization to control the WeChat backend.

Run from the skill directory:

```text
python3 scripts/build_wechat_preview.py /absolute/path/article.md /absolute/path/wechat-preview.html
```

The generated file must use the “摸鱼绿编号章节版” layout:

- White article surface, deep-brown headings, muted fishing-green accents, pale-green dividers, rounded image cards, and continuous `PART 01` to `PART 06` chapter labels.
- Every body image is a standard `<img>` element whose `src` is a complete `data:image/...;base64,...` URL.
- No CSS background image, `blob:`, `file://`, relative image path, or temporary remote image is allowed in the final HTML.
- All copyable content is inside `#output` and uses inline styles so rich-text paste retains as much formatting as possible.
- The `复制排版正文（含图片）` button begins disabled and becomes available only after every embedded image is loaded and decoded.
- Copy the rich HTML DOM from `#output` together with its images. Never implement a text-only copy action.

## Completion check and handoff

The script must report these three values separately and they must match exactly:

1. Markdown image count;
2. HTML `<img>` count;
3. successfully embedded `data:` image count.

Do not report the preview as ready if any count differs or any image cannot be decoded. At completion, show the article summary, core points, human-confirmation items, reference overview, numbered image list, image-verification result, and absolute paths for all files.

Only create the local preview. Never log in, publish, mass-send, or save a WeChat draft. Tell the learner to open `wechat-preview.html`, wait until the button becomes available, click it, paste into the Official Account editor, visually confirm all images, and save the draft themselves.
