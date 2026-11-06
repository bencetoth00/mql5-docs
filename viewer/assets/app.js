const $ = (s) => document.querySelector(s);

function syncThemeToggle() {
  const button = $("#themeToggle");
  if (!button) return;
  const isDark = document.documentElement.dataset.theme === "dark";
  const text = uiText[currentLanguage] || uiText.en;
  button.textContent = isDark ? text.lightMode : text.darkMode;
  button.setAttribute("aria-pressed", String(isDark));
  button.setAttribute(
    "aria-label",
    isDark
      ? currentLanguage === "hu" ? "Váltás világos módra" : "Switch to light mode"
      : currentLanguage === "hu" ? "Váltás sötét módra" : "Switch to dark mode",
  );
}

let navData = [],
  searchData = [],
  navSequence = [],
  currentLanguage = "en",
  currentDoc = "index.md";

const uiText = {
  en: {
    documentation: "DOCUMENTATION",
    search: "Search functions, constants, examples…",
    source: "Official docs ↗",
    previous: "Previous",
    next: "Next",
    darkMode: "Dark mode",
    lightMode: "Light mode",
    reference: "MQL5 Reference",
    fallback: "This page is not translated yet. Showing the English version.",
  },
  hu: {
    documentation: "DOKUMENTÁCIÓ",
    search: "Függvények, konstansok, példák keresése…",
    source: "Hivatalos dokumentáció ↗",
    previous: "Előző",
    next: "Következő",
    darkMode: "Sötét mód",
    lightMode: "Világos mód",
    reference: "MQL5-referencia",
    fallback: "Ez az oldal még nincs lefordítva. Az angol változatot látod.",
  },
};

function docUrl(path) {
  const query = new URLSearchParams({ doc: path });
  if (currentLanguage !== "en") query.set("lang", currentLanguage);
  return "?" + query.toString();
}

function applyUiLanguage() {
  const text = uiText[currentLanguage];
  document.documentElement.lang = currentLanguage;
  $("#languageSelect").value = currentLanguage;
  $("#search").placeholder = text.search;
  $(".sidebar-head span").textContent = text.documentation;
  $(".source-link").textContent = text.source;
  syncThemeToggle();
}

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

function collectNavigation(items) {
  for (const item of items) {
    if (item.path && !navSequence.some((entry) => entry.path === item.path)) {
      navSequence.push({ path: item.path, title: item.title });
    }
    if (item.children?.length) collectNavigation(item.children);
  }
}

function findNavigationTrail(items, path, trail = []) {
  for (const item of items) {
    const nextTrail = [...trail, item.title];
    if (item.path === path) return nextTrail;
    if (item.children?.length) {
      const nested = findNavigationTrail(item.children, path, nextTrail);
      if (nested) return nested;
    }
  }
  return null;
}

function updatePageNavigation(path) {
  const hosts = [$("#pageNav"), $("#pageNavBottom")].filter(Boolean);
  if (!hosts.length) return;
  const index = navSequence.findIndex((item) => item.path === path);
  const neighbors = index < 0 ? [undefined, undefined] : [navSequence[index - 1], navSequence[index + 1]];
  for (const host of hosts) {
    host.replaceChildren();
    for (const [direction, item] of [
      ["previous", neighbors[0]],
      ["next", neighbors[1]],
    ]) {
    const link = document.createElement("a");
    link.className = `page-nav-link page-nav-${direction}`;
    link.setAttribute("aria-label", item ? `${direction}: ${item.title}` : `No ${direction} page`);
    if (item) {
      link.href = docUrl(item.path);
      const arrow = document.createElement("span");
      arrow.className = "page-nav-arrow";
      arrow.textContent = direction === "previous" ? "←" : "→";
      const text = document.createElement("span");
      text.className = "page-nav-text";
      const label = document.createElement("small");
      label.textContent =
        direction === "previous" ? uiText[currentLanguage].previous : uiText[currentLanguage].next;
      const title = document.createElement("strong");
      title.textContent = item.title;
      text.append(label, title);
      if (direction === "previous") link.append(arrow, text);
      else link.append(text, arrow);
      link.onclick = (event) => {
        event.preventDefault();
        history.pushState({}, "", link.href);
        loadDoc(item.path);
        window.scrollTo({ top: 0, behavior: "smooth" });
      };
    } else {
      link.classList.add("is-disabled");
      link.setAttribute("aria-disabled", "true");
      link.tabIndex = -1;
    }
      host.append(link);
    }
  }
}

