#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scoreur_registre_mecanique.py — SCOREUR DU REGISTRE MÉCANIQUE (23/08).

Le registre strategie/REGISTRE_PREDICTIONS.md est alimenté par analyste.py
(déclenché par la vigie). Problème identifié le 23/08 :
  * 2713 lignes EN ATTENTE dont 2650 DOUBLONS (la même prédiction réécrite en
    boucle — vigie trop sensible, aucune dédup à l'écriture) ;
  * 2700 échues JAMAIS scorées → la boucle d'évaluation était morte ;
  * le scoreur existant (scoreur_predictions.py) comparait au prix ACTUEL, ce
    qui est faux pour des échéances passées.

Ce script fait le travail correctement :
  1. Lit le registre, DÉDUPLIQUE (une ligne par (échéance, paire, comp, cible),
     en gardant le ts_creation le plus ancien — la 1ʳᵉ fois que l'analyste a dit ça).
  2. Convention (affinée 23/08) :
     a. Échéance = FIN de la journée indiquée (23:59:59Z) — « d'ici le [date] »
        signifie avant minuit CE jour-là (l'ancienne convention à T00:00:00Z
        rendait la moitié des prédictions échues AVANT leur création).
     b. Score TOUCH : la prédiction est VRAIE si le prix a ATTEINT la cible à
        un moment de la fenêtre [création → fin de journée d'échéance]
        (>= : high max ; <= : low min) — pas seulement au close du jour.
     c. Filtre d'INFORMATION : une prédiction déjà vraie au moment où elle est
        écrite (« BTC >= 60000 » quand BTC est à 63500) est une tautologie
        sans valeur → marquée ⚪ DÉJÀ VRAIE et EXCLUE de la justesse.
  3. Réécrit le registre : ⏳ EN ATTENTE (non échues), ✅ VRAIE / ❌ FAUSSE,
     ⚪ DÉJÀ VRAIE (tautologies).
  4. Écrit strategie/JUSTESSE_REGISTRE.json : score global (vrais paris
     uniquement) + par paire + par échéance + compteur de tautologies.
  5. Le registre reste lisible par le cockpit et nourrit la boucle d'évaluation.

Usage : python3 scoreur_registre_mecanique.py [--dry]
Stdlib uniquement. Binance API publique (klines 1h).
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.request
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

HOME = Path.home()
REGISTRE = HOME / "ace777-test-day1" / "Index_Maison" / "strategie" / "REGISTRE_PREDICTIONS.md"
OUT_JSON = HOME / "ace777-test-day1" / "Index_Maison" / "strategie" / "JUSTESSE_REGISTRE.json"
UA = {"User-Agent": "scoreur-registre/1.0"}

MOTIF = re.compile(
    r"^- (?:⏳ EN ATTENTE|✅ VRAIE|❌ FAUSSE|⚠️ NON_VERIFIABLE|⚪ DÉJÀ VRAIE) \| "
    r"([^|]+) \| ([^|]+) \| ([^|]+) \| ([^|]+) \| ([\d.]+)\s*$"
)


def parse_iso(ts: str):
    return datetime.fromisoformat(ts.replace("Z", "+00:00"))


BASES = [
    "https://api.binance.com",
    "https://data-api.binance.vision",
    "https://api1.binance.com",
]


MOTIF_DEJA_VRAIE = re.compile(
    r"^- ⚪ DÉJÀ VRAIE \| "
    r"([^|]+) \| ([^|]+) \| ([^|]+) \| ([^|]+) \| ([\d.]+)\s*$"
)


def fetch_price_at(symbole: str, ts_iso: str) -> float | None:
    """Prix (close de la bougie 1h contenant ts) à un instant donné — sert à
    détecter les prédictions DÉJÀ vraies à la création (zéro information)."""
    ms = int(parse_iso(ts_iso).timestamp() * 1000)
    for base in BASES:
        url = (f"{base}/api/v3/klines?symbol={symbole}&interval=1h"
               f"&startTime={ms - 3600 * 1000}&endTime={ms}&limit=1")
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=15) as resp:
                rows = json.loads(resp.read().decode("utf-8"))
            if rows:
                return float(rows[0][4])  # index 4 = close
        except Exception:
            continue
    return None


def fetch_touch_binance(symbole: str, debut_iso: str, fin_iso: str):
    """Récupère les klines 1h entre deux instants (UTC) et retourne
    (high_max, low_min) sur la fenêtre — la convention TOUCH : une prédiction
    de niveau est VRAIE si le prix a ATTEINT la cible à un moment de la fenêtre
    (pas seulement au close). Retourne (None, None) si introuvable.
    Multi-endpoints (fallback) pour résister aux timeouts transitoires."""
    debut = int(parse_iso(debut_iso).timestamp() * 1000)
    fin = int(parse_iso(fin_iso).timestamp() * 1000)
    if fin <= debut:
        return None, None
    for base in BASES:
        url = (f"{base}/api/v3/klines?symbol={symbole}&interval=1h"
               f"&startTime={debut}&endTime={fin}&limit=1000")
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=20) as resp:
                rows = json.loads(resp.read().decode("utf-8"))
            if not rows:
                continue
            highs = [float(r[2]) for r in rows]   # index 2 = high
            lows = [float(r[3]) for r in rows]    # index 3 = low
            return max(highs), min(lows)
        except Exception:
            continue
    return None, None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry", action="store_true", help="affiche sans écrire")
    args = ap.parse_args()

    if not REGISTRE.exists():
        print(f"[X] registre introuvable : {REGISTRE}", file=sys.stderr)
        return 1

    lignes = REGISTRE.read_text(encoding="utf-8").splitlines(keepends=True)

    # 1) Parse + dédup : (échéance, paire, comp, cible) -> (ts_creation, ligne_brute)
    uniques: dict[tuple, tuple[str, str]] = {}
    total = 0
    for l in lignes:
        m = MOTIF.match(l.rstrip("\n"))
        if not m:
            continue
        total += 1
        ts_creation, ts_limite, symbole, comp, cible = (
            m.group(1).strip(), m.group(2).strip(),
            m.group(3).strip().upper(), m.group(4).strip(), m.group(5).strip(),
        )
        cle = (ts_limite, symbole, comp, cible)
        if cle not in uniques or ts_creation < uniques[cle][0]:
            uniques[cle] = (ts_creation, l)

    n_echues = 0
    stats = {"vraies": 0, "fausses": 0, "deja_vraies": 0, "en_attente": 0,
             "non_verifiables": 0, "erreur_prix": 0}
    par_paire = Counter()
    par_paire_hit = Counter()
    par_paire_deja = Counter()
    par_jour = Counter()
    par_jour_hit = Counter()

    nouvelles = []
    for cle in sorted(uniques):
        ts_creation, ligne = uniques[cle]
        ts_limite, symbole, comp, cible = cle
        try:
            creation_dt = parse_iso(ts_creation)
        except Exception:
            nouvelles.append(ligne)
            stats["non_verifiables"] += 1
            continue

        # Convention (affinée 23/08) : l'échéance signifie « d'ici la FIN de la
        # journée indiquée » (23:59:59Z), pas minuit. Les anciennes lignes écrites
        # à T00:00:00Z sont donc traitées comme la fin de ce jour-là.
        jour = ts_limite[:10]
        fin_jour = f"{jour}T23:59:59Z"
        try:
            fin_dt = parse_iso(fin_jour)
        except Exception:
            nouvelles.append(ligne)
            stats["non_verifiables"] += 1
            continue

        # En attente tant que la journée d'échéance n'est pas finie.
        # ⚠ Toujours RÉÉCRIRE avec le statut ⏳ (pas la ligne brute d'origine :
        # un run précédent peut l'avoir marquée ✅/❌ à tort — idempotence).
        if fin_dt >= datetime.now(timezone.utc):
            nouvelles.append(
                f"- ⏳ EN ATTENTE | {ts_creation} | {ts_limite} | {symbole} | {comp} | {cible}\n")
            stats["en_attente"] += 1
            continue

        # Fenêtre réelle de la prédiction : [création, fin de la journée d'échéance]
        # (si la création est après le début de la journée d'échéance — cas des
        # anciennes lignes à minuit — on garde la fenêtre complète de ce jour-là
        # plutôt qu'une fenêtre vide).
        debut_fenetre = min(creation_dt, parse_iso(f"{jour}T00:00:00Z"))

        n_echues += 1

        # PRÉ-FILTRE D'INFORMATION (affiné 23/08) : une prédiction DÉJÀ vraie au
        # moment où elle est écrite (« BTC >= 60000 » quand BTC est à 63500) ne
        # porte AUCUNE information — c'est une tautologie, pas un pari. On la
        # marque ⚪ DÉJÀ VRAIE et on l'exclut de la justesse (elle l'inflaterait).
        p0 = fetch_price_at(symbole, ts_creation)
        if p0 is not None:
            deja_vraie = (p0 >= float(cible)) if comp == ">=" else (p0 <= float(cible))
            if deja_vraie:
                statut = "⚪ DÉJÀ VRAIE"
                nouvelles.append(
                    f"- {statut} | {ts_creation} | {ts_limite} | {symbole} | {comp} | {cible}\n")
                stats["deja_vraies"] += 1
                par_paire[symbole] += 1
                par_paire_deja[symbole] += 1
                continue

        high, low = fetch_touch_binance(
            symbole, debut_fenetre.isoformat(), fin_jour)
        if high is None:
            nouvelles.append(ligne)
            stats["erreur_prix"] += 1
            print(f"  ⚠ pas de klines pour {symbole} sur [{debut_fenetre.isoformat()}, {fin_jour}]",
                  file=sys.stderr)
            continue

        # Convention TOUCH : la prédiction est vraie si le prix a ATTEINT la cible
        # (>= : high_max >= cible ; <= : low_min <= cible).
        if comp == ">=":
            vraie = high >= float(cible)
        elif comp == "<=":
            vraie = low <= float(cible)
        else:
            nouvelles.append(ligne)
            stats["non_verifiables"] += 1
            continue

        statut = "✅ VRAIE" if vraie else "❌ FAUSSE"
        nouvelles.append(f"- {statut} | {ts_creation} | {ts_limite} | {symbole} | {comp} | {cible}\n")
        stats["vraies" if vraie else "fausses"] += 1
        par_paire[symbole] += 1
        if vraie:
            par_paire_hit[symbole] += 1
        par_jour[jour] += 1
        if vraie:
            par_jour_hit[jour] += 1

    # Justesse = sur les VRAIS PARIS uniquement (cible pas encore atteinte à la
    # création). Les ⚪ DÉJÀ VRAIE (tautologies) sont comptées à part : elles
    # n'apportent aucune information et gonfleraient artificiellement le score.
    n_scorees = stats["vraies"] + stats["fausses"]
    pct = round(stats["vraies"] / n_scorees * 100, 1) if n_scorees else None

    rapport = {
        "ts": datetime.now(timezone.utc).isoformat(),
        "source": "scoreur_registre_mecanique.py (23/08, convention TOUCH + fin de journée)",
        "convention": "échéance = fin de la journée indiquée (23:59:59Z) · vraie si le prix a ATTEINT la cible dans la fenêtre [création → échéance] · ⚪ DÉJÀ VRAIE = cible déjà atteinte à la création (zéro information, exclue de la justesse)",
        "registre": str(REGISTRE),
        "lignes_lues": total,
        "predictions_uniques": len(uniques),
        "dedupliquees": total - len(uniques),
        "echues": n_echues,
        "scorrees": n_scorees,
        "vraies": stats["vraies"],
        "fausses": stats["fausses"],
        "deja_vraies_creation": stats["deja_vraies"],
        "pct_vraies": pct,
        "en_attente": stats["en_attente"],
        "non_verifiables": stats["non_verifiables"],
        "erreur_prix": stats["erreur_prix"],
        "par_paire": {k: {"n": v, "hit": par_paire_hit[k], "deja_vraies": par_paire_deja[k],
                           "paris": v - par_paire_deja[k],
                           "pct": round(par_paire_hit[k] / (v - par_paire_deja[k]) * 100, 1)
                                   if (v - par_paire_deja[k]) else None}
                       for k, v in par_paire.items()},
        "par_jour": {k: {"n": v, "hit": par_jour_hit[k], "pct": round(par_jour_hit[k] / v * 100, 1)} for k, v in sorted(par_jour.items())},
    }

    if args.dry:
        print(json.dumps(rapport, ensure_ascii=False, indent=2))
        return 0

    # 2) Réécrire le registre dédupliqué + scoré (en-tête conservé)
    entete = []
    for l in lignes:
        if MOTIF.match(l.rstrip("\n")):
            break
        entete.append(l)
    REGISTRE.write_text("".join(entete) + "\n".join(nouvelles) + "\n", encoding="utf-8")
    OUT_JSON.write_text(json.dumps(rapport, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"[OK] registre : {total} lignes -> {len(uniques)} uniques "
          f"(dédup {total - len(uniques)})")
    print(f"[OK] scorées : {n_scorees} ({stats['vraies']} ✅ / {stats['fausses']} ❌)"
          f" — justesse {pct}%")
    print(f"[OK] en attente : {stats['en_attente']} · non vérifiables : {stats['non_verifiables']}"
          f" · erreur prix : {stats['erreur_prix']}")
    print(f"[OK] écrit : {REGISTRE.name} (dédupliqué+scoré) + {OUT_JSON.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
