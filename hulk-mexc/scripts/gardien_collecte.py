#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GARDIEN DES TROUS DE COLLECTE — le journal paper ne perd plus en silence (28/09/2026)
=====================================================================================

POURQUOI IL EXISTE
------------------
Christophe, en ALPAGE : « le plus important c'est la COLLECTE des données, c'est
toujours là qu'il y a des problèmes ». Le 27/09 on a trouvé à la source que 95 % du
corpus paper avait été collecté SANS les 5 colonnes de provenance, et que 263 lignes
étaient des doublons — **personne ne l'avait vu**, parce que rien ne le mesurait.
`verif_schema_journal.py` (classe E15) vérifie la LARGEUR de l'en-tête. Il ne voit ni
les TROUS (le moteur silencieux 3 h), ni les DOUBLONS, ni une ligne TRONQUÉE par une
coupure franche (batterie / hibernation — cause mesurée des coupures alpage).

CE QU'IL MESURE sur chaque journal PAPER_V1_*.csv
-------------------------------------------------
  R1  SCHÉMA      — en-tête vs `paper_diprip.CSV_SCHEMA` (lu À LA SOURCE, jamais
                    recopié : une copie divergerait le jour où on ajoute une colonne).
  R2  LARGEURS    — distribution des largeurs de lignes ; toute ligne PLUS LARGE que
                    l'en-tête est IRRÉPARABLE sans perte → BLOQUANT (on ne tronque pas
                    une donnée en silence).
  R3  DOUBLONS    — lignes strictement dupliquées (le lecteur les compterait deux fois).
  R4  TRONCATURE  — un fichier qui ne finit PAS par un saut de ligne = la dernière
                    ligne est suspecte (écriture coupée en plein vol). On la DÉCLARE,
                    on ne la « bouche » pas avec des colonnes vides.
  R5  TROUS       — silence entre deux lignes consécutives au-delà d'un seuil DÉRIVÉ des
                    données (médiane des écarts × facteur, jamais un plafond en dur : R17).
                    Un trou n'est PAS une faute (le moteur s'arrête, redémarre) : il est
                    DÉCLARÉ, avec ses bornes, dans `runs/TROUS_DECLARES.json` — pour
                    qu'un lecteur distingue « trou connu » de « donnée manquante muette ».
  R6  AUTOTEST    — le gardien prouve qu'il SAIT échouer (trou injecté, doublon injecté,
                    dérive injectée, troncature injectée) ET qu'il SAIT réparer (après
                    `--reparer`, plus aucune largeur non conforme ni doublon). Un gardien
                    qu'on n'a jamais vu échouer ne garde rien (classe E10).

RÉPARATION (auto-réparatrice)
-----------------------------
  `--reparer` : pad des lignes courtes + dédoublonnage strict + mise en quarantaine de la
  ligne tronquée (+ backup horodaté + écriture ATOMIQUE tmp+os.replace + RE-VÉRIF après
  écriture). Il REFUSE d'écrire si un moteur tourne (le CSV est ouvert en append : un
  os.replace en vol perdrait les écritures du moteur). Le seul instant SÛR est moteur mort
  → c'est le moment que choisit le watchdog avant de relancer (`--auto`).

CE QU'IL N'EST PAS
------------------
  * Il n'invente AUCUNE donnée : un trou ne se répare pas, il se DÉCLARE.
  * Il ne touche à rien d'autre qu'aux journaux PAPER_V1_*.csv de `hulk-mexc/runs`.
  * Lecture seule par défaut.

Usage :
  python3 gardien_collecte.py                       # contrôle du journal ACTIF (rc 0/1)
  python3 gardien_collecte.py --tous                # tous les journaux
  python3 gardien_collecte.py --reparer             # répare (moteur arrêté exigé)
  python3 gardien_collecte.py --reparer --auto      # silencieux, pour le watchdog
