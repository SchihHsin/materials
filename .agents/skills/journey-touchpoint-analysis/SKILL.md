---
name: journey-touchpoint-analysis
description: Simulate a target user journey through a website or product, decompose it into lifecycle steps and touchpoints, collect evidence with real screenshots, annotate where the user clicks or looks, score each touchpoint, and produce a visual UX / competitive-analysis report. Use for UX journey audits, developer-portal benchmarking, "simulate a user and rate the experience", touchpoint heatmaps, screenshot-based click-path analysis, or turning webpage exploration into a structured report.
---

# Journey Touchpoint Analysis

Use this skill to turn "pretend I am a user trying to complete a task on this site" into a rigorous, visual report: journey map, touchpoint cards, annotated screenshots, scoring, heatmap, and recommendations.

This skill was distilled from the Ascend vs NVIDIA developer-portal analysis. The reusable pattern is independent of that domain.

## Core Output

Produce a report with these layers:

1. **Scenario and persona**: who the user is, what they are trying to accomplish, what success means.
2. **Lifecycle journey**: 5-8 sequential steps from landing to completion and later support.
3. **Touchpoint inventory**: concrete pages, search results, dialogs, downloads, docs, tools, community posts, or support surfaces visited in each step.
4. **Evidence**: real screenshots and source URLs for both sides of a comparison, or for current state vs proposed state.
5. **Annotated click path**: arrows and labels on screenshots showing where the user actually clicks or looks.
6. **Scoring**: per-touchpoint scores based on explicit friction metrics, not vibes.
7. **Visual analysis**: each touchpoint combines image, "what the picture shows", difference analysis, and recommendation.
8. **Synthesis**: heatmap, journey curve, biggest gaps, quick wins, and owner-oriented action plan.

## Workflow

### 1. Frame the user task

Define a task narrow enough to run end to end. Prefer "custom operator developer wants to write, compile, debug, and register an operator" over "developer experience".

Capture:

- persona / role
- starting knowledge
- target outcome
- environment constraints
- success criteria
- comparison baseline, if any

If the site supports multiple fundamentally different paths, create scenario tabs rather than mixing them. Example: operator development and training are two scenarios, because the pages and failure points differ.

### 2. Build the lifecycle

Use 5-8 lifecycle steps. Each step should be a real phase in the user's attempt, not an organizational category.

Good steps:

- find entry / choose direction
- get oriented
- get environment or toolkit
- write or configure
- run / compile / verify
- debug / ask for help
- advance / reuse / join ecosystem

Avoid fake phases like "awareness / learning / resources / support" if they are parallel content types rather than a chronological journey.

For cross-cutting capabilities such as search, language switch, account, or version selector, either map them to the step where they are first needed or keep a separate "cross-cutting" band.

### 3. Collect evidence by running the path

For every touchpoint:

- Record the URL.
- Capture the actual page state.
- Note whether login, region, language, cookie banner, or anti-bot behavior affected the evidence.
- If a page blocks headless capture, document that and use a manual screenshot rather than inventing a mockup.
- Never use a guessed 404 or search miss as evidence until you have checked the site's navigation or search for the real URL.

Screenshots must show the part of the page discussed in the text. If the relevant element is in the middle of a long page, crop that section and use the crop as the evidence image.

### 4. Annotate the click path

Use `scripts/annotate.py` in this skill, or an existing `click-annotation` skill if available.

Rules:

- Look at the screenshot before choosing coordinates.
- Arrow targets must point to the real element a user would click: button, menu item, card, search input, tab, or link.
- Use one annotated image per scenario when different roles click different places.
- Use a neutral color when all scenarios click the same place; use distinct colors when paths differ.
- Keep labels short. Put explanation in the report text, not in the label.
- Do not modify the original screenshot; write a new annotated file.

Command example:

```bash
python3 scripts/annotate.py source.png annotated-op.png \
  --ann "382,60,Operator developer -> click Docs,#7c5cf0,420" \
  --crop 0,0,1440,180 --pad 150 --fsz 30
```

If the page lacks the expected entry, use a note-only annotation:

```bash
python3 scripts/annotate.py source.png annotated-missing.png \
  --ann "None,,No direct operator entry in first screen,#2f6fed" \
  --pad 130 --fsz 28
```

### 5. Score touchpoints

Use explicit metrics. Do not only assign impression scores.

A practical friction model:

- **Efficiency**: clicks, choices, scroll distance, search rounds, fetch attempts, path length.
- **Cognitive load**: unclear product naming, competing entry points, missing task framing, version ambiguity.
- **Access friction**: login required, account region restriction, license gate, modal interruption.
- **Executability**: runnable code, complete command, dependencies, expected output, downloadable project, online environment.
- **Discoverability**: external search rank, official result first-screen presence, stable URL, page title / summary quality, internal search success.

Normalize each metric to 0-100 with documented best / worst anchors. For binary friction, use present=0 and absent=100. For capability, use present=100 and absent=0. Average available metrics into dimension scores, then average dimensions into the touchpoint score. If a metric is not applicable, omit it rather than filling a fake value.

For comparison reports, score both sides with the same metrics. Do not punish one side for a dimension that was not tested on the other.

### 6. Write each touchpoint card

Each card should contain:

- id and name
- scores for each side
- user point of view: first-person task sentence
- click path chips
- left and right screenshots or current/proposed screenshots
- caption directly below each image: "what this image shows"
- difference analysis bullets
- recommendation / "what to do"
- source URLs
- owner or topic tag if the user asks for implementation planning

Use complete sentences. Avoid telegraphic labels that cannot stand alone in a report.

### 7. Synthesize across touchpoints

After all cards, produce:

- lifecycle journey map with emotion/friction curve
- heatmap grouped by lifecycle step
- largest positive and negative gaps
- conclusions by problem topic, not only by department
- recommendations grouped by topic, with priority and evidence references

Good topic groups:

- search and entry discoverability
- content structure and AI usability
- onboarding and runnable path
- account / download / environment gates
- diagnosis and community support
- operating mechanism and responsibility loop

Keep department ownership as a final implementation layer, not the primary narrative unless the user explicitly asks for a responsibility report.

## Report Design Guidance

If building a web or slide report, combine this skill with the user's presentation/report template skill. The report should be image-led: annotated screenshots, journey maps, score heatmaps, and cards. Text should explain the evidence, not replace it.

For each screenshot, place the analysis close to the image. Do not separate image evidence from the conclusion it supports.

Use stable file naming:

- `01-product-step-op.png`
- `01-product-step-train.png`
- `tp-4.3-download-annotated.png`
- `journey-op.png`
- `touchpoint-heat.png`

## Quality Checks

Before finishing:

- Verify every screenshot path resolves.
- Open annotated images and check arrow landing points.
- Check each score has a metric or evidence trail.
- Confirm source URLs match the screenshot, not a nearby page.
- Confirm journey steps are chronological.
- Confirm conclusions cite touchpoints or metrics.
- If generating a web report, screenshot the final pages in desktop and mobile-ish widths and look for clipped text.
- Do not export PDF unless the user explicitly asks.

## Bundled Script

- `scripts/annotate.py`: draw transparent click markers, arrows, and label bars on UI screenshots. It is copied from the proven click-annotation workflow and requires Pillow.
