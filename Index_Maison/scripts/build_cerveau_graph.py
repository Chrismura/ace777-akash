#!/usr/bin/env python3
"""
Scan Index_Maison (+ OUTBOX) → cerveau galactique.
Forme cerveau inchangée. Familles = lumière. Liens = qualité (fresh/weight).
  python3 Index_Maison/scripts/build_cerveau_graph.py
"""
from __future__ import annotations

import json
import math
import re
import time
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path("/Users/christophe/ace777-test-day1/Index_Maison")
OUT = ROOT / "graph_cerveau"
OUTBOX = ROOT / "OUTBOX_OBSIDIAN"
LINK_RE = re.compile(r"\[\[([^\]|#]+)(?:[#|][^\]]*)?\]\]")

SKIP_DIRS = {"node_modules", ".git", "cockpit", "thermo", "graph_cerveau"}

# Lumière famille (RGBA soft — pas plat « vieux jeu »)
FAMILIES = {
    "attention": {"label": "Attention", "rgba": [255, 190, 220, 0.55]},
    "evaluations": {"label": "Évaluations", "rgba": [180, 230, 255, 0.55]},
    "protocoles": {"label": "Protocoles", "rgba": [255, 210, 150, 0.52]},
    "journal": {"label": "Journal", "rgba": [190, 255, 200, 0.52]},
    "cockpit": {"label": "Cockpit", "rgba": [210, 190, 255, 0.55]},
    "architecture": {"label": "Architecture", "rgba": [170, 240, 255, 0.52]},
    "index": {"label": "Index / commandes", "rgba": [200, 255, 180, 0.5]},
    "plan": {"label": "Plan / vol", "rgba": [255, 230, 170, 0.52]},
    "cerveau": {"label": "Cerveau / graph", "rgba": [255, 180, 240, 0.58]},
    "autre": {"label": "Autre", "rgba": [200, 210, 230, 0.38]},
}

# Fraîcheur : < 36h = vif, < 7j = ok, sinon lent
FRESH_SEC = 36 * 3600
OK_SEC = 7 * 24 * 3600


def family_of(path: Path | None, name: str) -> str:
    n = name.upper()
    s = str(path).replace("\\", "/") if path else ""
    if "A_Mon_Attention" in s or "ATTENTION" in n:
        return "attention"
    if "Evaluations" in s or n.startswith("EVAL"):
        return "evaluations"
    if "PROTOCOLE" in n or "PROTOCOL" in n:
        return "protocoles"
    if "Journal" in n or "Cahier" in s or "JOURNAL" in n:
        return "journal"
    if "COCKPIT" in n or "CORTANA" in n:
        return "cockpit"
    if "architecture" in s or "ARCHITECTURE" in n:
        return "architecture"
    if "CERVEAU" in n or "GRAPH" in n or "SYNAPSE" in n:
        return "cerveau"
    if "PLAN" in n or "VOL" in n or "MISSION" in n:
        return "plan"
    if "INDEX" in n or "COMMANDES" in n or "CONSOLE" in n or "MEMOIRE" in n:
        return "index"
    return "autre"


def norm(name: str) -> str:
    n = name.strip().replace("\\", "/")
    n = Path(n).name
    if n.endswith(".md"):
        n = n[:-3]
    return n.strip()


def iter_md(base: Path):
    if not base.exists():
        return
    for p in base.rglob("*.md"):
        if any(part in SKIP_DIRS for part in p.parts):
            continue
        yield p


def edge_quality(weight: int, age_sec: float | None) -> dict:
    """q 0..1 · state ok|slow — pour étincelle étoile vs rouge."""
    w_score = min(1.0, math.log2(1 + weight) / 3.0)
    if age_sec is None:
        fresh = 0.45
    elif age_sec <= FRESH_SEC:
        fresh = 1.0
    elif age_sec <= OK_SEC:
        fresh = 0.65
    else:
        fresh = 0.2
    q = round(0.45 * w_score + 0.55 * fresh, 3)
    state = "ok" if q >= 0.48 else "slow"
    return {"q": q, "state": state}


