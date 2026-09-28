#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""carte_organes.py — CHECK-UP GLOBAL Phase 1 (GO V5 du 11/09, LECTURE SEULE).

Produit la carte complète des organes réels d'ACE777 :
  - combien il y en a vraiment (plists posés vs chargés launchd)
  - ce que fait chacun (docstring du script réel du plist)
  - fréquence attendue (StartInterval / StartCalendarInterval / KeepAlive du plist)
  - source de vérité : launchctl list (chargé ? PID vivant ? dernier code de sortie ?)
  - produit + criticité : fusion avec criticite_organes.json
  - surveillé par le chien ? (présence dans criticite_organes.json)
  - candidats « critiques NON surveillés » : à statuer par la famille (le script propose, ne décide pas)

Lecture seule sur le système. N'écrit QUE le rapport CARTE_ORGANES_<date>.md.
Stdlib uniquement. Aucune clé, aucun ordre.
"""
import json
import os
import plistlib
import subprocess
from datetime import datetime, timezone
from pathlib import Path

HOME = Path.home()
BASE_DIR = Path(__file__).resolve().parent.parent.parent          # ~/ace777-test-day1
INDEX_MAISON = BASE_DIR / "Index_Maison"
PLISTS_DIRS = [HOME / "Library" / "LaunchAgents", INDEX_MAISON / "plists"]
CRITICITE_PATH = INDEX_MAISON / "strategie" / "criticite_organes.json"
RAPPORT = INDEX_MAISON / f"CARTE_ORGANES_{datetime.now(timezone.utc).strftime('%Y%m%d')}.md"
MAX_LIGNE = 90  # longueur max description


def launchd_etat():
    """label -> dict(pid, status). Vérité machine."""
    etat = {}
    try:
        out = subprocess.run(["launchctl", "list"], capture_output=True,
                             text=True, timeout=15).stdout
        for ligne in out.splitlines():
            parts = ligne.strip().split("\t")
            if len(parts) >= 3:
                etat[parts[-1].strip()] = {"pid": parts[0].strip(),
                                           "status": parts[1].strip()}
    except Exception:
        pass
    return etat


def charger_criticite():
    try:
        with open(CRITICITE_PATH, encoding="utf-8") as f:
            data = json.load(f)
        return {o["organe"]: o for o in data.get("organes", [])}
    except Exception:
        return {}


def derriere_lancement(args):
    """Retourne le chemin du script réel (.py/.sh) dans ProgramArguments."""
    for a in args or []:
        if isinstance(a, str) and (a.endswith(".py") or a.endswith(".sh")):
            return a
    return None


def decrire_script(chemin):
    """1re ligne utile de la docstring/commentaire du script = rôle."""
    if not chemin or not Path(chemin).exists():
        return "(script introuvable)"
    try:
        texte = Path(chemin).read_text(encoding="utf-8", errors="ignore")[:4000]
        lignes = []
        en_doc = False
        for ln in texte.splitlines():
            s = ln.strip()
            if s.startswith('"""') or s.startswith("'''"):
                if en_doc:
                    break
                en_doc = True
                s = s.lstrip('"\'' ).strip()
                if s:
                    lignes.append(s)
                continue
            if en_doc and s:
                lignes.append(s)
                if len(lignes) >= 3:
                    break
        if not lignes:
            for ln in texte.splitlines():
                s = ln.strip()
                if s.startswith("#") and not s.startswith("#!"):
                    lignes.append(s.lstrip("# ").strip())
                    if len(lignes) >= 2:
                        break
        for l in lignes:
            l = l.replace("Rôle :", "").replace("Rôle :", "").strip(" -:")
            if l and not l.startswith("*"):
                return (l[:MAX_LIGNE] + "…") if len(l) > MAX_LIGNE else l
    except Exception:
        pass
    return "(indescriptible)"


def freq_humaine(d):
    if d.get("StartInterval"):
        return f"{int(d['StartInterval'])} s"
    cal = d.get("StartCalendarInterval")
    if cal:
        if isinstance(cal, dict):
            h, m = cal.get("Hour", 0), cal.get("Minute", 0)
            return f"quotidien {h:02d}:{m:02d}"
        if isinstance(cal, list) and cal:
            e = cal[0]
            return f"calendrier (H={e.get('Hour','?')})"
    if d.get("KeepAlive"):
        return "permanent (daemon)"
    if d.get("RunAtLoad"):
        return "au chargement seulement"
    return "?"


