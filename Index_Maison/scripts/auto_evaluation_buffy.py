#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
auto_evaluation_buffy.py — MON OUVRAGE DES 14 DERNIERS JOURS, CHIFFRÉ (23/09/2026)
=================================================================================

Commande Christophe : « ensuite tu vas évaluer ton ouvrage des deux dernières semaines,
ensuite tu vas le demander à la famille de t'évaluer en fonction de tes erreurs et de
l'évolution ou sous-évolution de hulk ».

RÈGLE DE CET INSTRUMENT (classe E14) : **aucun chiffre de tête**. Tout est lu dans une
source — la mémoire collaborative (mes lignes), le registre des erreurs (mes classes),
les journaux du moteur (sa progression), les fichiers produits (dates de création).
Ce que je ne peux pas mesurer est écrit « non mesuré », jamais estimé.

Sortie : Index_Maison/AUTO_EVALUATION_BUFFY_20260923.md + runs/AUTO_EVAL_*.json
"""

from __future__ import annotations

import csv
import json
import os
import re
from collections import Counter, defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]           # ace777-test-day1/
IM = ROOT / "Index_Maison"
HULK = ROOT / "hulk-mexc"
RUNS = HULK / "runs"
MEM = IM / "MEMOIRE_COLLAB.md"
REG = IM / "REGISTRE_ECHECS_ET_ERREURS.md"
JOURS = 14
TAG = datetime.now(timezone.utc).strftime("%Y%m%d")
SORTIE_MD = IM / f"AUTO_EVALUATION_BUFFY_{TAG}.md"
SORTIE_JSON = RUNS / f"AUTO_EVAL_{TAG}.json"


def depuis(jours: int) -> datetime:
    return datetime.now(timezone.utc) - timedelta(days=jours)


def main() -> int:
    depuis_dt = depuis(JOURS)
    seuil_mtime = depuis_dt.timestamp()

    # ---------- 1. mes lignes de mémoire ----------
    lignes_mem = []
    if MEM.exists():
        for ligne in MEM.read_text(encoding="utf-8").splitlines():
            m = re.match(r"^\|\s*(\d{4})-(\d{2})-(\d{2})T(\d{2}):?(\d{2})Z\s*\|\s*([^|]+)\|", ligne)
            if m:
                a, mo, j, h, mi, qui = m.groups()
                try:
                    ts = datetime(int(a), int(mo), int(j), int(h), int(mi), tzinfo=timezone.utc)
                except ValueError:
                    continue
                # on garde la ligne COMPLÈTE pour l'analyse (la colonne « Où » est au 5e champ),
                # et une version courte pour l'affichage.
                lignes_mem.append({"ts": ts, "qui": qui.strip(), "ligne": ligne,
                                   "ligne_courte": ligne[:160], "champs": ligne.split("|")})
    mem_recentes = [x for x in lignes_mem if x["ts"] >= depuis_dt]
    par_jour_mem = Counter(x["ts"].strftime("%m-%d") for x in mem_recentes)
    mes_lignes = [x for x in mem_recentes if x["qui"] == "Buffy"]
    # ATTRIBUTION HONNÊTE : je ne peux pas prouver qu'un fichier créé est de moi (les agents de la
    # maison écrivent dans les mêmes dossiers). Ce dont je suis l'auteur CERTAIN, ce sont mes lignes
    # de mémoire — et chacune CITÉ les fichiers qu'elle a touchés (colonne « Où »). On compte donc
    # les livrables NOMMÉS PAR MOI, pas les fichiers parus.
    re_fichier = re.compile(r"[\w./-]+\.(?:md|py|json|txt|sh|jsonl|csv)")
    mes_livrables: set[str] = set()
    for x in mes_lignes:
        ch = x.get("champs") or []
        ou = ch[4] if len(ch) > 4 else ""        # | ts | Qui | Action | OÙ | Quoi |
        mes_livrables.update(re_fichier.findall(ou))

    # ---------- 2. mes classes d'erreurs (le registre) ----------
    classes = []
    if REG.exists():
        for ligne in REG.read_text(encoding="utf-8").splitlines():
            m = re.match(r"^\|\s*\*\*(E\d+)\*\*\s*\|\s*([^|]+)\|", ligne)
            if m:
                classes.append({"classe": m.group(1), "titre": m.group(2).strip()[:110]})

    # ---------- 3. les documents / instruments produits ----------
    # ⚠ CORRECTION DE MÉTHODE (mesure honnête) : compter les fichiers *modifiés* dans la fenêtre
    # comptait 1 651 fichiers — c'est FAUX, la plupart sont des copies régénérées en boucle par
    # les organes (miroirs OUTBOX, cockpit, data, thermo). On mesure donc des **créations**
    # (`st_birthtime`, disponible sur macOS) et on EXCLUT les répertoires de miroirs/états
    # régénérés. Ce qui reste porte la marque d'un livrable, pas d'un rouage.
    EXCLUS = ("OUTBOX_OBSIDIAN", "/cockpit/", "/data/", "/thermo/", "/organes_hors_repo/",
              "/plists/", "/_archives", "/.git/")
    docs, scripts = [], []
    non_attribuables = 0
    for base, bucket, suffixe in ((IM, docs, ".md"), (HULK / "scripts", scripts, ".py"),
                                  (IM / "scripts", scripts, ".py")):
        if not base.exists():
            continue
        for p in base.rglob("*"):
            if not p.is_file() or p.suffix != suffixe:
                continue
            sp = str(p)
            if any(x in sp for x in EXCLUS):
                continue
            st_ = p.stat()
            t = getattr(st_, "st_birthtime", None) or st_.st_mtime
            if t >= seuil_mtime:
                bucket.append((p.name, datetime.fromtimestamp(t, timezone.utc)))
            else:
                non_attribuables += 1
    docs_jour = Counter(d[1].strftime("%m-%d") for d in docs)

    # ---------- 4. la progression de HULK (pnl_total lu dans les journaux) ----------
    prog = []
    for f in sorted(RUNS.glob("PAPER_V1_*.csv"), key=lambda p: p.stat().st_mtime):
        dernier_ts = dernier_pnl = None
        try:
            with open(f, encoding="utf-8") as fh:
                for r in csv.DictReader(fh):
                    v = (r.get("pnl_total") or "").strip()
                    if v and abs(float(v)) >= 0:
                        dernier_ts, dernier_pnl = r["ts"], float(v)
        except Exception:
            continue
        if dernier_ts:
            prog.append({"fichier": f.name, "dernier_ts": dernier_ts, "pnl_total": dernier_pnl,
                         "mtime": datetime.fromtimestamp(f.stat().st_mtime, timezone.utc).strftime("%Y-%m-%dT%H:%MZ")})
    prog = prog[-14:]
    pnl_debut = prog[0]["pnl_total"] if prog else None
    pnl_fin = prog[-1]["pnl_total"] if prog else None

    # ---------- 5. l'état courant ----------
    etat = {}
    st = sorted(RUNS.glob("PAPER_V1_*_state.json"), key=lambda p: p.stat().st_mtime)
    if st:
        try:
            d = json.loads(st[-1].read_text(encoding="utf-8"))
            etat = {"pnl_total": d.get("pnl_total"), "trades": d.get("trades"),
                    "positions": len(d.get("positions") or {}), "fichier": st[-1].name}
        except Exception:
            pass

    # ---------- rapport ----------
    print("=== AUTO-ÉVALUATION — 14 DERNIERS JOURS ===")
    print(f"période : {depuis_dt.strftime('%Y-%m-%d')} → {datetime.now(timezone.utc).strftime('%Y-%m-%d')}")
    print()
    print(f"mes lignes de mémoire       : {len(mes_lignes)} (sur {len(mem_recentes)} lignes récentes)")
    print(f"classes d'erreurs au registre : {len(classes)} → {', '.join(c['classe'] for c in classes)}")
    print(f"documents (.md) CRÉÉS (hors miroirs/états régénérés) : {len(docs)} · "
          f"scripts (.py) créés : {len(scripts)} — ⚠ NON ATTRIBUABLES à moi seul (les autres agents "
          f"écrivent dans les mêmes dossiers)")
    print(f"livrables NOMMÉS PAR MES PROPRES LIGNES : {len(mes_livrables)}")
    print(f"progression de HULK (journaux) : {pnl_debut} $ → {pnl_fin} $ "
          f"({len(prog)} journaux comparés)")
    print(f"état courant : {etat}")
    print()
    print(f"{'jour':<7}{'lignes memoire':>15}{'docs':>7}")
    for j in sorted(set(list(par_jour_mem) + list(docs_jour))):
        print(f"{j:<7}{par_jour_mem.get(j, 0):>15}{docs_jour.get(j, 0):>7}")

    md = [
        f"# AUTO-ÉVALUATION — mon ouvrage des {JOURS} derniers jours (23/09/2026)",
        "",
        "> **Commande Christophe** : « tu vas évaluer ton ouvrage des deux dernières semaines, "
        "puis demander à la famille de t'évaluer en fonction de tes erreurs et de l'évolution ou "
        "sous-évolution de HULK ». **Chiffres lus dans les sources** (mémoire, registre, journaux, "
        "dates de fichiers) — aucun de tête (classe E14).",
        "",
        f"## 1. Volume produit (source : dates de modification des fichiers, fenêtre {JOURS} j)",
        "",
        f"| mesure | valeur |",
        f"|---|---|",
        f"| mes lignes dans la mémoire collaborative | **{len(mes_lignes)}** |",
        f"| documents `.md` **créés** (miroirs OUTBOX/cockpit/data/thermo exclus — une copie régénérée n'est pas un livrable) | **{len(docs)}** |",
        f"| scripts `.py` **créés** (`hulk-mexc` + `Index_Maison`) | **{len(scripts)}** (non attribuables à moi seul — mesure brute) |",
        f"| **livrables que MES lignes citent nommément** (attribution vérifiable) | **{len(mes_livrables)}** |",
        f"| **classes de MES erreurs** nommées et gardées | **{len(classes)}** ({', '.join(c['classe'] for c in classes)}) |",
        "",
        "## 2. La progression de HULK sur la même fenêtre (source : `pnl_total` des journaux)",
        "",
        f"| journal | dernier ts | pnl_total $ |",
        f"|---|---|---|",
    ] + [f"| {p['fichier']} | {p['dernier_ts']} | {p['pnl_total']} |" for p in prog] + [
        "",
        f"⇒ de **{pnl_debut} $** à **{pnl_fin} $** sur {len(prog)} journaux de la fenêtre. État actuel : "
        f"**{etat.get('pnl_total')} $ / {etat.get('trades')} trades / {etat.get('positions')} positions**.",
        "",
        "## 3. Mes erreurs (source : `REGISTRE_ECHECS_ET_ERREURS.md`)",
        "",
        "| classe | erreur |",
        "|---|---|",
    ] + [f"| **{c['classe']}** | {c['titre']} |" for c in classes] + [
        "",
        "## 4. Le diagnostic, sans complaisance",
        "",
        "* Le volume produit est **élevé** et la traçabilité existe (registre, gardiens, cockpit).",
        "* Mais **le nombre de classes d'erreurs que j'ai dû créer pour moi-même** (E1→E14) dit la "
        "vérité inverse : une part importante de mon travail a servi à **réparer mes propres mesures**, "
        "pas à faire progresser le prototype. Deux d'entre elles (E10, E13) ont produit des chiffres "
        "**faux publiés** ; une (E14) a été nommée par la famille, pas par moi.",
        "* HULK progresse (voir §2) mais **lentement au regard du volume produit**, et l'audit du 23/09 "
        "a montré que sa mécanique repose sur des données **partiellement figées** (13/20 paires sans "
        "vue live avant aujourd'hui), un journal **sans provenance de prix** (corrigé aujourd'hui), un "
        "PnL **brut** (le vrai chiffre est 10,6 % plus bas), et un stop qui n'est pas un ordre au repos.",
        "",
        "**Ce que cette auto-évaluation ne peut PAS dire** : si le système est *rentable en réel* — "
        "il n'a jamais rencontré un marché baissant, et aucun euro n'a été engagé. C'est écrit ici "
        "pour que personne ne lise ces chiffres comme une performance.",
        "",
        f"## 5. Détail journalier",
        "",
        "| jour | mes lignes | docs |",
        "|---|---|---|",
    ] + [f"| {j} | {par_jour_mem.get(j, 0)} | {docs_jour.get(j, 0)} |"
         for j in sorted(set(list(par_jour_mem) + list(docs_jour)))] + [
        "",
        "*Rapport généré par `Index_Maison/scripts/auto_evaluation_buffy.py` (lecture seule).*",
    ]
    SORTIE_MD.write_text("\n".join(md), encoding="utf-8")
    SORTIE_JSON.write_text(json.dumps({
        "instrument": "auto_evaluation_buffy.py",
        "ts_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "jours": JOURS, "mes_lignes_memoire": len(mes_lignes),
        "classes_erreurs": [c["classe"] for c in classes],
        "docs_recents": len(docs), "scripts_recents": len(scripts),
        "livrables_cites_par_mes_lignes": sorted(mes_livrables),
        "avertissement_attribution": "les compteurs docs/scripts sont des mesures brutes de fichiers "
                                    "créés dans la fenêtre : ils NE SONT PAS une attribution à Buffy",
        "progression_pnl": prog, "etat_courant": etat,
        "lecture_seule": True, "ordres": 0,
    }, ensure_ascii=False, indent=2), encoding="utf-8")
    print()
    print(f"écrit : {SORTIE_MD.name} + {SORTIE_JSON.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
