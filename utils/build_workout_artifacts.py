"""Build both workout artifacts: DOCX program and XLSX progress tracker."""

from __future__ import annotations

import argparse
from pathlib import Path

from build_progress_tracker_xlsx import build_xlsx
from build_workout_docx import build_docx
from plan_model import default_output_paths, load_plan, source_warnings


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build workout DOCX and progress XLSX artifacts.")
    parser.add_argument("plan_json", help="Path to workout plan JSON.")
    parser.add_argument("--output-dir", default="programms", help="Output directory for generated artifacts.")
    parser.add_argument("--docx-only", action="store_true", help="Only build the DOCX program.")
    parser.add_argument("--xlsx-only", action="store_true", help="Only build the XLSX progress tracker.")
    parser.add_argument("--validate-only", action="store_true", help="Validate the plan JSON and print planned outputs.")
    parser.add_argument("--log-rows", type=int, default=300, help="Number of editable log rows for the tracker.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.docx_only and args.xlsx_only:
        raise SystemExit("Choose at most one of --docx-only or --xlsx-only.")

    plan = load_plan(args.plan_json)
    docx_path, xlsx_path = default_output_paths(plan, Path(args.output_dir))

    if args.validate_only:
        print(f"valid: {args.plan_json}")
        if not args.xlsx_only:
            print(f"docx: {docx_path}")
        if not args.docx_only:
            print(f"xlsx: {xlsx_path}")
        for warning in source_warnings(plan):
            print(f"warning: {warning}")
        return 0

    built: list[Path] = []
    if not args.xlsx_only:
        built.append(build_docx(plan, docx_path))
    if not args.docx_only:
        built.append(build_xlsx(plan, xlsx_path, log_rows=args.log_rows))

    for warning in source_warnings(plan):
        print(f"warning: {warning}")
    for path in built:
        print(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
