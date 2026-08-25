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
import re
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
MISSION = INDEX / "cockpit" / "mission.json"
ANALYSES_DIR = INDEX / "thermo" / "analyses"
REGIME = INDEX / "thermo" / "regime_couleur.json"
REGIME_HIST = INDEX / "thermo" / "regime_couleur.jsonl"
JUSTESSE = INDEX / "scripts" / "regime_justesse.json"

SEUIL_MOVE_PCT = 0.3     # seuil de victoire réaliste (%)
HORIZON_H = 24           # horizon de validité de la couleur
SEUIL_FEAR = 50          # < 50 = peur (bearish), > 50 = greed (bullish)


# ============================== SOURCES AUXILIAIRES ==============================
def load_mission():
    """Charge cockpit/mission.json (combo trading, alert=red, PnL)."""
    if not MISSION.exists():
        return {}
    try:
        return json.loads(MISSION.read_text(encoding="utf-8"))
    except Exception:
        return {}


def load_dernier_avis():
    """Dernier AVIS STRICT de Cortana par indice (thermo/analyses/*.jsonl).
    Retourne {indice: {avis, horizon, confiance, ts}}."""
    if not ANALYSES_DIR.is_dir():
        return {}
    avis_par_indice = {}
    for fn in sorted(ANALYSES_DIR.glob("*.jsonl")):
        try:
            lines = fn.read_text(encoding="utf-8").splitlines()
        except Exception:
            continue
        for line in lines:
            line = line.strip()
            if not line:
                continue
            try:
                e = json.loads(line)
            except Exception:
                continue
            indice = e.get("indice")
            txt = e.get("analyse") or ""
            avis_m = horizon_m = conf_m = None
            for l in txt.splitlines():
                s = l.strip()
                if s.lower().startswith("avis strict"):
                    avis_m = re.search(r"AVIS\s*STRICT\s*:\s*(\w+)", s)
                elif s.lower().startswith("horizon"):
                    horizon_m = re.search(r"HORIZON\s*:\s*([^\n]+)", s)
                elif s.lower().startswith("confiance"):
                    conf_m = re.search(r"CONFIANCE\s*:\s*(\w+)", s)
            if not indice or not avis_m:
                continue
            avis_par_indice[indice] = {
                "avis": avis_m.group(1).upper(),
                "horizon": horizon_m.group(1).strip().lower() if horizon_m else None,
                "confiance": conf_m.group(1).lower() if conf_m else None,
                "ts": e.get("ts"),
            }
    return avis_par_indice


def direction_avis_ia(avis_par_indice: dict) -> tuple[str, str]:
    """Direction consensus des avis IA (LONG→bullish, SHORT→bearish, sinon neutral).
    Moyenne pondérée si plusieurs indices parlent."""
    if not avis_par_indice:
        return "neutral", "pas d'avis IA"
    bullish_n = bearish_n = 0
    for idx, a in avis_par_indice.items():
        av = a.get("avis", "")
        if av == "LONG":
            bullish_n += 1
        elif av == "SHORT":
            bearish_n += 1
    total = bullish_n + bearish_n
    if total == 0:
        return "neutral", "avis IA neutres (%d indices)" % len(avis_par_indice)
    if bullish_n > bearish_n:
        return "bullish", "avis IA: %d LONG / %d SHORT" % (bullish_n, bearish_n)
    if bearish_n > bullish_n:
        return "bearish", "avis IA: %d LONG / %d SHORT" % (bullish_n, bearish_n)
    return "neutral", "avis IA ex-aequo (%d/%d)" % (bullish_n, bearish_n)


# ============================== DIRECTIONS ==============================
def direction_onchain():
    """Direction du BRUT : whaleDir (scan onchain + proxy Cortana) + poussière en note.

    FIX 21/08 : le pont combine désormais le scan baleines (inflow/outflow) et le
    proxy de Cortana (prints aggTrades ≥ 500k$, bullish/bearish) dans whaleDir —
    la couleur sort enfin d'ORANGE quand l'un des deux parle.
    """
    b = brut_onchain()
    if isinstance(b, dict) and "whale_dir" in b:
        d = b.get("whale_dir", "neutral")
        # normalisation : scan onchain parle inflow/outflow, la matrice parle bullish/bearish
        d = {"inflow": "bullish", "outflow": "bearish"}.get(d, d)
        if d not in ("bullish", "bearish", "neutral"):
            d = "neutral"
        note = "dust=%s | blocs_fantomes=%s%%" % (
            b.get("poussiere_score"), b.get("blocs_privatises_pct_fantome"))
        return d, note
    return "neutral", "onchain indisponible"


