#!/usr/bin/env python3
"""
Restore Markdown heading levels using the FULL CHM breadcrumb in <td class="nav">.

Examples:
  MQL5 Reference / Account Information
    -> Account-Information/Account-Information.md

  MQL5 Reference / Timeseries and Indicators Access / BarsCalculated
    -> Timeseries-and-Indicators-Access/BarsCalculated/BarsCalculated.md

The H1 and <title> are NOT used to match files. The breadcrumb is authoritative.
Default mode is dry-run. Use --apply only after reviewing the report.
"""
from __future__ import annotations

import argparse
import re
import unicodedata
from collections import defaultdict
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent
HTML_DIR = ROOT / "chm-extracted"
MD_DIR = ROOT / "viewer" / "docs"
BACKUP_DIR = ROOT / "backup_before_heading_fix"


def norm_text(value: str) -> str:
    value = unicodedata.normalize("NFKC", value).replace("\xa0", " ")
    return re.sub(r"\s+", " ", value).strip()


def segment_key(value: str) -> str:
    """Normalize a breadcrumb label to the Markdown hyphenated naming convention."""
    value = norm_text(value).casefold()
    if value.endswith(".md"):
        value = value[:-3]
    # The CHM contains a Cyrillic capital Es (&#1057;) in "Economic Calendar".
    # The Markdown export omits this confusable character from the path.
    value = value.replace("\u0441", "")
    # Generic type names use <T> in CHM breadcrumbs and -T in Markdown paths.
    value = value.replace("<", "-").replace(">", "")
    # Slashes in breadcrumb labels separate words in the exported folder names.
    value = value.replace("/", " ")
    value = value.replace("&", " and ")
    value = re.sub(r"\s+", "-", value)
    value = re.sub(r"[^\w-]", "", value, flags=re.UNICODE)
    value = re.sub(r"-+", "-", value).strip("-")
    return value


def path_key(parts) -> tuple[str, ...]:
    return tuple(segment_key(part) for part in parts if segment_key(part))


def html_target_keys(html_path: Path, crumbs, headings, breadcrumb_complete=True):
    """Return the Markdown key, using H1 only when the breadcrumb is incomplete."""
    if not breadcrumb_complete:
        title = next((text for level, text in headings if level == 1), None)
        if title:
            title = re.sub(r"\s+\((?:the )?(?:get|set) method\)$", "", title, flags=re.IGNORECASE)
            # Keep the breadcrumb's parent path, then append the H1 title as
            # the page folder and filename for this incomplete-breadcrumb case.
            return [path_key(crumbs + [title, title + ".md"])]
        return []

    current_page = crumbs[-1]
    base_parts = crumbs + [current_page + ".md"]
    base_key = path_key(base_parts)
    keys = []
    html_stem = segment_key(html_path.stem)

    # These APIs have distinct Markdown names although the CHM breadcrumb uses
    # the same label for the getter and setter overloads.
    overload_aliases = {
        ("carray", "stepbool"): "StepSet",
        ("clist", "freemode"): "FreeModeGet",
        ("clist", "freemode2"): "FreeModeSet",
    }
    if len(crumbs) >= 2:
        class_key = segment_key(crumbs[-2])
        if html_stem.startswith(class_key):
            overload = overload_aliases.get((class_key, html_stem[len(class_key):]))
            if overload:
                alias_parts = crumbs[:-1] + [overload, overload + ".md"]
                keys.append(path_key(alias_parts))

    # CHM overload pages often keep the breadcrumb label unchanged while the
    # HTML filename contains the distinguishing suffix (for example,
    # AddArrayConst). The parent class name is the prefix in these filenames.
    if len(crumbs) >= 2:
        parent_key = segment_key(crumbs[-2])
        if parent_key and html_stem.startswith(parent_key):
            method_name = html_stem[len(parent_key):]
            current_key = segment_key(current_page)
            if method_name.startswith(current_key):
                # A longer filename suffix denotes a separate exported page,
                # such as AddArrayConst, so do not also index it as AddArray.
                suffix = method_name[len(current_key):]
                if suffix == "const":
                    derived_parts = crumbs[:-1] + [method_name, method_name + ".md"]
                    keys.append(path_key(derived_parts))

    # CObject accessors use get/set prefixes in CHM filenames, but the
    # exported Markdown paths use Next/Prev for getters and NextSet/PrevNext
    # for setters.
    cobject_aliases = {
        "getnext": "Next",
        "getprev": "Prev",
        "setnext": "NextSet",
        "setprev": "PrevNext",
    }
    method_name = segment_key(html_path.stem)
    if method_name.startswith("cobject"):
        alias = cobject_aliases.get(method_name[len("cobject"):])
        if alias:
            alias_parts = crumbs[:-1] + [alias, alias + ".md"]
            keys.append(path_key(alias_parts))

    if not keys:
        keys.append(base_key)
    return list(dict.fromkeys(keys))


