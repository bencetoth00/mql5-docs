const $ = (s) => document.querySelector(s);

let navData = [],
  searchData = [],
  currentDoc = "index.md";

const cleanPath = (p) =>
  decodeURIComponent(p).replace(/^\/+/, "").replace(/\\/g, "/");

function canonicalDocPath(path) {
  const aliases = [
    [/\/(AddArray)\/AddArray-\d+\.md$/i, "/AddArrayConst/AddArrayConst.md"],
    [/\/(InsertArray)\/InsertArray-\d+\.md$/i, "/InsertArrayConst/InsertArrayConst.md"],
    [/\/(AssignArray)\/AssignArray-\d+\.md$/i, "/AssignArrayConst/AssignArrayConst.md"],
    [/\/(CompareArray)\/CompareArray-\d+\.md$/i, "/CompareArrayConst/CompareArrayConst.md"],
    [/\/CArray\/Step\/Step-\d+\.md$/i, "/CArray/StepSet/StepSet.md"],
    [/\/CArrayObj\/FreeMode\/FreeMode-\d+\.md$/i, "/CArrayObj/FreeModeConst/FreeModeConst.md"],
    [/\/CList\/FreeMode\/FreeMode-\d+\.md$/i, "/CList/FreeModeSet/FreeModeSet.md"],
    [/\/CList\/FreeMode\/FreeMode\.md$/i, "/CList/FreeModeGet/FreeModeGet.md"],
    [/\/Basic-Class-CObject\/Prev\/Prev-\d+\.md$/i, "/Basic-Class-CObject/PrevNext/PrevNext.md"],
    [/\/Basic-Class-CObject\/Next\/Next-\d+\.md$/i, "/Basic-Class-CObject/NextSet/NextSet.md"],
  ];
  for (const [pattern, replacement] of aliases) {
    if (pattern.test(path)) return path.replace(pattern, replacement);
  }
  return path;
}

function titleFromPath(p) {
  return p.split("/").pop().replace(/\.md$/i, "").replace(/[-_]/g, " ");
}

function buildTree(items, host) {
  const ul = document.createElement("ul");
  ul.className = "tree-list";
  for (const item of items) {
    const li = document.createElement("li");
    li.className = "tree-item";
    const row = document.createElement("div");
    row.className = "tree-row";
    if (item.children?.length) {
      const t = document.createElement("button");
      t.className = "tree-toggle";
      t.textContent = "▾";
      t.onclick = () => {
        const c = li.querySelector(":scope > .tree-children");
        c.classList.toggle("collapsed");
        t.textContent = c.classList.contains("collapsed") ? "▸" : "▾";
      };
      row.append(t);
    } else {
      const spacer = document.createElement("span");
      spacer.style.width = "17px";
      row.append(spacer);
    }
    const a = document.createElement("a");
    a.className = "tree-link";
    a.textContent = item.title;
    a.href = item.path ? "?doc=" + encodeURIComponent(item.path) : "#";
    if (item.path) {
      a.onclick = (e) => {
        e.preventDefault();
        loadDoc(item.path);
        history.pushState({}, "", "?doc=" + encodeURIComponent(item.path));
        $("#sidebar").classList.remove("open");
      };
    }
    row.append(a);
    li.append(row);
    if (item.children?.length) {
      const child = document.createElement("div");
      child.className = "tree-children";
      buildTree(item.children, child);
      li.append(child);
    }
    ul.append(li);
  }
  host.append(ul);
}


