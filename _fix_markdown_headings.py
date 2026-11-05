#!/usr/bin/env python3
"""Restore Markdown heading levels by matching CHM breadcrumb paths. Dry-run by default."""
from __future__ import annotations
import argparse, re, unicodedata
from collections import defaultdict
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent
HTML_DIR = ROOT / "chm-extracted"
MD_DIR = ROOT / "viewer" / "docs"
BACKUP_DIR = ROOT / "backup_before_heading_fix"

def norm(s):
    s = unicodedata.normalize("NFKC", s).replace("\xa0", " ")
    return re.sub(r"\s+", " ", s).strip().casefold()

def path_key(parts):
    return tuple(norm(p).replace(" ", "-") for p in parts if p)

def plain_markdown_line(line):
    s = re.sub(r"^\s{0,3}#{1,6}\s+", "", line.strip())
    s = re.sub(r"^\s*[-*+]\s+|\s*\d+[.)]\s+", "", s)
    s = re.sub(r"!\[([^\]]*)\]\([^)]*\)", r"\1", s)
    s = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", s)
    s = re.sub(r"`([^`]*)`", r"\1", s)
    return norm(re.sub(r"[*_~]", "", s))

class HeadingParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True); self.headings=[]; self.level=None; self.parts=[]
    def handle_starttag(self, tag, attrs):
        classes=dict(attrs).get("class","").split()
        m=next((re.fullmatch(r"p_H([1-6])",c) for c in classes if re.fullmatch(r"p_H([1-6])",c)),None)
        if tag.lower()=="p" and m: self.level=int(m.group(1)); self.parts=[]
    def handle_data(self,data):
        if self.level is not None: self.parts.append(data)
    def handle_endtag(self,tag):
        if tag.lower()=="p" and self.level is not None:
            t=re.sub(r"\s+"," ","".join(self.parts)).strip()
            if t: self.headings.append((self.level,t))
            self.level=None; self.parts=[]

class MetadataParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.in_title=False; self.title_parts=[]; self.in_nav=False; self.in_a=False
        self.a_parts=[]; self.links=[]; self.tail=[]
    def handle_starttag(self,tag,attrs):
        tag=tag.lower(); attrs=dict(attrs)
        if tag=="title": self.in_title=True
        if tag=="td" and "nav" in attrs.get("class","").split():
            self.in_nav=True; self.links=[]; self.tail=[]
        elif tag=="a" and self.in_nav: self.in_a=True; self.a_parts=[]
    def handle_data(self,data):
        if self.in_title: self.title_parts.append(data)
        if self.in_nav:
            (self.a_parts if self.in_a else self.tail).append(data)
    def handle_endtag(self,tag):
        tag=tag.lower()
        if tag=="title": self.in_title=False
        elif tag=="a" and self.in_nav and self.in_a:
            t=re.sub(r"\s+"," ","".join(self.a_parts)).strip()
            if t: self.links.append(t)
            self.in_a=False
        elif tag=="td" and self.in_nav: self.in_nav=False
    @property
    def title(self): return re.sub(r"\s+"," ","".join(self.title_parts)).strip()
    @property
    def parents(self): return self.links[1:] if self.links else []

def read_text(p):
    raw=p.read_bytes()
    for enc in ("utf-8-sig","cp1252","latin-1"):
        try: return raw.decode(enc)
        except UnicodeDecodeError: pass
    return raw.decode("utf-8",errors="replace")

def html_heading_index():
    index=defaultdict(list)
    files=sorted(list(HTML_DIR.rglob("*.htm"))+list(HTML_DIR.rglob("*.html")))
    for n,p in enumerate(files,1):
        html=read_text(p); meta=MetadataParser(); meta.feed(html)
        if not meta.title:
            continue
        # Markdown folders: parent breadcrumb / page title / page title.md.
        parts=meta.parents+[meta.title]
        key=path_key(parts+[meta.title+".md"])
        hp=HeadingParser(); hp.feed(html)
        if hp.headings: index[key].append((p,hp.headings))
        if n%500==0: print(f"[HTML] {n}/{len(files)}",flush=True)
    return index,len(files)

def repair_markdown(md_text,headings):
    lines=md_text.splitlines(); changes=0; start=0
    for level,title in headings:
        wanted=norm(title); found=None
        for i in range(start,len(lines)):
            if lines[i].strip() and plain_markdown_line(lines[i])==wanted:
                found=i; break
        if found is None: continue
        new="#"*level+" "+title
        if lines[found].strip()!=new: lines[found]=new; changes+=1
        start=found+1
    h1=next((i for i,l in enumerate(lines) if re.match(r"^\s*#\s+",l)),None)
    if h1 is not None:
        title=plain_markdown_line(lines[h1]); j=h1+1
        while j<len(lines) and not lines[j].strip(): j+=1
        if j<len(lines) and not re.match(r"^\s*#{1,6}\s+",lines[j]) and plain_markdown_line(lines[j])==title:
            del lines[j]; changes+=1
    result="\n".join(lines)
    if md_text.endswith("\n"): result+="\n"
    return result,changes

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--apply",action="store_true")
    args=ap.parse_args()
    if not HTML_DIR.is_dir(): raise SystemExit(f"HTML folder not found: {HTML_DIR}")
    if not MD_DIR.is_dir(): raise SystemExit(f"Markdown folder not found: {MD_DIR}")
    print("[START] Indexing CHM HTML breadcrumbs...",flush=True)
    index,nhtml=html_heading_index()
    print(f"[HTML] Scanned: {nhtml}; unique breadcrumb paths: {len(index)}",flush=True)
    mds=sorted(p for p in MD_DIR.rglob("*.md") if p.name.lower()!="readme.md")
    matched=unmatched=ambiguous=changed_files=changed_lines=0; planned=[]
    for n,md in enumerate(mds,1):
        key=path_key(md.relative_to(MD_DIR).parts)
        choices=index.get(key,[])
        if len(choices)!=1:
            if len(choices)>1:
                ambiguous+=1; print(f"[AMBIGUOUS] {md.relative_to(MD_DIR)} ({len(choices)} HTML)",flush=True)
            else: unmatched+=1
            continue
        html_path,headings=choices[0]; matched+=1
        original=read_text(md); fixed,count=repair_markdown(original,headings)
        if count:
            changed_files+=1; changed_lines+=count; planned.append((md,original,fixed))
            print(f"[CHANGE] {md.relative_to(MD_DIR)} <- {html_path.name}: {count}",flush=True)
        if n%500==0: print(f"[MD] {n}/{len(mds)}",flush=True)
    print("\n--- Summary ---")
    print(f"Markdown files scanned: {len(mds)}")
    print(f"Matched to HTML: {matched}")
    print(f"Unmatched: {unmatched}")
    print(f"Ambiguous matches: {ambiguous}")
    print(f"Files needing changes: {changed_files}")
    print(f"Total changes: {changed_lines}")
    if not args.apply:
        print("\nDRY RUN: no files modified. Review the [CHANGE] lines first.")
        return
    if planned:
        BACKUP_DIR.mkdir(parents=True,exist_ok=True)
        for md,original,fixed in planned:
            rel=md.relative_to(MD_DIR); backup=BACKUP_DIR/rel
            backup.parent.mkdir(parents=True,exist_ok=True)
            if not backup.exists(): backup.write_text(original,encoding="utf-8")
            md.write_text(fixed,encoding="utf-8")
            print(f"[WRITE] {rel}",flush=True)
    print(f"Applied {changed_files} files. Backups: {BACKUP_DIR}")

if __name__=="__main__": main()
