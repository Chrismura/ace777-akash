#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""couleur_regime.py — COULEUR RÉGIME (portefeuille Hulk, 19/08/2026).

La couleur = l'ONCHAIN (le brut, la vérité) filtré par le NARRATIF (le bruit).
Un seul signal lisible pour Hulk : VERT / JAUNE / ROUGE / NOIR / ORANGE.

Matrice :
  onchain bullish + narratif bullish -> VERT   (aligné, tout confirme)
  onchain bullish + narratif bearish -> JAUNE   (contrarian : accumulation discrète)
  onchain bearish + narratif bullish -> ROUGE   (le piège : on te vend du rêve)
  onchain bearish + narratif bearish -> NOIR    (aligné baissier, rester dehors)
  l'un des deux neutre               -> ORANGE  (pas assez de signal)

BOUCLE AUTO-NOURRIE (comme El Niño / La Niña) :
  couleur du jour -> attendre l'horizon -> SCORE vs prix réel (HIT/MISS)
  -> LEÇONS : on garde fort les couleurs fiables, on ramollit les autres.

OBSERVATION par défaut : on note, on score, on NE TRADE PAS. L'exécution ne
viendra qu'après validation (famille -> juge -> backtest -> GO Christophe).

Usage :
  python3 couleur_regime.py --run      # calcule la couleur du moment
  python3 couleur_regime.py --score    # note les couleurs passées vs le prix
  python3 couleur_regime.py --lecons   # HIT/MISS -> ajustement des seuils
  python3 couleur_regime.py --test     # tests hermétiques
