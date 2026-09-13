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
MAX_INPUTS = 0          # 0 = TOUS les inputs (correction 13/09 : avant, 12 seulement)
MAX_ESSAIS = 4          # retries API avec backoff (avant : 0 — toute erreur = âge perdu en silence)
TS_CACHE_MAX = 4096     # plafond du cache timestamps de blocs

UA = {"User-Agent": "ACE777-vieuxbtc/1.0"}


def get_json(url, timeout=15):
    """GET JSON avec retries + backoff (correction 13/09 : avant, 1 seul essai et
    toute erreur était avalée → ages 0.0/null sur tout un run en cas de throttle)."""
    last_err = None
    for essai in range(MAX_ESSAIS):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except Exception as e:
            last_err = e
            time.sleep(0.5 * (2 ** essai))  # 0.5, 1, 2, 4 s
    raise last_err


def btc(v):
    return (v or 0) / 1e8


def get_text(url, timeout=15):
    """GET texte brut — mempool /block-height renvoie le hash SANS guillemets JSON
    (bug d'origine : json.loads sur cette réponse levait toujours)."""
    last_err = None
    for essai in range(MAX_ESSAIS):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return resp.read().decode("utf-8")
        except Exception as e:
            last_err = e
            time.sleep(0.5 * (2 ** essai))
    raise last_err


_ts_bloc_cache = {}


def bloc_ts(hauteur, tip):
    """Timestamp d'un bloc par hauteur : API d'abord (hash via /block-height puis
    /block/{hash}), approximation 600 s/bloc en repli, cache mémoire.
    (correction 13/09 : l'ancien code appelait /block/{hauteur} au lieu de
    /block/{hash} — l'API ne pouvait jamais répondre.)"""
    h = int(hauteur)
    if h in _ts_bloc_cache:
        return _ts_bloc_cache[h]
    ts_b = None
    try:
        bh = get_text(f"{MEMPOOL}/block-height/{h}").strip().strip('"')
        bloc = get_json(f"{MEMPOOL}/block/{bh}")
        ts_b = float(bloc["timestamp"])
    except Exception:
        ts_b = None
    if ts_b is None:
        ts_b = time.time() - (tip - h) * 600.0  # approximation honnête (dérive ~10 min/jour)
    if len(_ts_bloc_cache) < TS_CACHE_MAX:
        _ts_bloc_cache[h] = ts_b
    return ts_b


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
    #    (correction 13/09 : TOUS les inputs, retries, cache, et surtout HONNÊTETÉ —
    #    un input non résolu devient null, jamais 0.0 ; une tx dont aucun input
    #    n'est résoluble ressort inputs_ages=null et est écartée du fichier, pas
    #    enregistrée comme « fraîche ».)
    now = time.time()
    for g in grosses:
        ages = []
        inputs_ages = []
        n_non_resolus = 0
        vins = g["vins"] if MAX_INPUTS <= 0 else g["vins"][:MAX_INPUTS]
        for vin in vins:
            pv = vin.get("prevout") or {}
            # BUG D'ORIGINE CORRIGÉ (13/09) : le txid du prevout est dans vin["txid"]
            # (format esplora), PAS dans prevout["txid"] (toujours None) — l'ancien
            # code lisait un champ vide : chaque input était sauté en silence,
            # d'où age 0.0/null sur TOUS les runs depuis le 30/08.
            txid_p = vin.get("txid") or pv.get("txid")
            if not txid_p:
                continue  # input coinbase ou absent : pas une pièce datable
            try:
                ptx = get_json(f"{MEMPOOL}/tx/{txid_p}")
                st = ptx.get("status") or {}
                h = st.get("block_height")
                if h:
                    age_j = (now - bloc_ts(h, tip)) / 86400.0
                    ages.append(age_j)
                    inputs_ages.append({"age_jours": round(age_j, 1), "btc": round(btc(pv.get("value")), 4)})
                else:
                    n_non_resolus += 1  # prevout en attente dans la mempool
                time.sleep(0.15)
            except Exception:
                n_non_resolus += 1
                continue
        if ages:
            g["inputs_ages"] = inputs_ages
            g["age_max_jours"] = round(max(ages), 1)
            g["age_max_ans"] = round(max(ages) / 365.25, 1)
        else:
            g["inputs_ages"] = None
            g["age_max_jours"] = None
            g["age_max_ans"] = None
        g["inputs_non_resolus"] = n_non_resolus
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
        "note": "age_max = âge du plus vieil input (TOUS inputs, retry+cache, correction 13/09). inputs_ages=null = inputs non résolus — jamais comptés comme 0.0",
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
    n_non_dates = sum(1 for g in grosses if g["inputs_ages"] is None)
    if n_non_dates:
        print(f"  ⚠ {n_non_dates} grosse(s) tx non datable(s) (inputs non résolus) — écartées du verdict, pas comptées comme fraîches", flush=True)
    print(f"  sauvegardé : {SCAN_OUT}", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
