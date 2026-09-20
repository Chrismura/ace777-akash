#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""collecter_xrpl_onchain.py — RADAR ONCHAIN XRPL, collecteur PASSIF (P-XRPL-2).

═════════════════════════════════════════════════════════════════════════
SPÉCIFICATION FIGÉE AVANT LE PREMIER CYCLE (GO Christophe 14/09 « go pour
les trois » — les 4 trous identifiés par l'audit Buffy du même jour).
Protocole identique aux radars RWA/gouvernance : capter, ne rien alerter,
verdict à J+8. Zéro écriture hors data/ et thermo/. 0 €.
═════════════════════════════════════════════════════════════════════════

CE QUE ÇA COMBLE (les 4 trous de l'audit 14/09) :
  1. ONCHAIN : tx_count + destroyed_coins (burn) + total_coins (offre)
     par ledger via https://api.xrpscan.com/api/v1/ledger (public, gratuit)
     → taux tx/s, XRP brûlés/jour.
  2. FRAIS & RÉSERVE : base_fee_xrp / reserve_base / reserve_inc via
     server_info sur https://s1.ripple.com:51234 (JSON-RPC public).
  3. TOKENS / AMM : top 200 tokens xrpscan (holders, n_amms, marketcap)
     → la liquidité par projet candidat (DB CONNAISSANCE_PROJETS).
  4. HISTORIQUE : data/xrpl_onchain_hist.jsonl append-only, rotation
     gérée par rotation_jsonl.py (leçon journal_radar.log 3,3 Go).

CRITÈRE DE VERDICT J+8 — PRÉ-ENREGISTRÉ (écrit avant toute donnée) :
  SUCCÈS si AU MOINS UN de :
    a) taux moyen tx/ledger varie ≥ ±20 % entre semaine 1 et semaine 2
    b) burn XRP/jour varie ≥ ±20 % sur la fenêtre
    c) ≥ 1 token de la watchlist projets voit son n_amms ou holders
       bouger ≥ ±10 %
  ÉCHEC sinon = chaîne figée → pas de signal, on arrête (même discipline
  que RWA/gouvernance). Pas de deuxième essai.

ROBUSTESSE : 4 essais API avec backoff (2/10/30/60 s), échec = cycle
sauté honnêtement (api_ko), jamais de donnée inventée.

Usage : python3 collecter_xrpl_onchain.py           # 1 cycle
        python3 collecter_xrpl_onchain.py --status  # tableau de bord