"""
import argparse
import json
import os
import sys
import time
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sniffer_vrai import brut_onchain, fear_greed

INDEX = Path.home() / "ace777-test-day1" / "Index_Maison"
LIVE = INDEX / "thermo" / "live.json"
HISTORY = INDEX / "thermo" / "history.jsonl"
REGIME = INDEX / "thermo" / "regime_couleur.json"
REGIME_HIST = INDEX / "thermo" / "regime_couleur.jsonl"
JUSTESSE = INDEX / "scripts" / "regime_justesse.json"

SEUIL_MOVE_PCT = 0.3     # seuil de victoire réaliste (%)
HORIZON_H = 24           # horizon de validité de la couleur
SEUIL_FEAR = 50          # < 50 = peur (bearish), > 50 = greed (bullish)


# ============================== DIRECTIONS ==============================
def direction_onchain():
    """Direction du BRUT : whaleDir (surveiller_whales) + poussière en note."""
    b = brut_onchain()
    if isinstance(b, dict) and "whale_dir" in b:
        d = b.get("whale_dir", "neutral")
        if d not in ("bullish", "bearish", "neutral"):
            d = "neutral"
        note = "dust=%s | blocs_fantomes=%s%%" % (
            b.get("poussiere_score"), b.get("blocs_privatises_pct_fantome"))
        return d, note
    return "neutral", "onchain indisponible"


def direction_narratif():
    """Direction du NARRATIF : Fear&Greed (< 50 = peur/bearish, > 50 = greed/bullish)."""
    fg = fear_greed()
    try:
        v = int(fg.get("valeur", 50))
    except (TypeError, ValueError):
        v = 50
    if v < SEUIL_FEAR:
        return "bearish", v
    if v > SEUIL_FEAR:
        return "bullish", v
    return "neutral", v


# ============================== MATRICE ==============================
def couleur(onchain_dir, narratif_dir):
    if onchain_dir == "neutral" or narratif_dir == "neutral":
        return "ORANGE"
    if onchain_dir == "bullish" and narratif_dir == "bullish":
        return "VERT"
    if onchain_dir == "bullish" and narratif_dir == "bearish":
        return "JAUNE"
    if onchain_dir == "bearish" and narratif_dir == "bullish":
        return "ROUGE"
    if onchain_dir == "bearish" and narratif_dir == "bearish":
        return "NOIR"
    return "ORANGE"


def explication(couleur_):
    return {
        "VERT": "aligné : brut et narratif confirment -> favorable à l'entrée",
        "JAUNE": "contrarian : l'onchain accumule pendant que la foule a peur -> opportunité à confirmer",
        "ROUGE": "piège : narratif euphorique mais onchain vendeur -> NE PAS ENTRER",
        "NOIR": "aligné baissier : tout est vendeur -> rester dehors",
        "ORANGE": "pas assez de signal (un des deux neutre) -> attendre",
    }.get(couleur_, "?")


# ============================== SCORING ==============================
def load_history():
    out = []
    if not HISTORY.exists():
        return out
    try:
        with open(HISTORY, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    out.append(json.loads(line))
                except Exception:
                    continue
    except Exception:
        pass
    return out


def mark_at(history, target_ts, before=True):
    best = None
    for row in history:
        ts = row.get("tsUnix")
        v = row.get("mark")
        if ts is None or v is None:
            continue
        try:
            v = float(v)
        except (TypeError, ValueError):
            continue
        if before:
            if ts <= target_ts:
                best = v
        else:
            if ts >= target_ts:
                return v
    # before=False : aucun mark >= target -> horizon pas écoulé -> None
    return best


def juger(record, history):
    """Note une couleur passée vs le prix réel sur son horizon."""
    color = record.get("couleur")
    t0 = record.get("ts_unix")
    horizon_s = int(record.get("horizon_h", HORIZON_H)) * 3600
    if not color or not t0:
        return {"statut": "invalide"}
    p0 = mark_at(history, t0, before=True)
    p1 = mark_at(history, t0 + horizon_s, before=False)
    if p0 is None or p1 is None:
        return {"couleur": color, "statut": "en_attente"}
    move = (p1 - p0) / p0 * 100.0
    if color == "VERT":
        hit = move > SEUIL_MOVE_PCT
    elif color in ("ROUGE", "NOIR"):
        hit = move < -SEUIL_MOVE_PCT   # on a bien évité une baisse
    elif color == "JAUNE":
        hit = move > SEUIL_MOVE_PCT    # l'accumulation discrète a payé
    else:  # ORANGE
        hit = abs(move) < SEUIL_MOVE_PCT   # on a bien attendu un marché plat
    return {"couleur": color, "move_pct": round(move, 2),
            "statut": "HIT ✅" if hit else "MISS ❌"}


# ============================== MODES ==============================
def run_mode():
    onch, note_onch = direction_onchain()
    nar, fg_val = direction_narratif()
    c = couleur(onch, nar)
    now = datetime.now(timezone.utc)
    rec = {
        "ts": now.isoformat(),
        "ts_unix": int(time.time()),
        "couleur": c,
        "onchain_dir": onch,
        "narratif_dir": nar,
        "fear_greed": fg_val,
        "detail_onchain": note_onch,
        "horizon_h": HORIZON_H,
        "mode": "observation",
        "explication": explication(c),
    }
    REGIME.parent.mkdir(parents=True, exist_ok=True)
    REGIME.write_text(json.dumps(rec, ensure_ascii=False, indent=2), encoding="utf-8")
    with open(REGIME_HIST, "a", encoding="utf-8") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    print("COULEUR RÉGIME : %s (%s)" % (c, explication(c)))
    print("  onchain=%s (%s) | narratif=%s (fear&greed %s) | horizon=%dh | OBSERVATION"
          % (onch, note_onch, nar, fg_val, HORIZON_H))
    return 0


def score_mode():
    history = load_history()
    if not REGIME_HIST.exists():
        print("Aucune couleur historique à noter.")
        return 0
    par_couleur = {}
    total_hit = total_scored = 0
    with open(REGIME_HIST, encoding="utf-8") as f:
        for line in f:
            try:
                rec = json.loads(line)
            except Exception:
                continue
            v = juger(rec, history)
            if v.get("statut") in ("HIT ✅", "MISS ❌"):
                c = v["couleur"]
                total_scored += 1
                par_couleur.setdefault(c, {"hit": 0, "n": 0})
                par_couleur[c]["n"] += 1
                if v["statut"] == "HIT ✅":
                    total_hit += 1
                    par_couleur[c]["hit"] += 1
    for c in par_couleur:
        par_couleur[c]["taux_pct"] = round(par_couleur[c]["hit"] / par_couleur[c]["n"] * 100, 1)
    res = {"version": 1, "total_hit": total_hit, "total_scored": total_scored,
           "pct": round(total_hit / total_scored * 100, 1) if total_scored else None,
           "seuil_move_pct": SEUIL_MOVE_PCT, "par_couleur": par_couleur,
           "ts": datetime.now(timezone.utc).isoformat()}
    JUSTESSE.write_text(json.dumps(res, ensure_ascii=False, indent=2), encoding="utf-8")
    print("=== JUSTESSE COULEUR RÉGIME ===")
    if total_scored:
        print("GLOBAL : %d/%d = %s%% (sur %d couleurs notées)"
              % (total_hit, total_scored, res["pct"], len(par_couleur)))
    for c in sorted(par_couleur):
        s = par_couleur[c]
        print("  %-7s : %d/%d = %s%%" % (c, s["hit"], s["n"], s["taux_pct"]))
    print("(écrit : %s)" % JUSTESSE)
    return 0


def lecons_mode():
    if not JUSTESSE.exists():
        print("Pas de justesse encore — lancer --score d'abord.")
        return 0
    j = json.loads(JUSTESSE.read_text(encoding="utf-8"))
    print("=== LEÇONS (auto-nourries) ===")
    for c, s in sorted(j.get("par_couleur", {}).items()):
        n, taux = s.get("n", 0), s.get("taux_pct", 0)
        if n < 5:
            verdict = "pas assez de données (min 5)"
        elif taux >= 75:
            verdict = "FIABLE : garder ce signal fort"
        elif taux <= 50:
            verdict = "PEU FIABLE : ramollir ce signal (vérifier le seuil)"
        else:
            verdict = "neutre : corroborer avec un autre signal"
        print("  %-7s : %s%% (%d n) -> %s" % (c, taux, n, verdict))
    return 0


# ============================== TESTS ==============================
def run_tests():
    errors = 0

    def check(name, cond):
        nonlocal errors
        print("  %s %s" % ("✓" if cond else "✗", name))
        if not cond:
            errors += 1

    check("bullish+bullish -> VERT", couleur("bullish", "bullish") == "VERT")
    check("bullish+bearish -> JAUNE", couleur("bullish", "bearish") == "JAUNE")
    check("bearish+bullish -> ROUGE", couleur("bearish", "bullish") == "ROUGE")
    check("bearish+bearish -> NOIR", couleur("bearish", "bearish") == "NOIR")
    check("neutral -> ORANGE", couleur("neutral", "bullish") == "ORANGE")
    check("narratif neutral -> ORANGE", couleur("bullish", "neutral") == "ORANGE")

    # scoring : ROUGE (éviter) sur une baisse -> HIT
    base = 1_700_000_000
    hist = [{"tsUnix": base, "mark": 100000.0},
            {"tsUnix": base + 24 * 3600, "mark": 99000.0}]  # -1%
    v = juger({"couleur": "ROUGE", "ts_unix": base, "horizon_h": 24}, hist)
    check("ROUGE sur baisse -1% -> HIT", v["statut"] == "HIT ✅")
    v = juger({"couleur": "VERT", "ts_unix": base, "horizon_h": 24}, hist)
    check("VERT sur baisse -1% -> MISS", v["statut"] == "MISS ❌")
    print("=== %s (%d erreur%s) ===" % (
        "TOUS LES TESTS VERTS" if errors == 0 else "ÉCHEC",
        errors, "s" if errors > 1 else ""))
    return 0 if errors == 0 else 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", action="store_true")
    ap.add_argument("--score", action="store_true")
    ap.add_argument("--lecons", action="store_true")
    ap.add_argument("--test", action="store_true")
    a = ap.parse_args()
    if a.test:
        return run_tests()
    if a.score:
        return score_mode()
    if a.lecons:
        return lecons_mode()
    return run_mode()   # défaut = --run


if __name__ == "__main__":
    sys.exit(main())