def main() -> int:
    edges = defaultdict(int)
    nodes = set()
    node_fam: dict[str, str] = {}
    node_mtime: dict[str, float] = {}
    sources = 0
    now = time.time()

    for base in (ROOT, OUTBOX):
        for path in iter_md(base):
            try:
                text = path.read_text(encoding="utf-8", errors="ignore")
                mtime = path.stat().st_mtime
            except Exception:
                continue
            src = norm(path.stem)
            if not src:
                continue
            sources += 1
            nodes.add(src)
            node_fam[src] = family_of(path, src)
            node_mtime[src] = max(node_mtime.get(src, 0), mtime)
            for m in LINK_RE.finditer(text):
                dst = norm(m.group(1))
                if not dst or dst == src:
                    continue
                nodes.add(dst)
                node_fam.setdefault(dst, family_of(None, dst))
                a, b = sorted((src, dst))
                edges[(a, b)] += 1

    deg = defaultdict(int)
    for (a, b), w in edges.items():
        deg[a] += w
        deg[b] += w

    node_list = sorted(nodes, key=lambda n: (-deg[n], n))
    N = max(1, len(node_list))
    max_d = max(deg.values()) or 1
    placed = {}
    for i, name in enumerate(node_list):
        t = i / N
        lobe = -1 if (i % 2 == 0) else 1
        angle = t * math.pi * 1.7 + (0.3 if lobe > 0 else 0)
        r = 0.22 + 0.28 * (1 - deg[name] / max_d) ** 0.5
        jx = 0.04 * math.sin(i * 1.7)
        jy = 0.05 * math.cos(i * 2.3)
        x = 0.5 + lobe * (0.18 + r * abs(math.cos(angle))) * 0.85 + jx
        y = 0.48 + r * math.sin(angle) * 0.95 + jy
        x = min(0.96, max(0.04, x))
        y = min(0.96, max(0.04, y))
        fam = node_fam.get(name, "autre")
        age = (now - node_mtime[name]) if name in node_mtime else None
        placed[name] = {
            "id": name,
            "x": round(x, 4),
            "y": round(y, 4),
            "deg": deg[name],
            "hub": deg[name] >= 8,
            "fam": fam,
            "rgba": FAMILIES.get(fam, FAMILIES["autre"])["rgba"],
            "ageSec": None if age is None else int(age),
        }

    edge_list = []
    for (a, b), w in sorted(edges.items(), key=lambda kv: -kv[1]):
        ages = [now - node_mtime[n] for n in (a, b) if n in node_mtime]
        age = min(ages) if ages else None
        qinfo = edge_quality(w, age)
        edge_list.append(
            {
                "a": a,
                "b": b,
                "w": w,
                "q": qinfo["q"],
                "state": qinfo["state"],
            }
        )

    ok_n = sum(1 for e in edge_list if e["state"] == "ok")
    slow_n = len(edge_list) - ok_n

    payload = {
        "ts": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%MZ"),
        "families": FAMILIES,
        "nodes": [placed[n] for n in node_list if n in placed],
        "edges": edge_list[:2500],
        "stats": {
            "files": sources,
            "nodes": len(node_list),
            "edges": len(edge_list),
            "linksOk": ok_n,
            "linksSlow": slow_n,
        },
    }

    OUT.mkdir(parents=True, exist_ok=True)
    js = "window.__CERVEAU__ = " + json.dumps(payload, ensure_ascii=False) + ";\n"
    (OUT / "data.js").write_text(js, encoding="utf-8")
    (OUT / "data.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    dest = OUTBOX / "graph_cerveau"
    dest.mkdir(parents=True, exist_ok=True)
    for name in ("data.js", "data.json"):
        (dest / name).write_text((OUT / name).read_text(encoding="utf-8"), encoding="utf-8")

    print(
        f"CERVEAU_OK nodes={payload['stats']['nodes']} edges={payload['stats']['edges']} "
        f"ok={ok_n} slow={slow_n}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
