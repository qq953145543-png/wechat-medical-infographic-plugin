---
name: artifact-template-wechat
description: "Create a six-image Chinese WeChat medical-education series using the WeChat 公众号医学科普系列长图 template and its retained references. Use when the user supplies a health-series topic such as 高血压健康知识大全, asks for 公众号医学科普配图/长图/系列海报, selects WeChat 公众号医学科普系列长图, or explicitly invokes $artifact-template-wechat. First plan five progressive question titles plus a sixth 做／不做 checklist, then generate all six coherent portrait infographics."
---

# WeChat 公众号医学科普系列长图

Turn one Chinese health topic into a complete six-image WeChat series. Do not stop after proposing titles unless the user asks to approve them first.

## Required references

1. Read `artifact-template.json` and resolve all paths relative to this skill directory.
2. Read `references/series-spec.md` completely before planning or generating.
3. Use `assets/reference.png` as the primary composition reference and `assets/reference-data-cards.png` as the secondary reference for definition tables and caution cards. Keep both files unchanged.

## Workflow

1. Normalize the user's topic into a short series label, retaining their wording when it is already concise.
2. Verify medical facts before drafting. Prefer current Chinese health-authority or professional-society guidance; use WHO or another primary authority when appropriate. If region changes thresholds or emergency advice and the user did not specify one, default to mainland China and state that assumption outside the images.
3. Plan exactly six pages:
   - `01` basic definition, threshold, mechanism, or the first question a patient asks;
   - `02` correct self-check, measurement, preparation, or practical technique;
   - `03` treatment, medication, procedure, or a high-risk misconception;
   - `04` daily behavior, diet, exercise, sleep, or recovery management;
   - `05` warning signs, escalation, follow-up, or when to seek care;
   - `06` topic-specific “该做／不该做” checklist.
4. Write five concise question-style titles plus the sixth checklist title. Use `01｜标题` through `06｜标题`. Avoid overlap and make the sequence progress from understanding to action and safety.
5. Present the six-title plan briefly in commentary, then continue automatically unless the user requested approval.
6. Draft each page's factual copy before image generation. Keep copy short enough for legible Chinese type: one hero dialogue exchange, one main teaching block, one caution or takeaway block, and one footer sentence. Prefer 3–5 cards or steps per block.
7. Invoke `$imagegen` six times, one page at a time, using both retained PNGs as references. Generate portrait `2:3` images matching the reference dimensions and visual system. Use the completed prior page as an additional continuity reference when it has a local path.
8. Keep the same patient, nurse, clothing, series badge, palette, corner doodles, border radius, and footer mark across all six pages. Change only poses, props, expressions, copy, and the page-specific teaching modules.
9. Inspect every image at original detail. Check Chinese text, numbers, units, anatomy, hands, medical devices, page number, series title, and character continuity. Regenerate a page when a clinically meaningful statement, number, title, or label is wrong or unreadable.
10. Return all six images in numerical order, followed by a compact note listing the medical sources used and any regional assumption. Do not put URLs or dense citations inside the artwork.

## Safety and content rules

- Use patient-friendly education, not individualized diagnosis or treatment.
- Never invent thresholds, dosages, contraindications, emergency criteria, or guaranteed outcomes.
- Do not tell readers to start, stop, or change prescription treatment without clinician guidance.
- Distinguish routine follow-up from urgent and emergency care; use direct, calm wording.
- When evidence or guidelines genuinely differ, avoid false precision and say the recommendation depends on the reader's clinical context.
- Preserve the user's requested scope, but replace unsafe wording with a medically sound formulation and explain the adjustment outside the image.

## Output standard

The set is incomplete until all six pages exist and pass visual and medical checks. Preserve the reference's overall composition and visual hierarchy while adapting card types to the topic; do not mechanically force a blood-pressure table into unrelated topics.
