#!/usr/bin/env python3
"""consolider_profils_corpus.py — FINITION QUOTIDIENNE profils (GO Christophe 18/10 « brancher tout »).

Boucle les mesures vers les profils : lit les CORPUS_ASP quotidiens du satellite
(runs/CORPUS_ASP_YYYYMMDD.csv — spread + murs par paire, ~5 000 mesures/jour/paire),
agrège médiane/sigma sur N jours, et écrit dans strategie/universe_profils.json :
  spread_bps_med / spread_bps_sigma / spread_cout_bps / mur_bid_med / mur_ask_med
  + filet_mesure.spread_tempete_bps (= med+σ de LA paire, 0 seuil fixe).

Règles :
- R17 : aucun seuil fixe — tout est lu du mesuré. Seuil d'échantillon minimal
  (N_MIN=500) : en dessous, on NE TOUCHE PAS (pas d'invention, le provisoire reste
  marqué A_CONSOLIDER).
- reentry_dd (dip paire) et souche_crash (max drop_alerte/trail_arm) viennent du
  calibre — inchangés ici. Sans drop_alerte : repli global moteur, marqué.
- SQLite ? Non : même schéma CSV que les ASPIRATION_CALIB → pipeline compatible.
- Sec par défaut : DRY-RUN (affiche). --appliquer écrit (backup .bak-consolidation-DATE).

Usage :
  python3 consolider_profils_corpus.py              # dry-run, 7 jours
  python3 consolider_profils_corpus.py --jours 3     # dry-run, 3 jours
  python3 consolider_profils_corpus.py --appliquer   # écrit + backup
Branchement : plist quotidienne 04:10 (avant carte-paires 04:20).
IA=Buffy (Muse Spark 1.3, Freebuff).
"""
from __future__ import annotations

import argparse
import csv
import glob
import json
import statistics
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RUNS = ROOT / "runs"
PROFILS = ROOT / "strategie" / "universe_profils.json"
N_MIN = 500  # échantillon minimal pour consolider (sinon on ne touche pas)


def charger_corpus(jours: int) -> dict[str, dict[str, list[float]]]:
    files = sorted(glob.glob(str(RUNS / "CORPUS_ASP_*.csv")))[-jours:]
    agg: dict[str, dict[str, list[float]]] = defaultdict(lambda: defaultdict(list))
    for f in files:
        try:
            rdr = csv.DictReader(open(f, newline=""))
        except Exception as e:
            print(f"[consolidation] SKIP {Path(f).name} ({e})")
            continue
        if "spread_bps" not in (rdr.fieldnames or []):
            continue
        for r in rdr:
            p = r.get("pair")
            if not p:
                continue
            for col in ("spread_bps", "wall_bid_usdt", "wall_ask_usdt"):
                v = (r.get(col) or "").strip()
                if v and v != "None":
                    try:
                        agg[p][col].append(float(v))
                    except ValueError:
                        pass
    return agg, [Path(f).name for f in files]


def med_sig(vals: list[float]) -> tuple[float, float]:
    m = round(statistics.median(vals), 2)
    s = round(statistics.pstdev(vals), 2) if len(vals) > 1 else 0.0
    return m, s


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--jours", type=int, default=7)
    ap.add_argument("--appliquer", action="store_true")
    args = ap.parse_args()

    agg, files = charger_corpus(args.jours)
    print(f"[consolidation] {len(files)} fichiers : {files[0] if files else '?'} -> {files[-1] if files else '?'}")
    if not agg:
        print("[consolidation] RIEN à agréger — on ne touche à rien.")
        return 1

    profils = json.loads(PROFILS.read_text(encoding="utf-8"))
    cles = [k for k in profils if isinstance(profils[k], dict) and "calib" in profils[k]]
    jour = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    changes = 0
    for sym in sorted(cles):
        pr = profils[sym]
        c = pr["calib"]
        fm = pr.get("filet_mesure") or {}
        prov = fm.get("provenance", {})
        sp = agg.get(sym, {}).get("spread_bps", [])
        if len(sp) >= N_MIN:
            med, sig = med_sig(sp)
            avant = pr.get("spread_bps_med")
            pr["spread_bps_med"] = med
            pr["spread_bps_sigma"] = sig
            c["spread_cout_bps"] = med
            fm["spread_tempete_bps"] = round(med + sig, 2)
            prov["spread"] = f"corpus_{args.jours}j_n{len(sp)}_{jour}"
            wb = agg.get(sym, {}).get("wall_bid_usdt", [])
            wa = agg.get(sym, {}).get("wall_ask_usdt", [])
            if len(wb) >= N_MIN:
                pr["mur_bid_med"] = round(statistics.median(wb), 1)
                prov["mur"] = f"corpus_{args.jours}j_n{len(wb)}_{jour}"
            if len(wa) >= N_MIN:
                pr["mur_ask_med"] = round(statistics.median(wa), 1)
            changes += 1
            print(f"  {sym} spread {avant} -> med={med} sig={sig} tempete={fm['spread_tempete_bps']} (n={len(sp)})")
        else:
            print(f"  {sym} SKIP (n={len(sp)} < {N_MIN}) — provisoire conservé, rien d'inventé")
        dip = c.get("dip_pct")
        drop_a = c.get("drop_alerte")
        arm = c.get("trail_arm_pct")
        fm["reentry_dd_pct"] = dip
        fm["souche_crash_pct"] = round(max(drop_a, arm), 2) if (drop_a is not None and arm is not None) else None
        if fm["souche_crash_pct"] is None:
            prov["crash"] = "repli_global_20_calib_sans_drop_alerte_A_MESURER"
        fm["provenance"] = prov
        pr["filet_mesure"] = fm

    if not args.appliquer:
        print(f"[consolidation] DRY-RUN : {changes}/{len(cles)} paires consolidables — rien d'écrit (--appliquer pour écrire)")
        return 0
    bak = PROFILS.with_suffix(f".json.bak-consolidation-{jour}")
    bak.write_text(PROFILS.read_text(encoding="utf-8"), encoding="utf-8")
    PROFILS.write_text(json.dumps(profils, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"[consolidation] ÉCRIT {PROFILS.name} ({changes}/{len(cles)}), backup {bak.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
