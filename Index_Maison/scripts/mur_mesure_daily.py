#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""mur_mesure_daily.py — écrit thermo/mur_mesure.json (GO Christophe 02/11 §73 :
éliminer les fixes du Mur par conception).

Le Mur ne connaît AUCUN seuil en dur : seuil_jour = k × σ_20j (rendements
journaliers de l'equity rejouée), k lu dans disjoncteur_config.json (k_mur,
origine : grille sandbox 02/11 §72, re-lecture mensuelle au calendrier).

Preuve de vie par conception : le nourrisseur REFUSE de couper sur cache
stale (> 26 h) — et le rituel crie si ce fichier vieillit. Pas d'aveugle.
Lecture seule (journal + DIGEST), sortie thermo/. Exit 0 = écrit, 2 = échec.
"""
import json
import os
import statistics
import sys
from datetime import datetime, timezone

BASE = os.path.expanduser("~/ace777-test-day1")
sys.path.insert(0, os.path.join(BASE, "hulk-mexc", "scripts"))
from sandbox_degraissage import equity_snapshots  # noqa: E402

THERMO = os.path.join(BASE, "Index_Maison", "thermo")
OUT = os.path.join(THERMO, "mur_mesure.json")
CFG = os.path.join(BASE, "Index_Maison", "strategie", "disjoncteur_config.json")
FRAIS_MAX_H = 26.0


def main():
    try:
        cfg = json.load(open(CFG, encoding="utf-8"))
    except Exception:
        cfg = {}
    # R26 : AUCUN défaut silencieux — k sans origine = pas de mesure.
    # Config absente -> exit 2 -> pas de fichier -> SANS_MESURE en aval.
    if not cfg.get("k_mur") or not cfg.get("k_origine"):
        print("k_mur/k_origine absents de disjoncteur_config.json : REFUS (R26)")
        return 2
    k = float(cfg["k_mur"])
    try:
        eq = equity_snapshots()
    except Exception as e:
        print(f"impossible de rejouer l'equity : {e}")
        return 2
    if len(eq) < 30:
        print("pas assez de snapshots (< 30)")
        return 2
    # --- equity journalière (dernier snapshot du jour) -> σ_20j ---
    par_jour = {}
    for t, e in eq:
        par_jour[t.date().isoformat()] = (t, e)
    jours = sorted(par_jour)
    closes = [par_jour[j][1] for j in jours]
    rets = [(closes[i] - closes[i - 1]) / closes[i - 1]
            for i in range(1, len(closes)) if closes[i - 1] > 1e-9]
    if len(rets) < 20:
        print("pas assez de rendements journaliers (< 20)")
        return 2
    sigma = statistics.pstdev(rets[-20:])
    equity = closes[-1]
    # --- pires drawdowns intraday vs pivot 00:00 (ce que le nourrisseur voit) ---
    pivots, mins = {}, {}
    for t, e in eq:
        j = t.date().isoformat()
        if j not in pivots:
            pivots[j] = e
        mins[j] = min(mins.get(j, e), e)
    dd = {j: (mins[j] - pivots[j]) / pivots[j] if pivots[j] > 1e-9 else 0.0
          for j in pivots}
    dernieres = sorted(dd)[-20:]
    pire_dd_20j = min(dd[j] for j in dernieres)
    res = {"ts": datetime.now(timezone.utc).isoformat(timespec="seconds"),
           "equity": round(equity, 2),
           "sigma_20j_pct": round(sigma * 100, 4),
           "k": k,
           "k_origine": cfg.get("k_origine") or "grille sandbox 02/11 §72",
           "seuil_jour_pct": round(k * sigma * 100, 3),
           "seuil_jour_usd": round(k * sigma * equity, 2),
           "pire_dd_pivot_20j_pct": round(pire_dd_20j * 100, 3)}
    try:
        with open(OUT, "w", encoding="utf-8") as f:
            json.dump(res, f, ensure_ascii=False, indent=1)
    except Exception as e:
        print(f"écriture impossible : {e}")
        return 2
    print(f"[mur-mesure] equity={res['equity']}$ σ20j={res['sigma_20j_pct']}% "
          f"k={k} -> seuil={res['seuil_jour_pct']}% ({res['seuil_jour_usd']}$) "
          f"pireDD20j={res['pire_dd_pivot_20j_pct']}%")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
