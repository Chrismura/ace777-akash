#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""v2_confirmation_replay_4h.py — VARIANTE 4H (GO superviseur Christophe 17/09).
Zéro ordre, zéro euro. L'original scellé v2_confirmation_replay.py n'est PAS modifié.

SPÉCIFICATION FIGÉE AVANT LE RUN (directive de supervision 17/09, appliquée à la lettre) :
  TEMPORALITÉ : décisions sur bougies 4H Binance (BTCUSDT), fenêtre replay IDENTIQUE
     aux 4 replays précédents (90 jours finissant le 12/09, exclut le 12/09) — pour
     comparabilité. ~540 points de décision.
  RÉGIME MACRO (G) : SMA 50/200 CAUSALE sur clôtures JOURNALIÈRES reconstruites
     des bougies 4H (6/jour) ; le régime du jour n'utilise que les clôtures < jour.
     LONG si HAUSSIER, SHORT si BAISSIER, sinon silence.
  ENTRÉE (souplesse 2/3) : G valide + au moins 2 confirmations parmi :
     C1 (funding)  : dernier funding > moyenne 30 j (avg30 causale, ≥10 points).
     C3 (flux×variation) : LONG si net_btc_48h ≥ +5 ET chg4h ≤ −0,5 % ;
           SHORT si net_btc_48h ≤ −5 ET chg4h ≥ +0,5 %.
     C4 (volatilité/momentum) — INTERPRÉTATION FIXÉE ICI avant tout résultat :
           « variation 4H dans le sens de la panique » = chg4h ≤ −σ4h pour un LONG,
           chg4h ≥ +σ4h pour un SHORT, où σ4h = écart-type des rendements 4H sur
           les 30 derniers jours (causal). Convention σ maison, seuil non arbitraire.
     Conflit de direction entre confirmations → silence (règle maison).
     Exécution à l'ouverture de la bougie 4H suivante (causal).
  GARDE-FOUS None (robustesse exigée) : chaque indice est évalué indépendamment ;
     un indice indisponible (funding absent, flux masqué/absent, σ indisponible)
     rend SA porte indisponible sans crasher ni fausser les autres portes ; le
     compte des confirmations se fait sur les portes DISPONIBLES. Les
     indisponibilités sont comptées et consignées dans le résultat.
  VETO : PAS de veto statique. Veto négatif UNIQUEMENT : funding ≤ 0 → aucun trade.
  SORTIES (conventions maison transposées 4H) :
     S1 trailing σ4h : arm à entrée ± 1,0 σ4h×prix ; giveback 0,4 σ4h.
     S2 shock : clôture 4H contre le sens ≥ 2 σ4h → sortie à cette clôture.
     S3 invalidation : régime bascule 2 JOURS consécutifs → sortie à l'ouverture
        de la bougie suivante.
     FILET : 72 h = 18 bougies 4H (sortie à l'ouverture) — sécurité.
     Pas de ré-entrée sur la bougie d'une sortie.
  MASQUE R2 (conservé, honnêteté données) : flux (C3) masqué avant le 14/08 —
     C3 devient indisponible sur cette période, compteur consigné.
  ÉCONOMIE : notionnel 1 125 $ · frais 8 bps/côté = 1,80 $ aller-retour.
  VERDICT : critères pré-enregistrés C1 n≥30 · C2 net/trade > frais · C3 WR > 50 % ·
     C4 aucune raison > 40 % des pertes → PASS sinon ÉCHEC. Pas de 3e verdict.
"""
import json
import math
import statistics
import subprocess
from datetime import datetime, timedelta, timezone
from pathlib import Path

# ------------------------- constantes figées -------------------------
NOTIONNEL = 1125.0
FRAIS_AR = 1.80
SIGMA_ARM, SIGMA_GIVEBACK, SIGMA_SHOCK = 1.0, 0.4, 2.0
FILET_4H = 18                      # 72 h
SEUIL_FLUX_BTC = 5.0
CHG4H_PANIQUE = 0.5                # % pour C3
VETO_FUNDING_NEG = 0.0             # veto négatif seul : funding <= 0
FLUX_FIABLE_DES = "2026-08-14"     # masque R2 conservé
FIN_FENETRE = "2026-09-12"
JOURS_REPLAY = 90
SPOT_URL = "https://api.binance.com/api/v3/klines"
FUT_URL = "https://fapi.binance.com/fapi/v1/klines"
FUND_URL = "https://fapi.binance.com/fapi/v1/fundingRate"
BASE = Path.home() / "ace777-test-day1"
OUT_JSON = BASE / "Index_Maison/thermo/v2_confirmation_resultat_4h.json"

# ------------------------- acquisition (couche data) -----------------
def http_json(url, tag):
    h = str(abs(hash(url)))[:12]
    cache = Path("/tmp") / f"v2c4h_{tag}_{h}.json"
    if cache.exists():
        return json.loads(cache.read_text())
    r = subprocess.run(["curl", "-s", "-m", "25", url],
                       capture_output=True, text=True, timeout=30)
    data = json.loads(r.stdout)
    if not isinstance(data, list):
        raise RuntimeError(f"{tag}: {r.stdout[:160]}")
    cache.write_text(json.dumps(data))
    return data

def fetch_4h():
    """Bougies 4H sur ~240 jours (marge pour SMA journalière causale)."""
    end = int(datetime(2026, 9, 12, tzinfo=timezone.utc).timestamp() * 1000)
    start = int((datetime(2026, 9, 12, tzinfo=timezone.utc)
                 - timedelta(days=240)).timestamp() * 1000)
    kl, cursor = [], start
    while cursor < end:
        q = f"?symbol=BTCUSDT&interval=4h&startTime={cursor}&limit=1000"
        chunk = None
        for base in (SPOT_URL, FUT_URL):
            try:
                chunk = http_json(base + q, "kl4h")
                if chunk:
                    break
            except Exception:
                chunk = None
        if not chunk:
            raise RuntimeError("klines 4H indisponibles")
        kl.extend(chunk)
        cursor = chunk[-1][6] + 1
        if len(chunk) < 1000:
            break
    out = [{"t": int(k[0]), "o": float(k[1]), "h": float(k[2]),
            "l": float(k[3]), "c": float(k[4])} for k in kl]
    return [x for x in out if x["t"] < end]

def fetch_funding():
    data = http_json(FUND_URL + "?symbol=BTCUSDT&limit=1000", "fund")
    return [(datetime.fromtimestamp(x["fundingTime"] / 1000, timezone.utc)
             .strftime("%Y-%m-%dT%H:%M:%SZ"), float(x["fundingRate"])) for x in data]

def charger_flux():
    """Copie fidèle de l'original scellé (ledger dédup txid, direction vs registre)."""
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
            line = line.strip()
            if not line:
                continue
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
        return []
    evts = []
    for e in par_txid.values():
        m = e["ligne"]
        try:
            btc = max(float(m.get("btc") or 0.0), 0.0)
        except (TypeError, ValueError):
            btc = 0.0
        src = set(m.get("sources") or [])
        dst = {c.get("adresse") for c in (m.get("cibles") or []) if c.get("adresse")}
        if src & ex and not dst & ex:
            dirn = "SORTANT"
        elif dst & ex and not src & ex:
            dirn = "ENTRANT"
        else:
            dirn = "NEUTRE"
        evts.append({"ts": e["ts"], "dir": dirn, "btc": btc})
    return evts

# ------------------------- instruments causaux ----------------------
def funding_etat(fund, ts_ms):
    """(dernier funding ≤ instant, avg30 j avant) — causal. (None, None) si absent."""
    iso = datetime.fromtimestamp(ts_ms / 1000, timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    prec = [(t, r) for t, r in fund if t < iso]
    if not prec:
        return None, None
    dernier = prec[-1][1]
    avg30 = statistics.mean([r for _, r in prec[-90:]]) if len(prec) >= 10 else None
    return dernier, avg30

def flux_net_48h(evts, ts_ms):
    d1 = datetime.fromtimestamp(ts_ms / 1000, timezone.utc)
    d0 = d1 - timedelta(hours=48)
    net = 0.0
    for e in evts:
        try:
            t = datetime.strptime(e["ts"][:19], "%Y-%m-%dT%H:%M:%S").replace(tzinfo=timezone.utc)
        except Exception:
            continue
        if d0 <= t < d1:
            net += (-e["btc"] if e["dir"] == "SORTANT" else
                    e["btc"] if e["dir"] == "ENTRANT" else 0.0)
    return net

def jour_de(ts_ms):
    return datetime.fromtimestamp(ts_ms / 1000, timezone.utc).strftime("%Y-%m-%d")

# ------------------------- simulation -------------------------------
def run():
    kl4h = fetch_4h()
    fund = fetch_funding()
    evts = charger_flux()

    # clôtures journalières causales (dernière clôture 4H de chaque jour < jour courant)
    clos_par_jour = {}
    for k in kl4h:
        clos_par_jour[jour_de(k["t"])] = k["c"]
    jours_tri = sorted(clos_par_jour)
    def sma(n, avant_jour):
        vals = [clos_par_jour[j] for j in jours_tri if j < avant_jour][-n:]
        return sum(vals) / len(vals) if len(vals) == n else None

    # σ4h causale (30 derniers jours de rendements 4H)
    rets4h = [math.log(kl4h[i]["c"] / kl4h[i - 1]["c"]) for i in range(1, len(kl4h))]
    def sigma4h(i):
        seg = rets4h[max(0, i - 180):i]          # 180 bougies 4H = 30 jours
        return statistics.pstdev(seg) if len(seg) >= 120 else None

    trades, pos = [], None
    indispo = {"funding_absent": 0, "flux_masque": 0, "sigma_absente": 0, "portes_dispo_lt2": 0}
    refus = {"veto_funding_neg": 0, "conflit_direction": 0,
             "confirmations_insuffisantes": 0, "portes_dispo_lt2": 0}

    def fermer(k, px, raison):
        nonlocal pos
        brut = pos["dir"] * (px - pos["entree"]) / pos["entree"] * NOTIONNEL
        trades.append({"entree_t": pos["t_entree"], "sortie_t": k["t"], "side":
                       "LONG" if pos["dir"] > 0 else "SHORT", "entree": pos["entree"],
                       "sortie": px, "brut": round(brut, 2), "frais": FRAIS_AR,
                       "net": round(brut - FRAIS_AR, 2), "raison": raison})
        pos = None

    for i in range(1, len(kl4h) - 1):
        k, ksuiv = kl4h[i], kl4h[i + 1]
        jour = jour_de(k["t"])
        # ---- sorties d'abord ----
        if pos:
            held = i - pos["i"]
            if held >= FILET_4H:
                fermer(ksuiv, ksuiv["o"], "filet_72h")
                continue
            if pos["sortie_suivante"]:
                fermer(ksuiv, ksuiv["o"], "invalidation")
                continue
            s = pos["sigma_px"]
            chg = (k["c"] / kl4h[i - 1]["c"] - 1)
            if pos["dir"] > 0:
                pos["mfp"] = max(pos["mfp"], k["h"])
                if pos["mfp"] >= pos["arm"] and pos["mfp"] - SIGMA_GIVEBACK * s >= k["l"]:
                    fermer(ksuiv, max(k["l"], pos["mfp"] - SIGMA_GIVEBACK * s), "trailing")
                    continue
                if chg <= -SIGMA_SHOCK * pos["s4h"]:
                    fermer(ksuiv, k["c"], "shock")
                    continue
            else:
                pos["mfp"] = min(pos["mfp"], k["l"])
                if pos["mfp"] <= pos["arm"] and pos["mfp"] + SIGMA_GIVEBACK * s <= k["h"]:
                    fermer(ksuiv, min(k["h"], pos["mfp"] + SIGMA_GIVEBACK * s), "trailing")
                    continue
                if chg >= SIGMA_SHOCK * pos["s4h"]:
                    fermer(ksuiv, k["c"], "shock")
                    continue
        # ---- décision à la clôture 4H (données ≤ clôture) ----
        if pos is not None:
            # invalidation : bascule de régime 2 jours consécutifs
            r_j = (sma(50, jour), sma(200, jour))
            regime_j = "HAUSSIER" if (r_j[0] and r_j[1] and r_j[0] > r_j[1]) else (
                       "BAISSIER" if (r_j[0] and r_j[1]) else None)
            bascule = (pos["dir"] > 0 and regime_j != "HAUSSIER") or \
                      (pos["dir"] < 0 and regime_j != "BAISSIER")
            pos["n_bascule"] = pos.get("n_bascule", 0) + (1 if bascule else 0)
            if pos.get("n_bascule", 0) >= 2:
                pos["sortie_suivante"] = True
            continue
        regime = (lambda a, b: "HAUSSIER" if (a and b and a > b) else
                  ("BAISSIER" if (a and b) else None))(sma(50, jour), sma(200, jour))
        if regime is None:
            continue
        dernier_f, avg30 = funding_etat(fund, k["t"])
        s4h = sigma4h(i)
        chg4h = (k["c"] / kl4h[i - 1]["c"] - 1) * 100.0
        masque_flux = jour < FLUX_FIABLE_DES
        if masque_flux:
            indispo["flux_masque"] += 1
        # ---- veto négatif seul (directive §5) ----
        if dernier_f is not None and dernier_f <= VETO_FUNDING_NEG:
            refus["veto_funding_neg"] += 1
            continue
        confirmations, sens = [], None
        # C1 (funding) — None-safe : indisponible si avg30 absent
        if dernier_f is not None and avg30 is not None:
            if dernier_f > avg30:
                confirmations.append("C1")
                sens = "LONG" if regime == "HAUSSIER" else "SHORT"
        else:
            indispo["funding_absent"] += 1
        # C3 (flux×variation) — None-safe : indisponible si masqué
        if not masque_flux:
            net48 = flux_net_48h(evts, k["t"])
            if net48 >= SEUIL_FLUX_BTC and chg4h <= -CHG4H_PANIQUE:
                confirmations.append("C3")
                sens = "LONG" if sens is None else (sens if sens == "LONG" else "@CONFLIT")
            elif net48 <= -SEUIL_FLUX_BTC and chg4h >= CHG4H_PANIQUE:
                confirmations.append("C3")
                sens = "SHORT" if sens is None else (sens if sens == "SHORT" else "@CONFLIT")
        # C4 (σ-momentum) — None-safe : indisponible si σ absente
        if s4h is not None and s4h > 0:
            if chg4h <= -s4h * 100.0:
                confirmations.append("C4")
                sens = "LONG" if sens is None else (sens if sens == "LONG" else "@CONFLIT")
            elif chg4h >= s4h * 100.0:
                confirmations.append("C4")
                sens = "SHORT" if sens is None else (sens if sens == "SHORT" else "@CONFLIT")
        else:
            indispo["sigma_absente"] += 1
        if "@CONFLIT" in (sens or ""):
            refus["conflit_direction"] += 1
            continue
        if len(confirmations) < 2:
            refus["confirmations_insuffisantes" if confirmations else "portes_dispo_lt2"] += 1
            continue
        # G + 2/3 : LONG en HAUSSIER, SHORT en BAISSIER
        if sens == "LONG" and regime == "HAUSSIER":
            dirn = 1
        elif sens == "SHORT" and regime == "BAISSIER":
            dirn = -1
        else:
            continue
        s_px = (s4h or 0.0) * ksuiv["o"]
        pos = {"dir": dirn, "i": i + 1, "t_entree": ksuiv["t"], "entree": ksuiv["o"],
               "sigma_px": s_px, "s4h": s4h or 0.0, "mfp": ksuiv["o"],
               "arm": ksuiv["o"] + dirn * SIGMA_ARM * s_px,
               "sortie_suivante": False, "n_bascule": 0, "conf": confirmations}
    if pos:
        fermer(kl4h[-1], kl4h[-1]["c"], "fin_fenetre")

    # ------------------------- verdict mécanique -------------------------
    n = len(trades)
    nets = [t["net"] for t in trades]
    total_net = sum(nets)
    wins = sum(1 for x in nets if x > 0)
    raisons = {}
    for t in trades:
        raisons[t["raison"]] = raisons.get(t["raison"], 0) + 1
    pertes_tot = sum(-x for x in nets if x < 0)
    part_raison = {}
    for t in trades:
        if t["net"] < 0:
            part_raison[t["raison"]] = part_raison.get(t["raison"], 0) + (-t["net"])
    pire_part = max((v / pertes_tot for v in part_raison.values()), default=0.0)
    net_par_trade = total_net / n if n else 0.0
    crit = {
        "C1_n30": n >= 30,
        "C2_net_gt_frais": bool(n) and net_par_trade > FRAIS_AR,
        "C3_wr50": bool(n) and wins / n > 0.50,
        "C4_pertes": pire_part <= 0.40,
    }
    verdict = "PASS" if all(crit.values()) else "ÉCHEC"
    res = {
        "ts": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "spec": "VARIANTE 4H GO superviseur 17/09 : bougies 4H, entrée 2/3 confirmations "
                "(C1 funding>avg30 · C3 flux±5×chg4h±0.5% · C4 chg4h vs ±σ4h), veto "
                "négatif seul (funding<=0), garde-fous None, masque R2 conservé",
        "fenetre": f"{jours_tri[0]} -> {FIN_FENETRE} (bougies 4H)",
        "indispo_gardes_fous": indispo,
        "refus": refus,
        "raisons_sortie": raisons,
        "trades": trades,
        "stats": {"n": n, "wins": wins, "wr": round(wins / n, 3) if n else None,
                  "brut": round(sum(t["brut"] for t in trades), 2),
                  "frais": round(FRAIS_AR * n, 2), "net": round(total_net, 2),
                  "net_par_trade": round(net_par_trade, 2),
                  "part_pire_raison": round(pire_part, 3)},
        "criteres": crit,
        "verdict": verdict,
    }
    OUT_JSON.write_text(json.dumps(res, indent=2, ensure_ascii=False))
    return res

if __name__ == "__main__":
    r = run()
    s = r["stats"]
    print("═══ RÉSUMÉ VARIANTE 4H ═══")
    print(f"trades (n)        : {s['n']}")
    print(f"PnL brut          : {s['brut']} $")
    print(f"PnL net (frais AR): {s['net']} $")
    print(f"win-rate          : {s['wr']}")
    print(f"raisons de sortie : {r['raisons_sortie']}")
    print(f"refus             : {r['refus']}")
    print(f"indispo (None-safe): {r['indispo_gardes_fous']}")
    print(f"verdict           : {r['verdict']}  · critères: {r['criteres']}")
    print(f"-> {OUT_JSON}")
