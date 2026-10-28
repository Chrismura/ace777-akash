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

FIX §23 (28/10/2026, ORDRE Christophe — « fixe ces putains de tableaux ») :
le compteur ne filtrait que SELL/SELL_PARTIAL/BAG_SELL et ignorait BAG_CRASH
(EDEL 05/09 : −3,5578 $) → brut surestimé de +3,56 $. Désormais UN BOOKING =
toute ligne avec |pnl_usdt| > 0, par construction : le chiffrage ne peut plus
oublier une famille d'événements. La garde crie si journal ≠ moteur.

CE QUE CE SCRIPT FAIT — ET NE FAIT PAS
--------------------------------------
  FAIT : il recalcule, **par paire et au total**, le brut, les coûts ESTIMÉS (frais déclarés
  2 × 5 bps + spread) et le net ; il dit **quelle part du journal porte un spread MESURÉ**
  (colonnes ajoutées le 23/09) et quelle part retombe sur le profil (repli) ; il ajoute le
  LATENT (bags × prix live) et publie LE tableau portefeuille unique
  (`runs/PORTEFEUILLE_LATEST.md`) + `Index_Maison/thermo/pnl_net.json` pour le cockpit.
  NE FAIT PAS : il **ne touche pas** au `pnl_total` du moteur. Le disjoncteur, les seuils et
  les décisions reposent sur le brut tel quel — changer ça déplacerait des garde-fous, ce qui
  exige un GO explicite. Ici on **rend visible**, on ne recalibre pas.

