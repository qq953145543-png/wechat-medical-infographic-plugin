---
name: wechat-medical-oneclick
description: 一键制作中文微信公众号医学科普图文：检索并核对最新权威指南，撰写和格式化文章，使用固定女性医护角色一次性生成全部 6～8 张竖版配图，并输出图片内嵌、可富文本复制到微信公众号编辑器的单文件 HTML。用户要求“一键写公众号医学文章”“医学科普配图”“直接生成全部图片”“可复制到公众号草稿箱”或调用 $wechat-medical-oneclick 时使用。
---

# 医学公众号图文一键生成

## 核心规则

- 将当前调用视为对完整流程的授权：文章、格式化、全部配图和本地预览一次完成，不在封面后停顿，不逐张请求确认。
- 仅在缺少主题、指定参考图不可读取或存在会实质改变医学结论的歧义时询问。
- 不发布、不群发，也不替用户点击微信后台的发布按钮。
- 使用 `$baoyu-format-markdown` 整理结构，使用 `$baoyu-article-illustrator` 规划和生成配图，使用 `$baoyu-post-to-wechat` 的排版原则制作本地预览。
- 读取 [references/workflow.md](references/workflow.md) 并完整执行。

## 固定角色与视觉资产

首次使用时先运行：

```bash
python3 scripts/materialize_asset.py
```

该脚本把随技能下载的 `assets/female-clinician-reference.jpg.b64` 还原为 `assets/female-clinician-reference.jpg`。把还原后的 JPG 作为每次出图的直接人物与风格参考，复制到文章目录 `references/female-clinician-reference.jpg`，所有相关提示词通过 `referenced_image_paths` 传入该文件。

固定特征：亲切的中国女性医护科普角色、圆润大眼睛、墨绿色猫咪图案手术帽、青绿色医用口罩、墨绿色手术服、白色医用手套、深色夹板、柔和手绘线条。背景使用奶油色，主字深棕色，重点橙色，辅助浅绿色。

不要写成紫色手术帽或浅蓝色口罩。不要改变人物年龄、性别、民族特征、帽子图案或主要服装颜色。内容不需要人物时仍保持相同画风和色板。

## 输出

在独立文章目录中至少保存：

- `article-raw.md`
- `article-analysis.md`
- `article-formatted.md`
- `article-illustrated.md`
- `imgs/outline.md`
- `imgs/prompts/NN-{type}-{slug}.md`
- `imgs/01-cover.png` 至全部配图
- `wechat-preview.html`
- `medical-review.md`

使用 `scripts/build_wechat_preview.py` 从插图后的 Markdown 生成最终预览：

```bash
python3 scripts/build_wechat_preview.py article-illustrated.md wechat-preview.html
```

只有在脚本报告全部图片成功内嵌、HTML 中图片数与 Markdown 图片数一致、二级标题与 PART 编号一致后，才能报告完成。
