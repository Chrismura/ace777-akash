#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
archi_vivante.py — État VIVANT d'ACE777 pour la famille (ACE777)
Rôle : génère ARCHITECTURE_VIVANTE.md à partir de la RÉALITÉ du moment :
processus qui tournent, providers/tasks du routing, mission.json (bots/PnL),
journal des décisions, signets résumés. La famille le lit AVANT de valider
un choix — elle juge avec la vraie photo, pas un doc vieux de 8 jours.

Usage : python3 archi_vivante.py            # écrit ARCHITECTURE_VIVANTE.md
        python3 archi_vivante.py --stdout   # affiche sans écrire
"""

import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

BASE = Path.home() / "ace777-test-day1" / "Index_Maison"
OUT_FILE = BASE / "strategie" / "ARCHITECTURE_VIVANTE.md"
MISSION = BASE / "cockpit" / "mission.json"
ROUTING = Path.home() / "prise-ia" / "routing.json"
VEILLE_DIR = BASE
SIGNETS_CACHE = BASE / "strategie" / "SIGNETS_RESUMES.json"
FICHES_CACHE = BASE / "strategie" / "FICHES_OFFRES.json"
JOURNAL_RADAR = BASE / "strategie" / "journal_radar.log"

PROCESS_CLEFS = [
    ("hub", "hub_prise_ia"),
    ("pont cockpit", "cortana_cockpit_bridge"),
    ("radar", "vigie_live"),
    ("lecteur signets", "signets_lecture"),
    ("générateur fiches", "fiches_offres"),
    ("feed mission", "cockpit_mission_feed.py"),
    ("serveur cockpit", "17800"),
]

ROLES = {
    "alpha": "sniper (embuscade, ×13, revenge si claque)",
    "beta": "éclaireur (chatouille le marché, alimente Alpha)",
    "hulk": "gestionnaire de portefeuille (bag, escalier, courreur)",
}


def _pgrep(pat: str) -> bool:
    try:
        r = subprocess.run(["pgrep", "-f", pat], capture_output=True, text=True, timeout=10)
        return r.returncode == 0
    except Exception:
        return False


def _lire_json(p: Path) -> dict:
    try:
        if p.exists():
            return json.loads(p.read_text(encoding="utf-8"))
    except Exception:
        pass
    return {}


def _hms(iso: str) -> str:
    try:
        return iso.replace("T", " ")[:16] + "Z"
    except Exception:
        return str(iso)[:16]


def processus() -> list:
    lignes = []
    for nom, pat in PROCESS_CLEFS:
        etat = "✅" if _pgrep(pat) else "⛔"
        lignes.append(f"- {etat} {nom}")
    return lignes


def providers() -> list:
    lignes = []
    d = _lire_json(ROUTING)
    tasks = d.get("tasks", {})
    # tasks de décision/validation
    pour_famille = [t for t in tasks if any(
        k in t for k in ("famille", "audit", "juge", "strategie", "signets", "protocole")
    )]
    for t in sorted(pour_famille):
        rule = tasks[t]
        prov = rule.get("provider", "?")
        fb = rule.get("fallback", "")
        ligne = f"- `{t}` → {prov}" + (f" (repli {fb})" if fb else "")
        lignes.append(ligne)
    # providers branchés
    prov_list = d.get("providers", [])
    if isinstance(prov_list, list) and prov_list:
        ids = ", ".join(str(p.get("id", "?")) for p in prov_list[:8])
        lignes.append(f"- providers branchés : {ids}")
    return lignes


def mission() -> list:
    lignes = []
    d = _lire_json(MISSION)
    if not d:
        return ["- mission.json introuvable"]
    ts = _hms(d.get("ts", ""))
    lignes.append(f"- mission.json : {ts} · run `{d.get('run', '?')}` · alerte `{d.get('alert', '?')}`")
    pnl = d.get("comboPnl")
    if pnl is not None:
        arrow = "📉" if d.get("comboArrow") == "down" else ("📈" if d.get("comboArrow") == "up" else "➖")
        lignes.append(f"- PnL combiné : **{pnl:.2f} $** {arrow} (combo {d.get('comboPnl', '?')})")
    for nom, role in ROLES.items():
        b = d.get(nom) or {}
        bp = b.get("pnl")
        fills = b.get("fills", 0)
        skips = b.get("skips", 0)
        extra = f"· {fills} fills · {skips} skips" if nom != "hulk" else f"· {fills} fills"
        pnl_txt = f"**{bp:+.2f} $**" if isinstance(bp, (int, float)) else "?"
        lignes.append(f"- {nom.upper()} ({role}) : {pnl_txt} {extra}")
    saison = d.get("saison")
    if isinstance(saison, dict):
        lignes.append(f"- Saison : {saison.get('saison', '?')} {saison.get('emoji', '')} · {str(saison.get('detail', ''))[:60]}")
    elif saison:
        lignes.append(f"- Saison : {str(saison)[:80]}")
    gard = d.get("gardienne") or {}
    if gard:
        voilure = gard.get("voilure")
        if voilure is not None:
            lignes.append(f"- ADA gardienne : voilure **{voilure}** · zone {gard.get('zone', '?')}")
    return lignes


def journal() -> list:
    lignes = []
    # journal radar : dernières alertes
    if JOURNAL_RADAR.exists():
        try:
            lignes_radar = [l.strip() for l in JOURNAL_RADAR.read_text(
                encoding="utf-8", errors="ignore").splitlines() if l.strip()][-4:]
            if lignes_radar:
                lignes.append("- Radar (dernières alertes) :")
                for l in lignes_radar:
                    lignes.append(f"  · {l[:100]}")
        except Exception:
            pass
    # intention en cours
    int_live = _lire_json(BASE / "strategie" / "journal_intention_live.json")
    if int_live:
        story = int_live.get("story") or []
        if story:
            lignes.append("- Intention en cours : " + " | ".join(str(s)[:60] for s in story[:3]))
    return lignes


def veille() -> list:
    lignes = []
    aujourdhui = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    p = VEILLE_DIR / f"VEILLE_HUB_{aujourdhui}.md"
    if not p.exists():
        return ["- VEILLE du jour : pas encore passée"]
    try:
        txt = p.read_text(encoding="utf-8", errors="ignore")
        section = None
        offres = []
        for l in txt.splitlines():
            if l.startswith("## "):
                section = l[3:].strip()
                lignes.append(f"- [{section}]")
            elif l.startswith("- ") and section:
                contenu = l[2:].strip()
                if section.startswith("Nouvelles offres"):
                    offres.append(contenu)
                else:
                    lignes.append("  · " + contenu[:90])
        # Échantillon des offres (pas les ~120 lignes brutes : ça noierait le contexte)
        if offres:
            for x in offres[:3]:
                lignes.append("  · " + x[:70])
            lignes.append(f"  … {len(offres)} offres/pépites détectées ce matin")
    except Exception:
        pass
    return lignes


def signets() -> list:
    lignes = []
    d = _lire_json(SIGNETS_CACHE)
    n = len(d.get("signets", {}))
    jours = d.get("jours", {})
    aujourdhui = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    if n:
        lignes.append(f"- {n} signets X résumés (quota aujourd'hui : {jours.get(aujourdhui, 0)}/50)")
    else:
        lignes.append("- Signets X : pas encore de résumé")
    f = _lire_json(FICHES_CACHE)
    nf = len(f.get("fiches", {}))
    if nf:
        lignes.append(f"- {nf} fiches IA d'offres en cache (quota 8/jour)")
    return lignes


def generer() -> str:
    aujourdhui = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M")
    blocs = [
        f"# ARCHITECTURE VIVANTE — ACE777 ({aujourdhui} UTC)",
        "",
        "> Document GÉNÉRÉ AUTOMATIQUEMENT à l'instant. La famille valide",
        "> en s'appuyant sur CE contexte, pas sur des documents figés.",
        "",
        "## Qui tourne en ce moment",
    ]
    blocs += processus()
    blocs += ["", "## Routage des tâches de décision", ""]
    blocs += providers()
    blocs += ["", "## État de la mission (bots + PnL)", ""]
    blocs += mission()
    blocs += ["", "## Veille du jour", ""]
    blocs += veille()
    blocs += ["", "## Mémoire chaude (journal + résumés)", ""]
    blocs += journal()
    blocs += signets()
    blocs += ["", "---", "Généré par archi_vivante.py — relancé à chaque validation."]
    return "\n".join(blocs)


def main():
    txt = generer()
    if "--stdout" in sys.argv:
        print(txt)
        return
    OUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUT_FILE.write_text(txt, encoding="utf-8")
    print(f"[OK] {OUT_FILE} ({len(txt)} caractères)")


if __name__ == "__main__":
    main()
