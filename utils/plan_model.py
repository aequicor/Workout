"""Shared helpers for workout artifact builders."""

from __future__ import annotations

import copy
import datetime as dt
import json
import re
from pathlib import Path
from typing import Any, Iterable


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT_DIR = PROJECT_ROOT / "programms"


class PlanValidationError(ValueError):
    """Raised when a workout plan JSON cannot be used for artifact generation."""


def load_plan(path: str | Path) -> dict[str, Any]:
    plan_path = Path(path)
    with plan_path.open("r", encoding="utf-8-sig") as fh:
        data = json.load(fh)
    if not isinstance(data, dict):
        raise PlanValidationError("Plan JSON must contain an object at the top level.")
    return normalize_plan(data)


def normalize_plan(plan: dict[str, Any]) -> dict[str, Any]:
    normalized = copy.deepcopy(plan)

    if not normalized.get("title"):
        raise PlanValidationError("Plan JSON must include a non-empty 'title'.")
    if not isinstance(normalized.get("workouts"), list) or not normalized["workouts"]:
        raise PlanValidationError("Plan JSON must include a non-empty 'workouts' list.")

    normalized["date"] = normalize_date(normalized.get("date"))
    normalized["slug"] = slugify(normalized.get("slug") or normalized["title"])

    for workout in normalized["workouts"]:
        if not isinstance(workout, dict):
            raise PlanValidationError("Every workout must be an object.")
        if not isinstance(workout.get("exercises"), list) or not workout["exercises"]:
            label = workout.get("day") or workout.get("focus") or "unnamed workout"
            raise PlanValidationError(f"Workout '{label}' must include exercises.")

    return normalized


def normalize_date(value: Any) -> str:
    if not value:
        return dt.date.today().isoformat()
    if isinstance(value, dt.date):
        return value.isoformat()
    text = str(value).strip()
    try:
        return dt.date.fromisoformat(text).isoformat()
    except ValueError:
        raise PlanValidationError("Plan 'date' must use ISO format YYYY-MM-DD.") from None


def slugify(value: Any, default: str = "workout-plan") -> str:
    text = str(value or "").strip().lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    text = re.sub(r"-{2,}", "-", text).strip("-")
    return text or default


def default_output_paths(plan: dict[str, Any], output_dir: str | Path | None = None) -> tuple[Path, Path]:
    out_dir = Path(output_dir) if output_dir else DEFAULT_OUTPUT_DIR
    prefix = f"{plan['date']}-{plan['slug']}"
    return out_dir / f"{prefix}.docx", out_dir / f"{prefix}-progress.xlsx"


def iter_exercise_rows(plan: dict[str, Any]) -> Iterable[dict[str, Any]]:
    for workout in plan.get("workouts", []):
        base = {
            "week": workout.get("week", ""),
            "day": workout.get("day", ""),
            "focus": workout.get("focus", ""),
        }
        for exercise in workout.get("exercises", []):
            if not isinstance(exercise, dict):
                raise PlanValidationError("Every exercise must be an object.")
            row = dict(base)
            row.update(exercise)
            row.setdefault("block", "")
            row.setdefault("exercise", "")
            row.setdefault("visual_source", exercise.get("visual") or exercise.get("source") or "")
            row.setdefault("sets_reps", exercise.get("sets") or exercise.get("prescription") or "")
            row.setdefault("intensity", "")
            row.setdefault("rest", "")
            row.setdefault("notes", "")
            yield row


def list_value(plan: dict[str, Any], key: str) -> list[str]:
    value = plan.get(key) or []
    if isinstance(value, str):
        return [value]
    if isinstance(value, list):
        return [str(item) for item in value if str(item).strip()]
    return []


def source_warnings(plan: dict[str, Any]) -> list[str]:
    warnings: list[str] = []
    for row in iter_exercise_rows(plan):
        if not str(row.get("visual_source", "")).strip():
            exercise = row.get("exercise") or "unnamed exercise"
            day = row.get("day") or "unknown day"
            warnings.append(f"Missing visual_source for '{exercise}' on '{day}'.")
    return warnings


def ensure_output_dir(path: str | Path) -> Path:
    out_dir = Path(path)
    out_dir.mkdir(parents=True, exist_ok=True)
    return out_dir