def plain_markdown_line(line: str) -> str:
    value = line.strip()
    value = re.sub(r"^\s{0,3}#{1,6}\s+", "", value)
    value = re.sub(r"^\s*[-*+]\s+", "", value)
    value = re.sub(r"^\s*\d+[.)]\s+", "", value)
    value = re.sub(r"!\[([^\]]*)\]\([^)]*\)", r"\1", value)
    value = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", value)
    value = re.sub(r"`([^`]*)`", r"\1", value)
    value = re.sub(r"[*_~]", "", value)
    return norm_text(value).casefold()


class BreadcrumbParser(HTMLParser):
    """Read anchor labels and the final plain-text crumb inside td.nav."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.in_nav = False
        self.in_anchor = False
        self.anchor_text = []
        self.anchor_href = ""
        self.anchors = []
        self.trailing_text = []
        self.complete = False

    def handle_starttag(self, tag, attrs):
        tag = tag.lower()
        attrs = dict(attrs)
        if tag == "td" and "nav" in attrs.get("class", "").split():
            self.in_nav = True
            self.anchors = []
            self.trailing_text = []
        elif tag == "a" and self.in_nav:
            self.in_anchor = True
            self.anchor_text = []
            self.anchor_href = attrs.get("href", "")

    def handle_data(self, data):
        if not self.in_nav:
            return
        if self.in_anchor:
            self.anchor_text.append(data)
        else:
            self.trailing_text.append(data)

    def handle_endtag(self, tag):
        tag = tag.lower()
        if tag == "a" and self.in_nav and self.in_anchor:
            label = norm_text("".join(self.anchor_text))
            if label:
                self.anchors.append((label, self.anchor_href))
            self.in_anchor = False
            self.anchor_text = []
            self.anchor_href = ""
        elif tag == "td" and self.in_nav:
            self.in_nav = False

    def breadcrumb(self):
        # Ignore the virtual MQL5 Reference root, identified by href or label.
        parents = []
        for label, href in self.anchors:
            href_name = Path(href.replace("\\", "/")).name.casefold()
            if href_name == "mql5_guide.htm" or segment_key(label) == "mql5-reference":
                continue
            parents.append(label)

        # The current page is the final plain-text crumb after the last anchor.
        tail = norm_text("".join(self.trailing_text))
        tail = re.sub(r"^[\s/|>»›]+", "", tail)
        tail = re.sub(r"[\s/|>»›]+$", "", tail)
        self.complete = bool(tail)
        if not tail:
            return parents or None
        return parents + [tail]


class HeadingParser(HTMLParser):
    """Extract Help & Manual heading levels p_H1 ... p_H6."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.headings = []
        self.level = None
        self.parts = []

    def handle_starttag(self, tag, attrs):
        classes = dict(attrs).get("class", "").split()
        match = next(
            (re.fullmatch(r"p_H([1-6])", cls) for cls in classes
             if re.fullmatch(r"p_H([1-6])", cls)),
            None,
        )
        if tag.lower() == "p" and match:
            self.level = int(match.group(1))
            self.parts = []

    def handle_data(self, data):
        if self.level is not None:
            self.parts.append(data)

    def handle_endtag(self, tag):
        if tag.lower() == "p" and self.level is not None:
            heading = norm_text("".join(self.parts))
            if heading:
                self.headings.append((self.level, heading))
            self.level = None
            self.parts = []


def read_text(path: Path) -> str:
    raw = path.read_bytes()
    for encoding in ("utf-8-sig", "cp1252", "latin-1"):
        try:
            return raw.decode(encoding)
        except UnicodeDecodeError:
            pass
    return raw.decode("utf-8", errors="replace")


def html_heading_index():
    index = defaultdict(list)
    html_files = sorted(
        list(HTML_DIR.rglob("*.htm")) + list(HTML_DIR.rglob("*.html"))
    )
    pages_with_nav_and_headings = 0
    pages_without_nav = 0
    pages_without_headings = 0

    for number, html_path in enumerate(html_files, 1):
        content = read_text(html_path)

        # The Markdown docs index represents the virtual CHM root page, whose
        # breadcrumb is intentionally excluded by BreadcrumbParser.
        if html_path.name.casefold() == "mql5_guide.htm":
            heading_parser = HeadingParser()
            heading_parser.feed(content)
            index[path_key(("index.md",))].append(
                (html_path, heading_parser.headings, ["MQL5 Reference"])
            )
            pages_with_nav_and_headings += 1
            continue

        breadcrumb_parser = BreadcrumbParser()
        breadcrumb_parser.feed(content)
        crumbs = breadcrumb_parser.breadcrumb()

        if not crumbs:
            pages_without_nav += 1
            continue

        heading_parser = HeadingParser()
        heading_parser.feed(content)
        if not heading_parser.headings:
            pages_without_headings += 1

        for key in html_target_keys(
            html_path, crumbs, heading_parser.headings, breadcrumb_parser.complete
        ):
            index[key].append((html_path, heading_parser.headings, crumbs))
        pages_with_nav_and_headings += 1

        if number % 500 == 0:
            print(f"[HTML] {number}/{len(html_files)} scanned", flush=True)

    return index, len(html_files), pages_with_nav_and_headings, pages_without_nav, pages_without_headings


