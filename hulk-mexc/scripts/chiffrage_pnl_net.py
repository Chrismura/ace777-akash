#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
chiffrage_pnl_net.py — GO 2 : le PnL NET, à côté du brut (23/09/2026)
=====================================================================

POURQUOI CE FICHIER
-------------------
L'audit MEXC × HULK a établi que le journal inscrit un PnL **BRUT** :
`pnl = (price − entry) × sell_qty` — **ni frais, ni spread**. Sur les 100 séquences
vérifiables : **39,70 $ brut → 36,19 $ net estimé**, soit **−8,8 %**. La famille a été
unanime : « cesser de piloter avec un chiffre brut faux de 8,8 % ».

CE QUE CE SCRIPT FAIT — ET NE FAIT PAS
--------------------------------------
  FAIT : il recalcule, **par paire et au total**, le brut, les coûts ESTIMÉS (frais déclarés
  2 × 5 bps + spread) et le net ; il dit **quelle part du journal porte un spread MESURÉ**
  (colonnes ajoutées le 23/09) et quelle part retombe sur le profil (repli) ; il publie
  `Index_Maison/thermo/pnl_net.json` pour le cockpit.
  NE FAIT PAS : il **ne touche pas** au `pnl_total` du moteur. Le disjoncteur, les seuils et
  les décisions reposent sur le brut tel quel — changer ça déplacerait des garde-fous, ce qui
  exige un GO explicite. Ici on **rend visible**, on ne recalibre pas.

