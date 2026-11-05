#!/usr/bin/env python3
"""
List every folder under viewer/docs that contains exactly two Markdown files.

Run from the project root:
    python -u find_folders_with_two_md.py

This script is read-only: it does not rename, move, or modify any files.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DOCS_DIR = ROOT / "viewer" / "docs"


def main():
    if not DOCS_DIR.is_dir():
        raise SystemExit(f"Docs folder not found: {DOCS_DIR}")

    folders_with_two = []
    folders_with_more = []

    # Include the docs root itself, as well as every subfolder.
    folders = [DOCS_DIR] + sorted(p for p in DOCS_DIR.rglob("*") if p.is_dir())

    for folder in folders:
        md_files = sorted(
            (p for p in folder.iterdir() if p.is_file() and p.suffix.lower() == ".md"),
            key=lambda p: p.name.casefold(),
        )

        if len(md_files) == 2:
            folders_with_two.append((folder, md_files))
        elif len(md_files) > 2:
            folders_with_more.append((folder, md_files))

    print(f"Docs folder: {DOCS_DIR}")
    print(f"Folders scanned: {len(folders)}")
    print(f"Folders containing exactly 2 .md files: {len(folders_with_two)}")
    print()

    for number, (folder, files) in enumerate(folders_with_two, 1):
        relative_folder = folder.relative_to(DOCS_DIR)
        print(f"[{number}] {relative_folder if str(relative_folder) != '.' else '.'}")
        for file in files:
            print(f"    - {file.name}")
        print()

    print("--- Summary ---")
    print(f"Exactly 2 Markdown files: {len(folders_with_two)}")
    print(f"More than 2 Markdown files: {len(folders_with_more)}")

    if folders_with_more:
        print("\nFolders with more than 2 Markdown files (not included above):")
        for folder, files in folders_with_more:
            print(f"  {folder.relative_to(DOCS_DIR)} ({len(files)} files)")


if __name__ == "__main__":
    main()