Sortie verdict : runs/GARDIEN_COLLECTE.json + Index_Maison/thermo/collecte.json (cockpit).
"""
from __future__ import annotations

import argparse
import bisect
import csv
import json
import os
import re
import shutil
import statistics
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent      # hulk-mexc/
RUNS = RACINE / "runs"
MAISON = RACINE.parent                               # ace777-test-day1/
THERMO = MAISON / "Index_Maison" / "thermo"
SORTIE = RUNS / "GARDIEN_COLLECTE.json"
ETAT_COCKPIT = THERMO / "collecte.json"              # R15 : un verdict non affiché n'existe pas
TROUS = RUNS / "TROUS_DECLARES.json"

# ── PARAMÈTRES DE MESURE (déclarés, jamais cachés) ────────────────────────────────
# MESURÉ sur le journal actif (80 702 écarts) : p50 = 1 s, p75 = 41 s, p90 = 70 s,
# p99 = 180 s, p99.5 = 356 s, max 15 h. Le moteur écrit par RAFALES (une paire n'écrit
# une ligne SKIP que quand une garde refuse, et le dédoublonnage tait les refus
# répétés) : le silence est donc NORMAL jusqu'à plusieurs minutes, et un seuil fixe bas
# fabriquerait 12 000 fausses alertes (R14 : une alarme toujours allumée tue la
# confiance dans l'alarme). Le seuil est donc DÉRIVÉ du journal lui-même :
#     seuil = max(10 min, 3 × p99 des écarts)
# 3 × p99 = 540 s ici → plancher 600 s retenu. Justification du plancher : le p99.5
# observé vaut 356 s (6 min) ; en dessous de 10 min on ne saurait pas distinguer un
# trou d'une rafale calme. Le seuil est écrit dans le rapport, jamais caché.
FIGURE_SILENCE = 3.0        # un trou = un silence > 3 × p99 des écarts du journal
PLANCHER_SILENCE_S = 600.0  # plancher déclaré : sous 10 min, rafale calme et trou se
                            # confondent (mesuré : p99.5 = 356 s)

RE_LIGNE = re.compile(r"^\|")  # (non utilisé — réservé au format mémoire collaborative)
FORMATS_TS = ("%Y-%m-%dT%H:%M:%SZ", "%Y-%m-%dT%H:%M:%S.%fZ", "%Y-%m-%dT%H:%M:%S+00:00")


# ─────────────────────────────────────────────────────────────────────────────────
def charger_schema() -> list[str]:
    """Lit le schéma DANS la source (`paper_diprip.CSV_SCHEMA`), commentaires retirés.
    Jamais recopié : c'est exactement la faute E15 (un schéma recopié qui diverge)."""
    src = (RACINE / "scripts" / "paper_diprip.py").read_text(encoding="utf-8")
    m = re.search(r"^CSV_SCHEMA\s*=\s*\[(.*?)^\]", src, flags=re.S | re.M)
    if not m:
        raise SystemExit("SCHEMA_INTROUVABLE : paper_diprip.CSV_SCHEMA introuvable")
    corps = "\n".join(l.split("#")[0] for l in m.group(1).splitlines())
    cols = re.findall(r'"([^"]+)"', corps)
    if not cols:
        raise SystemExit("SCHEMA_VIDE : aucune colonne extraite")
    return cols


def lire(chemin: Path) -> tuple[list[list[str]], bool]:
    """(lignes, fichier_finit_par_un_saut_de_ligne)."""
    brut = chemin.read_bytes()
    finit_ok = brut.endswith(b"\n")
    texte = brut.decode("utf-8", errors="replace")
    return list(csv.reader(texte.splitlines())), finit_ok


def _ts(s: str) -> datetime | None:
    for f in FORMATS_TS:
        try:
            return datetime.strptime(s, f).replace(tzinfo=timezone.utc)
        except ValueError:
            continue
    return None


def analyser(chemin: Path, schema: list[str]) -> dict:
    """Mesure tout ce que le gardien sait mesurer, sans rien écrire."""
    rows, finit_ok = lire(chemin)
    entete = rows[0] if rows else []
    corps = rows[1:]
    largeurs: dict[int, int] = {}
    for r in corps:
        if len(r):
            largeurs[len(r)] = largeurs.get(len(r), 0) + 1

    # doublons stricts (garde la 1re occurrence, comme le normaliseur)
    vues, doublons = set(), 0
    for r in corps:
        k = tuple(r)
        if k in vues:
            doublons += 1
        else:
            vues.add(k)

    # horodatage du journal ACTIF = colonne 0
    dts: list[float] = []
    ts_list: list[datetime] = []
    ts_illisibles = 0
    dernier_ok: datetime | None = None
    for r in corps:
        if not r:
            continue
        t = _ts(r[0])
        if t is None:
            ts_illisibles += 1
            continue
        if dernier_ok is not None:
            dts.append(max(0.0, (t - dernier_ok).total_seconds()))
        dernier_ok = t
        ts_list.append(t)

    return {
        "fichier": chemin.name,
        "entete_largeur": len(entete),
        "schema_largeur": len(schema),
        "entete_court": len(entete) != len(schema),
        "n_lignes": len(corps),
        "largeurs": {str(k): v for k, v in sorted(largeurs.items())},
        "lignes_plus_larges": sum(v for k, v in largeurs.items() if k > len(entete)),
        "lignes_plus_etroites": sum(v for k, v in largeurs.items() if k < len(entete)),
        "vides": sum(1 for r in corps if len(r) == 0),
        "doublons": doublons,
        "tronquee": not finit_ok,
        "ts_illisibles": ts_illisibles,
        "duree_couverte_s": round(
            (ts_list[-1] - ts_list[0]).total_seconds(), 1) if len(ts_list) >= 2 else 0.0,
        "dt_mediane_s": round(statistics.median(dts), 2) if dts else 0.0,
        "dt_p99_s": round(sorted(dts)[int(len(dts) * 0.99)], 2) if len(dts) >= 1000 else 0.0,
        "dt_p995_s": round(sorted(dts)[int(len(dts) * 0.995)], 2) if len(dts) >= 2000 else 0.0,
        "dt_echantillon": len(dts),
        "dt_max_s": round(max(dts), 1) if dts else 0.0,
        "mtime_age_min": round(
            (datetime.now(timezone.utc).timestamp() - chemin.stat().st_mtime) / 60, 1),
        "_ts_list": ts_list,
        "_rows": corps,
    }


