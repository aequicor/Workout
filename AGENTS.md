# Project Instructions

This workspace contains a project-local Codex skill for personal fitness coaching:

- Skill: `.codex/skills/personal-fitness-trainer/SKILL.md`
- Detailed reference: `.codex/skills/personal-fitness-trainer/references/coaching-guide.md`
- Exercise illustration sourcing: `.codex/skills/personal-fitness-trainer/references/exercise-illustrations.md`
- Artifact workflow: `.codex/skills/personal-fitness-trainer/references/artifact-workflow.md`

For workout planning, exercise substitutions, progressive overload, warmups, cooldowns, mobility, conditioning, workout-log review, habit coaching, or general non-medical nutrition guidance, read and follow the project-local skill before answering.

Keep fitness advice conservative, personalized to the user's stated constraints, and clearly outside medical diagnosis or treatment.

Before composing a workout plan, ask for the person's minimum useful biometric data and make every field skippable. Ask for explicit permission before saving biometric intake locally; save it only in `res/` after clear consent, otherwise do not write it to disk.

When workout plans include exercises, include sourced visual technique references from specialized exercise/coaching sources. Do not create or generate exercise illustrations manually.

Workspace artifact conventions:

- Use `res/` for agent-writable scratch resources: downloaded source images, charts, graphs, working data, rendered QA previews, and other intermediate files.
- Use `programms/` for final workout deliverables. Keep the exact folder spelling `programms`.
- When creating a full workout program, save the program as a `.docx` in `programms/` using the Documents workflow and create a companion progress-tracking `.xlsx` in `programms/` using the Spreadsheets workflow.
- Prefer filenames like `programms/YYYY-MM-DD-program-slug.docx` and `programms/YYYY-MM-DD-program-slug-progress.xlsx`.
- Do not place final workout program files outside `programms/` unless the user explicitly asks for a different path.
