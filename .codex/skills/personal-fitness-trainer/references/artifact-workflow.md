# Artifact Workflow

Use this reference whenever creating or updating workout program files, progress trackers, downloaded exercise visuals, charts, rendered previews, or other generated assets in this workspace.

## Directories

- `res/`: agent-writable scratch directory for downloaded source visuals, images, charts, graphs, rendered QA previews, extracted data, and other intermediate resources.
- `programms/`: final deliverable directory for workout programs and tracking workbooks. Keep this exact spelling.

Do not place final workout program artifacts outside `programms/` unless the user explicitly asks for a different path.

## Required Deliverables For Full Programs

When the user asks for a complete workout program as an artifact, create both:

- `programms/YYYY-MM-DD-program-slug.docx`: the workout program document.
- `programms/YYYY-MM-DD-program-slug-progress.xlsx`: the companion progress-tracking workbook.

Use a concise lowercase ASCII slug based on the goal or audience, for example `beginner-strength`, `home-fat-loss`, or `hypertrophy-4-week`.

## DOCX Program Rules

- Use the Documents skill for `.docx` creation and verification.
- Include the program overview, assumptions/intake used, safety notes, weekly schedule, per-workout tables, progression rules, substitution rules, cooldown/mobility guidance, and check-in instructions.
- Include exercise technique visual links from specialized sources. Embed direct images only when permission is clear; otherwise link the verified source page.
- Store any downloaded visuals, page-render PNGs, or QA previews in `res/`.
- Render and inspect the `.docx` according to the Documents skill before delivery when the environment supports rendering.

## XLSX Progress Tracker Rules

- Use the Spreadsheets skill for `.xlsx` creation and verification.
- Save the workbook in `programms/` next to the `.docx`.
- Include sheets suitable for logging and review, typically:
  - `Plan`: program weeks, days, exercises, prescribed sets/reps/time, intensity, rest, and visual/source links.
  - `Log`: date, week, day, exercise, load, reps/time completed, RPE/RIR, pain flag, notes, and completion status.
  - `Summary`: adherence, volume or session counts, recent RPE trend, and next-action notes when useful.
- Use formulas, tables, filters, data validation, freeze panes, and readable formatting where helpful.
- Render or inspect the workbook according to the Spreadsheets skill before delivery.

## Git And Privacy

- `res/` and generated files in `programms/` are local working/output areas and should not be committed by default.
- Keep `.gitkeep` files so the directories exist in fresh clones.
- Do not commit private health data, personal workout logs, downloaded copyrighted media, rendered previews, or generated personal program files unless the user explicitly asks.
- Before saving biometric intake, ask for explicit permission to store it locally in `res/`.
- If permission is granted, save only the coaching-relevant biometric intake in a dated local file such as `res/YYYY-MM-DD-biometric-intake.md` or `.json`; if permission is declined, missing, or ambiguous, do not create a biometric intake file.

## Final Response Pattern

When artifacts are created, return links to the final files only:

- `[Program.docx](/absolute/path/to/programms/YYYY-MM-DD-program-slug.docx)`
- `[Progress Tracker.xlsx](/absolute/path/to/programms/YYYY-MM-DD-program-slug-progress.xlsx)`

Mention render/verification limitations only when a required verification step could not be completed.