function toggleTreePath(item, children, toggle) {
  if (!children.classList.contains("collapsed")) {
    children.classList.add("collapsed");
    toggle.textContent = "";
    return;
  }

  const pathBranches = new Set();
  let current = item;
  while (current) {
    const branch = current.querySelector(":scope > .tree-children");
    if (branch) pathBranches.add(branch);
    current = current.parentElement.closest(".tree-item");
  }

  document.querySelectorAll("#tree .tree-children").forEach((branch) => {
    const parentToggle = branch.parentElement.querySelector(
      ":scope > .tree-row > .tree-toggle",
    );
    const isExpanded = pathBranches.has(branch);
    branch.classList.toggle("collapsed", !isExpanded);
    parentToggle?.classList.toggle("expanded", isExpanded);
    if (parentToggle) parentToggle.textContent = isExpanded ? "â–¾" : "â–¸";
  });
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
        toggleTreePath(li, c, t);
        t.classList.toggle("expanded", !c.classList.contains("collapsed"));
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
    a.dataset.doc = item.path || "";
    a.href = item.path ? docUrl(item.path) : "#";
    if (item.path) {
      a.onclick = (e) => {
        e.preventDefault();
        loadDoc(item.path);
        history.pushState({}, "", docUrl(item.path));
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

function setActiveTreePath(path) {
  const tree = $("#tree");
  tree.querySelectorAll(".tree-children").forEach((children) => {
    children.classList.add("collapsed");
  });
  tree.querySelectorAll(".tree-toggle").forEach((toggle) => {
    toggle.classList.remove("expanded");
    toggle.textContent = "";
  });
  tree.querySelectorAll(".tree-row").forEach((row) => row.classList.remove("active"));

  const activeLink = [...tree.querySelectorAll(".tree-link")].find(
    (link) => link.dataset.doc === path,
  );
  if (!activeLink) return;
  const activeRow = activeLink.parentElement;
  activeRow.classList.add("active");

  let item = activeLink.closest(".tree-item");
  while (item) {
    const children = item.querySelector(":scope > .tree-children");
    if (children) {
      children.classList.remove("collapsed");
      item.querySelector(":scope > .tree-row > .tree-toggle").classList.add("expanded");
      item.querySelector(":scope > .tree-row > .tree-toggle").textContent = "";
    }
    item = item.parentElement.closest(".tree-item");
  }
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
      return `<a href="${docUrl(target)}${
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
  query.set("doc", path);
  if (currentLanguage === "en") query.delete("lang");
  else query.set("lang", currentLanguage);
  if (location.search !== "?" + query.toString())
    history.replaceState({}, "", "?" + query.toString());
  currentDoc = path;
  updatePageNavigation(path);
  $("#content").innerHTML = '<p class="muted">Loading…</p>';
  try {
    let fallbackToEnglish = false;
    let r = currentLanguage === "hu"
      ? await fetch("docs/hu/" + path, { cache: "no-store" })
      : await fetch("docs/" + path, { cache: "no-store" });
    if (!r.ok && currentLanguage !== "en") {
      fallbackToEnglish = true;
      r = await fetch("docs/" + path, { cache: "no-store" });
    }
    if (!r.ok) throw new Error("HTTP " + r.status);
    const md = await r.text();
    const fallbackNotice = fallbackToEnglish
      ? `<p class="translation-fallback">${uiText[currentLanguage].fallback}</p>`
      : "";
    $("#content").innerHTML = fallbackNotice + renderMarkdown(md, path);
    $("#breadcrumbs").textContent =
      findNavigationTrail(navData, path)?.join(" / ") || path.replace(/\.md$/, "").split("/").join(" / ");
    const pageTitle = navSequence.find((item) => item.path === path)?.title || titleFromPath(path);
    document.title = pageTitle + " · " + uiText[currentLanguage].reference;
    setActiveTreePath(path);
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
    a.href = docUrl(d.path);
    const strong = document.createElement("strong");
    strong.textContent = d.title;
    const small = document.createElement("small");
    small.textContent = d.path + " · " + d.excerpt;
    a.append(strong, small);
    a.onclick = (e) => {
      e.preventDefault();
      loadDoc(d.path);
      history.pushState({}, "", docUrl(d.path));
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
    const params = new URLSearchParams(location.search);
    const requestedLanguage = params.get("lang");
    currentLanguage = ["en", "hu"].includes(requestedLanguage)
      ? requestedLanguage
      : localStorage.getItem("mql5-reference-language") === "hu"
        ? "hu"
        : "en";
    applyUiLanguage();
    await loadLanguageData(currentLanguage);
    const p = params.get("doc") || "index.md";
    loadDoc(p);
  } catch (e) {
    $("#tree").innerHTML =
      '<p class="muted pad">Could not load navigation data. Run the build script first.</p>';
    $("#content").innerHTML = "<h1>Setup required</h1><p>" + e.message + "</p>";
  }
}

async function loadLanguageData(language) {
  const suffix = language === "hu" ? ".hu" : "";
  const [n, s] = await Promise.all([
    fetch(`data/navigation${suffix}.json`, { cache: "no-store" }),
    fetch(`data/search-index${suffix}.json`, { cache: "no-store" }),
  ]);
  if (!n.ok || !s.ok) throw new Error(`Could not load ${language} navigation data`);
    navData = await n.json();
    searchData = await s.json();
    navSequence = [];
    collectNavigation(navData);
    $("#tree").innerHTML = "";
    buildTree(navData, $("#tree"));
}

$("#search").addEventListener("input", (e) => showResults(e.target.value));

$("#languageSelect").addEventListener("change", async (event) => {
  currentLanguage = event.target.value;
  localStorage.setItem("mql5-reference-language", currentLanguage);
  applyUiLanguage();
  history.pushState({}, "", docUrl(currentDoc));
  try {
    await loadLanguageData(currentLanguage);
    loadDoc(currentDoc);
  } catch (error) {
    currentLanguage = "en";
    $("#languageSelect").value = "en";
    applyUiLanguage();
    await loadLanguageData("en");
    loadDoc(currentDoc);
  }
});

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

$("#themeToggle").addEventListener("click", () => {
  const nextTheme = document.documentElement.dataset.theme === "dark" ? "light" : "dark";
  document.documentElement.dataset.theme = nextTheme;
  localStorage.setItem("mql5-reference-theme", nextTheme);
  syncThemeToggle();
});
syncThemeToggle();

const sidebarLayout = document.querySelector(".layout");
const sidebarResize = $("#sidebarResize");
const sidebarMinWidth = 292;
const sidebarMaxWidth = 600;

function setSidebarWidth(width) {
  const maxWidth = Math.max(sidebarMinWidth, Math.min(sidebarMaxWidth, window.innerWidth - 420));
  const clampedWidth = Math.max(sidebarMinWidth, Math.min(maxWidth, width));
  sidebarLayout.style.setProperty("--sidebar-width", `${clampedWidth}px`);
  sidebarResize.setAttribute("aria-valuemin", String(sidebarMinWidth));
  sidebarResize.setAttribute("aria-valuemax", String(maxWidth));
  sidebarResize.setAttribute("aria-valuenow", String(clampedWidth));
  return clampedWidth;
}

const savedSidebarWidth = Number(localStorage.getItem("mql5-reference-sidebar-width"));
setSidebarWidth(savedSidebarWidth >= sidebarMinWidth ? savedSidebarWidth : sidebarMinWidth);

sidebarResize.addEventListener("pointerdown", (event) => {
  if (window.matchMedia("(max-width: 850px)").matches) return;
  event.preventDefault();
  sidebarLayout.classList.add("is-resizing");
  sidebarResize.setPointerCapture(event.pointerId);
});
sidebarResize.addEventListener("pointermove", (event) => {
  if (!sidebarResize.hasPointerCapture(event.pointerId)) return;
  setSidebarWidth(event.clientX);
});
sidebarResize.addEventListener("pointerup", (event) => {
  if (!sidebarResize.hasPointerCapture(event.pointerId)) return;
  sidebarResize.releasePointerCapture(event.pointerId);
  sidebarLayout.classList.remove("is-resizing");
  const width = getComputedStyle(sidebarLayout).getPropertyValue("--sidebar-width");
  localStorage.setItem("mql5-reference-sidebar-width", parseFloat(width));
});
sidebarResize.addEventListener("keydown", (event) => {
  if (event.key !== "ArrowLeft" && event.key !== "ArrowRight") return;
  event.preventDefault();
  const current = parseFloat(
    getComputedStyle(sidebarLayout).getPropertyValue("--sidebar-width"),
  );
  const delta = event.key === "ArrowRight" ? 20 : -20;
  localStorage.setItem("mql5-reference-sidebar-width", setSidebarWidth(current + delta));
});

$("#mobileMenu").onclick = () => $("#sidebar").classList.toggle("open");
window.addEventListener("popstate", async () => {
  const params = new URLSearchParams(location.search);
  const language = params.get("lang") === "hu" ? "hu" : "en";
  if (language !== currentLanguage) {
    currentLanguage = language;
    localStorage.setItem("mql5-reference-language", language);
    applyUiLanguage();
    await loadLanguageData(language);
  }
  loadDoc(params.get("doc") || "index.md");
});
init();