HONNÊTETÉ DES CHIFFRES : frais = 5 bps/côté **déclarés par le code**, jamais mesurés sur un
exchange réel (mode paper). Spread : MESURÉ quand la colonne existe, sinon profil (marqué).
"""

from __future__ import annotations

import csv
import json
import statistics as stats
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

RACINE = Path(__file__).resolve().parents[1]          # hulk-mexc/
RUNS = RACINE / "runs"
PROFILS = RACINE / "strategie" / "universe_profils.json"
ETAT_COCKPIT = Path(__file__).resolve().parents[2] / "Index_Maison" / "thermo" / "pnl_net.json"
FEE_BPS_COTE = 5.0          # DÉCLARÉ par le code (ESTIMÉ) — pas mesuré
TAG = datetime.now(timezone.utc).strftime("%Y%m%d")
SORTIE_JSON = RUNS / f"PNL_NET_{TAG}.json"
SORTIE_TXT = RUNS / f"PNL_NET_{TAG}.txt"


def main() -> int:
    csv_path = max(RUNS.glob("PAPER_V1_*.csv"), key=lambda p: p.stat().st_mtime)
    prof = {}
    try:
        d = json.loads(PROFILS.read_text(encoding="utf-8"))
        prof = {k: v for k, v in d.items() if isinstance(v, dict) and "calib" in v}
    except Exception:
        pass

    brut = 0.0
    couts = 0.0
    par_paire: dict[str, dict] = defaultdict(lambda: {"n": 0, "brut": 0.0, "couts": 0.0,
                                                      "spread_mesure": 0, "spread_profil": 0,
                                                      "spread_absent": 0, "spreads": []})
    n_lignes = n_events = 0
    n_avec_colonnes = 0
    with open(csv_path, encoding="utf-8") as f:
        rd = csv.DictReader(f)
        champs = rd.fieldnames or []
        a_les_colonnes = "spread_bps" in champs
        for r in rd:
            n_lignes += 1
            if (r.get("ts_prix_utc") or "").strip():
                n_avec_colonnes += 1
            if r["event"] not in ("SELL", "SELL_PARTIAL", "BAG_SELL"):
                continue
            n_events += 1
            pnl = float(r.get("pnl_usdt") or 0.0)
            qte = float(r.get("qty") or 0.0)
            px = float(r.get("price") or 0.0)
            notional = qte * px
            sp = (r.get("spread_bps") or "").strip()
            src = (r.get("spread_source") or "").strip()
            d_p = par_paire[r["pair"]]
            if sp:
                try:
                    spread = float(sp)
                except ValueError:
                    spread = None
            else:
                spread = None
            if spread is None:
                # repli DÉCLARÉ : spread médian du profil (sinon RIZE-like 15 bps par défaut)
                spread = float((prof.get(r["pair"]) or {}).get("spread_bps_med") or 15.0)
                d_p["spread_profil"] += 1
            elif src == "asp":
                d_p["spread_mesure"] += 1
            else:
                d_p["spread_profil"] += 1
            d_p["spreads"].append(spread)
            cout = notional * (2 * FEE_BPS_COTE + spread) / 10000.0
            brut += pnl
            couts += cout
            d_p["n"] += 1
            d_p["brut"] += pnl
            d_p["couts"] += cout

    net = brut - couts
    print("=== PnL NET vs BRUT (GO 2) ===")
    print(f"journal : {csv_path.name} · {n_lignes} lignes · {n_events} ventes")
    print(f"colonnes de provenance présentes : {'oui' if a_les_colonnes else 'NON (ancien format)'} "
          f"· {n_avec_colonnes} lignes porteuses (`ts_prix_utc` non vide)")
    print()
    print(f"{'paire':<12}{'n ventes':>9}{'brut $':>10}{'coûts est. $':>14}{'net est. $':>12}"
          f"{'% brut':>8}{'spread méd bps':>16}{'mesuré/profil':>15}")
    for p in sorted(par_paire, key=lambda x: -par_paire[x]["brut"]):
        d_p = par_paire[p]
        pct = (d_p["couts"] / abs(d_p["brut"]) * 100) if d_p["brut"] else 0.0
        print(f"{p:<12}{d_p['n']:>9}{d_p['brut']:>10.2f}{d_p['couts']:>14.2f}"
              f"{d_p['brut'] - d_p['couts']:>12.2f}{pct:>8.1f}"
              f"{stats.median(d_p['spreads']):>16.2f}"
              f"{str(d_p['spread_mesure']) + '/' + str(d_p['spread_profil']):>15}")
    pct_tot = (couts / abs(brut) * 100) if brut else 0.0
    print()
    print(f"TOTAL : brut {brut:.2f} $ · coûts ESTIMÉS {couts:.2f} $ ({pct_tot:.1f} % du brut) "
          f"· NET {net:.2f} $")
    print(f"MOTEUR (son chiffre, inchangé, BRUT) : {json.loads(max(RUNS.glob('PAPER_V1_*_state.json'), key=lambda p: p.stat().st_mtime).read_text()).get('pnl_total')} $")

    rapport = {
        "instrument": "chiffrage_pnl_net.py",
        "ts_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "journal": csv_path.name, "n_lignes": n_lignes, "n_ventes": n_events,
        "colonnes_provenance_presentes": a_les_colonnes,
        "lignes_avec_provenance": n_avec_colonnes,
        "frais_bps_cote_ESTIME": FEE_BPS_COTE,
        "brut_usdt": round(brut, 2), "couts_estimes_usdt": round(couts, 2),
        "net_estime_usdt": round(net, 2), "couts_pct_du_brut": round(pct_tot, 1),
        "par_paire": {p: {"n": d_p["n"], "brut": round(d_p["brut"], 2),
                          "couts": round(d_p["couts"], 2),
                          "net": round(d_p["brut"] - d_p["couts"], 2),
                          "spread_med_bps": round(stats.median(d_p["spreads"]), 2),
                          "spread_mesure": d_p["spread_mesure"],
                          "spread_profil": d_p["spread_profil"]} for p, d_p in par_paire.items()},
        "limites": ["frais 5 bps/côté DÉCLARÉS (paper : rien n'est prélevé)",
                    "le pnl_total du moteur reste BRUT (aucun garde-fou déplacé)",
                    "spread de repli = médiane du profil quand la colonne est absente"],
        "lecture_seule": True, "ordres": 0,
    }
    SORTIE_JSON.write_text(json.dumps(rapport, ensure_ascii=False, indent=2), encoding="utf-8")
    SORTIE_TXT.write_text("\n".join([
        f"PnL NET vs BRUT — {rapport['ts_utc']} — {csv_path.name}",
        f"ventes {n_events} · brut {brut:.2f} $ · coûts estimés {couts:.2f} $ ({pct_tot:.1f} %) "
        f"· net {net:.2f} $",
        f"lignes avec provenance de prix : {n_avec_colonnes}/{n_lignes}",
    ] + [f"  {p}: net {d['net']:.2f} $ (spread méd {d['spread_med_bps']} bps)" for p, d in rapport["par_paire"].items()]),
        encoding="utf-8")
    ETAT_COCKPIT.parent.mkdir(parents=True, exist_ok=True)
    ETAT_COCKPIT.write_text(json.dumps({
        "ts": rapport["ts_utc"], "conforme": True,
        "brut": rapport["brut_usdt"], "couts": rapport["couts_estimes_usdt"],
        "net": rapport["net_estime_usdt"], "couts_pct_du_brut": rapport["couts_pct_du_brut"],
        "n_ventes": n_events, "frais_bps_cote_estime": FEE_BPS_COTE,
        "spread_mesure_ventes": sum(d["spread_mesure"] for d in rapport["par_paire"].values()),
        "spread_repli_ventes": sum(d["spread_profil"] for d in rapport["par_paire"].values()),
    }, ensure_ascii=False, indent=2), encoding="utf-8")
    print()
    print(f"écrit : {SORTIE_JSON.name} + {SORTIE_TXT.name} + thermo/pnl_net.json (cockpit)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