def main():
    etat = launchd_etat()
    crit = charger_criticite()

    organes = {}
    for pdir in PLISTS_DIRS:
        if not pdir.exists():
            continue
        for pf in sorted(pdir.glob("com.ace777.*.plist")):
            nom = pf.stem.replace("com.ace777.", "")
            try:
                with open(pf, "rb") as f:
                    d = plistlib.load(f)
            except Exception:
                d = {}
            script = derriere_lancement(d.get("ProgramArguments"))
            label = d.get("Label", pf.stem)
            le = etat.get(label)
            organes[nom] = {
                "nom": nom,
                "plist": pf.name,
                "emplacement": "LaunchAgents" if "LaunchAgents" in str(pdir) else "plists/(archive)",
                "script": script or "(aucun)",
                "role": decrire_script(script),
                "freq": freq_humaine(d),
                "keepalive": bool(d.get("KeepAlive")),
                "charge": le is not None,
                "pid": (le or {}).get("pid", "-"),
                "status": (le or {}).get("status", "-"),
                "surveille": nom in crit,
                "produit": crit.get(nom, {}).get("chemin_pouls_ou_produit", "—"),
                "criticite": crit.get(nom, {}).get("criticite", "MINEUR"),
            }

    # Dernier rapport du chien = fraîcheur vue par le chien
    fraicheur_chien = {}
    try:
        with open(INDEX_MAISON / "thermo" / "CHIEN_RAPPORT.json", encoding="utf-8") as f:
            r = json.load(f)
        for v in r.get("vivants", []):
            fraicheur_chien[v["organe"]] = f"vivant ({v['age_sec']}s)"
        for v in r.get("vieillissants", []):
            fraicheur_chien[v["organe"]] = f"VIEUX ({v['age_sec']}s)"
    except Exception:
        pass

    total = len(organes)
    charges = sum(1 for o in organes.values() if o["charge"])
    grise = [o["nom"] for o in organes.values() if not o["charge"]]
    surveilles = [o for o in organes.values() if o["surveille"]]
    crashes = [o["nom"] for o in organes.values()
               if o["charge"] and o["status"] not in ("0", "-")]

    # Candidats « critiques NON surveillés » : proposition heuristique, la famille tranche.
    MOTS_VITAUX = ("cockpit", "hub", "disjoncteur", "hulk", "paper", "trading",
                   "alert", "alarm", "vortex", "vigie", "satellite", "ofi",
                   "state", "sante", "gitpush", "backup", "watchdog", "sentinel",
                   "superviseur", "cortana", "archi", "thermo", "signal")
    a_statuer = []
    for o in organes.values():
        if o["surveille"] or not o["charge"]:
            continue
        grain = (o["nom"] + " " + o["script"]).lower()
        if o["keepalive"] or any(m in grain for m in MOTS_VITAUX):
            a_statuer.append(o)

    lignes = []
    a = lignes.append
    a(f"# 🗺️ CARTE DES ORGANES ACE777 — CHECK-UP GLOBAL Phase 1")
    a(f"*Généré le {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')} · GO V5 Christophe · LECTURE SEULE (aucun changement)*")
    a(f"*Sources : `launchctl list` (vérité machine) · plists réels (fréquence/lancement) · docstrings des scripts (rôle) · `criticite_organes.json` (surveillance chien) · `CHIEN_RAPPORT.json` (fraîcheur)*")
    a("")
    a("## 📊 Chiffres")
    a("")
    a(f"- **Organes réels (plists posés) : {total}** — chargés launchd : **{charges}** · zone grise (posés non chargés) : **{len(grise)}** ({', '.join(grise) or '—'})")
    a(f"- **Surveillés par le chien : {len(surveilles)}** (dont le chien lui-même) · **non surveillés : {total - len(surveilles)}**")
    a(f"- Candidats critiques NON surveillés (à statuer famille) : **{len(a_statuer)}**")
    a(f"- Organes chargés dont le DERNIER run a échoué (status ≠ 0) : **{len(crashes)}** {('→ ' + ', '.join(crashes)) if crashes else ''}")
    a("")
    a("## 🐕 Table 1 — les organes SURVEILLÉS par le chien")
    a("")
    a("| organe | rôle | fréquence | produit surveillé | fraîcheur (dernier rapport chien) | chargé | dernier statut |")
    a("|---|---|---|---|---|---|---|")
    for o in sorted(surveilles, key=lambda x: x["nom"]):
        a(f"| **{o['nom']}** | {o['role']} | {o['freq']} | `{o['produit']}` | {fraicheur_chien.get(o['nom'], '—')} | {'✅' if o['charge'] else '❌'} | {o['status']} |")
    a("")
    a("## 📋 Table 2 — les organes NON surveillés (cartographie brute)")
    a("")
    a("| organe | rôle | fréquence | script | chargé | dernier statut | criticité proposée |")
    a("|---|---|---|---|---|---|---|")
    for o in sorted((x for x in organes.values() if not x["surveille"]),
                    key=lambda x: (x["nom"] not in [y["nom"] for y in a_statuer], x["nom"])):
        prop = "⚠️ **à statuer (vital ?)**" if o in a_statuer else "MINEUR ?"
        a(f"| {o['nom']} | {o['role']} | {o['freq']} | `{os.path.basename(str(o['script']))}` | {'✅' if o['charge'] else '❌ gris'} | {o['status']} | {prop} |")
    a("")
    a("## ⚠️ Liste demandée — organes CRITIQUES potentiels NON surveillés par le chien")
    a("")
    a("*Proposition heuristique (KeepAlive ou mots vitaux dans le nom/script). La famille tranche : ajouter au chien, ou classer MINEUR officiellement.*")
    a("")
    for o in sorted(a_statuer, key=lambda x: x["nom"]):
        a(f"- **{o['nom']}** — {o['role']} · fréquence {o['freq']} · statut launchd {o['status']}")
    a("")
    a("---")
    a("*Carte produite par `Index_Maison/scripts/carte_organes.py` (lecture seule) · GO V5 · prochaine étape possible : la famille statue sur les « à statuer » puis on complète `criticite_organes.json` (V6).*")

    RAPPORT.write_text("\n".join(lignes), encoding="utf-8")
    print(f"Carte écrite : {RAPPORT}")
    print(f"Organes : {total} | chargés : {charges} | gris : {len(grise)} | surveillés chien : {len(surveilles)} | à statuer : {len(a_statuer)} | crashes : {len(crashes)}")


if __name__ == "__main__":
    main()
