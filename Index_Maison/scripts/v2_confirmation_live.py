#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""v2_confirmation_live.py — RUN TESTÉ LIVE de la spec V2-CONFIRMATION (papier).
GO Christophe 13/09 : « je le veux en live, pas une reconstruction, un vrai run testé ».
La spécification est CELLE DU SCRIPT SCELLÉ v2_confirmation_replay.py (md5 d76c2c17,
figée AVANT toute donnée live — un run live est donc plus propre que le replay :
aucune règle n'a été choisie en regardant ces données-ci).

Même spec, exécutée en temps réel :
  ENTRÉE à la décision 00h00 UTC : G (régime SMA hebdo 50×200 causale) + 2 confirmations
  (F1a funding>avg30×HAUSSIER ; F1b flux48h≥±5 BTC×chg24 ; OFI et C2 purge restent
  masqués — même règle R1/R3 que le scellé) ; VETO zone morte funding<0,0002.
  SORTIES mesurées : trailing σ (arm 1.0σ, giveback 0.4σ), shock-inversion 2σ,
  invalidation (régime bascule 2 jours), filet 72 h.
  PAPIER : notionnel 1 125 $, frais 8 bps/côté — AUCUN ordre, AUCUN échange.

Boucle : toutes les 5 min il vérifie sorties/état ; à 00h00 UTC il décide l'entrée.
Produits (Index_Maison/thermo/) : v2conf_etat.json (état live), v2conf_log.jsonl
(chaque cycle 1 ligne), v2conf_trades.jsonl (1 ligne par trade papier).
"""
import json
import math
import statistics
import subprocess
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

# ---- constantes : identiques au scellé, inchangées ----
NOTIONNEL = 1125.0
FRAIS_AR = 1.80
SIGMA_ARM, SIGMA_GIVEBACK, SIGMA_SHOCK = 1.0, 0.4, 2.0
HOLD_MAX_J = 3
SEUIL_FLUX_BTC, CHG24_MIN, ZONE_MORTE = 5.0, 1.0, 0.0002
SPOT_URL = "https://api.binance.com/api/v3/klines"
FUT_URL = "https://fapi.binance.com/fapi/v1/klines"
FUND_URL = "https://fapi.binance.com/fapi/v1/fundingRate"
BASE = Path.home() / "ace777-test-day1"
TH = BASE / "Index_Maison/thermo"
ETAT, LOGJ, TRJ = TH / "v2conf_etat.json", TH / "v2conf_log.jsonl", TH / "v2conf_trades.jsonl"

def z(): return datetime.now(timezone.utc)

def log(msg, **kw):
    ligne = {"ts": z().strftime("%Y-%m-%dT%H:%M:%SZ"), "msg": msg, **kw}
    with LOGJ.open("a") as f:
        f.write(json.dumps(ligne, ensure_ascii=False) + "\n")

def http_json(url):
    r = subprocess.run(["curl", "-s", "-m", "20", url], capture_output=True, text=True, timeout=25)
    return json.loads(r.stdout)

def bougies_5m():
    """Bougies JOURNALIÈRES 1d (1450 pour les SMA hebdo 50×200) — couche acquisition
    corrigée 22:4xZ : le régime a besoin de 1400 clôtures journalières, pas de 5m.
    La RÈGLE du scellé est inchangée (même SMA, même causalité : clôtures ≤ hier)."""
    # API plafonnée à 1000 bougies/appel -> 2 pages paginées (1450 nécessaires aux SMA hebdo)
    kl = http_json(SPOT_URL + "?symbol=BTCUSDT&interval=1d&limit=1000")
    if not kl:
        kl = http_json(FUT_URL + "?symbol=BTCUSDT&interval=1d&limit=1000")
    if kl:
        try:
            plus_anciennes = http_json(SPOT_URL + f"?symbol=BTCUSDT&interval=1d&endTime={kl[0][0]-1}&limit=1000")
            kl = plus_anciennes + kl
        except Exception:
            pass
    out = []
    for k in kl or []:
        d = datetime.fromtimestamp(k[0] / 1000, timezone.utc).strftime("%Y-%m-%d")
        out.append({"jour": d, "o": float(k[1]), "h": float(k[2]),
                    "l": float(k[3]), "c": float(k[4])})
    return out

def regime(jours):
    """SMA hebdo 50×200 causale — même règle que le scellé (clôtures ≤ hier)."""
    closes = [j["c"] for j in jours]
    if len(closes) < 1401:
        return None, None, None
    s50 = sum(closes[-350:]) / 350
    s200 = sum(closes[-1400:]) / 1400
    return ("HAUSSIER" if s50 > s200 else "BAISSIER"), s50, s200

def sigma30(jours):
    closes = [j["c"] for j in jours]
    if len(closes) < 32:
        return None
    rets = [math.log(closes[k] / closes[k - 1]) for k in range(len(closes) - 30, len(closes))]
    return statistics.pstdev(rets)

def funding_etat():
    data = http_json(FUND_URL + "?symbol=BTCUSDT&limit=1000")
    pts = [(datetime.fromtimestamp(x["fundingTime"] / 1000, timezone.utc)
            .strftime("%Y-%m-%dT%H:%M:%SZ"), float(x["fundingRate"])) for x in data]
    dernier = pts[-1][1] if pts else None
    prec = [r for _, r in pts]
    avg30 = statistics.mean(prec[-90:]) if len(prec) >= 10 else None
    return dernier, avg30

def flux_48h():
    """Ledger dédup + registre exchange — même règle que flux_nets_exchanges.py."""
    ledger = BASE / "Index_Maison/data/whales_mouvements.jsonl"
    registre = BASE / "Index_Maison/data/whales.json"
    ex = set()
    try:
        d = json.loads(registre.read_text())
        ex = {p["address"] for p in d.get("portefeuilles", [])
              if p.get("type") in {"exchange_hot", "exchange_cold", "exchange_reserve"}}
    except Exception:
        pass
    par_txid = {}
    try:
        for line in ledger.read_text().splitlines():
            try:
                o = json.loads(line)
            except Exception:
                continue
            txid = o.get("txid") or ""
            if not txid:
                continue
            e = par_txid.get(txid)
            if e is None:
                par_txid[txid] = {"ts": o.get("ts", ""), "ligne": o}
            elif o.get("ts", "") < e["ts"]:
                par_txid[txid]["ts"] = o.get("ts", "")
    except FileNotFoundError:
        return 0.0
    d1 = z().replace(microsecond=0)
    d0 = d1 - timedelta(hours=48)
    net = 0.0
    for e in par_txid.values():
        try:
            t = datetime.strptime(e["ts"][:19], "%Y-%m-%dT%H:%M:%S").replace(tzinfo=timezone.utc)
        except Exception:
            continue
        if d0 <= t < d1:
            m = e["ligne"]
            try:
                btc = max(float(m.get("btc") or 0.0), 0.0)
            except (TypeError, ValueError):
                btc = 0.0
            src = set(m.get("sources") or [])
            dst = {c.get("adresse") for c in (m.get("cibles") or []) if c.get("adresse")}
            if src & ex and not dst & ex:
                net -= btc
            elif dst & ex and not src & ex:
                net += btc
    return net

def charge():
    try:
        return json.loads(ETAT.read_text())
    except Exception:
        return {"position": None, "trades": [], "bascule": 0, "derniere_decision": None}

def sauve(etat):
    ETAT.write_text(json.dumps(etat, indent=2, ensure_ascii=False))

def fermer(etat, px, raison, prix_jour):
    pos = etat["position"]
    brut = pos["dir"] * (px - pos["entree"]) / pos["entree"] * NOTIONNEL
    t = {"entree_j": pos["jour"], "sortie_ts": z().strftime("%Y-%m-%dT%H:%M:%SZ"),
         "side": "LONG" if pos["dir"] > 0 else "SHORT", "entree": pos["entree"],
         "sortie": round(px, 2), "brut": round(brut, 2), "frais": FRAIS_AR,
         "net": round(brut - FRAIS_AR, 2), "raison": raison}
    etat["trades"].append(t)
    with TRJ.open("a") as f:
        f.write(json.dumps(t, ensure_ascii=False) + "\n")
    log(f"FERMÉ {t['side']} net {t['net']:+.2f}$ ({raison})", **t)
    etat["position"] = None
    etat["bascule"] = 0

def cycle():
    etat = charge()
    dernier_log = etat.get("dernier_cycle")
    maintenant = z()
    jours = bougies_5m()
    j_hier, j_veille = jours[-2], jours[-3]
    hier = j_hier["jour"]
    prix_ref = j_hier["c"]                     # dernière clôture journalière connue
    reg, s50, s200 = regime(jours)
    sig = sigma30(jours)
    dern_f, avg30 = funding_etat()
    net48 = flux_48h()
    chg24 = (j_hier["c"] / j_veille["c"] - 1) * 100

    # ---------- 1. sorties mesurées (position ouverte) ----------
    pos = etat.get("position")
    if pos:
        s_px = sig * pos["entree"]
        if pos["dir"] > 0:
            pos["mfp"] = max(pos["mfp"], prix_ref)
            if pos["mfp"] - SIGMA_GIVEBACK * s_px <= prix_ref and pos["mfp"] >= pos["arm"]:
                fermer(etat, prix_ref, "trailing", prix_ref)
            elif chg24 <= -SIGMA_SHOCK * sig:
                fermer(etat, prix_ref, "shock_inversion", prix_ref)
        else:
            pos["mfp"] = min(pos["mfp"], prix_ref)
            if pos["mfp"] + SIGMA_GIVEBACK * s_px >= prix_ref and pos["mfp"] <= pos["arm"]:
                fermer(etat, prix_ref, "trailing", prix_ref)
            elif chg24 >= SIGMA_SHOCK * sig:
                fermer(etat, prix_ref, "shock_inversion", prix_ref)
        pos = etat.get("position")

    # ---------- 2. filet 72 h ----------
    if pos and (maintenant - datetime.fromisoformat(pos["entree_ts"])).days >= HOLD_MAX_J:
        fermer(etat, prix_ref, "filet_72h", prix_ref)
        pos = None

    # ---------- 3. invalidation : régime bascule 2 cycles consécutifs ----------
    if pos:
        oppose = (pos["dir"] > 0 and reg != "HAUSSIER") or (pos["dir"] < 0 and reg != "BAISSIER")
        etat["bascule"] = etat.get("bascule", 0) + (1 if oppose else 0)
        if etat["bascule"] >= 2:
            fermer(etat, prix_ref, "invalidation", prix_ref)
            pos = None

    # ---------- 4. décision d'entrée (une fois par jour UTC) ----------
    jour_utc = maintenant.strftime("%Y-%m-%d")
    if pos is None and etat.get("derniere_decision") != jour_utc and reg and sig:
        preuve = []
        sens = None
        veto_zm = dern_f is not None and dern_f < ZONE_MORTE
        c1 = bool(reg == "HAUSSIER" and dern_f is not None and avg30 and dern_f > avg30)
        c3 = (net48 >= SEUIL_FLUX_BTC and chg24 <= -CHG24_MIN) or \
             (net48 <= -SEUIL_FLUX_BTC and chg24 >= CHG24_MIN)
        if c1:
            sens = "LONG"
            preuve.append(f"C1 funding {dern_f:.2e} > avg30 {avg30:.2e}")
        if net48 >= SEUIL_FLUX_BTC and chg24 <= -CHG24_MIN:
            sens = sens or "LONG"
            preuve.append(f"C3 flux {net48:+.1f} BTC + baisse {chg24:+.1f}%")
        if net48 <= -SEUIL_FLUX_BTC and chg24 >= CHG24_MIN and reg == "BAISSIER" and dern_f is not None and avg30 and dern_f > avg30:
            sens = "SHORT"
            preuve.append(f"C3 flux {net48:+.1f} BTC + hausse {chg24:+.1f}%")
        entree = None
        if not veto_zm and c1 and c3 and sens == "LONG" and reg == "HAUSSIER":
            entree = {"dir": 1, "side": "LONG"}
        elif not veto_zm and sens == "SHORT" and reg == "BAISSIER":
            entree = {"dir": -1, "side": "SHORT"}
        if entree:
            entree_px = prix_ref
            etat["position"] = {"side": entree["side"], "dir": entree["dir"],
                                "jour": hier, "entree_ts": maintenant.isoformat(),
                                "entree": entree_px, "mfp": entree_px,
                                "arm": entree_px + entree["dir"] * SIGMA_ARM * sig * entree_px,
                                "confirmations": preuve}
            log(f"OUVERT {entree['side']} @ {entree_px:.2f} (papier)", confirmations=preuve, regime=reg)
        else:
            raisons = []
            if veto_zm:
                raisons.append(f"zone morte (funding {dern_f:.2e} < {ZONE_MORTE})")
            if not c1 and not c3:
                raisons.append("confirmations insuffisantes (règle 2 sources)")
            elif c1 != c3:
                raisons.append("1 seule confirmation (règle 2 sources)")
            log(f"aucune entrée aujourd'hui — {reg}, funding {dern_f:.2e}, flux48 {net48:+.1f} BTC, chg24 {chg24:+.1f}% · " + " · ".join(raisons) if raisons else "silence", regime=reg)
        etat["derniere_decision"] = jour_utc

    etat["dernier_cycle"] = z().strftime("%Y-%m-%dT%H:%M:%SZ")
    etat["contexte"] = {"regime": reg, "funding": dern_f, "flux48_btc": round(net48, 2),
                        "chg24_pct": round(chg24, 2), "sigma_jour": sig, "prix_ref": prix_ref}
    sauve(etat)
    log("cycle OK", regime=reg, funding=dern_f, flux48=round(net48, 2), prix_ref=prix_ref,
        position=bool(etat.get("position")))

def main():
    log("DÉMARRAGE moteur live V2-CONFIRMATION (papier, zéro ordre) — spec = scellé d76c2c17")
    while True:
        try:
            cycle()
        except Exception as e:
            log(f"ERREUR cycle (reprise dans 5 min) : {e}")
        time.sleep(300)

if __name__ == "__main__":
    main()