def repair_markdown(md_text: str, headings):
    lines = md_text.splitlines()
    changes = 0
    search_from = 0

    # Restore each source heading at its original level, in document order.
    for level, heading_text in headings:
        wanted = norm_text(heading_text).casefold()
        found = None
        for i in range(search_from, len(lines)):
            if lines[i].strip() and plain_markdown_line(lines[i]) == wanted:
                found = i
                break
        if found is None:
            continue

        replacement = "#" * level + " " + heading_text
        if lines[found].strip() != replacement:
            lines[found] = replacement
            changes += 1
        search_from = found + 1

    # Remove a duplicated plain-text title paragraph directly after the H1.
    h1_index = next(
        (i for i, line in enumerate(lines) if re.match(r"^\s*#\s+", line)),
        None,
    )
    if h1_index is not None:
        h1_text = plain_markdown_line(lines[h1_index])
        next_index = h1_index + 1
        while next_index < len(lines) and not lines[next_index].strip():
            next_index += 1
        if next_index < len(lines):
            if (
                not re.match(r"^\s*#{1,6}\s+", lines[next_index])
                and plain_markdown_line(lines[next_index]) == h1_text
            ):
                del lines[next_index]
                changes += 1

    result = "\n".join(lines)
    if md_text.endswith("\n"):
        result += "\n"
    return result, changes


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true",
                        help="write changes (default: dry run)")
    args = parser.parse_args()

    if not HTML_DIR.is_dir():
        raise SystemExit(f"HTML folder not found: {HTML_DIR}")
    if not MD_DIR.is_dir():
        raise SystemExit(f"Markdown folder not found: {MD_DIR}")

    print("[START] Indexing HTML pages by full td.nav breadcrumb (not H1/title)...", flush=True)
    index, html_count, indexed, no_nav, no_headings = html_heading_index()
    print(f"[HTML] Files scanned: {html_count}")
    print(f"[HTML] Pages indexed (breadcrumb + heading structure): {indexed}")
    print(f"[HTML] Pages without usable breadcrumb: {no_nav}")
    print(f"[HTML] Pages without heading structure: {no_headings}")
    print(f"[HTML] Distinct target paths: {len(index)}")

    md_files = sorted(
        p for p in MD_DIR.rglob("*.md")
        if p.name.lower() != "readme.md"
    )

    matched = unmatched = ambiguous = changed_files = changed_lines = 0
    planned = []
    matched_examples = []
    ambiguous_paths = []

    for number, md_path in enumerate(md_files, 1):
        relative = md_path.relative_to(MD_DIR)
        key = path_key(relative.parts)
        candidates = index.get(key, [])

        if len(candidates) == 0:
            unmatched += 1
            continue
        if len(candidates) > 1:
            ambiguous += 1
            ambiguous_paths.append((str(relative), len(candidates)))
            continue

        html_path, headings, crumbs = candidates[0]
        matched += 1
        if len(matched_examples) < 12:
            matched_examples.append((str(relative), html_path.name, " / ".join(crumbs)))

        original = read_text(md_path)
        repaired, changes = repair_markdown(original, headings)
        if changes:
            changed_files += 1
            changed_lines += changes
            planned.append((md_path, original, repaired))
            print(f"[CHANGE] {relative} <- {html_path.name}: {changes} heading/duplicate change(s)", flush=True)

        if number % 500 == 0:
            print(f"[MD] {number}/{len(md_files)} scanned", flush=True)

    print("\n--- Sample exact breadcrumb matches ---")
    for md_name, html_name, breadcrumb in matched_examples:
        print(f"[MATCH] {md_name} <- {html_name} | {breadcrumb}")

    print("\n--- Summary ---")
    print(f"Markdown files scanned: {len(md_files)}")
    print(f"Matched by exact breadcrumb path: {matched}")
    print(f"Unmatched: {unmatched}")
    print(f"Ambiguous exact paths: {ambiguous}")
    print(f"Files needing changes: {changed_files}")
    print(f"Total heading/duplicate changes: {changed_lines}")

    print("\n--- Ambiguous exact paths ---")
    if ambiguous_paths:
        for md_name, candidate_count in ambiguous_paths:
            print(f"[AMBIGUOUS] {md_name} <- {candidate_count} HTML pages")
    else:
        print("None")

    if not args.apply:
        print("\nDRY RUN: no files were modified.")
        print("Review the exact matches and changes before using --apply.")
        return

    if planned:
        print(f"\n[BACKUP] Creating backups under {BACKUP_DIR}", flush=True)
        BACKUP_DIR.mkdir(parents=True, exist_ok=True)
        for md_path, original, repaired in planned:
            relative = md_path.relative_to(MD_DIR)
            backup_path = BACKUP_DIR / relative
            backup_path.parent.mkdir(parents=True, exist_ok=True)
            if not backup_path.exists():
                backup_path.write_text(original, encoding="utf-8")
            md_path.write_text(repaired, encoding="utf-8")
            print(f"[WRITE] {relative}", flush=True)

    print(f"\nApplied changes to {changed_files} files.")
    print(f"Backups: {BACKUP_DIR}")


if __name__ == "__main__":
    main()
