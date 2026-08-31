#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""score_justesse.py — le PROFESSEUR note l'analyste (chantier 3, C6) — v2 (F1)

Exigence Christophe (06/08) : chaque analyse est ENREGISTRÉE, et on compare
ensuite avec ce que le marché a RÉELLEMENT fait -> score de justesse de
l'analyste (Cortana/Gemini).

=== v2 (15/08, F1 fondations acteurs — validé famille 4/4) ===
Corrections (le v1 jugeait mal, cf. VERDICT_FAMILLE) :
1. SEUIL réaliste : 0,05 % -> SEUIL_MOVE_PCT = 0,3 % (0,05 % = bruit).
2. NEUTRE désormais NOTÉ : marché plat (< seuil) = HIT (bien resté dehors) ;
   marché bougé (>= seuil) = MISS (a raté un vrai mouvement). Fini l'échappatoire.
3. Chaque indice est vérifié CONTRE SA PROPRE ÉVOLUTION (pas tout vs BTC) :
   - le call (AVIS STRICT LONG/SHORT) reste jugé sur le prix BTC (l'instrument tradé) ;
   - en PLUS, on trace `indice_move_pct` = évolution propre de l'indice analysé
     (via history.jsonl) pour identifier quels indices sont réellement prédictifs.
4. `derniere` = la DERNIÈRE analyse (le v1 renvoyait la première — bug).
5. Sortie VERSIONNÉE `justesse_v2.json` + rétro-compat `justesse_cockpit.json`
   (mêmes clés lues par cortana_analyse.py).
6. Backfill : re-scorer l'historique complet (93 analyses) sur la nouvelle logique.
7. `--test` : tests de régression hermétiques (seuil, NEUTRE, derniere, self-move).

Usage :
  python3 score_justesse.py            # note toutes les analyses (+ écrit v2)
  python3 score_justesse.py --jour 2026-08-06
  python3 score_justesse.py --detail   # détail ligne par ligne
  python3 score_justesse.py --test     # auto-tests hermétiques (sans fichiers réels)
"""
import argparse
import json
import os
import re
import sys
import tempfile
import shutil
from datetime import datetime, timezone

# === CONSTANTES v2 (F1) ===
SEUIL_MOVE_PCT = 0.3          # seuil de victoire réaliste (% : le 0,05 % d'avant = bruit)
SEUIL_FLAT_PCT = SEUIL_MOVE_PCT  # bande "marché indécis" pour LONG/SHORT

# === ZONE MORTE (31/08, GO Christophe) ===
# Un indice collé à sa valeur neutre ne porte AUCUNE information directionnelle :
# l'analyse n'est PAS notée (ni HIT ni MISS). La décision vient de la DONNÉE
# (le chiffre), jamais de l'analyste → pas d'échappatoire possible.
# Funding Binance : 0.01% = neutre, < 0.02%/8h = zone morte (notre base entière).
FUNDING_DEAD_ZONE = 0.0002
# Compteur anti-fuite : si l'analyste répond NEUTRE sur plus de 60% des analyses
# où le signal EXISTE, c'est de l'évitement → alarme (elle esquive le verdict).
NEUTRE_FUITE_MAX = 0.60

THERMO_DIR = os.path.expanduser("~/ace777-test-day1/Index_Maison/thermo")
ANALYSES_DIR = os.path.join(THERMO_DIR, "analyses")
HISTORY = os.path.join(THERMO_DIR, "history.jsonl")
OUT_V2 = os.path.join(os.path.dirname(os.path.abspath(__file__)), "justesse_v2.json")
OUT_COCKPIT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "justesse_cockpit.json")

HORIZONS = {"24h": 24 * 3600, "1 semaine": 7 * 24 * 3600, "1sem": 7 * 24 * 3600,
            "semaine": 7 * 24 * 3600, "48h": 48 * 3600, "1h": 3600, "4h": 4 * 3600}

# === MAPPING indice -> clé de sa propre série dans history.jsonl (self-vérification) ===
# Un indice ABSENT de ce mapping = pas de série propre traçable -> self_move = None.
INDICE_SELF_KEY = {
    "funding": "funding",
    "fundingAvg30": "fundingAvg30",
    "oi": "oi",
    "longShort": "longShort",
    "takerRatio": "takerRatio",
    "topTraderLS": "topTraderLS",
    "fearGreed": "fearGreed",
    "marketCapUsd": "marketCapUsd",
    "btcDominance": "btcDominance",
    "altSeason": "altSeasonScore",   # altSeason (label) -> son score numérique
    "liq24Usd": "liq24Usd",
    "gexPutCall": "gexPutCall",
    "etfBtcM": "etfBtcM",
    "chg24": "chg24",
    "panierDownPct": "panierDownPct",
    "whaleUsd": "whaleUsd",
    "whaleN": "whaleN",
    "score": "score",
    "mark": "mark",
    "radar": "score",               # virtuel : radar = score climat
    "bassine": "score",             # virtuel : bassine = score
    "volumeCachedTaker": "volumeCachedTaker",
    "volumeCachedPerpSpot": "volumeCachedPerpSpot",
    # ─── Nouveaux indices (PIPELINE UNIFIÉ 25/08 + onchain/geopol, ajoutés 27/08) ───
    # Série propre pas encore dans history.jsonl → self-move = None pour l'instant
    # (noté vs BTC), l'auto-vérification s'activera dès que la série existera.
    "sdi": "sdi",
    "ipt": "ipt",
    "rbf": "rbf_score",
    "indice_onchain": "indiceOnchain",
    "pipeline_health": "global_score",
    "geopol": "score",
}


def load_history():
    out = []
    if not os.path.exists(HISTORY):
        return out
    try:
        with open(HISTORY) as f:
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


def load_analyses(jour=None):
    entries = []
    if not os.path.isdir(ANALYSES_DIR):
        return entries
    for fn in sorted(os.listdir(ANALYSES_DIR)):
        if not fn.endswith(".jsonl"):
            continue
        if jour and jour not in fn:
            continue
        with open(os.path.join(ANALYSES_DIR, fn)) as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    entries.append(json.loads(line))
                except Exception:
                    continue
    return entries


def parse_avis(analyse):
    txt = analyse.get("analyse", "") or ""
    avis = re.search(r"AVIS\s*STRICT\s*:\s*(\w+)", txt)
    horizon = re.search(r"HORIZON\s*:\s*([0-9]+h|1\s*semaine|semaine|48h|24h|1h|4h)", txt)
    confiance = re.search(r"CONFIANCE\s*:\s*(\w+)", txt)
    return {
        "avis": avis.group(1).upper() if avis else None,
        "horizon": horizon.group(1).strip().lower() if horizon else None,
        "confiance": confiance.group(1).lower() if confiance else None,
    }


def ts_of(analyse):
    raw = analyse.get("faits_bruts") or {}
    if raw.get("ts"):
        try:
            return datetime.fromisoformat(raw["ts"].replace("Z", "+00:00")).timestamp()
        except Exception:
            pass
    try:
        return datetime.fromisoformat(analyse["ts"].replace("Z", "+00:00")).timestamp()
    except Exception:
        return None


def value_at(history, key, target_ts, before=True):
    """Valeur de la clé `key` la plus proche de target_ts (before=True -> dernier point <= target)."""
    best = None
    for row in history:
        ts = row.get("tsUnix")
        v = row.get(key)
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
            best = v
    return best


def pct_move(p0, p1):
    if p0 is None or p1 is None or p0 == 0:
        return None
    return (p1 - p0) / p0 * 100.0


def juger(analyse, history):
    """Retourne le verdict v2 pour une analyse (call BTC + move propre de l'indice)."""
    avis_info = parse_avis(analyse)
    avis = avis_info["avis"]
    indice = analyse.get("indice")
    out = {**avis_info, "indice": indice, "indice_move_pct": None}

    # move propre de l'indice (self-vérification), indépendant du call
    self_key = INDICE_SELF_KEY.get(indice)
    t0 = ts_of(analyse)
    if t0 is not None and self_key:
        hor = avis_info["horizon"] or "24h"
        seconds = HORIZONS.get(hor, 24 * 3600)
        s0 = value_at(history, self_key, t0, before=True)
        s1 = value_at(history, self_key, t0 + seconds, before=False)
        out["indice_move_pct"] = round(pct_move(s0, s1), 2) if pct_move(s0, s1) is not None else None

    # ZONE MORTE (31/08, GO Christophe) : indice sans signal = NON NOTÉ.
    # C'est la DONNÉE qui décide (le chiffre), pas l'analyste → elle ne peut pas
    # s'y cacher : si le funding est dans la zone morte, AUCUN avis n'est noté,
    # même un LONG/SHORT affirmé (le signal n'existe pas, le verdict serait du bruit).
    if indice == "funding" and t0 is not None:
        f0 = value_at(history, "funding", t0, before=True)
        if f0 is not None and abs(float(f0)) < FUNDING_DEAD_ZONE:
            return {**out, "statut": "zone_morte",
                    "detail": f"funding {float(f0):.6f} < seuil {FUNDING_DEAD_ZONE:.6f} (neutre, non noté)"}

    if avis not in ("LONG", "SHORT", "NEUTRE"):
        return {**out, "statut": "sans_verdict" if not avis else "abstention",
                "detail": f"avis={avis}"}

    if t0 is None:
        return {**out, "statut": "ts_introuvable"}

    hor = avis_info["horizon"] or "24h"
    seconds = HORIZONS.get(hor, 24 * 3600)

    p0 = value_at(history, "mark", t0, before=True)
    if p0 is None:
        return {**out, "statut": "prix_depart_introuvable"}

    t1 = t0 + seconds
    p1 = value_at(history, "mark", t1, before=False)
    if p1 is None:
        return {**out, "statut": "en_attente",
                "detail": f"horizon {hor} pas encore écoulé (p0={p0:.0f})"}

    move = pct_move(p0, p1)
    out["move_pct"] = round(move, 2)

    if avis == "LONG":
        if move > SEUIL_MOVE_PCT:
            statut = "HIT ✅"
        elif move < -SEUIL_MOVE_PCT:
            statut = "MISS ❌"
        else:
            statut = "FLAT ➖"
    elif avis == "SHORT":
        if move < -SEUIL_MOVE_PCT:
            statut = "HIT ✅"
        elif move > SEUIL_MOVE_PCT:
            statut = "MISS ❌"
        else:
            statut = "FLAT ➖"
    else:  # NEUTRE désormais NOTÉ (v2)
        if abs(move) < SEUIL_MOVE_PCT:
            statut = "HIT ✅"
        else:
            statut = "MISS ❌"

    return {**out, "statut": statut, "p0": p0, "p1": p1,
            "detail": f"{p0:.0f} -> {p1:.0f} ({move:+.2f}%)"}


def build_resume(analyses, history):
    """Construit le résumé v2 complet (pour justesse_v2.json + cockpit)."""
    total_hit = total_scored = 0
    par_indice = {}
    neutre_par_indice = {}
    derniere = None
    # Compteur anti-fuite (31/08, GO Christophe) : NEUTRE émis alors que le signal
    # EXISTE (hors zone morte) = évitement possible. Compté séparément, alarme > 60%.
    n_avis = 0          # analyses avec avis LONG/SHORT/NEUTRE (hors abstention)
    n_neutre_signal = 0  # NEUTRE émis avec signal présent (HIT/MISS/FLAT)

    for an in analyses:
        v = juger(an, history)
        indice = an.get("indice", "?")
        if v.get("avis") in ("LONG", "SHORT", "NEUTRE"):
            n_avis += 1
            if v.get("avis") == "NEUTRE" and v["statut"] in ("HIT ✅", "MISS ❌", "FLAT ➖"):
                n_neutre_signal += 1
        # derniere = LA DERNIÈRE analyse (fix v2 : v1 prenait la première)
        if v.get("avis") in ("LONG", "SHORT", "NEUTRE"):
            derniere = {
                "ts": an.get("ts"), "indice": indice,
                "avis": v.get("avis"), "horizon": v.get("horizon"),
                "confiance": v.get("confiance"), "statut": v.get("statut"),
                "detail": v.get("detail"), "move_pct": v.get("move_pct"),
                "indice_move_pct": v.get("indice_move_pct"),
            }
        # FLAT (marché indécis, bande < seuil) = NON NOTÉ : il ne doit ni compter
        # comme échec ni diluer le score (fix 23/08 : il était compté au
        # dénominateur alors que l'affichage le déclarait « non noté » → biais -12 pts).
        if v["statut"] in ("HIT ✅", "MISS ❌"):
            total_scored += 1
            par_indice.setdefault(indice, {"hit": 0, "n": 0})
            par_indice[indice]["n"] += 1
            if v["statut"] == "HIT ✅":
                total_hit += 1
                par_indice[indice]["hit"] += 1
        if v.get("avis") == "NEUTRE":
            neutre_par_indice[indice] = neutre_par_indice.get(indice, 0) + 1

    # enrichir par_indice du compteur NEUTRE (biais par indice)
    for indice in par_indice:
        par_indice[indice]["neutre"] = neutre_par_indice.get(indice, 0)

    # Alarme anti-fuite : NEUTRE avec signal présent > 60% des avis = elle esquive.
    neutre_taux = (n_neutre_signal / n_avis * 100.0) if n_avis else None
    alerte_fuite = bool(n_avis and (n_neutre_signal / n_avis) > NEUTRE_FUITE_MAX)

    return {
        "version": "v2",
        "n": len(analyses),
        "total_hit": total_hit,
        "total_scored": total_scored,
        "pct": round(total_hit / total_scored * 100, 1) if total_scored else None,
        "seuil_move_pct": SEUIL_MOVE_PCT,
        "par_indice": {k: par_indice[k] for k in sorted(par_indice)},
        "derniere": derniere,
        # ZONE MORTE + ANTI-FUITE (31/08, GO Christophe)
        "zone_morte": {"seuil_funding": FUNDING_DEAD_ZONE},
        "evitement": {
            "neutre_signal": n_neutre_signal,
            "n_avis": n_avis,
            "taux_pct": round(neutre_taux, 1) if neutre_taux is not None else None,
            "alerte": alerte_fuite,
            "seuil_pct": NEUTRE_FUITE_MAX * 100,
            "note": "NEUTRE émis alors que le signal existe — si >60% des avis, alarme évitement",
        },
        "ts": datetime.now(timezone.utc).isoformat(),
    }


def write_json(path, data):
    try:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return True
    except Exception:
        return False


def main():
    ap = argparse.ArgumentParser(description="Score de justesse de l'analyste (v2)")
    ap.add_argument("--jour", default=None, help="YYYY-MM-DD (défaut: tous)")
    ap.add_argument("--detail", action="store_true", help="détail ligne par ligne")
    ap.add_argument("--json", metavar="PATH", help="écrit le score dans PATH (JSON)")
    ap.add_argument("--test", action="store_true", help="auto-tests hermétiques (sans fichiers réels)")
    a = ap.parse_args()

    if a.test:
        sys.exit(run_tests())

    history = load_history()
    analyses = load_analyses(a.jour)
    if not analyses:
        print("Aucune analyse dans le journal. (lancer d'abord cortana_analyse.py)")
        return 0

    print(f"=== SCORE DE JUSTESSE v2 — {len(analyses)} analyse(s) · seuil {SEUIL_MOVE_PCT}% ===")

    total_hit = total_scored = 0
    for an in analyses:
        v = juger(an, history)
        ligne = f"  [{an.get('ts','?')[:16]}] {an.get('indice','?'):14} "
        ligne += f"{v['avis'] or '-':6} h={v['horizon'] or '?':9} c={v['confiance'] or '?':7} "
        ligne += f"→ {v['statut']}"
        if v.get("indice_move_pct") is not None:
            ligne += f"  (indice {v['indice_move_pct']:+.2f}%)"
        if a.detail and v.get("detail"):
            ligne += f"  ({v['detail']})"
        print(ligne)
        # FLAT (marché indécis) = NON NOTÉ (cohérent avec build_resume, fix 23/08)
        if v["statut"] in ("HIT ✅", "MISS ❌"):
            total_scored += 1
            if v["statut"] == "HIT ✅":
                total_hit += 1

    print()
    if total_scored:
        pct = total_hit / total_scored * 100
        print(f"  GLOBAL : {total_hit}/{total_scored} = {pct:.0f} % de justesse (NEUTRE noté)")
    else:
        print("  Aucun verdict noté pour l'instant — attendre que les horizons s'écoulent.")
    print("  NB: NEUTRE noté (plat=HIT, bougé=MISS) · FLAT = marché indécis (non noté)")
    print("      ZONE MORTE (31/08, GO Christophe) : funding < 0.02%% = signal inexistant -> non noté (décidé par la donnée).")

    resume = build_resume(analyses, history)
    write_json(OUT_V2, resume)
    write_json(OUT_COCKPIT, resume)  # rétro-compat cockpit (mêmes clés de base)
    print(f"\n[score_justesse] v2 écrit : {OUT_V2}")
    print(f"[score_justesse] cockpit (compat) : {OUT_COCKPIT}")

    if a.json:
        write_json(a.json, resume)
        print(f"[score_justesse] JSON écrit : {a.json}")
    return 0


# === TESTS HERMÉTIQUES (v2) ===
def run_tests():
    global ANALYSES_DIR, HISTORY, THERMO_DIR, OUT_V2, OUT_COCKPIT
    _sauve = (ANALYSES_DIR, HISTORY, THERMO_DIR, OUT_V2, OUT_COCKPIT)
    tmp = tempfile.mkdtemp(prefix="score_justesse_test_")
    ANALYSES_DIR = os.path.join(tmp, "analyses")
    HISTORY = os.path.join(tmp, "history.jsonl")
    os.makedirs(ANALYSES_DIR, exist_ok=True)
    OUT_V2 = os.path.join(tmp, "justesse_v2.json")
    OUT_COCKPIT = os.path.join(tmp, "justesse_cockpit.json")
    errors = 0

    def check(name, cond):
        nonlocal errors
        print("  %s %s" % ("✓" if cond else "✗", name))
        if not cond:
            errors += 1

    def restore():
        global ANALYSES_DIR, HISTORY, THERMO_DIR, OUT_V2, OUT_COCKPIT
        (ANALYSES_DIR, HISTORY, THERMO_DIR, OUT_V2, OUT_COCKPIT) = _sauve

    # Historique synthétique : mark 100000 -> 100000 (plat) ; funding 0.0005 -> 0.0005
    # (0.0005 > zone morte 0.0002 → le funding PARLE ici, la logique HIT/MISS est testable)
    base = 1_700_000_000
    hist = [
        {"tsUnix": base, "mark": 100000.0, "funding": 0.0005},
        {"tsUnix": base + 24 * 3600, "mark": 100000.0, "funding": 0.0005},   # plat
    ]
    with open(HISTORY, "w") as f:
        for r in hist:
            f.write(json.dumps(r) + "\n")

    def mk_analyse(ts, indice, avis, horizon="24h"):
        return {
            "ts": datetime.fromtimestamp(ts, timezone.utc).isoformat(),
            "indice": indice,
            "faits_bruts": {"ts": datetime.fromtimestamp(ts, timezone.utc).isoformat()},
            "analyse": f"FAITS : ...\nAVIS STRICT : {avis}\nHORIZON : {horizon}\nCONFIANCE : moyenne",
        }

    # NEUTRE sur marché plat -> HIT (v2 : NEUTRE noté)
    v = juger(mk_analyse(base, "funding", "NEUTRE"), hist)
    check("NEUTRE marché plat -> HIT", v["statut"] == "HIT ✅")

    # NEUTRE sur marché bougé -> MISS
    hist2 = [
        {"tsUnix": base, "mark": 100000.0, "funding": 0.0005},
        {"tsUnix": base + 24 * 3600, "mark": 101000.0, "funding": 0.0005},   # +1%
    ]
    v = juger(mk_analyse(base, "funding", "NEUTRE"), hist2)
    check("NEUTRE marché bougé (+1%) -> MISS", v["statut"] == "MISS ❌")

    # LONG + move > seuil -> HIT (avec +1%, seuil 0,3%)
    v = juger(mk_analyse(base, "funding", "LONG"), hist2)
    check("LONG +1% -> HIT", v["statut"] == "HIT ✅")

    # LONG sur plat -> FLAT (bande indécise < 0,3%)
    v = juger(mk_analyse(base, "funding", "LONG"), hist)
    check("LONG marché plat -> FLAT", v["statut"] == "FLAT ➖")

    # SHORT + baisse -> HIT
    hist3 = [
        {"tsUnix": base, "mark": 100000.0, "funding": 0.0005},
        {"tsUnix": base + 24 * 3600, "mark": 99000.0, "funding": 0.0005},    # -1%
    ]
    v = juger(mk_analyse(base, "funding", "SHORT"), hist3)
    check("SHORT -1% -> HIT", v["statut"] == "HIT ✅")

    # Self-move : funding analysé -> sa propre série tracée (pas seulement BTC)
    hist4 = [
        {"tsUnix": base, "mark": 100000.0, "funding": 0.0005},
        {"tsUnix": base + 24 * 3600, "mark": 100000.0, "funding": 0.0010},   # funding x2, BTC plat
    ]
    v = juger(mk_analyse(base, "funding", "LONG"), hist4)
    check("indice_move_pct tracé pour funding (+100%)", v.get("indice_move_pct") == 100.0)

    # ─── ZONE MORTE (31/08, GO Christophe) : la DONNÉE décide, pas l'analyste ───
    # funding 0.0001 (< seuil 0.0002) → zone_morte, même avec un LONG affirmé
    hist_z = [
        {"tsUnix": base, "mark": 100000.0, "funding": 0.0001},
        {"tsUnix": base + 24 * 3600, "mark": 100000.0, "funding": 0.0001},   # funding neutre
    ]
    v = juger(mk_analyse(base, "funding", "LONG"), hist_z)
    check("funding zone morte (0.0001) -> non noté même si LONG", v["statut"] == "zone_morte")
    v = juger(mk_analyse(base, "funding", "NEUTRE"), hist_z)
    check("funding zone morte (0.0001) -> non noté même si NEUTRE", v["statut"] == "zone_morte")
    # zone morte hors funding : un autre indice n'est PAS affecté par la règle funding
    v = juger(mk_analyse(base, "fearGreed", "LONG"), hist_z)
    check("hors funding, la zone morte ne s'applique pas (fearGreed noté)",
          v["statut"] in ("HIT ✅", "MISS ❌", "FLAT ➖"))
    # non compté dans le score global (marché qui bouge pour que fearGreed soit noté)
    hist_z2 = [
        {"tsUnix": base, "mark": 100000.0, "funding": 0.0001},
        {"tsUnix": base + 24 * 3600, "mark": 101000.0, "funding": 0.0001},   # +1%
    ]
    res = build_resume([mk_analyse(base, "funding", "NEUTRE"), mk_analyse(base, "fearGreed", "LONG")], hist_z2)
    check("zone morte exclue du score (scored=1 sur 2 analyses)",
          res["total_scored"] == 1 and res["total_hit"] == 1)

    # ─── ANTI-FUITE (31/08, GO Christophe) : NEUTRE avec signal = compté, alarme >60% ───
    # 3 analyses : 2 NEUTRE avec signal (funding 0.0005 parle) + 1 LONG → taux 66% > 60% → alerte
    hist_f = [
        {"tsUnix": base, "mark": 100000.0, "funding": 0.0005},
        {"tsUnix": base + 24 * 3600, "mark": 100000.0, "funding": 0.0005},   # plat
    ]
    res = build_resume([
        mk_analyse(base, "funding", "NEUTRE"),
        mk_analyse(base, "funding", "NEUTRE"),
        mk_analyse(base, "funding", "LONG"),
    ], hist_f)
    check("anti-fuite : 2/3 NEUTRE avec signal -> alerte True",
          res["evitement"]["alerte"] is True and res["evitement"]["neutre_signal"] == 2)
    # NEUTRE en zone morte ne compte PAS comme fuite
    res = build_resume([
        mk_analyse(base, "funding", "NEUTRE"),   # zone morte -> pas une fuite
        mk_analyse(base, "fearGreed", "LONG"),
        mk_analyse(base, "fearGreed", "LONG"),
    ], hist_z)
    check("anti-fuite : NEUTRE en zone morte ne compte pas (pas d'alarme)",
          res["evitement"]["alerte"] is False and res["evitement"]["neutre_signal"] == 0)

    # derniere = dernière analyse (bug v1 corrigé)
    an1 = mk_analyse(base, "funding", "LONG")
    an2 = mk_analyse(base, "fearGreed", "SHORT")
    res = build_resume([an1, an2], hist)
    check("derniere = DERNIÈRE analyse (fearGreed/SHORT)",
          res["derniere"] is not None and res["derniere"]["indice"] == "fearGreed"
          and res["derniere"]["avis"] == "SHORT")

    # Sans AVIS -> sans_verdict, pas noté
    an0 = mk_analyse(base, "funding", "LONG")
    an0["analyse"] = "pas d'avis ici"
    v = juger(an0, hist)
    check("analyse sans AVIS -> sans_verdict", v["statut"] == "sans_verdict")

    shutil.rmtree(tmp, ignore_errors=True)
    restore()
    print("=== %s (%d erreur%s) ===" % (
        "TOUS LES TESTS SONT VERTS" if errors == 0 else "ÉCHEC",
        errors, "s" if errors > 1 else ""))
    return 0 if errors == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
