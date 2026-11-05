#!/usr/bin/env python3
"""
Reorganize numbered Markdown files into dedicated companion folders.

Rules:
- Basic-Class-CObject:
    Next-<number>.md -> NextSet/NextSet.md
    Prev-<number>.md -> PrevNext/PrevNext.md
- Standard-Library/Data-Collections:
    Step-<number>.md -> StepSet/StepSet.md
    <Name>-<number>.md -> <Name>Const/<Name>Const.md

The script only considers numbered Markdown files in folders that also
contain the corresponding plain <Name>.md file (except the explicit
Next/Prev/Step rules, which use that same pairing check).

Default is a dry run. Apply with --apply. Before moving, the script copies
each source file into backup_before_md_reorganization, preserving its
relative path. It never overwrites an existing destination.
"""
from __future__ import annotations

import argparse
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DOCS = ROOT / "viewer" / "docs"
BACKUP = ROOT / "backup_before_md_reorganization"

NUMBERED_RE = re.compile(r"^(?P<base>.+)-(?P<number>\d+)\.md$", re.IGNORECASE)


def plan_moves():
    plans = []
    skipped = []

    for source in sorted(DOCS.rglob("*.md")):
        if not source.is_file():
            continue

        try:
            rel = source.relative_to(DOCS)
        except ValueError:
            continue

        parts = rel.parts
        parent_text = "\\".join(parts[:-1]).casefold()
        filename = source.name

        match = NUMBERED_RE.match(filename)
        if not match:
            continue

        base = match.group("base")
        base_plain = source.with_name(base + ".md")

        # Only act on explicitly requested areas.
        in_cobject = any(part.casefold() == "basic-class-cobject" for part in parts[:-1])
        in_data_collections = (
            len(parts) >= 2
            and parts[0].casefold() == "standard-library"
            and parts[1].casefold() == "data-collections"
        )

        if not (in_cobject or in_data_collections):
            continue

        if not base_plain.exists():
            skipped.append((rel, "matching plain Markdown file not found: " + base_plain.name))
            continue

        if in_cobject:
            if base.casefold() == "next":
                folder_name, dest_name = "NextSet", "NextSet.md"
            elif base.casefold() == "prev":
                folder_name, dest_name = "PrevNext", "PrevNext.md"
            else:
                continue
        else:
            if base.casefold() == "step":
                folder_name, dest_name = "StepSet", "StepSet.md"
            else:
                folder_name = base + "Const"
                dest_name = folder_name + ".md"

        destination = source.parent.parent / folder_name / dest_name

        # Avoid silently overwriting or colliding with another planned move.
        if destination.exists():
            skipped.append((rel, f"destination already exists: {destination.relative_to(DOCS)}"))
            continue

        plans.append((source, destination))

    return plans, skipped


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="perform moves; default is dry run")
    args = parser.parse_args()

    if not DOCS.is_dir():
        raise SystemExit(f"Docs directory not found: {DOCS}")

    print(f"[SCAN] Scanning {DOCS}", flush=True)
    plans, skipped = plan_moves()

    print("\n--- Planned moves ---")
    if not plans:
        print("No matching files found.")
    for source, destination in plans:
        print(f"[MOVE] {source.relative_to(DOCS)}")
        print(f"    -> {destination.relative_to(DOCS)}")

    if skipped:
        print("\n--- Skipped ---")
        for rel, reason in skipped:
            print(f"[SKIP] {rel}: {reason}")

    print("\n--- Summary ---")
    print(f"Files to move: {len(plans)}")
    print(f"Skipped: {len(skipped)}")

    if not args.apply:
        print("\nDRY RUN: no files or folders were changed.")
        print("If the destinations and names are correct, run with --apply.")
        return

    moved = 0
    for source, destination in plans:
        relative = source.relative_to(DOCS)
        backup_path = BACKUP / relative
        backup_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, backup_path)

        destination.parent.mkdir(parents=True, exist_ok=True)
        # Recheck at apply time; never overwrite.
        if destination.exists():
            print(f"[SKIP-EXISTS] {destination.relative_to(DOCS)}", flush=True)
            continue

        shutil.move(str(source), str(destination))
        moved += 1
        print(f"[MOVED] {relative} -> {destination.relative_to(DOCS)}", flush=True)

    print("\n--- Applied ---")
    print(f"Files moved: {moved}")
    print(f"Source backups: {BACKUP}")


if __name__ == "__main__":
    main()