# ── CROISEMENT AVEC LE JOURNAL DU WATCHDOG : QUELLE EST LA CAUSE DU TROU ? ────────
# MESURÉ le 28/09 : sur 259 trous déclarés (276 h), le watchdog de la maison prouve que
# 234 (170,7 h) sont un SILENCE NORMAL (le moteur était VIVANT tout le temps : aucune
# garde ne refusait, donc rien à écrire — un journal par rafales ressemble à un journal
# troué). Sans ce croisement, on croirait à 276 h de données perdues et on irait
# « empêcher la machine de dormir » pour un problème qui n'existe pas aux deux tiers.
# Le reste est classé : moteur MORT (le watchdog l'a vu et relancé) ou MACHINE FIGÉE
# (presque aucun passage du watchdog pendant le trou : macOS endormi / machine coupée —
# c'est le seul cas où le watchdog lui-même ne tournait pas). Source = machine, pas avis.
RE_WD = re.compile(r"^(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2})Z\s+(.*)$")


def _timeline_watchdog() -> tuple[list[datetime], list[str]]:
    ts: list[datetime] = []
    st: list[str] = []
    try:
        for line in (RUNS / "WATCHDOG_GHOST.log").open(encoding="utf-8", errors="replace"):
            m = RE_WD.match(line)
            if not m:
                continue
            t = datetime.strptime(m.group(1), "%Y-%m-%dT%H:%M:%S").replace(tzinfo=timezone.utc)
            txt = m.group(2)
            if "PAPER: OK" in txt:
                ts.append(t); st.append("ok")
            elif ("PAPER: MORT" in txt or "PAPER: RELANCÉ" in txt
                  or "PAPER: FAIL" in txt or "pas de relance" in txt):
                ts.append(t); st.append("down")
    except Exception:
        return [], []
    return ts, st


