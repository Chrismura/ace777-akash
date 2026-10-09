#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CHIFFRAGE DU GIVEBACK — FIXE (carnet) vs RELATIF À L'AMPLITUDE MESURÉE
=====================================================================
Demande Christophe (09/10/2026) : « attaque le 2e plus gros poste du Hulk-vs-HOLD (EDEL) et
explique pourquoi les sorties fixes coupent les gros gagnants. » Puis « go 1,2,3 » sur les
mesures proposées.

CE QUE CE SCRIPT MESURE (lecture seule, aucun ordre, aucune écriture moteur) :
  GO1 · Rejoue la lignée du seed EDEL (bougies 1 h MEXC en cache) sous deux familles de sortie :
        giveback FIXE (points) vs giveback RELATIF (k × amplitude médiane glissante). Dit ce
        que chacune capture vs tenir la souche, avec et sans ré-entrée.
  GO2 · Croise, sur tout l'univers : archétype/calibre de CARNET (trail_giveback_pct) ×
        amplitude de PRIX mesurée (amp7) × écart Hulk-vs-HOLD (mission.json). Teste l'hypothèse
        « une sortie calibrée sur le carnet, sur une paire violente en prix, coupe le gagnant ».

LIMITES DÉCLARÉES (R8) : EDEL = 1 paire, 1 épisode ; bougies 1 h (les mèches intra-heure sont
manquées) ; coût appliqué = spread du profil (53,9 bps/côté). Les valeurs ne sont pas des
prévisions — ce sont des rejouées sur le passé.

Sortie : Index_Maison/thermo/chiffrage_giveback.json (+ tableaux au terminal).
"""
from __future__ import annotations

import glob
import json
import os
import statistics as st
from datetime import datetime, timezone
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent.parent      # ace777-test-day1
HULK = RACINE / "hulk-mexc"
PROFILS = HULK / "strategie" / "universe_profils.json"
MISSION = RACINE / "Index_Maison" / "cockpit" / "mission.json"
OUT = RACINE / "Index_Maison" / "thermo" / "chiffrage_giveback.json"
COST = 0.00539            # spread_cout_bps du profil EDEL (53,9 bps) par transaction


def _freshest(pat: str):
    f = list(HULK.glob(pat))
    return max(f, key=lambda p: p.stat().st_mtime) if f else None


def _klines_1h(pair: str) -> list[dict]:
    """Bougies 1 h en cache `replay_cache/<PAIR>_1h_45j.json`. Aucune donnée moteur n'entre ici."""
    p = HULK / "runs" / "replay_cache" / f"{pair}_1h_45j.json"
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else []


# ── GO1 — sortie fixe vs relative sur la lignée du seed ──────────────────────────────────────
def rejouer_giveback(d: list[dict], entry: float, mise: float = 10.0) -> dict:
    """Rejoue UNE souche sous plusieurs règles de sortie. gb=None & k=None → aucune sortie (hold)."""
    qty0 = mise / entry

    def sim(gb=None, k=None, reentry=True):
        cash = 0.0
        pos = qty0
        ent = entry
        armed = False
        peak = 0.0
        trades = 0
        for i, b in enumerate(d):
            o, h, c = b["o"], b["h"], b["c"]
            if pos > 0:
                peak = max(peak, h)
                gain = (c / ent - 1) * 100.0
                peakp = (peak / ent - 1) * 100.0
                thr = gb if gb is not None else k * _amp(d, i)
                if armed and gain <= peakp - thr:
                    cash += pos * c * (1 - COST)
                    pos = 0
                    trades += 1
                    continue
                if gain >= 10.0:
                    armed = True
            if pos == 0 and reentry:
                pos = cash * (1 - COST) / o
                cash = 0.0
                ent = o
                armed = False
                peak = o
        return round(cash + pos * d[-1]["c"], 2), trades

    hold = round(qty0 * d[-1]["c"], 2)
    fixe = {g: sim(gb=g) for g in (4, 8, 12, 16, 20, 30)}
    relatif = {k: sim(k=k) for k in (1, 2, 3, 4, 6)}
    return {"hold": hold, "fixe": fixe, "relatif": relatif,
            "trainee_sans_reentree": {g: sim(gb=g, reentry=False) for g in (4, 12, 30, 60)}}


def _amp(d, i, win=48):
    w = [(b["h"] - b["l"]) / b["o"] * 100.0 for b in d[max(0, i - win): i + 1]]
    return st.median(w)


