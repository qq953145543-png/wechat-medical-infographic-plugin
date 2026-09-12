# Copy and WeChat publishing

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
└── images/
    ├── 01.png
    ├── 02.png
    ├── 03.png
    ├── 04.png
    ├── 05.png
    └── 06.png
```

Use the first image as the visual cover when a cover is required. Keep the six captions intact in article mode; do not use WeChat's short image-text/贴图 mode because six captions of about 300 characters exceed its 1000-character content limit.

## One-click WeChat draft import

Treat “复制图文到公众号”, “一键导入公众号”, and “发布公众号” as requests to use `$baoyu-post-to-wechat` with the assembled `article.md`.

1. Prefer the browser method for learners because it does not require an AppID/AppSecret.
2. On first use, follow `$baoyu-post-to-wechat` first-time setup and select `browser` as the default publishing method unless the user explicitly prefers API.
3. Open Chrome through the publisher workflow and let the user scan the WeChat Official Account QR code when required.
4. Import the complete Markdown article with all six inline images.
5. Save to the Official Account draft box by default.
6. Report success only after the editor or script confirms that the draft was saved.
7. Require explicit user confirmation before any live publication or mass send.

If `$baoyu-post-to-wechat` is unavailable, ask the user to install it with `$skill-installer` from:

```text
https://github.com/JimLiu/baoyu-skills/tree/main/skills/baoyu-post-to-wechat
```

Do not claim one-click import is available until that dependency is installed and its first-time setup is complete.
