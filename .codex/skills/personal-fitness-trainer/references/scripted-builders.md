# Scripted Artifact Builders

Use this reference when the agent needs to create workout program files with the project scripts in `utils/`.

## When To Use

Use the scripted builders when the user wants a finished workout program artifact and the plan can be represented as structured JSON. The scripts create:

- `.docx` workout program in `programms/`
- `.xlsx` progress tracker in `programms/`

The main command is:

```powershell
python utils/build_workout_artifacts.py <plan-json>
```

Prefer the Codex workspace/bundled Python runtime when available, because it includes `python-docx` and `openpyxl`.

## Agent Workflow

1. Complete the coaching intake and safety checks required by `SKILL.md` and `coaching-guide.md`.
2. Verify exercise visuals according to `exercise-illustrations.md`; each prescribed exercise in the JSON should include a `visual_source` URL.
3. Create a structured plan JSON using `utils/sample_plan.json` as the schema example.
4. Store generated plan JSON in `res/` when it is an intermediate working file, for example `res/YYYY-MM-DD-program-slug-plan.json`.
5. Do not include biometric details in that JSON unless the user clearly allowed local storage of biometric intake. Use generic assumptions or omit private fields when consent is missing.
6. Validate before building:

```powershell
python utils/build_workout_artifacts.py res/YYYY-MM-DD-program-slug-plan.json --validate-only
```

7. Build both artifacts:

```powershell
python utils/build_workout_artifacts.py res/YYYY-MM-DD-program-slug-plan.json
```

Use `--docx-only` or `--xlsx-only` only when the user explicitly asks for one artifact.

## Expected Outputs

By default the scripts write:

- `programms/YYYY-MM-DD-program-slug.docx`
- `programms/YYYY-MM-DD-program-slug-progress.xlsx`

The generated files are ignored by git by default. Do not commit generated user programs, logs, private data, downloaded visuals, or render previews unless the user explicitly asks.

## Verification

Before delivering generated files:

- Confirm the script exits with code `0`.
- Confirm both output files exist and are non-empty.
- Open the DOCX and XLSX structurally with Python when possible.
- For final user-facing artifacts, still follow the Documents and Spreadsheets verification expectations where practical: render/inspect outputs, fix obvious layout or formula issues, and disclose any skipped render step.
- Treat `warning: Missing visual_source ...` as incomplete work unless the user explicitly requested text-only output or approved missing visuals.

## Final Response

Return only final artifact links plus any verification limitation:

- `[Program.docx](/absolute/path/to/programms/YYYY-MM-DD-program-slug.docx)`
- `[Progress Tracker.xlsx](/absolute/path/to/programms/YYYY-MM-DD-program-slug-progress.xlsx)`
