#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tester_arbitrage_xrpl.py — TEST PAPIER 24 h : DEX XRPL (XRP/RLUSD) vs Binance
(consensus famille 14/09 : Cortana + Grok → D ; DeepSeek → variante market making)
0 ordre · 0 euro · lecture seule.

CALIBRAGE FAIT (1er cycle vérifié à la main) :
  Seul carnet USD vivant sur le ledger = RLUSD, issuer rvYAfWj5gh67oV6fW32ZzP3Aw4Eubs59B.
  Book « acheter XRP contre RLUSD » : TakerGets = drops XRP (STR), TakerPays = RLUSD (STR aussi).
  Prix USD/XRP de chaque offre = TakerPays.value / (TakerGets / 1e6).
  Il existe aussi le carnet inverse (vendre XRP pour RLUSD) — on mesure LES DEUX côtés,
  car l'arbitrage réel = acheter d'un côté, vendre de l'autre, moins TOUTES les frictions.

CRITÈRES DE SURVIE FIGÉS AVANT LE RUN (consensus famille, notés dans le dossier) :
  Cortana  : ≥ 5 opportunités/jour NETTES de frais avec rendement > 0,5 %/aller-retour → GO réel 200 $.
  Grok     : delta ≥ 1,5 % persistant ≥ 3 s, ≥ 10 fois/jour → edge existe.
  Sanction : écarts comblés < 1 s ou carnets trop minces → on arrête définitivement ce terrain.

FRICTIONS COMPTÉES (conservateur) : 0,2 % aller-retour (spread Binance ~0,05 %, fee taker Binance
0,1 % ×2 à l'entrée/sortie, frais XRPL négligeables mais slippage RLUSD pris à 0,05 %).
"""
import json, time, hashlib, urllib.request
from pathlib import Path
from datetime import datetime, timezone

BASE = Path.home() / "ace777-test-day1" / "Index_Maison"
DATA = BASE / "data" / "xrpl_arbitrage_hist.jsonl"
ETAT = BASE / "thermo" / "xrpl_arbitrage_etat.json"

RLUSD = "rvYAfWj5gh67oV6fW32ZzP3Aw4Eubs59B"
RPC_URL = "https://s1.ripple.com:51234"
FRICTION = 0.002          # 0,2 % aller-retour, conservateur
SEUIL_NET = 0.005         # Cortana : > 0,5 % NET par aller-retour
SEUIL_GROK = 0.015        # Grok : delta brut ≥ 1,5 %

def rpc(methode, **params):
    body = json.dumps({"method": methode, "params": [params]}).encode()
    req = urllib.request.Request(RPC_URL, data=body, headers={"Content-Type": "application/json"})
    return json.loads(urllib.request.urlopen(req, timeout=15).read()).get("result", {})

def prix_binance():
    d = json.loads(urllib.request.urlopen(
        "https://api.binance.com/api/v3/ticker/price?symbol=XRPUSDT", timeout=8).read())
    return float(d["price"])

def carnet_xrpl():
    """Prix USD/XRP des deux carnets RLUSD : (meilleur_ask_achat_xrp, meilleur_bid_vente_xrp, profondeurs)."""
    # Carnet A : taker_gets=XRP, taker_pays=RLUSD → on ACHÈTE du XRP (les offres triées du meilleur prix)
    rA = rpc("book_offers", taker_gets={"currency": "XRP"},
             taker_pays={"currency": "USD", "issuer": RLUSD}, limit=10)
    prix_achat, prof_achat = None, 0.0
    for o in rA.get("offers") or []:
        gets = o.get("TakerGets")
        pays = o.get("TakerPays")
        if not isinstance(gets, str) or not isinstance(pays, dict): continue
        xrp = float(gets) / 1e6
        usd = float(pays["value"])
        p = usd / xrp if xrp else 0
        if prix_achat is None or p < prix_achat:
            prix_achat = p
        prof_achat += xrp
    # Carnet B : taker_gets=RLUSD, taker_pays=XRP → on VEND du XRP
    rB = rpc("book_offers", taker_gets={"currency": "USD", "issuer": RLUSD},
             taker_pays={"currency": "XRP"}, limit=10)
    prix_vente, prof_vente = None, 0.0
    for o in rB.get("offers") or []:
        gets = o.get("TakerGets")
        pays = o.get("TakerPays")
        if not isinstance(gets, dict) or not isinstance(pays, str): continue
        usd = float(gets["value"])
        xrp = float(pays) / 1e6
        p = usd / xrp if xrp else 0
        if prix_vente is None or p > prix_vente:
            prix_vente = p
        prof_vente += xrp
    return prix_achat, prof_achat, prix_vente, prof_vente

def mesure():
    px_bin = prix_binance()
    pa, prof_a, pv, prof_v = carnet_xrpl()
    if pa is None or pv is None:
        return {"err": "carnet incomplet", "pa": pa, "pv": pv}
    # spread interne XRPL : acheter au ask (pa), vendre au bid (pv)
    spread_interne_pct = (pv - pa) / pa * 100 if pa else None
    # écarts vs Binance
    ecart_achat_pct = (pa / px_bin - 1) * 100    # XRPL plus cher que Binance → acheter sur Binance, vendre XRPL
    ecart_vente_pct = (pv / px_bin - 1) * 100
    # opportunité NETTE aller-retour (achat Binance → vente XRPL, ou l'inverse) moins frictions
    net1 = (pv - px_bin) / px_bin - FRICTION      # acheter Binance, vendre XRPL
    net2 = (px_bin - pa) / pa - FRICTION          # acheter XRPL, vendre Binance
    meilleur_net = max(net1, net2)
    return {"ts": datetime.now(timezone.utc).isoformat(),
            "binance": px_bin, "xrpl_ask": round(pa, 5), "xrpl_bid": round(pv, 5),
            "prof_xrp_ask": round(prof_a), "prof_xrp_bid": round(prof_v),
            "spread_interne_pct": round(spread_interne_pct, 3),
            "net_binaire_vers_xrpl": round(net1 * 100, 3),
            "net_xrpl_vers_binaire": round(net2 * 100, 3),
            "meilleur_net_pct": round(meilleur_net * 100, 3),
            "opportunite_nette": meilleur_net >= SEUIL_NET,
            "opportunite_grok": meilleur_net + FRICTION >= SEUIL_GROK}

def main():
    ligne = mesure()
    ligne["md5_script"] = hashlib.md5(Path(__file__).read_bytes()).hexdigest()[:8]
    DATA.parent.mkdir(parents=True, exist_ok=True)
    with DATA.open("a") as f:
        f.write(json.dumps(ligne, ensure_ascii=False) + "\n")
    etat = {"cycles": 0, "opportunites_nettes": 0, "opportunites_grok": 0, "dernier": None}
    if ETAT.exists():
        try: etat.update(json.loads(ETAT.read_text()))
        except Exception: pass
    etat["cycles"] = etat.get("cycles", 0) + 1
    if ligne.get("opportunite_nette"): etat["opportunites_nettes"] = etat.get("opportunites_nettes", 0) + 1
    if ligne.get("opportunite_grok"): etat["opportunites_grok"] = etat.get("opportunites_grok", 0) + 1
    etat["dernier"] = {k: ligne.get(k) for k in ("ts", "meilleur_net_pct", "spread_interne_pct")}
    ETAT.parent.mkdir(parents=True, exist_ok=True)
    ETAT.write_text(json.dumps(etat, ensure_ascii=False, indent=1))
    print(json.dumps(ligne, ensure_ascii=False))

if __name__ == "__main__":
    main()
