# Series specification

## Visual identity

- Canvas: portrait 2:3, matching the retained references (1024 × 1536 when supported).
- Background: warm white with generous breathing room.
- Primary colors: deep medical blue and cobalt; use coral red for critical words and numbers, pale sky blue for outlines, soft pink for warning cards, mint/cyan as a small secondary accent, and yellow for attention rays.
- Type: bold rounded Chinese display lettering for the headline; compact heavy sans-serif Chinese for body copy. Use dark blue body text and red only for emphasis.
- Rendering: polished cute medical infographic, soft anime/chibi illustration, clean vector-like edges, gentle highlights and shadows, no photorealism.
- Shapes: rounded cards, thin blue borders, speech bubbles, numbered circles, clipboard/heart icons, short handwritten corner slogans, and small doodle marks.

## Locked recurring elements

Keep these elements visually consistent on every page:

1. Top-left rounded series badge containing the short topic label and a pink heartbeat/heart motif.
2. Blue circular page badge with a white two-digit number.
3. Oversized two-line headline centered at the top, mostly deep blue with one coral-red key phrase, pale blue outer stroke, and small yellow attention rays.
4. Upper-right blue handwritten micro-slogan with a pink heart and underline flourish.
5. Hero consultation panel in a softly blurred clinic: patient on the left, nurse on the right, two readable speech bubbles.
6. Patient: young adult woman, long wavy chestnut-brown hair, large brown eyes, pink long-sleeve top, friendly expressive face.
7. Nurse educator: adult woman, black hair in a low bun, black-rim glasses, white nurse cap, purple scrubs, ID badge, clipboard, warm confident expression.
8. Bottom-left clipboard/heart mark reading `知安有护`, with small teal leaves when space allows.
9. One-line footer takeaway with one coral-red emphasized phrase and a small handwritten encouragement at right.

Do not redesign or swap the two main characters between pages. Keep facial features, hair, clothing colors, and proportions stable; vary natural gestures and relevant props.

## Page anatomy

Use this vertical hierarchy:

- Header: about 14% of height.
- Hero consultation: about 23%.
- Primary teaching module: about 25–32%.
- Secondary caution/takeaway module: about 18–25%.
- Footer: about 8–10%.

Select teaching modules by content rather than using every module on every page:

- definition or threshold: comparison table with 3–4 rows plus a small device illustration;
- technique or process: 4–5 numbered step cards;
- misconception: myth/fact or wrong/right paired cards;
- lifestyle: 4–6 compact behavior cards with icons;
- warning signs: severity ladder or routine/urgent/emergency grouping;
- final checklist: two clear columns, green-blue `该做` and coral-pink `不该做`, 4–6 matched items per side.

## Copy limits

- Series badge: preferably 4–10 Chinese characters over one or two lines.
- Main headline: preferably 8–16 Chinese characters, split into two lines.
- Hero speech bubbles: 35–70 Chinese characters each, conversational and non-redundant.
- Card heading: 4–10 Chinese characters.
- Card body: 18–45 Chinese characters, usually no more than three short lines.
- Footer: 24–45 Chinese characters.
- Use Arabic numerals and standard clinical units. Do not compress so much text that legibility depends on tiny type.

## Title quality bar

Titles must sound like real patient questions, answer different intents, and form a learning arc. For a topic similar to hypertension, a good shape is:

1. What counts as the condition?
2. How do I measure or assess it correctly?
3. Can treatment be stopped or changed casually?
4. What should daily management look like?
5. Which signs require prompt care?
6. What should and should not be done?

Adapt the structure to the topic. For example, a surgical-recovery topic may use preparation, immediate recovery, pain/wound care, activity/diet, red flags, and a checklist. Do not reuse hypertension-specific facts or modules when irrelevant.

## Image-generation brief pattern

For each page, provide ImageGen with:

- the page number, exact series badge, exact headline, and all required Chinese copy;
- the locked character descriptions and the instruction to match the retained references;
- the selected page anatomy and teaching module;
- the exact palette and portrait aspect ratio;
- the instruction that every Chinese character, number, unit, and label must be legible and copied exactly;
- a short negative list: no extra characters, no duplicate limbs, no garbled text, no incorrect medical-device placement, no watermarks, no QR codes, no English filler.

Generate one page per call. Do not ask for a six-page contact sheet.