def _sim_trailing(d: list[dict], entry: float, gb: float, mise: float = 10.0) -> float:
    """UNE position tenue puis RE-ENTRÉE, sortie trailing giveback `gb` (points), armée à +10 %."""
    pos = mise / entry
    cash = 0.0
    ent = entry
    armed = False
    peak = 0.0
    for b in d:
        o, h, c = b["o"], b["h"], b["c"]
        if pos > 0:
            peak = max(peak, h)
            if armed and (c / ent - 1) * 100.0 <= (peak / ent - 1) * 100.0 - gb:
                cash += pos * c * (1 - COST)
                pos = 0
                continue
            if (c / ent - 1) * 100.0 >= 10.0:
                armed = True
        if pos == 0:
            pos = cash * (1 - COST) / o
            cash = 0.0
            ent = o
            armed = False
            peak = o
    return round(cash + pos * d[-1]["c"], 2)


def rejouer_toutes(profils: dict, mission: dict, scores: dict) -> list[dict]:
    """GO1bis : giveback FIXE (carnet) vs RELATIF (max(gb, 0,5 × amp7)) sur TOUTES les paires
    ayant des klines en cache et un prix de seed. Une seule position (avec ré-entrée), coût
    spread du profil. Rend, par paire, hold / fixed / relatif."""
    seed = {p["pair"]: p["seedPx"] for p in (mission.get("hulk", {}).get("portfolio") or [])
            if p.get("seedPx")}
    out = []
    for pair, v in profils.items():
        if not isinstance(v, dict) or "calib" not in v or pair not in seed:
            continue
        d = _klines_1h(pair)
        if not d:
            continue
        sc = scores.get(pair) or {}
        try:
            a7 = float(sc.get("amp7_pct") or sc.get("move24_pct"))
        except Exception:
            continue
        gb = float(v["calib"].get("trail_giveback_pct") or 0)
        ent = seed[pair]
        gb_rel = max(gb, 0.5 * a7)
        out.append({"pair": pair, "amp7": round(a7, 1), "gb_carnet": gb,
                    "gb_relatif": round(gb_rel, 2), "hold": round(10.0 / ent * d[-1]["c"], 2),
                    "fixed": _sim_trailing(d, ent, gb), "relatif": _sim_trailing(d, ent, gb_rel)})
    for r in out:
        r["delta"] = round(r["relatif"] - r["fixed"], 2)
    return out


# ── GO2 — carnet (calibre) × prix (amplitude) × écart ────────────────────────────────────────
def croiser(profils: dict, mission: dict, scores: dict) -> list[dict]:
    hv = {p["pair"]: p for p in (mission.get("hulk", {}).get("hulkVsHold", {}) or {}).get("pairs", [])}
    out = []
    for pair, v in profils.items():
        if not isinstance(v, dict) or "calib" not in v:
            continue
        h = hv.get(pair)
        if not h or h.get("ecart") is None:
            continue
        sc = scores.get(pair) or {}
        amp = sc.get("amp7_pct") or sc.get("move24_pct")
        try:
            amp = float(amp)
        except Exception:
            continue
        gb = v["calib"].get("trail_giveback_pct")
        if not gb:
            continue
        gb = float(gb)
        out.append({"pair": pair, "archetype": v.get("archetype"), "spread_bps": v.get("spread_bps_med"),
                    "gb_carnet": gb, "amp7": round(amp, 1), "ratio": round(amp / gb, 1),
                    "ecart": h["ecart"], "hold": h.get("hold"),
                    "gb_propose_f05": round(max(gb, 0.5 * amp), 1)})
    return sorted(out, key=lambda r: r["ecart"])


def _correlation(xs, ys):
    n = len(xs)
    if n < 3:
        return None
    mx, my = sum(xs) / n, sum(ys) / n
    cov = sum((a - mx) * (b - my) for a, b in zip(xs, ys))
    sx = sum((a - mx) ** 2 for a in xs) ** 0.5
    sy = sum((b - my) ** 2 for b in ys) ** 0.5
    return round(cov / (sx * sy), 2) if sx and sy else None


