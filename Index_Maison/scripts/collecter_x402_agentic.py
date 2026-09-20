#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
collecter_x402_agentic.py — RADAR AGENTIQUE (GO Christophe 14/09)
Économie des machines sur XRPL : paiements x402 (machine→machine) via facilitateur t54.

SPEC FIGÉE AVANT LA PREMIÈRE DONNÉE (anti data-snooping) :
  Détection (spec publique t54 xrpl-x402-standard.md) :
    Payment validé avec SourceTag == 804681468 → paiement x402.
  Deux modes de capture passifs, 0 € :
    1) Fenêtre LIVE : WebSocket subscribe 'transactions' pendant 60 s.
    2) Scan LEDGER : le dernier ledger validé, toutes tx, filtre SourceTag.
  Critère de verdict J+8 = 22/09 (figé le 14/09, avant tout run) :
    CONTINUER si : a) ≥ 50 paiements x402 captés au total (fenêtres+scans)
               ET b) ≥ 5 marchands distincts (Destination)
               ET c) les ledgers avancent (source vivante, anti-figage).
    SINON : économie agentique trop mince à capter → on arrête le radar.
  Zéro ordre, zéro euro, zéro écriture moteur/profils/config. Append-only.

Sorties :
  data/x402_agentic_hist.jsonl   — 1 ligne par cycle (rotation [C5] 50 Mo)
  thermo/x402_agentic_etat.json  — cumul + compteur anti-figage
"""
import json, ssl, time, hashlib, sys
import urllib.request
from pathlib import Path
from datetime import datetime, timezone

BASE = Path.home() / "ace777-test-day1" / "Index_Maison"
DATA = BASE / "data" / "x402_agentic_hist.jsonl"
ETAT = BASE / "thermo" / "x402_agentic_etat.json"

WSS = "wss://xrplcluster.com"
REST = "https://xrplcluster.com"
FACILITATEUR_TAG = 804681468          # t54 XRPL Facilitator (spec publique)
FENETRE_LIVE_S = 60                   # fenêtre d'écoute passive par cycle

def utc():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

def rpc(commande, **params):
    # JSON-RPC enrobé (dialecte rippled vérifié : method + params[])
    body = json.dumps({"method": commande,
                       "params": [dict(params, id="ace")]},
                      ).encode()
    req = urllib.request.Request(REST, data=body,
                                 headers={"Content-Type": "application/json"})
    return json.loads(urllib.request.urlopen(req, timeout=15).read())

def fenetre_live():
    """Écoute passive 60 s du flux transactions ; compte les x402."""
    import websocket
    res = {"tx_total": 0, "x402": 0, "drips": 0,
           "marchands": set(), "acheteurs": set()}
    try:
        ws = websocket.create_connection(WSS, timeout=10,
                                         sslopt={"cert_reqs": ssl.CERT_NONE})
        ws.send(json.dumps({"id": 1, "command": "subscribe",
                            "streams": ["transactions"]}))
        deadline = time.time() + FENETRE_LIVE_S
        while time.time() < deadline:
            try:
                ws.settimeout(max(1, deadline - time.time()))
                msg = json.loads(ws.recv())
            except Exception:
                break
            tx = (msg.get("transaction")
                  if isinstance(msg.get("transaction"), dict) else msg.get("tx"))
            if not isinstance(tx, dict) or tx.get("TransactionType") != "Payment":
                continue
            res["tx_total"] += 1
            if tx.get("SourceTag") == FACILITATEUR_TAG:
                res["x402"] += 1
                res["marchands"].add(tx.get("Destination", "?"))
                res["acheteurs"].add(tx.get("Account", "?"))
                amt = tx.get("Amount")
                if isinstance(amt, str):
                    res["drips"] += int(amt)
        try: ws.close()
        except Exception: pass
    except Exception as e:
        res["err"] = str(e)[:120]
    return res

def scan_ledger():
    """Dernier ledger validé : toutes les tx, filtre x402."""
    try:
        d = rpc("ledger", ledger_index="validated", transactions=True, expand=True)
        led = d["result"]["ledger"]
        idx = led.get("ledger_index") or d["result"]["ledger_index"]
        txs = led.get("transactions") or []
        x402, drips, marchands = 0, 0, set()
        for tx in txs:
            t = tx.get("tx") or tx
            if (t.get("TransactionType") == "Payment"
                    and t.get("SourceTag") == FACILITATEUR_TAG):
                x402 += 1
                marchands.add(t.get("Destination", "?"))
                amt = t.get("Amount")
                if isinstance(amt, str):
                    drips += int(amt)
        return {"ledger": idx, "tx_total": len(txs), "x402": x402,
                "drips": drips, "marchands": sorted(marchands)}
    except Exception as e:
        return {"err": str(e)[:120]}

def main():
    live = fenetre_live()
    scan = scan_ledger()

    # --- cumul depuis l'état précédent (anti-figage sur l'index de ledger) ---
    prec = {}
    if ETAT.exists():
        try: prec = json.loads(ETAT.read_text())
        except Exception: prec = {}
    cum_x402 = prec.get("cum_x402", 0)
    cum_tx = prec.get("cum_tx", 0)
    marchands = set(prec.get("marchands", []))
    der_ledger = prec.get("dernier_ledger", 0)
    fige = prec.get("fige", 0)

    nouveau_ledger = scan.get("ledger") or 0
    if isinstance(nouveau_ledger, str):   # l'index arrive en CHAINE DECIMALE ('106985381') - piege hexa corrige 14/09 (vérifier le dialecte AVANT de convertir)
        try: nouveau_ledger = int(nouveau_ledger.strip(), 10)
        except Exception: nouveau_ledger = 0
    if nouveau_ledger and nouveau_ledger <= der_ledger:
        fige += 1
    elif nouveau_ledger:
        fige = 0

    total_cycle = live.get("x402", 0) + scan.get("x402", 0)
    total_tx_cycle = live.get("tx_total", 0) + scan.get("tx_total", 0)
    cum_x402 += total_cycle
    cum_tx += total_tx_cycle
    marchands |= set(live.get("marchands", [])) | set(scan.get("marchands", []))

    ligne = {
        "ts": utc(),
        "live_x402": live.get("x402", 0), "live_tx": live.get("tx_total", 0),
        "live_drips": live.get("drips", 0),
        "scan_ledger": scan.get("ledger"), "scan_tx": scan.get("tx_total", 0),
        "scan_x402": scan.get("x402", 0), "scan_drips": scan.get("drips", 0),
        "cum_x402": cum_x402, "cum_tx": cum_tx,
        "marchands_distincts": len(marchands),
        "anti_fige": fige,
    }
    if live.get("err"): ligne["err_live"] = live["err"]
    if scan.get("err"): ligne["err_scan"] = scan["err"]

    DATA.parent.mkdir(parents=True, exist_ok=True)
    with DATA.open("a") as f:
        f.write(json.dumps(ligne, ensure_ascii=False) + "\n")

    ETAT.write_text(json.dumps({
        "cum_x402": cum_x402, "cum_tx": cum_tx,
        "marchands": sorted(marchands), "dernier_ledger": nouveau_ledger,
        "fige": fige, "ts": utc(),
    }, ensure_ascii=False, indent=1))
    print(json.dumps(ligne, ensure_ascii=False))

if __name__ == "__main__":
    main()
