#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""sniffer_vieux_btc.py — SNIFF « vieux BTC qui bougent » (30/08/2026).

Détection des baleines dormantes qui se réveillent : scanne les derniers blocs
(mempool.space, gratuit sans clé), garde les transactions >= SEUIL_BTC, puis
remonte l'âge du PLUS VIEIL input de chaque grosse tx (via l'API tx des
prevouts). Un input âgé de N années = vieux coins en mouvement.

Sortie :
  Index_Maison/data/vieux_btc_scan.json        (dernier scan, complet)
  Index_Maison/data/vieux_btc_mouvements.jsonl (historique append-only)

Usage : python3 sniffer_vieux_btc.py [--blocs N] [--seuil BTC] [--min-age-ans A]
Défauts : 8 blocs · 50 BTC · 2 ans.
"""
import json
import os
import sys
import time
import urllib.request
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data")
SCAN_OUT = os.path.join(DATA, "vieux_btc_scan.json")
HISTO = os.path.join(DATA, "vieux_btc_mouvements.jsonl")

MEMPOOL = "https://mempool.space/api"
NB_BLOCS = 8
SEUIL_BTC = 50.0
MIN_AGE_ANS = 2.0

UA = {"User-Agent": "ACE777-vieuxbtc/1.0"}


def get_json(url, timeout=15):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8"))


def btc(v):
    return (v or 0) / 1e8


def hauteur_vers_ts(hauteur):
    """Timestamp approximatif d'un bloc : 600 s par bloc depuis le tip."""
    return time.time() - (int(hauteur) and 0)  # placeholder, remplacé ci-dessous


def main():
    global NB_BLOCS, SEUIL_BTC, MIN_AGE_ANS
    args = sys.argv[1:]
    if "--blocs" in args:
        NB_BLOCS = int(args[args.index("--blocs") + 1])
    if "--seuil" in args:
        SEUIL_BTC = float(args[args.index("--seuil") + 1])
    if "--min-age-ans" in args:
        MIN_AGE_ANS = float(args[args.index("--min-age-ans") + 1])

    ts = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    print(f"[{ts}] sniff vieux BTC — {NB_BLOCS} blocs, seuil {SEUIL_BTC} BTC, âge min {MIN_AGE_ANS} ans", flush=True)

    # 1) tip + derniers blocs (hash par hauteur)
    tip = get_json(f"{MEMPOOL}/blocks/tip/height")
    blocs_hashes = get_json(f"{MEMPOOL}/blocks")[:NB_BLOCS]  # les plus récents d'abord
    # mempool /blocks renvoie [{id, height, timestamp, tx_count, ...}]
    blocs = []
    for b in blocs_hashes:
        try:
            blocs.append({"hauteur": b["height"], "hash": b["id"], "timestamp": b["timestamp"], "tx_count": b["tx_count"]})
        except Exception:
            pass
    print(f"  tip={tip}, {len(blocs)} blocs à scanner", flush=True)

    # 2) grosses tx des blocs récents (API mempool : par HASH de bloc)
    grosses = []
    for b in blocs_hashes:
        hauteur = b["height"]
        hash_bloc = b["id"]
        ts_bloc = b["timestamp"]
        # API mempool pagine les tx d'un bloc par 25 : /block/{hash}/txs/{index}
        txs = []
        index = 0
        try:
            while True:
                page = get_json(f"{MEMPOOL}/block/{hash_bloc}/txs/{index}")
                if not page:
                    break
                txs.extend(page)
                if len(page) < 25:
                    break
                index += 25
        except Exception as e:
            print(f"  bloc {hauteur}: erreur txs {e}", flush=True)
            continue
        for tx in txs:
            total_out = sum(btc(v.get("value")) for v in tx.get("vout", []))
            if total_out < SEUIL_BTC:
                continue
            grosses.append({
                "txid": tx.get("txid"),
                "hauteur_bloc": hauteur,
                "ts_bloc": ts_bloc,
                "btc": round(total_out, 2),
                "n_inputs": len(tx.get("vin", [])),
                "vins": tx.get("vin", []),
            })
        print(f"  bloc {hauteur}: {len(txs)} tx, {sum(1 for t in grosses if t['hauteur_bloc']==hauteur)} grosses", flush=True)
        time.sleep(0.25)

    print(f"  {len(grosses)} grosses tx retenues — remontée de l'âge des inputs…", flush=True)

    # 3) âge du plus vieil input de chaque grosse tx
    now = time.time()
    for g in grosses:
        ages = []
        inputs_ages = []
        for vin in g["vins"][:12]:  # max 12 inputs remontés par tx
            pv = vin.get("prevout") or {}
            txid_p = pv.get("txid")
            if not txid_p:
                continue
            try:
                ptx = get_json(f"{MEMPOOL}/tx/{txid_p}")
                st = ptx.get("status") or {}
                h = st.get("block_height")
                if h:
                    # timestamp du bloc du prevout
                    try:
                        pb = get_json(f"{MEMPOOL}/block/{h}")
                        age_j = (now - pb["timestamp"]) / 86400.0
                    except Exception:
                        age_j = (now - (ts_bloc_approx(h, tip))) / 86400.0
                    ages.append(age_j)
                    inputs_ages.append({"age_jours": round(age_j, 1), "btc": round(btc(pv.get("value")), 4)})
                time.sleep(0.15)
            except Exception:
                continue
        g["inputs_ages"] = inputs_ages
        g["age_max_jours"] = round(max(ages), 1) if ages else None
        g["age_max_ans"] = round((g["age_max_jours"] or 0) / 365.25, 1)
        del g["vins"]
        del g["n_inputs"]

    # 4) filtrage : vieux coins uniquement
    vieux = [g for g in grosses if (g["age_max_ans"] or 0) >= MIN_AGE_ANS]
    vieux.sort(key=lambda g: -(g["age_max_ans"] or 0))

    resultat = {
        "ts": ts,
        "hauteur_tip": tip,
        "nb_blocs": NB_BLOCS,
        "seuil_btc": SEUIL_BTC,
        "min_age_ans": MIN_AGE_ANS,
        "nb_grosses_tx": len(grosses),
        "nb_vieux_mouvements": len(vieux),
        "vieux_mouvements": vieux,
        "note": "age_max = âge du plus vieil input de la tx (source mempool.space)",
    }
    os.makedirs(DATA, exist_ok=True)
    with open(SCAN_OUT, "w", encoding="utf-8") as f:
        json.dump(resultat, f, ensure_ascii=False, indent=2)
    for g in vieux:
        with open(HISTO, "a", encoding="utf-8") as f:
            f.write(json.dumps({"ts": ts, **g}, ensure_ascii=False) + "\n")

    print(f"  → {len(vieux)} mouvement(s) de vieux coins (âge ≥ {MIN_AGE_ANS} ans)", flush=True)
    for g in vieux[:15]:
        print(f"    {g['btc']:>10,.2f} BTC  âge max {g['age_max_ans']} ans  bloc {g['hauteur_bloc']}  {g['txid'][:20]}…", flush=True)
    print(f"  sauvegardé : {SCAN_OUT}", flush=True)
    return 0


def ts_bloc_approx(hauteur, tip):
    """Timestamp approx si l'API bloc échoue : 600s/bloc depuis le tip."""
    return time.time() - (tip - hauteur) * 600.0


if __name__ == "__main__":
    sys.exit(main())