def main() -> int:
    profils = json.loads(PROFILS.read_text(encoding="utf-8"))
    stt = _freshest("runs/PAPER_V1_*_state.json")
    scores = (json.loads(stt.read_text(encoding="utf-8")).get("scores") or {}) if stt else {}
    mission = json.loads(MISSION.read_text(encoding="utf-8"))

    # GO1
    d = _klines_1h("EDELUSDT")
    rng = [(b["h"] - b["l"]) / b["o"] * 100.0 for b in d]
    go1 = {"fenetre": [datetime.fromtimestamp(d[0]["t"] / 1000, tz=timezone.utc).strftime("%Y-%m-%d"),
                       datetime.fromtimestamp(d[-1]["t"] / 1000, tz=timezone.utc).strftime("%Y-%m-%d")],
           "n_bougies": len(d), "amp_horaire_med_pct": round(st.median(rng), 2),
           "amp_horaire_p90_pct": round(sorted(rng)[int(0.9 * len(rng))], 2)}
    go1.update(rejouer_giveback(d, entry=0.00874))
    print("## GO1 — EDEL, lignée du seed (entry 0,00874)")
    print(f"  HOLD souche = {go1['hold']} $ · amplitude horaire méd {go1['amp_horaire_med_pct']}% / p90 {go1['amp_horaire_p90_pct']}%")
    print("  giveback FIXE (avec ré-entrée) :", {g: v[0] for g, v in go1["fixe"].items()})
    print("  giveback RELATIF k×amp (48 h) :", {k: v[0] for k, v in go1["relatif"].items()})
    print("  sans ré-entrée (1 sortie)      :", {g: v[0] for g, v in go1["trainee_sans_reentree"].items()})

    # GO2
    rows = croiser(profils, mission, scores)
    xs = [r["ratio"] for r in rows]
    ys = [r["ecart"] for r in rows]
    lo = [r["ecart"] for r in rows if r["ratio"] <= 4]
    hi = [r["ecart"] for r in rows if r["ratio"] > 4]
    go2 = {"n_paires": len(rows), "corr_ratio_ecart": _correlation(xs, ys),
           "moy_ecart_ratio_le4": round(st.mean(lo), 2) if lo else None,
           "moy_ecart_ratio_gt4": round(st.mean(hi), 2) if hi else None,
           "paires": rows}
    print("\n## GO2 — carnet × amplitude × écart (n=%d)" % len(rows))
    for r in rows:
        print(f"  {r['pair']:12} {str(r['archetype'])[:18]:18} gb={r['gb_carnet']:>4} amp7={r['amp7']:>5}% "
              f"ratio x{r['ratio']:>4}  ecart {r['ecart']:>+7.2f}$")
    print(f"  corrélation (ratio amp/gb) vs écart = {go2['corr_ratio_ecart']}")
    print(f"  écart moyen : ratio≤4 {go2['moy_ecart_ratio_le4']}$ (n={len(lo)}) · ratio>4 {go2['moy_ecart_ratio_gt4']}$ (n={len(hi)})")

    # GO1bis — toutes les paires
    rows_all = rejouer_toutes(profils, mission, scores)
    tot = {"hold": round(sum(r["hold"] for r in rows_all), 2),
           "fixed": round(sum(r["fixed"] for r in rows_all), 2),
           "relatif": round(sum(r["relatif"] for r in rows_all), 2)}
    go1b = {"n_paires": len(rows_all), "totaux": tot,
            "delta_relatif_vs_fixe": round(tot["relatif"] - tot["fixed"], 2), "paires": rows_all}
    print(f"\n## GO1bis — giveback sur toutes les paires (n={len(rows_all)})")
    for r in sorted(rows_all, key=lambda r: r["delta"]):
        print(f"  {r['pair']:12} amp7={r['amp7']:>5} gb {r['gb_carnet']:>5}→{r['gb_relatif']:>5}  "
              f"hold {r['hold']:>6.2f} fixed {r['fixed']:>6.2f} rel {r['relatif']:>6.2f}  Δ {r['delta']:>+5.2f}")
    print(f"  TOTAUX : hold {tot['hold']} · fixed {tot['fixed']} · relatif {tot['relatif']} "
          f"→ Δ relatif vs fixe {go1b['delta_relatif_vs_fixe']:+}")

    # GO3 : proposition
    go3 = {"regle": "gb = max(gb_carnet, 0.5 × amp7)", "n_changees": sum(1 for r in rows if r["gb_propose_f05"] - r["gb_carnet"] > 0.05),
           "n_total": len(rows)}
    print(f"\n## GO3 — proposition : giveback = max(gb_carnet, 0,5 × amp7) → {go3['n_changees']}/{go3['n_total']} paires élargies")

    j = {"ts": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), "source": "klines 1h cache + mission.json + state",
         "go1_edel": go1, "go1b_toutes": go1b, "go2_croisement": go2, "go3_proposition": go3}
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(j, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\n(état écrit : {OUT})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
