#!/usr/bin/env python3
"""
Fix the previous reorganization: move generated companion folders OUT of the
original method folder and place them beside it.

Example:
  .../CArrayChar/AddArray/AddArrayConst/AddArrayConst.md
becomes:
  .../CArrayChar/AddArrayConst/AddArrayConst.md

Likewise:
  Next/NextSet/NextSet.md       -> NextSet/NextSet.md
  Prev/PrevNext/PrevNext.md     -> PrevNext/PrevNext.md
  Step/StepSet/StepSet.md       -> StepSet/StepSet.md

Default is dry-run. Use --apply to perform moves. Existing destinations are
never overwritten. A backup copy is made before each move.
"""
from __future__ import annotations

import argparse
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DOCS = ROOT / "viewer" / "docs"
BACKUP = ROOT / "backup_before_md_reorganization_level_fix"

# destination folder name -> original sibling folder name
COMPANION_TO_ORIGINAL = {
    "nextset": "next",
    "prevnext": "prev",
    "stepset": "step",
}


def expected_original_name(companion_name: str) -> str | None:
    low = companion_name.casefold()
    if low in COMPANION_TO_ORIGINAL:
        return COMPANION_TO_ORIGINAL[low]
    if low.endswith("const") and len(companion_name) > len("Const"):
        return companion_name[:-5]
    return None


def collect_moves():
    moves = []
    skipped = []

    for companion_dir in sorted(p for p in DOCS.rglob("*") if p.is_dir()):
        original_name = expected_original_name(companion_dir.name)
        if not original_name:
            continue

        original_dir = companion_dir.parent / original_name
        # Only fix the erroneous nesting pattern: companion dir is inside
        # its original method folder, and the sibling destination is outside.
        if not original_dir.is_dir():
            continue

        md_files = sorted(p for p in companion_dir.glob("*.md") if p.is_file())
        for source in md_files:
            destination_dir = companion_dir.parent.parent / companion_dir.name
            destination = destination_dir / source.name

            if destination.exists():
                skipped.append((source, f"destination already exists: {destination}"))
                continue

            moves.append((source, destination))

        # If no markdown files remain, report it so user knows whether the
        # old nested folder can be removed. Do not delete directories.
        if not md_files:
            skipped.append((companion_dir, "no Markdown files found; folder left untouched"))

    return moves, skipped


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="perform moves")
    args = parser.parse_args()

    if not DOCS.is_dir():
        raise SystemExit(f"Docs directory not found: {DOCS}")

    print(f"[SCAN] {DOCS}", flush=True)
    moves, skipped = collect_moves()

    print("\n--- Planned moves ---")
    for source, destination in moves:
        print(f"[MOVE] {source.relative_to(DOCS)}")
        print(f"    -> {destination.relative_to(DOCS)}")

    if skipped:
        print("\n--- Skipped ---")
        for source, reason in skipped:
            try:
                shown = source.relative_to(DOCS)
            except ValueError:
                shown = source
            print(f"[SKIP] {shown}: {reason}")

    print("\n--- Summary ---")
    print(f"Files to move: {len(moves)}")
    print(f"Skipped: {len(skipped)}")

    if not args.apply:
        print("\nDRY RUN: no files or folders changed.")
        print("Review the destinations, then rerun with --apply.")
        return

    moved = 0
    for source, destination in moves:
        rel = source.relative_to(DOCS)
        backup_path = BACKUP / rel
        backup_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, backup_path)

        destination.parent.mkdir(parents=True, exist_ok=True)
        if destination.exists():
            print(f"[SKIP-EXISTS] {destination.relative_to(DOCS)}", flush=True)
            continue

        shutil.move(str(source), str(destination))
        moved += 1
        print(f"[MOVED] {rel} -> {destination.relative_to(DOCS)}", flush=True)

    print("\n--- Applied ---")
    print(f"Files moved: {moved}")
    print(f"Backup copies: {BACKUP}")
    print("Empty old folders were not deleted; remove them only after checking.")


if __name__ == "__main__":
    main()