def direction_thermo(mission: dict) -> tuple[str, str]:
    """Direction du THERMO (alert=red, combo PnL) — lecture de mission.json.

    alert=red → les baleines tradent en perdition → prudence (bearish lean)
    alert=ok → le combo tourne bien → pas de frein (neutral)
    """
    alert = mission.get("alert", "unknown")
    pnl_net = mission.get("comboPnlNet", 0)
    session = mission.get("sessionSince", "?")
    if alert == "red":
        # Le combo est en alerte : pnl net négatif depuis le début de session
        if pnl_net and pnl_net < -100:
            return "bearish", "thermo: alert=red, combo net=%.0f$ (depuis %s)" % (pnl_net, session)
        return "bearish", "thermo: alert=red (depuis %s)" % session
    if alert == "ok":
        return "neutral", "thermo: alert=ok"
    return "neutral", "thermo: alert=%s" % alert


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

    # === 3e source : avis IA (LLMs analystes) ===
    avis_par_indice = load_dernier_avis()
    avis_dir, note_avis = direction_avis_ia(avis_par_indice)

    # === 4e source : thermo (mission trading, alert=red) ===
    mission = load_mission()
    thermo_dir, note_thermo = direction_thermo(mission)

    # === Matrice avec 4 directions ===
    # Règle : onchain + narratif = base, avis = confirmation, thermo = frein/accélérateur
    c = couleur(onch, nar)

    # Thermo : si alert=red, il freine un VERT (affaiblir) ou confirme un ROUGE/NOIR
    if thermo_dir == "bearish" and c == "VERT":
        c = "ORANGE"  # le combo trading perd → pas confiant pour entrer
        exp = "VERT affaibli par alert=red (thermo prudence)"
    elif thermo_dir == "bearish" and c == "JAUNE":
        c = "ORANGE"  # l'accumulation discrète + combo qui perd → trop risqué
        exp = "JAUNE affaibli par alert=red"
    elif thermo_dir == "bearish" and c in ("ROUGE", "NOIR"):
        exp = explication(c) + " + alert=red confirme"
    else:
        exp = explication(c)

    # Avis IA : si 2/3+ LLMs disent SHORT alors que onchain=bullish → affaiblir
    if avis_dir == "bearish" and onch == "bullish" and c == "VERT":
        c = "ORANGE"  # divergence avis/onchain → prudence
        exp += " | avis IA divergent (SHORT vs bullish onchain)"
    elif avis_dir == "bullish" and c == "ORANGE" and onch != "neutral":
        exp += " | avis IA confirme (%s)" % note_avis
    else:
        if avis_dir != "neutral":
            exp += " | avis IA: %s" % note_avis

    now = datetime.now(timezone.utc)
    rec = {
        "ts": now.isoformat(),
        "ts_unix": int(time.time()),
        "couleur": c,
        "onchain_dir": onch,
        "narratif_dir": nar,
        "avis_ia_dir": avis_dir,
        "thermo_dir": thermo_dir,
        "fear_greed": fg_val,
        "detail_onchain": note_onch,
        "detail_avis": note_avis,
        "detail_thermo": note_thermo,
        "horizon_h": HORIZON_H,
        "mode": "observation",
        "explication": exp,
    }
    REGIME.parent.mkdir(parents=True, exist_ok=True)
    REGIME.write_text(json.dumps(rec, ensure_ascii=False, indent=2), encoding="utf-8")
    with open(REGIME_HIST, "a", encoding="utf-8") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    print("COULEUR RÉGIME : %s (%s)" % (c, exp))
    print("  onchain=%s (%s) | narratif=%s (F&G %s)" % (onch, note_onch, nar, fg_val))
    print("  avis_ia=%s (%s) | thermo=%s (%s)" % (avis_dir, note_avis, thermo_dir, note_thermo))
    print("  horizon=%dh | OBSERVATION" % HORIZON_H)
    return 0


def score_mode():
    history = load_history()
    if not REGIME_HIST.exists():
        print("Aucune couleur historique à noter.")
        return 0
    # DÉDUPLICATION par créneau horaire (fix 23/08) : la boucle KeepAlive
    # (plist cassé) a écrit ~10 000 lignes en 3 jours -> les doublons faussaient
    # le score (34 % affiché, dont 99 % de copies). On garde UNE couleur par heure
    # (la dernière du créneau = l'état le plus récent du calcul).
    creneaux = {}
    with open(REGIME_HIST, encoding="utf-8") as f:
        for line in f:
            try:
                rec = json.loads(line)
            except Exception:
                continue
            ts = rec.get("ts")
            if isinstance(ts, str) and len(ts) >= 13:
                creneaux[ts[:13]] = rec  # dernière couleur du créneau horaire
    par_couleur = {}
    total_hit = total_scored = 0
    for rec in creneaux.values():
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
           "creneaux_uniques": len(creneaux), "lignes_brutes": 0,
           "ts": datetime.now(timezone.utc).isoformat()}
    JUSTESSE.write_text(json.dumps(res, ensure_ascii=False, indent=2), encoding="utf-8")
    print("=== JUSTESSE COULEUR RÉGIME (dédup par heure) ===")
    if total_scored:
        print("GLOBAL : %d/%d = %s%% (sur %d créneaux horaires uniques)"
              % (total_hit, total_scored, res["pct"], len(creneaux)))
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

    # tests des nouvelles sources
    d, _ = direction_thermo({"alert": "red", "comboPnlNet": -200, "sessionSince": "13:48Z"})
    check("thermo alert=red + pnl_net=-200 -> bearish", d == "bearish")
    d, _ = direction_thermo({"alert": "ok"})
    check("thermo alert=ok -> neutral", d == "neutral")
    d, _ = direction_thermo({})
    check("thermo absent -> neutral", d == "neutral")

    d, _ = direction_avis_ia({})
    check("avis IA vide -> neutral", d == "neutral")
    d, _ = direction_avis_ia({"radar": {"avis": "LONG"}, "funding": {"avis": "LONG"}, "btc": {"avis": "SHORT"}})
    check("avis 2 LONG / 1 SHORT -> bullish", d == "bullish")
    d, _ = direction_avis_ia({"radar": {"avis": "SHORT"}, "funding": {"avis": "SHORT"}})
    check("avis 2 SHORT -> bearish", d == "bearish")
    d, _ = direction_avis_ia({"radar": {"avis": "LONG"}, "funding": {"avis": "SHORT"}})
    check("avis 1/1 ex-aequo -> neutral", d == "neutral")

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
