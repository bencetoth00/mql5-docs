#!/usr/bin/env python3
"""Build navigation and full-text search data for the MQL5 static viewer."""
from pathlib import Path
import json, re
ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / 'viewer' / 'docs'
DATA = ROOT / 'viewer' / 'data'
DATA.mkdir(parents=True, exist_ok=True)

def title_of(path, text):
    for line in text.splitlines():
        m = re.match(r'^#\s+(.+?)\s*#*$', line.strip())
        if m: return m.group(1).strip()
    return path.stem.replace('-', ' ').replace('_', ' ')

# Az eredeti CHM tartalomjegyzék teljes (akár 6 szintű) sorrendje.
# Másold a mql5-toc-order.json fájlt a viewer/data/ mappába.
TOC_FILE = DATA / "mql5-toc-order.json"
if not TOC_FILE.exists():
    raise FileNotFoundError(
        f"Hiányzik a teljes MQL5 tartalomjegyzék: {TOC_FILE}. "
        "Másold ide a mql5-toc-order.json fájlt."
    )

with TOC_FILE.open(encoding="utf-8") as f:
    TOC = json.load(f)

def norm(value):
    """Összehasonlításhoz kiszedi a szóközöket és írásjeleket."""
    return re.sub(r"[^a-z0-9]+", "", value.casefold())

def sort_tree_from_toc(node, toc_node):
    """A létrejött navigációs fa gyerekeit az eredeti CHM TOC szerint rendezi."""
    toc_children = toc_node.get("children", []) if toc_node else []
    ranks = {norm(item.get("title", "")): i for i, item in enumerate(toc_children)}

    children = node.get("children", [])
    children.sort(key=lambda child: (
        0 if norm(child.get("title", "")) in ranks else 1,
        ranks.get(norm(child.get("title", "")), 0),
        norm(child.get("title", ""))
    ))

    # A megfelelő CHM csomópontot cím alapján keressük meg.
    toc_by_title = {norm(item.get("title", "")): item for item in toc_children}
    for child in children:
        matching_toc = toc_by_title.get(norm(child.get("title", "")))
        sort_tree_from_toc(child, matching_toc)

files = sorted(DOCS.rglob("*.md"))

root = {'title': 'MQL5 Reference', 'children': []}

for f in files:
    rel = f.relative_to(DOCS).as_posix()
    text = f.read_text(encoding='utf-8', errors='replace')
    title = title_of(f, text)

    parts = rel.split('/')
    node = root

    for folder in parts[:-1]:
        node.setdefault('_map', {})

        if folder not in node['_map']:
            child = {
                'title': folder.replace('-', ' ').replace('_', ' '),
                'children': []
            }
            node['_map'][folder] = child
            node['children'].append(child)

        node = node['_map'][folder]

    # Ha a Markdown-fájl neve megegyezik a mappáéval,
    # akkor az adott mappa saját oldalaként kezeljük.
    if parts[-1].lower() == parts[-2].lower() + '.md' if len(parts) > 1 else False:
        node['title'] = title
        node['path'] = rel
    else:
        node.setdefault('children', []).append({
            'title': title,
            'path': rel
        })

def strip_md(s):
    s=re.sub(r'```.*?```', ' ', s, flags=re.S)
    s=re.sub(r'`([^`]*)`', r'\1', s)
    s=re.sub(r'!\[[^]]*\]\([^)]*\)', ' ', s)
    s=re.sub(r'\[([^]]+)\]\([^)]*\)', r'\1', s)
    s=re.sub(r'<[^>]+>', ' ', s)
    return re.sub(r'\s+', ' ', s).strip()
search=[]
for f in files:
    rel=f.relative_to(DOCS).as_posix(); raw=f.read_text(encoding='utf-8',errors='replace')
    title=title_of(f,raw); plain=strip_md(raw)
    search.append({'title':title,'path':rel,'text':plain,'excerpt':plain[:180]})

sort_tree_from_toc(root, TOC)

def clean(node):
    node.pop('_map',None)
    for c in node.get('children',[]): clean(c)
clean(root)
(DATA/'navigation.json').write_text(json.dumps(root['children'],ensure_ascii=False,separators=(',',':')),encoding='utf-8')
(DATA/'search-index.json').write_text(json.dumps(search,ensure_ascii=False,separators=(',',':')),encoding='utf-8')
print(f'Built navigation and search index for {len(files)} Markdown files.')
print(f'Navigation: {(DATA/"navigation.json").stat().st_size/1024:.1f} KB')
print(f'Search index: {(DATA/"search-index.json").stat().st_size/1024/1024:.2f} MB')