"""
import argparse
import json
import time
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

MAISON = Path.home() / "ace777-test-day1" / "Index_Maison"
DATA = MAISON / "data"
THERMO = MAISON / "thermo"
HIST = DATA / "xrpl_onchain_hist.jsonl"
ETAT = THERMO / "xrpl_onchain_etat.json"

URL_LEDGER = "https://api.xrpscan.com/api/v1/ledger"
URL_TOKENS = "https://api.xrpscan.com/api/v1/tokens"
URL_RPC = "https://s1.ripple.com:51234/"

# Watchlist projets (figée 14/09) : les actifs de la DB dont la liquidité
# XRPL compte (tokens émis sur le DEX XRPL, pas les MEXC watchlist seules)
WATCHLIST_CODES = ["SOLO", "RLUSD", "CSC", "EQUILIBRIUM", "XRP"]

BACKOFFS = [2, 10, 30, 60]


def http_json(url: str, payload: dict = None, timeout: float = 15.0):
    last_err = None
    for i, b in enumerate(BACKOFFS):
        try:
            if payload is None:
                req = urllib.request.Request(url, headers={"User-Agent": "ACE777-radar/1.0"})
            else:
                req = urllib.request.Request(
                    url, data=json.dumps(payload).encode(),
                    headers={"Content-Type": "application/json", "User-Agent": "ACE777-radar/1.0"})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return json.loads(r.read().decode())
        except Exception as e:
            last_err = e
            if i < len(BACKOFFS) - 1:
                time.sleep(b)
    raise last_err


def cycle() -> dict:
    now = datetime.now(timezone.utc)
    ts = now.strftime("%Y-%m-%dT%H:%M:%SZ")
    rec = {"ts": ts, "api_ko": False}

    # 1) dernier ledger : tx_count, burn, offre
    try:
        led = http_json(URL_LEDGER)
        l = led["ledgers"][-1]
        rec["ledger_index"] = l.get("ledger_index")
        rec["tx_count"] = l.get("tx_count")
        rec["destroyed_drops"] = l.get("destroyed_coins")
        rec["total_drops"] = l.get("total_coins")
        rec["ledger_time"] = l.get("close_time_human")
    except Exception as e:
        rec["api_ko"] = True
        rec["err_ledger"] = str(e)[:120]

    # 2) frais & réserves (JSON-RPC public)
    try:
        si = http_json(URL_RPC, payload={"method": "server_info", "params": [{}]})
        vl = si["result"]["info"]["validated_ledger"]
        rec["base_fee_xrp"] = vl.get("base_fee_xrp")
        rec["reserve_base_xrp"] = vl.get("reserve_base_xrp")
        rec["reserve_inc_xrp"] = vl.get("reserve_inc_xrp")
    except Exception as e:
        rec["err_rpc"] = str(e)[:120]

    # 3) tokens : watchlist + top par holders
    try:
        toks = http_json(URL_TOKENS)
        rec["n_tokens_indexes"] = len(toks)
        watch = {}
        for t in toks:
            code = t.get("code", "")
            if code in WATCHLIST_CODES:
                watch[code] = {
                    "holders": t.get("holders"), "amms": t.get("amms"),
                    "marketcap": t.get("marketcap"), "price": t.get("price"),
                }
        rec["watchlist"] = watch
        top = sorted(toks, key=lambda x: -(x.get("holders") or 0))[:5]
        rec["top5_holders"] = [{"code": t.get("code"), "holders": t.get("holders"),
                                "amms": t.get("amms")} for t in top]
    except Exception as e:
        rec["err_tokens"] = str(e)[:120]

    # [C5] append + rotation gérée par rotation_jsonl.py
    DATA.mkdir(parents=True, exist_ok=True)
    with HIST.open("a", encoding="utf-8") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")

    # 4) état chien (produit frais, 1 h attendu)
    etat = {
        "ts": ts, "organe": "xrpl-onchain",
        "role": "radar passif onchain XRPL — AUCUNE alerte (P-XRPL-2, GO 14/09)",
        "api_ko": rec.get("api_ko", False),
        "dernier_ledger": rec.get("ledger_index"),
        "tx_count": rec.get("tx_count"),
        "burn_drops": rec.get("destroyed_drops"),
        "reserve_base_xrp": rec.get("reserve_base_xrp"),
        "n_tokens": rec.get("n_tokens_indexes"),
    }
    ETAT.write_text(json.dumps(etat, ensure_ascii=False, indent=1), encoding="utf-8")
    return rec


def status():
    if not HIST.exists():
        print("aucun cycle encore")
        return
    lines = HIST.read_text(encoding="utf-8").strip().splitlines()
    print(f"== RADAR ONCHAIN XRPL · {len(lines)} cycles ==")
    for ln in lines[-3:]:
        r = json.loads(ln)
        if r.get("api_ko"):
            print(f"  {r['ts']} — API KO ({r.get('err_ledger','?')})")
        else:
            print(f"  {r['ts']} — ledger {r.get('ledger_index')} : {r.get('tx_count')} tx, "
                  f"burn {r.get('destroyed_drops')} drops, tokens {r.get('n_tokens_indexes')}")
    print("\nverdict pré-enregistré : J+8 (22/09) — a) tx/ledger ±20 % · b) burn ±20 % · c) watchlist ±10 %")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--status", action="store_true")
    args = ap.parse_args()
    if args.status:
        status()
    else:
        r = cycle()
        print(f"[xrpl-onchain] cycle OK — ledger {r.get('ledger_index')}, {r.get('tx_count')} tx, "
              f"api_ko={r.get('api_ko', False)}")
