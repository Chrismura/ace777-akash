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
import plistlib
import socket
import sys
import time
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

# FIX 03/11/2026 (audit V6) : cette carte testait des NOMS DE PROCESSUS (`pgrep`).
# Elle affichait 4 ⛔ alors que mission.json était frais à 1 min : « signets_lecture »
# et « fiches_offres » ne sont PAS des daemons (run-and-exit), et le feed mission
# vit DANS le pont cockpit. Un ⛔ faux détruit la confiance dans toute la carte.
# Désormais on juge LA DONNÉE PRODUITE : âge du produit vs cadence DÉCLARÉE par
# le plist (aucune constante ici : si la cadence change, la tolérance suit).
PRODUITS = [
    ("hub LLM", "~/prise-ia/heartbeat.json", "llm-gate-hub"),
    ("pont cockpit", "cockpit/mission.json", "cockpit-pont"),
    ("radar", "strategie/journal_radar.log", "vigie-live"),
    ("feed mission", "cockpit/hub.json", "hub-cockpit-feed"),
    ("lecteur signets", "strategie/SIGNETS_RESUMES.json", None),
    ("générateur fiches", "strategie/FICHES_OFFRES.json", "fiches-offres"),
    ("serveur cockpit", "PORT:17800", "cockpit-http"),
]

ROLES = {
    "alpha": "sniper (embuscade, ×13, revenge si claque)",
    "beta": "éclaireur (chatouille le marché, alimente Alpha)",
    "hulk": "gestionnaire de portefeuille (bag, escalier, courreur)",
}


def _cadence(label):
    """Tolérance LUE dans le plist — (secondes, texte). None = pas de cadence."""
    if not label:
        return None, "pas de cadence déclarée (organe non planifié)"
    p = BASE / "plists" / f"com.ace777.{label}.plist"
    try:
        d = plistlib.loads(p.read_bytes())
    except Exception:
        return None, f"plist introuvable ({p.name})"
    si = d.get("StartInterval")
    if si:
        tol = max(int(si) * 3, 300)
        return tol, f"toutes les {int(si)} s (tolérance ×3 = {tol // 60} min)"
    if d.get("StartCalendarInterval"):
        return 26 * 3600, "calendaire (tolérance 26 h)"
    if d.get("KeepAlive"):
        return 3600, "daemon (tolérance 60 min)"
    return None, "plist sans cadence"


def _age_txt(sec: float) -> str:
    return f"{sec / 60:.0f} min" if sec < 7200 else f"{sec / 3600:.1f} h"


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
    """Ce qui PRODUIT (la donnée), pas ce qui porte un nom de processus."""
    lignes = []
    n_ok = n_lent = n_muet = 0
    for nom, cible, label in PRODUITS:
        tol, txt = _cadence(label)
        if cible.startswith("PORT:"):
            port = int(cible.split(":", 1)[1])
            try:
                with socket.create_connection(("127.0.0.1", port), timeout=2):
                    joignable = True
            except Exception:
                joignable = False
            if joignable:
                n_ok += 1
                lignes.append(f"- ✅ {nom} · port {port} répond · {txt}")
            else:
                n_muet += 1
                lignes.append(f"- ⛔ {nom} · port {port} NE répond PAS · {txt}")
            continue
        p = Path(os.path.expanduser(cible)) if cible.startswith("~") else BASE / cible
        if not p.exists():
            n_muet += 1
            lignes.append(f"- ⛔ {nom} · `{p.name}` ABSENT · {txt}")
            continue
        age = max(0.0, time.time() - p.stat().st_mtime)
        if tol is None:
            lignes.append(f"- ⚪ {nom} · `{p.name}` {_age_txt(age)} · {txt}")
        elif age <= tol:
            n_ok += 1
            lignes.append(f"- ✅ {nom} · `{p.name}` {_age_txt(age)} · {txt}")
        elif age <= 2 * tol:
            n_lent += 1
            lignes.append(f"- ⚠️ {nom} · `{p.name}` {_age_txt(age)} (lent) · {txt}")
        else:
            n_muet += 1
            lignes.append(f"- ⛔ {nom} · `{p.name}` {_age_txt(age)} (PÉRIMÉ) · {txt}")
    lignes.append(f"- **{n_ok} frais · {n_lent} lents · {n_muet} muets** — "
                  "critère = la donnée produite, jamais le nom du processus")
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
        "## Ce qui produit en ce moment (donnée datée)",
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
