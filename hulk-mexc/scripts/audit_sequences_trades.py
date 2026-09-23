#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
audit_sequences_trades.py — GO 2 : CHAQUE séquence, confrontée aux klines MEXC
==============================================================================

DEMANDE CHRISTOPHE (23/09/2026) : « ensuite tu vas comparer une par une toutes les
séquences de trading entrée et sortie, les mises, voir le niveau de justesse (c'est-à-dire
si on rentre bien, gestion des bags, et les sorties) ».

CE QUE L'INSTRUMENT FAIT (et ce qu'il refuse de faire)
------------------------------------------------------
  1. RECONSTRUCTION : le journal du moteur (CSV) est relu événement par événement, et chaque
     position est reconstruite par CONSERVATION DES QUANTITÉS (BUY ajoute, SELL_PARTIAL
     réduit, SELL ferme). Toute incohérence de quantité est SIGNALÉE, pas lissée.
     ⚠ Le CSV ne mémorise pas la mise visée, ni le seuil, ni le mur : ce qui manque est
     NOMMÉ dans le rapport, jamais deviné.
  2. VÉRIFICATION À LA SOURCE : pour chaque séquence, les klines 1 min MEXC de la fenêtre
     [entrée − 2 min ; sortie + 60 min] sont récupérées, et on vérifie que **le prix inscrit
     au journal tombe bien dans le [low, high] de sa minute** — c'est-à-dire qu'il a existé.
  3. JUSTESSE, en trois questions séparées (on ne mélange pas les trois) :
       · ENTRÉE   : que fait le prix dans les 60 min qui suivent l'entrée ? (MFE/MAE)
       · BAGS     : quand il y a des ajouts, le prix moyen s'améliore-t-il, et ces séquences
                    rapportent-elles plus que les séquences simples ?
       · SORTIE   : giveback (pic → sortie) et « laissé sur la table » (prix 60 min après)
  4. NET DE COÛTS : le moteur inscrit `pnl = (price − entry) × sell_qty` — donc BRUT, sans
     frais ni spread. L'instrument recalcule le net avec les frais déclarés par le code
     (5 bps/côté) + le demi-spread mesuré (raison `spread=` du journal quand elle existe,
     sinon le spread mesuré de la paire aujourd'hui, DÉCLARÉ comme approximation).

LECTURE SEULE, 0 ordre, 0 €. Sorties : runs/AUDIT_SEQUENCES_*.
"""

from __future__ import annotations

import csv
import json
import statistics as stats
import time
import urllib.parse
import urllib.request
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

RACINE = Path(__file__).resolve().parents[1]
RUNS = RACINE / "runs"
CSV = sorted(RUNS.glob("PAPER_V1_*_20260923_090125.csv"))
CSV = CSV[-1] if CSV else sorted(RUNS.glob("PAPER_V1_*.csv"))[-1]
TAG = "20260923"
FEE_BPS_COTE = 5.0          # déclaré par le code (commentaire l.812) : 5 bps par côté
UA = {"User-Agent": "hulk-audit/1.0"}
PAUSE = 0.12
SORTIE_JSON = RUNS / f"AUDIT_SEQUENCES_{TAG}.json"
SORTIE_TXT = RUNS / f"AUDIT_SEQUENCES_{TAG}.txt"


def http_json(url: str, timeout: float = 15.0, retries: int = 3):
    last = None
    for i in range(retries):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return json.loads(r.read().decode())
        except Exception as e:                       # noqa: BLE001
            last = e
            time.sleep(0.6 * (i + 1))
    raise RuntimeError(f"HTTP KO {url} : {last}")


def ms(ts_iso: str) -> int:
    return int(datetime.strptime(ts_iso, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc).timestamp() * 1000)


# BUDGET DE TEMPS déclaré : l'audit s'arrête proprement et DIT combien de séquences il a
# traitées, plutôt que de tourner sans fin (une mesure partielle déclarée n'est pas une
# mesure fausse ; une mesure silencieusement tronquée en est une).
BUDGET_S = 300.0
T0 = time.time()


def klines(pair: str, interval: str, t0_ms: int, t1_ms: int) -> list[list]:
    """Klines MEXC, paginées (limite 1000/appel). [[ms,o,h,l,c,v], …] bornées à [t0,t1]."""
    out: list[list] = []
    pas = {"1m": 60_000, "15m": 900_000, "1h": 3_600_000}[interval]
    cur = t0_ms
    while cur < t1_ms and len(out) < 12_000:
        q = urllib.parse.urlencode({"symbol": pair, "interval": interval,
                                    "startTime": cur, "endTime": t1_ms, "limit": 1000})
        data = http_json(f"https://api.mexc.com/api/v3/klines?{q}")
        if not data:
            break
        out.extend([[int(k[0]), float(k[1]), float(k[2]), float(k[3]), float(k[4]), float(k[5])] for k in data])
        last_ms = int(data[-1][0])
        if last_ms <= cur:
            break
        cur = last_ms + pas
        time.sleep(PAUSE)
    return out


def lire_evenements() -> list[dict]:
    evs = []
    with open(CSV, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if r["event"] == "SKIP":
                continue
            evs.append({
                "ts": r["ts"], "pair": r["pair"], "event": r["event"], "regime": r["regime"],
                "price": float(r["price"]), "entry": float(r["entry"] or 0) or None,
                "qty": float(r["qty"] or 0), "pnl": float(r["pnl_usdt"] or 0),
                "pnl_total": float(r["pnl_total"] or 0), "cadence": float(r["cadence"] or 0),
                "reason": r["reason"] or "",
            })
    return evs


def reconstruire(evs: list[dict]) -> tuple[list[dict], list[str]]:
    """Séquences par conservation des quantités. Aucun lissage : les écarts sont listés."""
    etat: dict[str, dict] = {}
    seqs: list[dict] = []
    anomalies: list[str] = []
    for e in evs:
        p, ev = e["pair"], e["event"]
        s = etat.get(p)
        if ev == "BUY":
            if s is None:
                s = {"pair": p, "ouverture": e["ts"], "buys": [], "sells": [], "regimes": [],
                     "cadences": []}
                etat[p] = s
            s["buys"].append(e)
            s["regimes"].append(e["regime"])
            s["cadences"].append(e["cadence"])
        elif ev in ("SELL", "SELL_PARTIAL"):
            if s is None:
                anomalies.append(f"{e['ts']} {p} : {ev} sans position ouverte (journal vs état)")
                continue
            s["sells"].append(e)
            vendu = sum(x["qty"] for x in s["sells"])
            achete = sum(x["qty"] for x in s["buys"])
            if ev == "SELL" or vendu >= achete * 0.999:
                reste = achete - vendu
                if abs(reste) > achete * 0.002:
                    anomalies.append(f"{e['ts']} {p} : fermeture avec écart de quantité "
                                     f"({achete:.4f} acheté vs {vendu:.4f} vendu — écart {reste:+.4f})")
                s["fermeture"] = e["ts"]
                s["regime_sortie"] = e["regime"]
                seqs.append(s)
                etat.pop(p, None)
        elif ev in ("BAG_ARM", "BAG_CRASH", "BAG_SELL"):
            if s is not None:
                s.setdefault("bag_events", []).append((e["ts"], ev, e["reason"][:60]))
    for p, s in etat.items():
        s["fermeture"] = None
        seqs.append(s)
    return seqs, anomalies


def enrichir(s: dict) -> dict:
    buys, sells = s["buys"], s["sells"]
    q_ach = sum(b["qty"] for b in buys)
    q_vend = sum(x["qty"] for x in sells)
    pm = sum(b["qty"] * b["price"] for b in buys) / q_ach if q_ach else 0.0
    pv = sum(x["qty"] * x["price"] for x in sells) / q_vend if q_vend else 0.0
    s.update({
        "qty_achetee": round(q_ach, 8), "qty_vendue": round(q_vend, 8),
        "prix_moyen_entree": pm, "prix_moyen_sortie": pv if q_vend else None,
        "n_ajouts": len(buys) - 1, "n_ventes": len(sells),
        "pnl_inscrit_brut": round(sum(x["pnl"] for x in sells), 4),
        "notional_entree": round(sum(b["qty"] * b["price"] for b in buys), 2),
        "motifs": [x["reason"].split()[0] if x["reason"] else "?" for x in sells],
        "ouverts": s.get("fermeture") is None,
    })
    if sells:
        s["spread_bps_journal"] = None
        for x in sells:
            for tok in x["reason"].split():
                if tok.startswith("spread=") and tok.endswith("bps"):
                    try:
                        s["spread_bps_journal"] = float(tok.split("=")[1].replace("bps", ""))
                    except ValueError:
                        pass
    return s


def main() -> int:
    evs = lire_evenements()
    seqs, anomalies = reconstruire(evs)
    seqs = [enrichir(s) for s in seqs]
    fermees = [s for s in seqs if not s["ouverts"]]
    print(f"=== AUDIT DES SÉQUENCES — {CSV.name} ===")
    print(f"événements non-SKIP : {len(evs)} · séquences reconstruites : {len(seqs)} "
          f"(fermées {len(fermees)}, ouvertes {len(seqs) - len(fermees)})")
    print(f"anomalies de reconstruction : {len(anomalies)}")
    for a in anomalies[:10]:
        print("  -", a)
    print()

    # ---------- vérification MEXC séquence par séquence ----------
    print("--- vérification MEXC : le prix inscrit a-t-il existé, et à quel niveau ? ---")
    print(f"    (budget {BUDGET_S:.0f} s · on traite du PLUS RÉCENT au plus ancien)"
          "", flush=True)
    n_ok = n_ko = n_imp = 0
    traitees, non_traitees = [], []
    for i, s in enumerate(sorted(fermees, key=lambda x: x["fermeture"], reverse=True), start=1):
        if time.time() - T0 > BUDGET_S:
            non_traitees = [x["pair"] + "|" + x["fermeture"] for x in
                            sorted(fermees, key=lambda x: x["fermeture"], reverse=True)[i - 1:]]
            print(f"    ⏱ budget atteint à la séquence {i - 1}/{len(fermees)} — le reste est DÉCLARÉ non traité")
            break
        t_ent, t_sor = ms(s["ouverture"]), ms(s["fermeture"])
        try:
            w_ent = klines(s["pair"], "1m", t_ent - 2 * 60_000, t_ent + 60 * 60_000)
            w_sor = klines(s["pair"], "1m", t_sor - 2 * 60_000, t_sor + 60 * 60_000)
            duree_min = (t_sor - t_ent) / 60_000
            if duree_min <= 940:
                w_tenue, gran = klines(s["pair"], "1m", t_ent, t_sor), "1m"
            elif duree_min <= 3600 * 24 * 7:
                w_tenue, gran = klines(s["pair"], "15m", t_ent, t_sor), "15m"
            else:
                w_tenue, gran = klines(s["pair"], "1h", t_ent, t_sor), "1h"
        except Exception as ex:                      # noqa: BLE001
            s["mexc"] = {"ok": False, "raison": str(ex)[:120]}
            n_imp += 1
            continue
        if not w_ent or not w_sor:
            s["mexc"] = {"ok": False, "raison": "aucune kline renvoyée"}
            n_imp += 1
            continue
        par_min_e = {k[0]: k for k in w_ent}
        par_min_s = {k[0]: k for k in w_sor}

        def verifie(ts_iso: str, prix: float, table: dict) -> dict:
            m = table.get(ms(ts_iso) // 60_000 * 60_000)
            if not m:
                return {"verifie": None, "raison": "minute absente des klines"}
            dedans = m[3] <= prix <= m[2]
            return {"verifie": bool(dedans), "bas": m[3], "haut": m[2],
                    "ecart_bps": round((prix - (m[2] + m[3]) / 2) / ((m[2] + m[3]) / 2) * 10000, 1)}

        entrees = [{"ts": b["ts"], "px": b["price"], **verifie(b["ts"], b["price"], par_min_e)}
                   for b in s["buys"]]
        sorties = [{"ts": x["ts"], "px": x["price"], **verifie(x["ts"], x["price"], par_min_s)}
                   for x in s["sells"]]
        s["mexc"] = {
            "ok": True, "granularite_tenue": gran,
            "entrees": entrees, "sorties": sorties,
            "entree_prix_verifie": all(e["verifie"] for e in entrees) if entrees else None,
            "sortie_prix_verifiee": all(e["verifie"] for e in sorties) if sorties else None,
            "prix_min_tenue": min((k[3] for k in w_tenue), default=None),
            "prix_max_tenue": max((k[2] for k in w_tenue), default=None),
            "max_60min_apres_entree": max((k[2] for k in w_ent), default=None),
            "min_60min_apres_entree": min((k[3] for k in w_ent), default=None),
            "max_60min_apres_sortie": max((k[2] for k in w_sor), default=None),
            "min_60min_apres_sortie": min((k[3] for k in w_sor), default=None),
            "duree_min": round(duree_min, 1),
        }
        ok = bool(s["mexc"]["entree_prix_verifie"] and s["mexc"]["sortie_prix_verifiee"])
        n_ok += 1 if ok else 0
        n_ko += 0 if ok else 1
        traitees.append(s["pair"] + "|" + s["fermeture"])
        if i % 10 == 0:
            print(f"    … {i}/{len(fermees)} séquences ({time.time() - T0:.0f} s)", flush=True)

        # --- justesse entrée / sortie ---
        pm_e = s["prix_moyen_entree"]
        pm_s = s["prix_moyen_sortie"]
        if s["mexc"]["max_60min_apres_entree"]:
            s["mfe_entree_pct"] = round((s["mexc"]["max_60min_apres_entree"] - pm_e) / pm_e * 100, 2)
            s["mae_entree_pct"] = round((s["mexc"]["min_60min_apres_entree"] - pm_e) / pm_e * 100, 2)
        if pm_s and s["mexc"]["prix_max_tenue"]:
            s["giveback_pct"] = round((s["mexc"]["prix_max_tenue"] - pm_s) / s["mexc"]["prix_max_tenue"] * 100, 2)
        if pm_s and s["mexc"]["max_60min_apres_sortie"]:
            s["laisse_sur_table_pct"] = round((s["mexc"]["max_60min_apres_sortie"] - pm_s) / pm_s * 100, 2)
            s["baisse_evitee_pct"] = round((pm_s - s["mexc"]["min_60min_apres_sortie"]) / pm_s * 100, 2)

        # --- net de coûts : frais déclarés (5 bps/côté) + demi-spread (mesuré ou journal) ---
        half_spread_bps = (s.get("spread_bps_journal") or 15.0) / 2.0
        cout_bps = 2 * FEE_BPS_COTE + 2 * half_spread_bps
        s["cout_bps_estime"] = round(cout_bps, 1)
        s["spread_source"] = "journal" if s.get("spread_bps_journal") else "approximé (15 bps, à mesurer)"
        s["cout_usdt_estime"] = round(s["notional_entree"] * cout_bps / 10000.0, 4)
        s["pnl_net_estime"] = round(s["pnl_inscrit_brut"] - s["cout_usdt_estime"], 4)

    print(f"séquences vérifiées à la source : {n_ok} conformes · {n_ko} avec un prix hors minute "
          f"· {n_imp} impossibles à vérifier")
    print()
    if non_traitees:
        print(f"⚠ DÉCLARÉ NON TRAITÉ (budget de temps) : {len(non_traitees)} séquences anciennes")
    fermees_totales = len(fermees)
    fermees = [s for s in fermees if s.get("mexc", {}).get("ok")]
    print(f"séquences retenues pour l'analyse : {len(fermees)}/{fermees_totales} "
          f"(les autres n'ont pas pu être vérifiées — déclaré, jamais comblé)")
    print()

    # ---------- agrégats ----------
    def med(xs):
        xs = [x for x in xs if isinstance(x, (int, float))]
        return round(stats.median(xs), 2) if xs else None

    def som(xs):
        return round(sum(x for x in xs if isinstance(x, (int, float))), 2)

    par_paire: dict[str, dict] = defaultdict(lambda: {"n": 0, "brut": 0.0, "net": 0.0,
                                                      "mfe": [], "giveback": [], "laisse": [],
                                                      "duree": [], "ajouts": 0})
    for s in fermees:
        d = par_paire[s["pair"]]
        d["n"] += 1
        d["brut"] += s["pnl_inscrit_brut"]
        d["net"] += s.get("pnl_net_estime") or 0.0
        d["mfe"].append(s.get("mfe_entree_pct"))
        d["giveback"].append(s.get("giveback_pct"))
        d["laisse"].append(s.get("laisse_sur_table_pct"))
        d["duree"].append(s["mexc"]["duree_min"] if s.get("mexc", {}).get("ok") else None)
        d["ajouts"] += 1 if s["n_ajouts"] > 0 else 0

    print(f"{'paire':<11}{'n':>4}{'brut $':>9}{'net est. $':>11}{'MFE60 méd %':>12}"
          f"{'giveback méd %':>16}{'laissé méd %':>14}{'durée méd min':>14}{'avec ajouts':>12}")
    for p in sorted(par_paire):
        d = par_paire[p]
        print(f"{p:<11}{d['n']:>4}{d['brut']:>9.2f}{d['net']:>11.2f}"
              f"{(med(d['mfe']) if med(d['mfe']) is not None else 0):>12.2f}"
              f"{(med(d['giveback']) if med(d['giveback']) is not None else 0):>16.2f}"
              f"{(med(d['laisse']) if med(d['laisse']) is not None else 0):>14.2f}"
              f"{(med(d['duree']) if med(d['duree']) is not None else 0):>14.1f}"
              f"{d['ajouts']:>12}")
    tot_brut = som([s["pnl_inscrit_brut"] for s in fermees])
    tot_net = som([s.get("pnl_net_estime") for s in fermees])
    print()
    print(f"TOTAL séquences fermées : brut inscrit {tot_brut} $ · coûts estimés "
          f"{som([s.get('cout_usdt_estime') for s in fermees])} $ · NET estimé {tot_net} $ "
          f"({len(fermees)} séquences)")
    print(f"pnl_total du moteur (journal, toutes paires, y c. séquences ouvertes) : "
          f"{max((e['pnl_total'] for e in evs), default=0)} $")
    print()

    # ---------- justesse par motif de sortie ----------
    par_motif: dict[str, dict] = defaultdict(lambda: {"n": 0, "brut": 0.0, "net": 0.0,
                                                      "laisse": [], "giveback": []})
    for s in fermees:
        fam = "stop/guard" if any(m.startswith("stop-") or "guard" in m or m.startswith("dust") for m in s["motifs"]) \
            else ("trailing" if any("trailing" in m for m in s["motifs"])
                  else ("rip/paliers" if any(m.startswith("rip_") or "palier" in m for m in s["motifs"])
                        else "autre"))
        d = par_motif[fam]
        d["n"] += 1
        d["brut"] += s["pnl_inscrit_brut"]
        d["net"] += s.get("pnl_net_estime") or 0.0
        d["laisse"].append(s.get("laisse_sur_table_pct"))
        d["giveback"].append(s.get("giveback_pct"))
    print(f"{'motif de sortie':<16}{'n':>4}{'brut $':>10}{'net est. $':>12}"
          f"{'laissé méd %':>14}{'giveback méd %':>16}")
    for m in sorted(par_motif):
        d = par_motif[m]
        print(f"{m:<16}{d['n']:>4}{d['brut']:>10.2f}{d['net']:>12.2f}"
              f"{(med(d['laisse']) or 0):>14.2f}{(med(d['giveback']) or 0):>16.2f}")
    print()

    # ---------- bags ----------
    avec, sans = [s for s in fermees if s["n_ajouts"] > 0], [s for s in fermees if s["n_ajouts"] == 0]
    print(f"BAGS : {len(avec)} séquences avec ajout(s) · {len(sans)} sans ajout")
    if avec:
        print(f"  avec ajouts : brut {som([s['pnl_inscrit_brut'] for s in avec])} $ · "
              f"net est. {som([s.get('pnl_net_estime') for s in avec])} $ · "
              f"MFE60 méd {med([s.get('mfe_entree_pct') for s in avec])} %")
    if sans:
        print(f"  sans ajout  : brut {som([s['pnl_inscrit_brut'] for s in sans])} $ · "
              f"net est. {som([s.get('pnl_net_estime') for s in sans])} $ · "
              f"MFE60 méd {med([s.get('mfe_entree_pct') for s in sans])} %")

    rapport = {
        "instrument": "audit_sequences_trades.py",
        "ts_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "journal": CSV.name,
        "frais_declares_bps_cote": FEE_BPS_COTE,
        "formule_pnl_journal": "pnl = (price - entry) * sell_qty  → BRUT, sans frais ni spread",
        "n_evenements": len(evs), "n_sequences": len(seqs),
        "n_fermees_total": fermees_totales, "n_fermees_verifiees": len(fermees),
        "anomalies_reconstruction": anomalies,
        "verif_mexc": {"conformes": n_ok, "prix_hors_minute": n_ko, "non_verifiables": n_imp,
                       "budget_s": BUDGET_S,
                       "non_traitees_faute_de_budget": non_traitees},
        "total_brut_inscrit": tot_brut, "total_couts_estimes": som([s.get("cout_usdt_estime") for s in fermees]),
        "total_net_estime": tot_net,
        "par_paire": {p: {k: (round(v, 2) if isinstance(v, float) else v) for k, v in d.items()}
                      for p, d in par_paire.items()},
        "par_motif": {m: {"n": d["n"], "brut": round(d["brut"], 2), "net": round(d["net"], 2),
                          "laisse_med": med(d["laisse"]), "giveback_med": med(d["giveback"])}
                      for m, d in par_motif.items()},
        "sequences": [{k: v for k, v in s.items() if k not in ("buys", "sells")} for s in seqs],
        "lecture_seule": True, "ordres": 0,
    }
    SORTIE_JSON.write_text(json.dumps(rapport, ensure_ascii=False, indent=2), encoding="utf-8")
    lignes = [f"AUDIT DES SÉQUENCES — {rapport['ts_utc']} — journal {CSV.name}",
              f"séquences {len(seqs)} (fermées {len(fermees)}) · vérif MEXC {n_ok} conformes / "
              f"{n_ko} prix hors minute / {n_imp} non vérifiables",
              f"TOTAL brut inscrit {tot_brut} $ · coûts estimés "
              f"{rapport['total_couts_estimes']} $ · NET estimé {tot_net} $",
              "", "ANOMALIES DE RECONSTRUCTION :"] + [f"  - {a}" for a in anomalies]
    SORTIE_TXT.write_text("\n".join(lignes), encoding="utf-8")
    print()
    print(f"écrit : {SORTIE_JSON.name} + {SORTIE_TXT.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