def classer_trous(trous: list[dict], ts: list[datetime], st: list[str]) -> dict:
    """Classe chaque trou. Retourne {'silence_normal'|'moteur_mort'|'machine_figee':
    {'trous': n, 'heures': h}} + le détail par trou (champ `classe`)."""
    res = {k: {"trous": 0, "heures": 0.0} for k in
           ("silence_normal", "moteur_mort", "machine_figee")}
    for t in trous:
        if not ts:
            t["classe"] = "indetermine"
            continue
        a = datetime.strptime(t["debut_utc"], "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
        b = datetime.strptime(t["fin_utc"], "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
        i0 = bisect.bisect_right(ts, a)
        i1 = bisect.bisect_left(ts, b)
        attendus = t["duree_s"] / 120.0        # le watchdog tourne toutes les 2 min
        if (i1 - i0) < 0.2 * attendus:
            k = "machine_figee"                 # le watchdog non plus ne tournait pas
        elif any(st[i] == "down" for i in range(i0, i1)):
            k = "moteur_mort"
        else:
            k = "silence_normal"
        t["classe"] = k
        res[k]["trous"] += 1
        res[k]["heures"] = round(res[k]["heures"] + t["duree_s"] / 3600, 2)
    return res


def _ecarts(a: dict) -> list[float]:
    """Écarts entre lignes consécutives (non stockés dans l'analyse, recalculés ici)."""
    ts = a.get("_ts_list") or []
    return [(ts[i] - ts[i - 1]).total_seconds() for i in range(1, len(ts))]


def trouver_trous(a: dict) -> tuple[list[dict], float]:
    """R5 — silences entre lignes consécutives. Retourne (trous, seuil_s).

    Un trou n'est PAS une faute : c'est un fait (moteur arrêté, réseau tombé). On le
    DÉCLARE avec ses bornes et les 2 lignes qui l'encadrent, pour qu'un lecteur sache
    ce qui manque et pourquoi — au lieu de lire un journal « continu » qui ne l'est pas.
    """
    ts = a.get("_ts_list") or []
    # R8 (bornes écrites) : le seuil n'est DÉRIVÉ du journal que si l'échantillon est
    # suffisant (≥ 1000 écarts). Sur 3 lignes, le « p99 » EST le trou qu'on cherche →
    # se dériver de soi-même (mesuré : seuil 32 340 s, trou de 3 h manqué).
    if (a.get("dt_echantillon") or 0) >= 1000:
        seuil = max(PLANCHER_SILENCE_S, FIGURE_SILENCE * (a.get("dt_p99_s") or 0.0))
    else:
        seuil = PLANCHER_SILENCE_S
    trous: list[dict] = []
    if len(ts) < 2:
        return trous, seuil
    rows = a.get("_rows") or []
    # index des lignes valides (avec ts lisible) pour encadrer le trou
    idx_ok = [i for i, r in enumerate(rows) if r and _ts(r[0]) is not None]
    for k in range(1, len(idx_ok)):
        i0, i1 = idx_ok[k - 1], idx_ok[k]
        d = (ts[k] - ts[k - 1]).total_seconds()
        if d <= seuil:
            continue
        r0, r1 = rows[i0], rows[i1]
        trous.append({
            "debut_utc": r0[0], "fin_utc": r1[0],
            "duree_s": round(d, 1), "duree_h": round(d / 3600, 2),
            "derniere_reason": (r0[10] if len(r0) > 10 else ""),
            "premiere_reason": (r1[10] if len(r1) > 10 else ""),
            "dernier_event": (r0[2] if len(r0) > 2 else ""),
            "premier_event": (r1[2] if len(r1) > 2 else ""),
        })
    trous.sort(key=lambda t: t["duree_s"], reverse=True)
    return trous, seuil


# ─────────────────────────────────────────────────────────────────────────────────
# ── QUEL JOURNAL EST « L'ACTIF » ? ──────────────────────────────────────────────
# PIÈGE MESURÉ LE 28/09 (trouvé par l'assainissement du corpus lui-même) : `--tous --reparer`
# RÉÉCRIT les vieux journaux via `os.replace` → leur mtime repasse à MAINTENANT → au passage
# suivant, le « journal le plus récent » n'est plus celui du moteur mais un vieux journal qu'on
# vient de réparer, et on surveille/annonce le mauvais fichier (mesuré : le cockpit a annoncé
# PAPER_V1_20260729_080720.csv, 446 lignes, au lieu du journal vivant). DEUX CORRECTIFS :
#   (1) le POINTEUR canonique du moteur (`runs/.hulk_resume_pointer`) désigne SANS AMBIGUÏTÉ
#       le journal courant — on le lit d'abord, c'est la vérité du moteur ;
#   (2) une RÉPARATION NE CHANGE PAS LA DATE DU FICHIER (mtime restauré) : réparer n'est pas
#       écrire de la donnée neuve, ça ne doit pas réordonner le corpus.
# En dernier recours seulement : le mtime le plus récent.
def _journal_actif() -> Path | None:
    try:
        nom = (RUNS / ".hulk_resume_pointer").read_text(encoding="utf-8").strip()
        j = RUNS / nom.replace("_state.json", ".csv")
        if nom and j.exists():
            return j
    except Exception:
        pass
    js = sorted(RUNS.glob("PAPER_V1_*.csv"), key=lambda p: p.stat().st_mtime, reverse=True)
    return js[0] if js else None


def paper_tourne() -> bool:
    """Vrai si un process paper_diprip est vivant. Lit le LOCK (pas pgrep -f, qui
    s'auto-matche sur la ligne de commande du watchdog — leçon du 28/08)."""
    lock = RUNS / ".paper_diprip.lock"
    try:
        pid = lock.read_text(encoding="utf-8").strip()
        if pid.isdigit():
            return subprocess.run(["kill", "-0", pid], capture_output=True).returncode == 0
    except Exception:
        pass
    return False


def reparer(chemin: Path, schema: list[str], force: bool, est_actif: bool = True) -> dict:
    """Pad + dédoublonne + met en quarantaine une ligne tronquée. Atomique, idempotent.

    REFUSE d'écrire si le moteur tourne (CSV ouvert en append : un os.replace en vol
    perdrait les écritures du moteur). REFUSE aussi s'il existe une ligne PLUS LARGE que
    l'en-tête : la réparer exigerait de tronquer une donnée en silence (R11 fail-safe).
    """
    a = analyser(chemin, schema)
    cible = a["entete_largeur"] or len(schema)
    res = {"fichier": chemin.name, "applique": False, "raison": ""}

    if a["lignes_plus_larges"]:
        res["raison"] = (f"IRRÉPARABLE AUTOMATIQUEMENT : {a['lignes_plus_larges']} ligne(s) "
                         f"PLUS LARGE(S) que l'en-tête — les réparer exigerait de tronquer "
                         f"une donnée en silence. Relevé à la main (R11 : dans le doute, "
                         f"on ne décide pas).")
        return res
    # Le garde « moteur vivant » ne vaut que pour le journal ACTIF : c'est le SEUL que le
    # moteur tient ouvert en append. Un journal HISTORIQUE n'est réécrit par personne →
    # le réparer pendant que le moteur tourne est sûr (et c'est tout l'objet du
    # `--reparer --tous` d'assainissement du corpus).
    if est_actif and paper_tourne() and not force:
        res["raison"] = ("moteur VIVANT : le CSV est ouvert en append, un os.replace en vol "
                         "perdrait ses écritures. Réparer moteur arrêté (ou --force).")
        return res
    if not (a["doublons"] or a["lignes_plus_etroites"] or a["tronquee"] or a["vides"]):
        res["raison"] = "rien à réparer (déjà conforme)"
        return res

    rows, _ = lire(chemin)
    entete, corps = rows[0], rows[1:]
    quarantaine = []
    if a["tronquee"] and corps:
        quarantaine.append(corps[-1])       # dernière ligne suspecte : on ne la « bouche » pas
        corps = corps[:-1]

    vues, out, nb_pad, nb_dup = set(), [], 0, 0
    for r in corps:
        if len(r) == 0:
            continue
        # ORDRE CRITIQUE (trouvé par la RE-VÉRIF du 28/09, elle-même) : on PAD d'ABORD,
        # on dédoublonne ENSUITE. Dédoublonner avant de padder compare une ligne à 11
        # champs à sa jumelle à 16 → elles ne sont pas « égales » et le doublon survit,
        # puis il devient identique APRÈS padding (mesuré : verif_apres NON). La re-vérif
        # après écriture est ce qui a attrapé cette faute — on ne déclare jamais une
        # réparation sans la relire.
        if len(r) < cible:
            nb_pad += 1
            r = r + [""] * (cible - len(r))
        k = tuple(r)
        if k in vues:
            nb_dup += 1
            continue
        vues.add(k)
        out.append(r)

    ts_tag = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    bak = chemin.with_name(chemin.name + f".bak-avant-gardien-{ts_tag}")
    shutil.copy2(chemin, bak)
    st_avant = chemin.stat()          # pour RESTAURER le mtime après écriture (cf. _journal_actif)
    if quarantaine:
        (chemin.with_name(chemin.name + f".ligne-tronquee-{ts_tag}")).write_text(
            ",".join(quarantaine[-1]) + "\n", encoding="utf-8")

    fd, tmp = tempfile.mkstemp(dir=str(chemin.parent), prefix=chemin.name + ".", suffix=".tmp")
    try:
        with open(fd, "w", encoding="utf-8", newline="") as f:
            w = csv.writer(f, lineterminator="\r\n")
            w.writerow(entete)
            w.writerows(out)
        Path(tmp).replace(chemin)
        # RÉPARER N'EST PAS COLLECTER : on remet la date d'origine, sinon le corpus se
        # réordonne et un vieux journal réparé passe pour « le plus récent ».
        os.utime(chemin, (st_avant.st_atime, st_avant.st_mtime))
    except Exception:
        Path(tmp).unlink(missing_ok=True)
        raise

    # RE-VÉRIF après écriture (on ne déclare jamais une réparation sans la relire)
    apres = analyser(chemin, schema)
    ok = (apres["doublons"] == 0 and apres["lignes_plus_etroites"] == 0
          and apres["lignes_plus_larges"] == 0 and not apres["tronquee"])
    res.update({
        "applique": True, "backup": bak.name, "paddées": nb_pad, "doublons_retires": nb_dup,
        "lignes_quarantaine": len(quarantaine), "lignes_apres": apres["n_lignes"],
        "verif_apres": "OUI" if ok else "NON — à inspecter",
        "raison": "réparé",
    })
    return res


# ─────────────────────────────────────────────────────────────────────────────────
def autotest(schema: list[str]) -> list[tuple[str, bool, str]]:
    """Le gardien SAIT-il échouer ET réparer ? Fichiers synthétiques, rien de réel touché."""
    res: list[tuple[str, bool, str]] = []
    with tempfile.TemporaryDirectory() as d:
        base = Path(d)

        def ecrire(nom: str, lignes: list[list[str]], fin_nl: bool = True) -> Path:
            p = base / nom
            with p.open("w", encoding="utf-8", newline="") as f:
                w = csv.writer(f, lineterminator="\r\n")
                w.writerow(schema)
                w.writerows(lignes)
            if not fin_nl:                      # simule une écriture coupée en plein vol
                b = p.read_bytes()
                p.write_bytes(b[:-2] if b.endswith(b"\r\n") else b[:-1])
            return p

        L = lambda ts: [ts] + ["x"] * (len(schema) - 1)   # noqa: E731

        # 1) fichier sain
        p = ecrire("sain.csv", [L("2026-09-28T10:00:00Z"), L("2026-09-28T10:00:20Z")])
        a = analyser(p, schema)
        res.append(("fichier sain : aucun défaut",
                    a["doublons"] == 0 and a["largeurs"] == {str(len(schema)): 2}
                    and not a["tronquee"], f"largeurs {a['largeurs']}"))

        # 2) dérive de schéma (ligne courte) détectée ET réparée
        p = ecrire("derive.csv", [[*L("2026-09-28T10:00:00Z")][:11],
                                  L("2026-09-28T10:00:20Z")])
        a = analyser(p, schema)
        det = a["lignes_plus_etroites"] == 1
        r = reparer(p, schema, force=True)
        a2 = analyser(p, schema)
        res.append(("dérive de largeur détectée puis RÉPARÉE",
                    det and r["applique"] and a2["lignes_plus_etroites"] == 0
                    and r["verif_apres"] == "OUI",
                    f"avant {a['largeurs']} → après {a2['largeurs']}"))

        # 3) doublon strict détecté ET retiré
        p = ecrire("dup.csv", [L("2026-09-28T10:00:00Z"), L("2026-09-28T10:00:00Z")])
        a = analyser(p, schema)
        r = reparer(p, schema, force=True)
        a2 = analyser(p, schema)
        res.append(("doublon détecté puis RETIRÉ",
                    a["doublons"] == 1 and r["doublons_retires"] == 1 and a2["doublons"] == 0,
                    f"{a['doublons']} → {a2['doublons']}"))

        # 4) TROU injecté (3 h) détecté
        p = ecrire("trou.csv", [L("2026-09-28T10:00:00Z"), L("2026-09-28T10:00:20Z"),
                                L("2026-09-28T13:00:00Z"), L("2026-09-28T13:00:20Z")])
        a = analyser(p, schema)
        trous, seuil = trouver_trous(a)
        res.append(("TROU de 3 h détecté (et pas les écarts normaux)",
                    len(trous) == 1 and abs(trous[0]["duree_s"] - 10780) < 5,
                    f"seuil {seuil:.1f}s · {len(trous)} trou(s) · {trous[0]['duree_s']}s"))

        # 5) ligne TRONQUÉE détectée et mise en quarantaine (jamais « bouchée »)
        p = ecrire("tronq.csv", [L("2026-09-28T10:00:00Z"), L("2026-09-28T10:00:20Z")],
                   fin_nl=False)
        a = analyser(p, schema)
        r = reparer(p, schema, force=True)
        res.append(("ligne tronquée détectée + mise en quarantaine (pas bouchée)",
                    a["tronquee"] and r["lignes_quarantaine"] == 1,
                    f"tronquee={a['tronquee']} · quarantaine={r['lignes_quarantaine']}"))

        # 6) ligne COURTE qui devient un DOUBLON après padding (piège d'ORDRE)
        p = ecrire("pad_dup.csv", [L("2026-09-28T10:00:00Z")])
        with p.open("a", encoding="utf-8", newline="") as f:
            # la MÊME ligne, mais tronquée à l'ancien schéma : elle ne devient identique
            # à la première qu'APRÈS padding → elle teste l'ORDRE pad/dédup.
            csv.writer(f, lineterminator="\r\n").writerow(L("2026-09-28T10:00:00Z")[:11])
        r = reparer(p, schema, force=True)
        a2 = analyser(p, schema)
        res.append(("ligne courte devenue doublon APRÈS padding : dédoublonnée",
                    a2["doublons"] == 0 and a2["lignes_plus_etroites"] == 0
                    and r["verif_apres"] == "OUI", f"doublons {a2['doublons']}"))

        # 7) ligne PLUS LARGE = irréparable, refus d'écrire (fail-safe)
        p = ecrire("large.csv", [L("2026-09-28T10:00:00Z"),
                                 [*L("2026-09-28T10:00:20Z"), "extra"]])
        r = reparer(p, schema, force=True)
        res.append(("ligne PLUS LARGE : refus de réparer (fail-safe, rien tronqué)",
                    not r["applique"] and "IRRÉPARABLE" in r["raison"], r["raison"][:60]))

        # 8) CLASSEMENT DES TROUS — le gardien distingue une VRAIE perte d'un silence normal
        #    (sinon il déclarerait 276 h de « pertes » là où le moteur n'avait rien à écrire).
        T = lambda s: datetime.strptime(s, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)  # noqa: E731
        tro3 = [{"debut_utc": "2026-09-28T10:00:00Z", "fin_utc": "2026-09-28T10:10:00Z", "duree_s": 600},
                {"debut_utc": "2026-09-28T11:00:00Z", "fin_utc": "2026-09-28T11:10:00Z", "duree_s": 600},
                {"debut_utc": "2026-09-28T12:00:00Z", "fin_utc": "2026-09-28T13:00:00Z", "duree_s": 3600}]
        ts_wd = [T("2026-09-28T10:02:00Z"), T("2026-09-28T10:04:00Z"), T("2026-09-28T10:06:00Z"),
                 T("2026-09-28T10:08:00Z"), T("2026-09-28T11:02:00Z"), T("2026-09-28T11:04:00Z"),
                 T("2026-09-28T11:06:00Z")]
        c = classer_trous(tro3, ts_wd, ["ok", "ok", "ok", "ok", "ok", "down", "ok"])
        res.append(("classement : silence normal · moteur mort · machine figée",
                    c["silence_normal"]["trous"] == 1 and c["moteur_mort"]["trous"] == 1
                    and c["machine_figee"]["trous"] == 1,
                    f"{c['silence_normal']['trous']} normal · {c['moteur_mort']['trous']} mort"
                    f" · {c['machine_figee']['trous']} figée"))

    return res


# ─────────────────────────────────────────────────────────────────────────────────
def main() -> int:
    ap = argparse.ArgumentParser(description="Gardien des trous de collecte du journal paper Hulk.")
    ap.add_argument("--csv", default=None, help="journal à contrôler (défaut : le plus récent)")
    ap.add_argument("--tous", action="store_true", help="contrôler TOUS les journaux")
    ap.add_argument("--reparer", action="store_true",
                    help="réparer le journal actif (pad + dédup + quarantaine tronquée)")
    ap.add_argument("--force", action="store_true", help="réparer même moteur vivant (DANGEREUX)")
    ap.add_argument("--auto", action="store_true", help="mode silencieux (watchdog)")
    ap.add_argument("--json", default=str(SORTIE))
    args = ap.parse_args()

    schema = charger_schema()
    if args.csv:
        cibles = [Path(args.csv)]
    else:
        cibles = sorted(RUNS.glob("PAPER_V1_*.csv"), key=lambda p: p.stat().st_mtime,
                        reverse=True)
        if not args.tous:
            cibles = cibles[:1]
    if not cibles:
        print("AUCUN journal PAPER_V1_*.csv trouvé", file=sys.stderr)
        return 2

    actif = _journal_actif()
    if actif is None:
        print("AUCUN journal PAPER_V1_*.csv trouvé", file=sys.stderr)
        return 2
    res_auto = autotest(schema)
    auto_ok = all(ok for _, ok, _ in res_auto)

    # RÉPARATION — l'ACTIF n'est réparable que moteur ARRÊTÉ (il l'a ouvert en append) ;
    # les HISTORIQUES ne sont réécrits par personne → réparables à tout moment (`--tous`,
    # c'est l'assainissement du corpus).
    reps: list[dict] = []
    if args.reparer:
        for p in cibles:
            reps.append(reparer(p, schema, args.force, est_actif=(p.name == actif.name)))
    rep = next((r for r in reps if r["fichier"] == cibles[0].name), None)

    analyses = [analyser(p, schema) for p in cibles]

    tous_trous, seuils, pauses = [], {}, {}
    for a in analyses:
        t, s = trouver_trous(a)
        tous_trous.append((a["fichier"], t))
        seuils[a["fichier"]] = round(s, 1)
        pauses[a["fichier"]] = sum(1 for x in _ecarts(a) if x > s)
    for a in analyses:
        a["trous_n"] = len(dict(tous_trous)[a["fichier"]])

    # CAUSE de chaque trou, croisée au journal du WATCHDOG (source machine, pas avis).
    ts_wd, st_wd = _timeline_watchdog()
    cls_par_journal = {a["fichier"]: classer_trous(dict(tous_trous)[a["fichier"]], ts_wd, st_wd)
                       for a in analyses}

    # BLOQUANT = défaut RÉPARABLE/fautif dans le journal COURANT (trou = fait, non bloquant)
    act = analyses[0]
    cls = cls_par_journal[act["fichier"]]
    pertes_h = round(cls["machine_figee"]["heures"] + cls["moteur_mort"]["heures"], 2)
    pertes_n = cls["machine_figee"]["trous"] + cls["moteur_mort"]["trous"]
    bloquants = {
        "doublons": act["doublons"],
        "lignes_plus_larges": act["lignes_plus_larges"],
        "lignes_plus_etroites": act["lignes_plus_etroites"],
        "tronquee": act["tronquee"],
        "entete_court": act["entete_court"],
    }
    actif_bloquant = any(bloquants.values())
    trous_actif = tous_trous[0][1]
    rc = 0 if (auto_ok and not actif_bloquant) else 1

    # Déclaration DURABLE des trous (pour qu'un lecteur distingue trou connu / perte muette)
    TROUS.write_text(json.dumps({
        "instrument": "gardien_collecte.py",
        "ts_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "journal_actif": act["fichier"],
        "seuil_s": seuils.get(act["fichier"]),
        "dt_mediane_s": act.get("dt_mediane_s"),
        "dt_p99_s": act.get("dt_p99_s"),
        "duree_couverte_s": act.get("duree_couverte_s"),
        "classification": cls,
        "vraies_pertes_heures": pertes_h,
        "trous": trous_actif,
        "note": ("Un trou n'est pas une faute : il est DÉCLARÉ pour qu'aucune donnée "
                 "manquante ne soit silencieuse. Aucune donnée n'est inventée. "
                 "La `classification` croise chaque trou au journal du WATCHDOG (source "
                 "machine) : silence_normal = le moteur était VIVANT et n'avait rien à "
                 "écrire (pas une perte) ; moteur_mort / machine_figee = vraies coupures."),
    }, indent=2, ensure_ascii=False), encoding="utf-8")

    # Assainissement du corpus : quand on examine TOUS les journaux, on déclare
    # aussi leurs trous (chacun avec sa cause) — le passé n'est pas réécrit, il est DÉCLARÉ.
    if args.tous:
        (RUNS / "TROUS_DECLARES_HISTORIQUE.json").write_text(json.dumps({
            "instrument": "gardien_collecte.py",
            "ts_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "journaux": [{
                "fichier": a["fichier"], "n_lignes": a["n_lignes"],
                "largeurs": a["largeurs"], "doublons": a["doublons"],
                "tronquee": a["tronquee"], "en_tete": a["entete_largeur"],
                "schema_courant": (a["entete_largeur"] == len(schema)),
                "dt_mediane_s": a["dt_mediane_s"], "dt_max_s": a["dt_max_s"],
                "trous_n": a["trous_n"],
                "classification": cls_par_journal[a["fichier"]],
            } for a in analyses],
            "reparations": reps,
            "note": ("Le passé n'est pas réécrit : il est DÉCLARÉ (trous + cause + réparation tentée). "
                     "ATTENTION : ne PAS additionner les heures trou par trou à travers les journaux — "
                     "chaque run recopie l'historique de son prédécesseur (le RESUME copie les lignes), "
                     "donc la MÊME absence est comptée dans chaque journal descendant (mesuré : somme "
                     "brute ~5 815 h pour ~105 h réelles sur le journal courant). La mesure de référence "
                     "est celle du JOURNAL VIVANT (runs/TROUS_DECLARES.json)."),
        }, indent=2, ensure_ascii=False), encoding="utf-8")

    verdict = {
        "instrument": "gardien_collecte.py",
        "ts_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "schema": schema, "schema_largeur": len(schema),
        "journaux_examines": len(cibles),
        "journal_actif": act["fichier"],
        "actif": {k: v for k, v in act.items() if not k.startswith("_")},
        "defauts_bloquants": bloquants,
        "trous_actif_n": len(trous_actif),
        "trous_actif_total_h": round(sum(t["duree_s"] for t in trous_actif) / 3600, 2),
        "classification": cls,
        "vraies_pertes_n": pertes_n,
        "vraies_pertes_heures": pertes_h,
        "trous_actif_top": trous_actif[:10],
        "seuils_silence_s": seuils,
        "reparation": rep,
        "autotest_fiable": auto_ok,
        "autotest": [{"cas": n, "ok": ok, "detail": d} for n, ok, d in res_auto],
        "rc": rc,
    }
    Path(args.json).write_text(json.dumps(verdict, indent=2, ensure_ascii=False),
                               encoding="utf-8")
    try:
        ETAT_COCKPIT.parent.mkdir(parents=True, exist_ok=True)
        ETAT_COCKPIT.write_text(json.dumps({
            "instrument": "gardien_collecte.py",
            "ts_utc": verdict["ts_utc"],
            "journal_actif": act["fichier"],
            "conforme": rc == 0,
            "defauts_bloquants": bloquants,
            "trous_n": len(trous_actif),
            "trous_total_h": verdict["trous_actif_total_h"],
            "classification": cls,
            "vraies_pertes_n": pertes_n,
            "vraies_pertes_heures": pertes_h,
            "dt_max_s": act.get("dt_max_s"),
            "dt_mediane_s": act.get("dt_mediane_s"),
            "lignes": act.get("n_lignes"),
            "autotest_fiable": auto_ok,
            "rc": rc,
        }, indent=2, ensure_ascii=False), encoding="utf-8")
    except Exception:
        pass

    if not args.auto:
        print(f"SCHEMA COURANT : {len(schema)} colonnes")
        for a in analyses:
            tro = dict(tous_trous)[a["fichier"]]
            print(f"· {a['fichier']:34} en-tête {a['entete_largeur']:>3} · largeurs {a['largeurs']}"
                  f" · {a['n_lignes']} lignes · doublons {a['doublons']}"
                  f" · tronquée {'OUI' if a['tronquee'] else 'non'}")
            print(f"    écarts : médiane {a['dt_mediane_s']}s · p99 {a['dt_p99_s']}s"
                  f" · p99.5 {a.get('dt_p995_s')}s · max {a['dt_max_s']}s"
                  f" · seuil de trou {seuils[a['fichier']]}s"
                  f" · pauses > seuil {pauses[a['fichier']]}")
            cl_j = cls_par_journal[a["fichier"]]
            if tro:
                print(f"    TROUS DÉCLARÉS : {len(tro)}"
                      f" ({round(sum(t['duree_s'] for t in tro)/3600, 2)} h au total)"
                      f"  → dont VRAIES PERTES "
                      f"{cl_j['machine_figee']['trous'] + cl_j['moteur_mort']['trous']} trous"
                      f" ({round(cl_j['machine_figee']['heures'] + cl_j['moteur_mort']['heures'], 1)} h)"
                      f" · silence NORMAL {cl_j['silence_normal']['trous']} trous"
                      f" ({cl_j['silence_normal']['heures']:.1f} h, moteur VIVANT)")
                for t in sorted(tro, key=lambda x: -x["duree_s"])[:5]:
                    print(f"      – [{t.get('classe','?'):14}] {t['duree_s']:>8.0f}s"
                          f"  {t['debut_utc']} → {t['fin_utc']}")
        if rep:
            print(f"\nRÉPARATION : {rep['raison']}")
            if rep.get("applique"):
                print(f"   backup {rep['backup']} · paddées {rep['paddées']}"
                      f" · doublons retirés {rep['doublons_retires']}"
                      f" · quarantaine {rep['lignes_quarantaine']}"
                      f" · vérif après {rep['verif_apres']}")
        autres = [r for r in reps if r is not rep]
        if autres:
            faits = [r for r in autres if r.get("applique")]
            print(f"\nCORPUS HISTORIQUE : {len(reps)} journal(aux) · {len(faits)} réparé(s)"
                  f" · déclaration → runs/TROUS_DECLARES_HISTORIQUE.json")
        print("\nAUTOTEST :")
        for n, ok, d in res_auto:
            print(f"   [{'OK ' if ok else 'RATE'}] {n} — {d}")
        print(f"\nVERDICT : {'CONFORME' if rc == 0 else 'DÉFAUT DE COLLECTE'}"
              f" · autotest {'FIABLE' if auto_ok else 'NON FIABLE'} (rc={rc})")
        print("Un trou est DÉCLARÉ, jamais réparé : on n'invente aucune donnée.")
    return rc


if __name__ == "__main__":
    raise SystemExit(main())
