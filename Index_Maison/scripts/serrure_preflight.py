#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""SERRURE PREFLIGHT — la porte au boot, pas un passager du moteur.

Incident Maladie des Organes (10/09, GO Christophe V1+V2) :
  données = fail-open (JAMAIS bloquer une sortie) / CONFIGURATION = fail-fast
  (ne plus naître incomplet). Ce script ne trade jamais, ne bloque jamais un
  ordre, ne touche jamais à une sortie : il vérifie la configuration AVANT le
  boot des agents décisionnaires et crie NOMMANT l'organe malade.

LEÇON DU 10/09 17h (faux négatifs de la v1, autopsie demandée par Christophe :
« c'est un problème récurrent ») : on ne dit PAS « absent » avant d'avoir
cherché PARTOUT. Les fiches md (OBSIDIAN FICHE_SETUP_*) existent pour TOUTES
les paires actives — ce qui manque pour 4 d'entre elles, c'est le calib JSON
du moteur. Cortana est VIVANTE (data/cortana_analysis.json frais). La serrure
v2 distingue donc : fiche md absente (rien trouvé nulle part) ≠ fiche md
présente sans calib moteur (fiche non calibrée) ≠ contradiction famille/moteur.

Contrôles (CHANTIER_CHECKUP_GLOBAL_20260910 §2) :
  1. Fiches actives : fiche md absente → ALARME (organe orphelin) ; calib
     moteur incomplet sur fiche EXISTANTE → FATAL (V1) ; contradiction famille
     (verdict NON dans paires_croisement.json) vs présence dans PAPER_PAIRS
     → ALARME nommée (décision famille, jamais tranchée par la serrure).
     Exception documentée : BTC/ETH sans mur_bid_med (banc de preuve, l.1858).
  2. TODO interdits — moteur HULK (paper_diprip.py) : FATAL. Agents vivants
     (cortana_analyzer.py) : ALARME = branches V3 à câbler.
  3. Cerveaux gelés — cortana_analysis.json (Index_Maison/data/) et
     data/fiches_analyse/*.json non modifiés > 7 j → ALARME.
  4. Registre de naissance — md5 déclarés conformes → ALARME sinon. La serrure
     se déclare elle-même (SEUL fichier qu'elle écrit).

Usage :
  python3 serrure_preflight.py            # rapport, exit 0/1/2
  python3 serrure_preflight.py --strict   # mode boot agent décisionnaire
  python3 serrure_preflight.py --json     # sortie machine pour la veilleuse
  python3 serrure_preflight.py --hulk-root CHEMIN   # test sur copie (boot troué volontaire)

Exit : 0 = OK · 1 = alarmes (non bloquant) · 2 = FATAL (refus de boot)
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

INDEX = Path(__file__).resolve().parent.parent          # Index_Maison/
HULK_DEFAULT = INDEX.parent / "hulk-mexc"
REGISTRE = INDEX / "strategie" / "REGISTRE_SYNAPSES.json"
CROISEMENT = HULK_DEFAULT / "strategie" / "paires_croisement.json"

# S1 — les 11 clés lues par paper_diprip.py dans calib (extraction EXHAUSTIVE
# re-faite le 10/09 17h : tous les lecteurs _cal.get / prof.get("calib")).
CLES_OBLIGATOIRES = [
    "mode_entree",                # l.89   mode_entree()
    "impulse_pct",                # l.436  seuil impulsion
    "cooling_dd_pct",             # l.437  seuil cooling
    "dip_pct",                    # l.490  plancher dip
    "rip_pct",                    # l.491  plancher rip
    "stop_pct",                   # l.492  plancher stop
    "cooling_pullback_frac",      # l.507  pullback cooling
    "impulse_pullback_min_pct",   # l.511  pullback impulse
    "mise_max_pct_mur",           # l.1860 plafond de mise
    "trail_arm_pct",              # l.2213 trailing arm (V4 Option A)
    "trail_giveback_pct",         # l.2214 trailing giveback (V4 Option A)
]

# Clé de fiche (hors calib) lue par le moteur, avec exception documentée :
# BTC/ETH = banc de preuve, plafond mur fail-open (l.1858 `if med:`).
CLES_FICHE = [("mur_bid_med", {"BTCUSDT", "ETHUSDT"})]

TODO_RE = re.compile(r"\b(TODO|FIXME|XXX|PLACEHOLDER)\b")

# Contrôle 2 : fichiers de décision par agent.
# FATAL = TODO interdit dès maintenant. ALARME = maladie connue (V3 en cours).
HULK_DECISION_FATAL = ["scripts/paper_diprip.py"]        # moteur HULK
AGENTS_ALARME = [("Index_Maison/scripts/cortana_analyzer.py", "branches V3 à câbler")]

# Contrôle 3 : cerveaux — chemins VÉRIFIÉS le 10/09 17h (pas supposés).
CERVEAUX = [
    ("cortana analyses", INDEX / "data" / "cortana_analysis.json", 7 * 86400),
    ("fiches_analyse", INDEX / "data" / "fiches_analyse", 7 * 86400),  # dossier
]

JOUR = "%Y-%m-%dT%H:%M:%SZ"


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime(JOUR)


def md5_of(path: Path) -> str:
    h = hashlib.md5()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def load_env(hulk: Path) -> dict[str, str]:
    cfg: dict[str, str] = {}
    env = hulk / "config" / "defaults.env"
    if env.exists():
        for line in env.read_text().splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, _, v = line.partition("=")
                cfg[k.strip()] = v.strip()
    return cfg


def pick_pairs_actives(hulk: Path) -> list[str]:
    """Reproduit pick_pairs() du moteur : PAPER_PAIRS moins tier B hors extra."""
    cfg = load_env(hulk)
    extra = {p.strip().upper() for p in (cfg.get("PAPER_EXTRA_PAIRS") or "").split(",") if p.strip()}
    inv: dict[str, dict] = {}
    invp = hulk / "data" / "universe_mexc_inventory.csv"
    if invp.exists():
        import csv
        with invp.open() as f:
            for r in csv.DictReader(f):
                p = (r.get("pair") or "").strip().upper()
                if p:
                    inv[p] = r
    out: list[str] = []
    for p in (cfg.get("PAPER_PAIRS", "") or "").split(","):
        p = p.strip().upper()
        if not p:
            continue
        t = (inv.get(p) or {}).get("tier", "A")
        if t == "B" and p not in extra:
            continue
        out.append(p)
    return out


def verdict_famille(pair: str) -> str | None:
    """Verdict deepdive famille depuis paires_croisement.json (lecteur, jamais juge)."""
    try:
        d = json.loads(CROISEMENT.read_text())
    except Exception:
        return None
    dd = d.get("deepdive_validees") or {}
    if pair in dd:
        return "deepdive GO"
    obs = d.get("observation_setup") or {}
    if pair in obs and str(obs[pair]).startswith("OBSERVATION (NON"):
        return "famille NON (croisement prix seul)"
    if pair in (d.get("ejectees") or {}):
        return "ÉJECTÉE"
    return None


def check_fiches(hulk: Path) -> tuple[list[dict], list[dict]]:
    """Fiche md absente = ALARME (on a cherché partout avant de le dire).
    Calib moteur trouée sur fiche existante = FATAL (V1).
    Contradiction famille NON vs PAPER_PAIRS = ALARME nommée."""
    fatals: list[dict] = []
    alarmes: list[dict] = []

    # 1) fiches md (OBSIDIAN) — recherchées PARTOUT avant tout verdict
    fiches_md: dict[str, Path] = {}
    outbox = INDEX / "OUTBOX_OBSIDIAN"
    if outbox.exists():
        for p in outbox.rglob("FICHE_SETUP_*.md"):
            nom = p.stem.replace("FICHE_SETUP_", "").split("_")[0].upper()
            if nom.endswith("USDT"):
                # garde la plus récente si plusieurs versions (archives _traites/)
                if nom not in fiches_md or p.stat().st_mtime > fiches_md[nom].stat().st_mtime:
                    fiches_md[nom] = p

    profils_path = hulk / "strategie" / "universe_profils.json"
    try:
        profils = json.loads(profils_path.read_text())
    except Exception as e:
        return [], [{"organe": "universe_profils.json",
                     "fait": f"illisible: {e}",
                     "quoi": "fiche de configuration moteur illisible"}]

    for pair in pick_pairs_actives(hulk):
        verdict = verdict_famille(pair)

        # fiche md : on cherche AVANT de crier « absent »
        if pair not in fiches_md:
            alarmes.append({
                "organe": f"fiche md {pair}",
                "fait": "aucune FICHE_SETUP_* trouvée dans OUTBOX_OBSIDIAN (recherche rglob complète)",
                "quoi": "organe orphelin — fiche de set-up inexistante",
            })

        # calib moteur (universe_profils.json)
        fiche = profils.get(pair)
        if not isinstance(fiche, dict):
            if verdict == "famille NON (croisement prix seul)":
                alarmes.append({
                    "organe": f"paire {pair}",
                    "fait": "dans PAPER_PAIRS mais verdict famille = NON, et SANS calib moteur",
                    "quoi": "contradiction famille/moteur — décision famille requise (jamais tranchée par la serrure)",
                })
            else:
                alarmes.append({
                    "organe": f"paire {pair}",
                    "fait": f"dans PAPER_PAIRS sans calib moteur (verdict: {verdict or 'inconnu'})",
                    "quoi": "le moteur la trade sur les défauts globaux — fiche à calibrer",
                })
            continue

        calib = fiche.get("calib") or {}
        manquantes = [k for k in CLES_OBLIGATOIRES if calib.get(k) in (None, "")]
        if manquantes:
            fatals.append({
                "organe": f"fiche {pair}",
                "fait": f"clés calib manquantes: {', '.join(manquantes)}",
                "quoi": "fiche active incomplète — boot refusé (V1)",
            })
        for cle, exceptions in CLES_FICHE:
            if pair not in exceptions and fiche.get(cle) in (None, ""):
                alarmes.append({
                    "organe": f"fiche {pair}",
                    "fait": f"clé {cle} absente (le moteur fail-open dessus, l.1858)",
                    "quoi": "plafond de profondeur inopérant pour cette paire",
                })
    return fatals, alarmes


def check_todos(hulk: Path) -> tuple[list[dict], list[dict]]:
    fatals: list[dict] = []
    alarmes: list[dict] = []
    for rel in HULK_DECISION_FATAL:
        p = hulk / rel
        if not p.exists():
            fatals.append({"organe": rel, "fait": "fichier de décision ABSENT", "quoi": "moteur incomplet"})
            continue
        for i, line in enumerate(p.read_text(errors="replace").splitlines(), 1):
            m = TODO_RE.search(line)
            if m:
                fatals.append({
                    "organe": rel,
                    "fait": f"{m.group(1)} ligne {i}: {line.strip()[:100]}",
                    "quoi": "TODO dans un chemin de décision du moteur — boot refusé (V2)",
                })
    for rel, raison in AGENTS_ALARME:
        p = INDEX.parent / rel
        if not p.exists():
            continue
        hits = []
        for i, line in enumerate(p.read_text(errors="replace").splitlines(), 1):
            m = TODO_RE.search(line)
            if m:
                hits.append(f"ligne {i}: {line.strip()[:90]}")
        if hits:
            alarmes.append({
                "organe": rel,
                "fait": f"{len(hits)} TODO ({raison}) — ex: {hits[0]}",
                "quoi": "branches non câblées dans un agent vivant (V3)",
            })
    return fatals, alarmes


def check_cerveaux() -> list[dict]:
    alarmes: list[dict] = []
    now = time.time()
    for nom, chemin, ttl in CERVEAUX:
        if not chemin.exists():
            alarmes.append({"organe": f"cerveau {nom}", "fait": f"{chemin} ABSENT", "quoi": "cerveau manquant"})
            continue
        cibles = ([chemin] if chemin.is_file()
                  else sorted(chemin.glob("*") if chemin.is_dir() else []))
        for c in cibles:
            if not c.is_file():
                continue
            age = now - c.stat().st_mtime
            if age > ttl:
                alarmes.append({
                    "organe": f"cerveau {nom}",
                    "fait": f"{c.name} gelé depuis {age / 86400:.1f} j (> {ttl // 86400} j)",
                    "quoi": "fiche d'analyses non vivante — ALARME (pas un warning)",
                })
    return alarmes


def check_registre(hulk: Path) -> list[dict]:
    alarmes: list[dict] = []
    try:
        reg = json.loads(REGISTRE.read_text())
    except Exception as e:
        return [{"organe": "REGISTRE_SYNAPSES", "fait": f"illisible: {e}", "quoi": "registre de naissance illisible"}]
    declares = {f.get("nom"): f for f in reg.get("fichier", []) if f.get("nom")}
    surveilles = ["hulk-mexc/scripts/paper_diprip.py", "hulk-mexc/strategie/universe_profils.json"]
    for nom in surveilles:
        if nom not in declares:
            continue
        chemin = INDEX.parent / nom
        if not chemin.exists():
            continue
        attendu = (declares[nom] or {}).get("md5")
        if attendu and md5_of(chemin) != attendu:
            alarmes.append({
                "organe": nom,
                "fait": "md5 ≠ registre (modifié sans re-déclaration)",
                "quoi": "naissance non déclarée — re-déclarer avec note de la modification",
            })
    return alarmes


def declare_au_registre(nom: str, role: str, origine: str, note: str) -> str:
    """Déclaration/actualisation d'une entrée md5 — SEULE écriture de la serrure."""
    chemin = INDEX.parent / nom
    if not chemin.exists():
        return f"{nom} introuvable — rien déclaré"
    md5 = md5_of(chemin)
    entree = {
        "nom": nom,
        "role": role,
        "origine": origine,
        "verif": "md5",
        "auto_modifiable": False,
        "md5": md5,
        "note": note,
    }
    try:
        reg = json.loads(REGISTRE.read_text())
    except Exception:
        return "registre illisible — déclaration non écrite"
    fichiers = reg.get("fichier", [])
    for i, f in enumerate(fichiers):
        if f.get("nom") == nom:
            if f.get("md5") == md5:
                return f"{nom} déjà déclaré à jour"
            entree["note"] = f"{note} | re-déclaré {utc_now()} (md5 changé, modification tracée en MEMOIRE_COLLAB)"
            fichiers[i] = entree
            break
    else:
        entree["note"] = f"{note} | déclaré {utc_now()}"
        fichiers.append(entree)
    reg["fichier"] = fichiers
    reg["updated"] = utc_now()
    bak = f"/tmp/REGISTRE_SYNAPSES.json.bak-avant-serrure-{int(time.time())}"
    try:
        REGISTRE.rename(bak)
    except Exception:
        bak = "none"
    tmp = REGISTRE.with_suffix(".tmp")
    tmp.write_text(json.dumps(reg, indent=1, ensure_ascii=False) + "\n")
    os.replace(tmp, REGISTRE)
    return f"{nom} déclaré (md5 {md5[:8]}…, backup {bak})"


def main() -> int:
    ap = argparse.ArgumentParser(description="Serrure preflight — config fail-fast, moteur intact")
    ap.add_argument("--strict", action="store_true", help="mode boot agent décisionnaire")
    ap.add_argument("--json", action="store_true", help="sortie machine (veilleuse)")
    ap.add_argument("--hulk-root", default=str(HULK_DEFAULT), help="racine hulk (tests sur copie)")
    ap.add_argument("--declare", action="store_true",
                    help="re-déclare au registre les fichiers dont le md5 a légitimement changé")
    args = ap.parse_args()
    hulk = Path(args.hulk_root).resolve()

    fatals: list[dict] = []
    alarmes: list[dict] = []

    f_fat, f_alm = check_fiches(hulk)
    fatals += f_fat
    alarmes += f_alm
    t_fat, t_alm = check_todos(hulk)
    fatals += t_fat
    alarmes += t_alm
    alarmes += check_cerveaux()
    alarmes += check_registre(hulk)

    statut = "OK" if not fatals and not alarmes else ("FATAL" if fatals else "ALARMES")
    exit_code = 0 if statut == "OK" else (2 if fatals else 1)

    if args.json:
        print(json.dumps({
            "ts": utc_now(), "statut": statut, "exit": exit_code,
            "fatals": fatals, "alarmes": alarmes,
        }, indent=1, ensure_ascii=False))
    else:
        print(f"🔒 SERRURE — {utc_now()}  statut: {statut}")
        if fatals:
            print(f"  FATAL ({len(fatals)}) — boot refusé :")
            for f in fatals:
                print(f"    ✗ {f['organe']} : {f['fait']}")
        if alarmes:
            print(f"  ALARMES ({len(alarmes)}) :")
            for a in alarmes:
                print(f"    ! {a['organe']} : {a['fait']} — {a['quoi']}")
        if statut == "OK":
            print("  fiches complètes, zéro TODO moteur, cerveaux vivants, registre conforme.")
        print(f"  (exit {exit_code} — données fail-open préservées, configuration fail-fast)")

    if args.declare:
        print("  registre:",
              declare_au_registre(
                  "Index_Maison/scripts/serrure_preflight.py",
                  "Serrure preflight (V2 incident maladie des organes) — porte au boot, jamais dans la boucle",
                  "CHANTIER_CHECKUP_GLOBAL_20260910 S2/S6",
                  "v2 post-autopsie faux négatifs (fiches md cherchées partout, cerveaux aux vrais chemins)"))
    return exit_code


if __name__ == "__main__":
    sys.exit(main())
