# Workout Artifact Utilities

These scripts build the project deliverables from a single workout plan JSON file:

- `.docx` workout program in `programms/`
- `.xlsx` progress tracker in `programms/`

Generated outputs are ignored by git by default. Keep private intake, logs, downloaded images, charts, and render previews out of commits unless explicitly requested.

## Quick Start

Run from the project root:

```powershell
python utils/build_workout_artifacts.py utils/sample_plan.json
```

With the Codex bundled Python runtime on this machine:

```powershell
& "C:\Users\kruz18\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe" utils/build_workout_artifacts.py utils/sample_plan.json
```

The default output paths are:

- `programms/<date>-<slug>.docx`
- `programms/<date>-<slug>-progress.xlsx`

## Input Shape

Use `utils/sample_plan.json` as the canonical example. Each exercise should include:

- `block`
- `exercise`
- `visual_source`
- `sets_reps`
- `intensity`
- `rest`
- `notes`

`visual_source` must point to a verified specialized exercise source. The scripts preserve and hyperlink the source; they do not verify or download it.

## Individual Builders

```powershell
python utils/build_workout_docx.py utils/sample_plan.json
python utils/build_progress_tracker_xlsx.py utils/sample_plan.json
```