function renderMarkdown(md, path) {
  const base = path.split("/").slice(0, -1).join("/");

  // Az első H1 címet megőrizzük, az utána közvetlenül
  // ismétlődő, azonos című bekezdést eltávolítjuk.
  const lines = md.replace(/^\uFEFF/, "").split(/\r?\n/);
  const h1Index = lines.findIndex((line) => /^#\s+/.test(line.trim()));

  if (h1Index !== -1) {
    const h1Text = lines[h1Index]
      .trim()
      .replace(/^#\s+/, "")
      .replace(/\s+#+$/, "")
      .trim();

    let next = h1Index + 1;

    while (next < lines.length && !lines[next].trim()) {
      next++;
    }

    if (
      next < lines.length &&
      lines[next].trim().replace(/^>\s*/, "") === h1Text
    ) {
      lines.splice(next, 1);
    }
  }

  md = lines.join("\n");

  const renderer = new marked.Renderer();

  renderer.link = (href, title, text) => {
    if (!href) return text;

    if (/^(https?:|mailto:|#|data:)/i.test(href))
      return `<a href="${href}" ${
        /^https?:/i.test(href)
          ? 'target="_blank" rel="noopener"'
          : ""
      }>${text}</a>`;

    const [file, hash] = href.split("#");

    if (file.endsWith(".md")) {
      const target = cleanPath((base ? base + "/" : "") + file);
      return `<a href="?doc=${encodeURIComponent(target)}${
        hash ? "#" + hash : ""
      }" data-doc="${target}">${text}</a>`;
    }

    return `<a href="${href}">${text}</a>`;
  };

  renderer.image = (href, title, text) => {
    const src = /^(https?:|data:)/i.test(href)
      ? href
      : "docs/" + cleanPath((base ? base + "/" : "") + href);

    return `<img src="${src}" alt="${text || ""}" ${
      title ? `title="${title}"` : ""
    } loading="lazy">`;
  };

  marked.setOptions({ renderer, gfm: true, breaks: false });

  return DOMPurify.sanitize(marked.parse(md));
}


async function loadDoc(path) {
  path = cleanPath(path || "index.md");
  if (!path.endsWith(".md")) path += ".md";
  path = canonicalDocPath(path);
  const query = new URLSearchParams(location.search);
  if (query.has("doc") && query.get("doc") !== path) {
    query.set("doc", path);
    history.replaceState({}, "", "?" + query.toString());
  }
  currentDoc = path;
  $("#content").innerHTML = '<p class="muted">Loading…</p>';
  try {
    const r = await fetch("docs/" + path, { cache: "no-store" });
    if (!r.ok) throw new Error("HTTP " + r.status);
    const md = await r.text();
    $("#content").innerHTML = renderMarkdown(md, path);
    $("#breadcrumbs").textContent = path
      .replace(/\.md$/, "")
      .split("/")
      .join(" / ");
    document.title = titleFromPath(path) + " · MQL5 Reference";
    $("#tree")
      .querySelectorAll(".tree-row")
      .forEach((x) => x.classList.remove("active"));
    const active = [...document.querySelectorAll("#tree a")].find(
      (a) => a.getAttribute("href") === "?doc=" + encodeURIComponent(path),
    );
    if (active) active.parentElement.classList.add("active");
    $("#content")
      .querySelectorAll("pre code")
      .forEach((el) => window.hljs?.highlightElement(el));
    if (location.hash)
      setTimeout(
        () =>
          document
            .getElementById(decodeURIComponent(location.hash.slice(1)))
            ?.scrollIntoView(),
        100,
      );
  } catch (e) {
    $("#content").innerHTML =
      `<h1>Page unavailable</h1><p>Could not load <code>${path}</code>.</p><p>${e.message}</p>`;
  }
}

function showResults(q) {
  const box = $("#searchResults");
  if (q.trim().length < 2) {
    box.classList.add("hidden");
    return;
  }
  const terms = q.toLowerCase().split(/\s+/).filter(Boolean);
  const scored = [];
  for (const d of searchData) {
    const title = d.title.toLowerCase(),
      text = d.text.toLowerCase();
    let score = 0;
    for (const t of terms) {
      if (title.includes(t)) score += 8;
      if (text.includes(t)) score += 1;
    }
    if (score) scored.push({ d, score });
  }
  scored.sort((a, b) => b.score - a.score);
  box.innerHTML = "";
  for (const { d } of scored.slice(0, 30)) {
    const a = document.createElement("a");
    a.className = "result";
    a.href = "?doc=" + encodeURIComponent(d.path);
    const strong = document.createElement("strong");
    strong.textContent = d.title;
    const small = document.createElement("small");
    small.textContent = d.path + " · " + d.excerpt;
    a.append(strong, small);
    a.onclick = (e) => {
      e.preventDefault();
      loadDoc(d.path);
      history.pushState({}, "", "?doc=" + encodeURIComponent(d.path));
      box.classList.add("hidden");
      $("#search").value = "";
    };
    box.append(a);
  }
  if (!scored.length)
    box.innerHTML = '<div class="result">No results found</div>';
  box.classList.remove("hidden");
}

async function init() {
  try {
    const [n, s] = await Promise.all([
      fetch("data/navigation.json", { cache: "no-store" }),
      fetch("data/search-index.json", { cache: "no-store" }),
    ]);
    navData = await n.json();
    searchData = await s.json();
    $("#tree").innerHTML = "";
    buildTree(navData, $("#tree"));
    const p = new URLSearchParams(location.search).get("doc") || "index.md";
    loadDoc(p);
  } catch (e) {
    $("#tree").innerHTML =
      '<p class="muted pad">Could not load navigation data. Run the build script first.</p>';
    $("#content").innerHTML = "<h1>Setup required</h1><p>" + e.message + "</p>";
  }
}

$("#search").addEventListener("input", (e) => showResults(e.target.value));

$("#search").addEventListener("keydown", (e) => {
  if (e.key === "Escape") $("#searchResults").classList.add("hidden");
  if (e.key === "Enter") {
    const first = $("#searchResults .result");
    if (first) first.click();
  }
});

document.addEventListener("keydown", (e) => {
  if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === "k") {
    e.preventDefault();
    $("#search").focus();
  }
});

$("#expandAll").onclick = () => {
  const items = [...document.querySelectorAll(".tree-children")];

  // Ha van becsukott elem, mindent kinyitunk.
  // Ha minden nyitva van, mindent becsukunk.
  const shouldExpand = items.some((x) =>
    x.classList.contains("collapsed")
  );

  items.forEach((x) => {
    x.classList.toggle("collapsed", !shouldExpand);
  });

  $("#expandAll").textContent = shouldExpand
    ? "Collapse all"
    : "Expand all";
};

$("#mobileMenu").onclick = () => $("#sidebar").classList.toggle("open");
window.addEventListener("popstate", () =>
  loadDoc(new URLSearchParams(location.search).get("doc") || "index.md"),
);
init();