HONNÊTETÉ DES CHIFFRES : frais = 5 bps/côté **déclarés par le code**, jamais mesurés sur un
exchange réel (mode paper). Spread : MESURÉ quand la colonne existe, sinon profil (marqué).
Latent : prix `aspiration_live.json` (public MEXC), horodaté — pas un prix d'exécution.
"""

from __future__ import annotations

import csv
import json
import statistics as stats
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
from couts_communs import couts_journal  # §24 : modèle de coûts UNIQUE (partagé cockpit)

RACINE = Path(__file__).resolve().parents[1]          # hulk-mexc/
RUNS = RACINE / "runs"
PROFILS = RACINE / "strategie" / "universe_profils.json"
ETAT_COCKPIT = Path(__file__).resolve().parents[2] / "Index_Maison" / "thermo" / "pnl_net.json"
FEE_BPS_COTE = 5.0          # DÉCLARÉ par le code (ESTIMÉ) — pas mesuré
SEUIL_BOOKING = 1e-9        # §23 : un booking = |pnl_usdt] > 0, TOUT événement confondu
TAG = datetime.now(timezone.utc).strftime("%Y%m%d")
SORTIE_JSON = RUNS / f"PNL_NET_{TAG}.json"
SORTIE_TXT = RUNS / f"PNL_NET_{TAG}.txt"
SORTIE_PORTEFEUILLE = RUNS / "PORTEFEUILLE_LATEST.md"


def dernier_state() -> dict:
    états = sorted(RUNS.glob("PAPER_V1_*_state.json"), key=lambda p: p.stat().st_mtime)
    if not états:
        return {}
    try:
        return json.loads(états[-1].read_text(encoding="utf-8"))
    except Exception:
        return {}


def prix_live() -> tuple[dict, str]:
    """Prix live publics + horodatage (pour le latent)."""
    f = RUNS / "aspiration_live.json"
    try:
        d = json.loads(f.read_text(encoding="utf-8"))
        px = {k: float(v.get("prix")) for k, v in (d.get("paires") or {}).items()
              if v.get("prix") is not None}
        return px, str(d.get("ts_utc", "?"))
    except Exception:
        return {}, "?"


def main() -> int:
    csv_path = max(RUNS.glob("PAPER_V1_*.csv"), key=lambda p: p.stat().st_mtime)
    prof = {}
    try:
        d = json.loads(PROFILS.read_text(encoding="utf-8"))
        prof = {k: v for k, v in d.items() if isinstance(v, dict) and "calib" in v}
    except Exception:
        pass

    brut = 0.0
    par_paire: dict[str, dict] = defaultdict(lambda: {"n": 0, "brut": 0.0,
                                                      "spread_mesure": 0, "spread_profil": 0,
                                                      "spread_absent": 0, "spreads": []})
    mix_events: Counter = Counter()
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
            try:
                pnl = float(r.get("pnl_usdt") or 0.0)
            except ValueError:
                continue
            if abs(pnl) <= SEUIL_BOOKING:
                continue  # §23 : pas de liste d'événements — tout booking compte
            n_events += 1
            mix_events[str(r.get("event") or "?")] += 1
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
            brut += pnl
            d_p["n"] += 1
            d_p["brut"] += pnl

    # §24 : les coûts viennent du modèle UNIQUE (même fonction que le cockpit).
    cc = couts_journal(csv_path, RACINE)
    frais = cc["frais"]
    spread_tot = cc["spread"]
    couts = cc["couts"]
    net = cc["net"]
    # Sécurité : le brut recompté par le modèle unique doit égaler notre somme.
    assert abs(cc["brut"] - round(brut, 2)) <= 0.015, "divergence brut modele unique"

    # --- MOTEUR (son chiffre, inchangé) + RÉCONCILIATION §23 ---
    st = dernier_state()
    moteur_total = float(st.get("pnl_total") or 0.0) if st else 0.0
    moteur_trades = int(st.get("trades") or 0) if st else 0
    ecart = brut - moteur_total
    reconcile_ok = abs(ecart) <= 0.01 and (not st or n_events == moteur_trades)

    # --- LATENT (bags × prix live) ---
    px_live, ts_px = prix_live()
    bags = (st.get("bags") or {}) if st else {}
    latent_total = 0.0
    latent_par_paire: dict[str, dict] = {}
    latent_sans_prix: list[str] = []
    for paire, b in bags.items():
        try:
            entry = float(b.get("entry") or 0.0)
            qty = float(b.get("qty") or 0.0)
        except (TypeError, ValueError):
            continue
        px = px_live.get(paire)
        if px is None or entry <= 0:
            latent_sans_prix.append(paire)
            continue
        unreal = (px - entry) * qty
        latent_total += unreal
        latent_par_paire[paire] = {"qty": qty, "entry": entry, "px": px, "unreal": unreal}

    portefeuille = net + latent_total

    print("=== PnL NET vs BRUT (GO 2 + FIX §23) ===")
    print(f"journal : {csv_path.name} · {n_lignes} lignes · {n_events} bookings "
          f"({', '.join(f'{k} {v}' for k, v in sorted(mix_events.items()))})")
    print(f"colonnes de provenance présentes : {'oui' if a_les_colonnes else 'NON (ancien format)'} "
          f"· {n_avec_colonnes} lignes porteuses (`ts_prix_utc` non vide)")
    print()
    print(f"{'paire':<12}{'n':>5}{'brut $':>10}{'coûts est. $':>14}{'net est. $':>12}"
          f"{'latent $':>11}{'total $':>10}")
    toutes = sorted(set(par_paire) | set(latent_par_paire),
                    key=lambda p: -((par_paire.get(p) or {}).get("brut", 0.0)
                                    - (par_paire.get(p) or {}).get("couts", 0.0)
                                    + (latent_par_paire.get(p) or {}).get("unreal", 0.0)))
    for p in toutes:
        d_p = par_paire.get(p) or {"n": 0, "brut": 0.0}
        lat = (latent_par_paire.get(p) or {}).get("unreal", 0.0)
        net_p = d_p["brut"] - cc["par_paire"].get(p, {}).get("couts", 0.0)
        print(f"{p:<12}{d_p['n']:>5}{d_p['brut']:>10.2f}{cc['par_paire'].get(p, {}).get('couts', 0.0):>14.2f}"
              f"{net_p:>12.2f}{lat:>11.2f}{net_p + lat:>10.2f}")
    pct_tot = (couts / abs(brut) * 100) if brut else 0.0
    print()
    print(f"RÉALISÉ : brut {brut:.2f} $ · frais {frais:.2f} $ + spread {spread_tot:.2f} $ "
          f"= coûts {couts:.2f} $ ({pct_tot:.1f} % du brut) · NET {net:.2f} $ (modèle unique §24)" )
    print(f"LATENT : {latent_total:+.2f} $ ({len(latent_par_paire)} bags pricés, "
          f"{len(latent_sans_prix)} sans prix live"
          + (f" : {','.join(latent_sans_prix)}" if latent_sans_prix else "") + f", px {ts_px})")
    print(f"PORTEFEUILLE (net + latent) : {portefeuille:+.2f} $")
    print(f"MOTEUR (son chiffre, inchangé) : {moteur_total:+.4f} $ / {moteur_trades} trades "
          f"→ ÉCART journal−moteur {ecart:+.4f} $ "
          f"({'OK' if reconcile_ok else 'KO — À AUDITER, voir §23'})")

    rapport = {
        "instrument": "chiffrage_pnl_net.py",
        "ts_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "journal": csv_path.name, "n_lignes": n_lignes, "n_ventes": n_events,
        "n_bookings": n_events, "mix_evenements": dict(sorted(mix_events.items())),
        "colonnes_provenance_presentes": a_les_colonnes,
        "lignes_avec_provenance": n_avec_colonnes,
        "frais_bps_cote_ESTIME": FEE_BPS_COTE,
        "brut_usdt": round(brut, 2), "frais_usdt": frais, "spread_usdt": spread_tot,
        "couts_estimes_usdt": couts,
        "net_estime_usdt": net, "couts_pct_du_brut": round(pct_tot, 1),
        "modele_couts": "unique §24 (couts_communs) : notional x (2x5bps + spread) par booking",
        "reconciliation": {"moteur_pnl_total": round(moteur_total, 4),
                           "moteur_trades": moteur_trades,
                           "ecart_journal_moins_moteur": round(ecart, 4),
                           "ok": bool(reconcile_ok)},
        "latent": {"ts_prix": ts_px, "total_usdt": round(latent_total, 2),
                   "sans_prix": latent_sans_prix,
                   "par_paire": {p: {k: (round(v, 4) if isinstance(v, float) else v)
                                     for k, v in d.items()}
                                 for p, d in latent_par_paire.items()}},
        "portefeuille_usdt": round(portefeuille, 2),
        "par_paire": {p: {"n": d_p["n"], "brut": round(d_p["brut"], 2),
                          "frais": cc["par_paire"].get(p, {}).get("frais", 0.0),
                          "spread": cc["par_paire"].get(p, {}).get("spread", 0.0),
                          "couts": cc["par_paire"].get(p, {}).get("couts", 0.0),
                          "net": round(d_p["brut"], 2) - cc["par_paire"].get(p, {}).get("couts", 0.0),
                          "spread_med_bps": round(stats.median(d_p["spreads"]), 2) if d_p.get("spreads") else None,
                          "spread_mesure": d_p["spread_mesure"],
                          "spread_profil": d_p["spread_profil"],
                          "latent": round((latent_par_paire.get(p) or {}).get("unreal", 0.0), 2),
                          } for p, d_p in par_paire.items()},
        "limites": ["frais 5 bps/côté DÉCLARÉS (paper : rien n'est prélevé)",
                    "le pnl_total du moteur reste BRUT (aucun garde-fou déplacé)",
                    "spread de repli = médiane du profil quand la colonne est absente",
                    "latent = prix publics live, pas prix d'exécution ; hors frais de sortie"],
        "lecture_seule": True, "ordres": 0,
    }
    SORTIE_JSON.write_text(json.dumps(rapport, ensure_ascii=False, indent=2), encoding="utf-8")
    SORTIE_TXT.write_text("\n".join([
        f"PnL NET vs BRUT — {rapport['ts_utc']} — {csv_path.name}",
        f"bookings {n_events} ({', '.join(f'{k} {v}' for k, v in sorted(mix_events.items()))}) "
        f"· brut {brut:.2f} $ · coûts estimés {couts:.2f} $ ({pct_tot:.1f} %) · net {net:.2f} $",
        f"latent {latent_total:+.2f} $ (px {ts_px}) · PORTEFEUILLE {portefeuille:+.2f} $",
        f"moteur {moteur_total:+.4f} $ · écart {ecart:+.4f} $ ({'OK' if reconcile_ok else 'KO'})",
        f"lignes avec provenance de prix : {n_avec_colonnes}/{n_lignes}",
    ] + [f"  {p}: net {d['net']:+.2f} $ + latent {d['latent']:+.2f} $ = {d['net'] + d['latent']:+.2f} $"
         for p, d in sorted(rapport["par_paire"].items(),
                            key=lambda kv: -(kv[1]["net"] + kv[1]["latent"]))]),
        encoding="utf-8")

    # --- LE tableau unique : le coup d'œil portefeuille ---
    lignes = [
        f"# Portefeuille Hulk — {rapport['ts_utc']}",
        "",
        f"Journal : `{csv_path.name}` · prix latent : `{ts_px}` (publics, pas d'exécution).",
        "",
        f"**RÉALISÉ : brut {brut:+.2f} $ · coûts est. {couts:.2f} $ · NET {net:+.2f} $** "
        f"({n_events} bookings : {', '.join(f'{k} {v}' for k, v in sorted(mix_events.items()))}).",
        f"**LATENT : {latent_total:+.2f} $** ({len(latent_par_paire)} bags pricés"
        + (f", sans prix : {', '.join(latent_sans_prix)}" if latent_sans_prix else "") + ").",
        f"**PORTEFEUILLE (net + latent) : {portefeuille:+.2f} $**.",
        f"Réconciliation : journal − moteur = {ecart:+.4f} $ ({'OK' if reconcile_ok else 'KO — voir §23'}) "
        f"· bookings {n_events} vs trades moteur {moteur_trades}.",
        "",
        "| paire | réalisé net $ | latent $ | total $ |",
        "|---|---|---|---|",
    ]
    for p in toutes:
        d_p = par_paire.get(p) or {"n": 0, "brut": 0.0}
        net_p = d_p["brut"] - cc["par_paire"].get(p, {}).get("couts", 0.0)
        lat = (latent_par_paire.get(p) or {}).get("unreal", 0.0)
        lignes.append(f"| {p} | {net_p:+.2f} | {lat:+.2f} | {net_p + lat:+.2f} |")
    lignes += ["",
               "_Frais 5 bps/côté déclarés (paper). Spread mesuré ou profil. "
               "Latent hors frais de sortie. Lecture seule, 0 ordre._"]
    SORTIE_PORTEFEUILLE.write_text("\n".join(lignes) + "\n", encoding="utf-8")

    ETAT_COCKPIT.parent.mkdir(parents=True, exist_ok=True)
    ETAT_COCKPIT.write_text(json.dumps({
        "ts": rapport["ts_utc"], "conforme": True,
        "brut": rapport["brut_usdt"], "frais": frais, "spread": spread_tot,
        "couts": rapport["couts_estimes_usdt"],
        "net": rapport["net_estime_usdt"], "couts_pct_du_brut": rapport["couts_pct_du_brut"],
        "n_ventes": n_events, "n_bookings": n_events,
        "frais_bps_cote_estime": FEE_BPS_COTE,
        "latent": rapport["latent"]["total_usdt"],
        "portefeuille": rapport["portefeuille_usdt"],
        "reconciliation_ok": bool(reconcile_ok),
        "ecart_journal_moteur": round(ecart, 4),
        "spread_mesure_ventes": sum(d["spread_mesure"] for d in rapport["par_paire"].values()),
        "spread_repli_ventes": sum(d["spread_profil"] for d in rapport["par_paire"].values()),
    }, ensure_ascii=False, indent=2), encoding="utf-8")
    print()
    print(f"écrit : {SORTIE_JSON.name} + {SORTIE_TXT.name} + PORTEFEUILLE_LATEST.md + thermo/pnl_net.json (cockpit)")
    return 0 if reconcile_ok else 2


if __name__ == "__main__":
    raise SystemExit(main())
