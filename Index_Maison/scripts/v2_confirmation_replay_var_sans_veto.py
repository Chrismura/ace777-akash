#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""v2_confirmation_replay_var_sans_veto.py — VARIANTE v3 (DÉCISIONS SUPERVISEUR 17/09 :
D3 « À SIMPLIFIER » → veto funding SUPPRIMÉ). Zéro ordre, zéro euro.

SPÉCIFICATION FIGÉE AVANT LE RUN : identique à la spec scellée du 12/09 SAUF :
  VETO ZONE MORTE SUR FUNDING = SUPPRIMÉ. Justification (décision du propriétaire) :
  la Porte C1 exige déjà funding > avg30 ; un veto sur la même mesure est redondant
  et ne peut que restreindre davantage. AUCUN autre changement.
NOTE D'EXÉCUTION (consignée avant le run) : mathématiquement identique à la variante
E29 (avg30×1.2) pour ce replay — tout chemin d'entrée exige avg30 non nul, donc le
fallback 0.0001 est inatteignable en pratique. Prédiction : mêmes chiffres qu'E29.
Aucun autre paramètre modifié. Originaux scellés INTACTS (demande D2 en suspens).

ENTRÉE (aucune horloge — seulement des mesures concordantes) :
  G  régime de fond P1 (SMA hebdo 50/200, règle du moteur_paternes_btc l.67) :
     LONG seulement si HAUSSIER, SHORT seulement si BAISSIER, sinon silence.
  F1a croisement C1 régime×levier : LONG si funding > funding_avg30
     (branche taker<1 du C1 non reconstructable gratuitement → masquée, R3).
  F1b croisement C3 onchain×prix : LONG si net_btc(48h) ≥ +5 ET chg24 ≤ −1%
     (achat pendant baisse) ; SHORT si net_btc ≤ −5 ET chg24 ≥ +1% (distribution).
  RÈGLE D'ENTRÉE : G + 2 confirmations parmi {F1a, F1b, F2, F3}, dont au moins
     une F1. En replay, F2/F3 sont masquées (règles R1/R3) → il faut F1a ET F1b
     concordantes. Si les 2 sources ne tirent pas ensemble : silence.
  VETO zone morte (règle 31/08 du C2) : funding < seuil (défaut 0.0002,
     justesse_cockpit.json zone_morte.seuil_funding) → AUCUN trade.

SORTIES (aucun timer — seulement des mesures) :
  S1 trailing σ : σ = écart-type des rendements journaliers sur 30 jours clos ;
     arm quand le prix atteint entrée ± 1.0σ ; sortie au giveback 0.4σ
     (convention maison arm σ×1.0 / giveback σ×0.4, vérifiée 10/09).
  S2 shock-inversion : clôture journalière contre le sens ≥ 2σ → sortie.
  S3 invalidation : la source qui a confirmé se retourne 2 jours de décision
     consécutifs → sortie à l'ouverture du jour suivant.
  FILET : hold max 72 h (sortie à l'ouverture du 4e jour) — sécurité, jamais
     la sortie prévue.

MASQUES PRÉ-ENREGISTRÉS (honnêteté sur la profondeur des données, constatée
à la source le 12/09 AVANT le run) :
  R1 OFI (F2) : ofi_historique.jsonl commence le 08/09 → F2 masquée sur TOUTE
     la fenêtre replay. L'essai ne teste PAS F2.
  R2 Flux (F3/F1b) : ledger whales_mouvements.jsonl n'est fiable qu'à partir
     du 14/08 (documenté dans flux_nets_exchanges.py) → F1b masquée avant le
     14/08. Déductions : txid unique, événement daté à la PREMIÈRE détection.
  R3 C2 « purge unilatérale » : historique de liquidations gratuit inexistant
     → branche masquée ; seul le VETO zone morte (funding) reste actif.
  Le funding réel vient de l'endpoint public /fapi/v1/fundingRate (historique
  8 h, gratuit) — c'est la mesure du levier nommée au dossier, pas un nouvel
  instrument.

RÈGLE D'INTERPRÉTATION PRÉ-ENREGISTRÉE (avant tout résultat) :
  Le verdict est celui des critères check_edge_criteria (MIN_TRADES=30 cumulé,
  net/trade > frais/trade, WR net > 50 %, aucune raison > 40 % des pertes),
  sans 3e verdict. SI échec ET si TOUS les trades viennent de la fenêtre non
  masquée ET n < 30, le verdict reste ÉCHEC et une clause est enregistrée
  automatiquement : « hypothèse fenêtrée jamais mise à l'épreuve (données
  trop courtes) » — clause constatée par la machine, jamais par un humain
  après coup.

CONVENTIONS ÉCONOMIQUES (identiques à V2-REPLAY pour comparabilité) :
  Notionnel 1 125 $ · frais 8 bps taker par côté (1,80 $ aller-retour) ·
  décision à 00h00 UTC sur données closes · exécution à l'ouverture du jour ·
  une position à la fois · pas de ré-entrée le jour d'une sortie.
"""
import csv
import io
import json
import math
import statistics
import subprocess
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

# ------------------------- constantes figées -------------------------
NOTIONNEL = 1125.0
FRAIS_AR = NOTIONNEL * 0.0008 * 2          # 1.80 $
SIGMA_ARM = 1.0
SIGMA_GIVEBACK = 0.4
SIGMA_SHOCK = 2.0
HOLD_MAX_J = 3                              # 72 h = 3 jours pleins
SEUIL_FLUX_BTC = 5.0                        # moteur P2 l.50
CHG24_MIN = 1.0                             # % — moteur P2 l.132
ZONE_MORTE_DEF = 0.0002                     # défaut C2, l.201 (INUTILISÉ dans cette variante — veto relatif)
FLUX_FIABLE_DES = "2026-08-14"              # R2
FIN_FENETRE = "2026-09-12"                  # jour de l'essai exclu
SPOT_URL = "https://api.binance.com/api/v3/klines"
FUT_URL = "https://fapi.binance.com/fapi/v1/klines"
FUND_URL = "https://fapi.binance.com/fapi/v1/fundingRate"
BASE = Path.home() / "ace777-test-day1"
OUT_JSON = BASE / "Index_Maison/thermo/v2_confirmation_resultat_sans_veto.json"

# ------------------------- acquisition (couche data, pas stratégie) --
def http_json(url, tag):
    h = str(abs(hash(url)))[:12]
    cache = Path("/tmp") / f"v2conf_{tag}_{h}.json"
    if cache.exists():
        return json.loads(cache.read_text())
    last = None
    for u in (url,):
        r = subprocess.run(["curl", "-s", "-m", "25", u],
                           capture_output=True, text=True, timeout=30)
        try:
            data = json.loads(r.stdout)
        except Exception:
            last = RuntimeError(f"rc={r.returncode} {r.stdout[:100]!r}")
            continue
        if isinstance(data, list):
            cache.write_text(json.dumps(data))
            return data
        last = RuntimeError(r.stdout[:160])
    raise last or RuntimeError("acquisition KO")

def fetch_daily(days):
    """Bougies 5m -> jours (spot, repli futures). Retour (jours, klines_par_jour)."""
    end = int(datetime(2026, 9, 12, tzinfo=timezone.utc).timestamp() * 1000)
    start = int((datetime(2026, 9, 12, tzinfo=timezone.utc)
                 - timedelta(days=days)).timestamp() * 1000)
    kl = []
    cursor = start
    while cursor < end:
        q = f"?symbol=BTCUSDT&interval=5m&startTime={cursor}&limit=1000"
        chunk = None
        for base in (SPOT_URL, FUT_URL):
            try:
                chunk = http_json(base + q, "kl")
                if chunk:
                    break
            except Exception:
                chunk = None
        if not chunk:
            raise RuntimeError("klines indisponibles")
        kl.extend(chunk)
        cursor = chunk[-1][6] + 1
        if len(chunk) < 1000:
            break
    jours = {}
    for k in kl:
        d = datetime.fromtimestamp(k[0] / 1000, timezone.utc).strftime("%Y-%m-%d")
        jours.setdefault(d, []).append(k)
    out = []
    for d in sorted(jours):
        b = jours[d]
        out.append({"jour": d, "o": float(b[0][1]), "h": max(float(x[2]) for x in b),
                    "l": min(float(x[3]) for x in b), "c": float(b[-1][4])})
    return out, jours

def fetch_funding():
    """Historique de funding réel (fapi, 8 h). Retour liste (ts_iso, rate)."""
    data = http_json(FUND_URL + "?symbol=BTCUSDT&limit=1000", "fund")
    return [(datetime.fromtimestamp(x["fundingTime"] / 1000, timezone.utc)
             .strftime("%Y-%m-%dT%H:%M:%SZ"), float(x["fundingRate"])) for x in data]

# ------------------------- données maison (lecture seule) ------------
def charger_flux():
    """Ledger dédup par txid, direction vs registre exchange (règle
    flux_nets_exchanges.py). Retour liste d'événements {ts, net_dir, btc}."""
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

def charger_seuil_zone_morte():
    try:
        jm = json.loads((BASE / "Index_Maison/scripts/justesse_cockpit.json").read_text())
        return float(((jm.get("zone_morte") or {}).get("seuil_funding")) or ZONE_MORTE_DEF)
    except Exception:
        return ZONE_MORTE_DEF

# ------------------------- instruments reconstruits (causaux) --------
def regime_par_jour(jours):
    """SMA hebdo 50/200 sur l'historique COMPLET, évaluée causalement :
    le régime du jour i n'utilise que les clôtures ≤ i-1 (règle moteur l.67)."""
    closes = [j["c"] for j in jours]
    # bougies hebdo (7 clôtures journalières approx = convention simple figée)
    week = [closes[max(0, i - 6):i + 1] for i in range(len(closes))]
    s50, s200 = [], []
    for i in range(len(closes)):
        w = closes[:i]                     # clôtures STRICTEMENT avant i
        s50.append(sum(w[-350:]) / min(len(w), 350) if w else None)
        s200.append(sum(w[-1400:]) / min(len(w), 1400) if w else None)
    del week
    return s50, s200

def funding_etat(fund, jour):
    """(dernier funding ≤ jour, moyenne 30 j glissante avant) — causal."""
    prec = [r for t, r in fund if t[:10] < jour]
    if not prec:
        return None, None
    dernier = prec[-1]
    avg30 = statistics.mean(prec[-90:]) if len(prec) >= 10 else None
    return dernier, avg30

def flux_net_48h(evts, jour):
    """Net BTC 48 h avant le jour J (événements datés première détection)."""
    d1 = datetime.strptime(jour, "%Y-%m-%d").replace(tzinfo=timezone.utc)
    d0 = d1 - timedelta(days=2)
    net = 0.0
    for e in evts:
        try:
            t = datetime.strptime(e["ts"][:19], "%Y-%m-%dT%H:%M:%S").replace(tzinfo=timezone.utc)
        except Exception:
            continue
        if d0 <= t < d1:
            if e["dir"] == "SORTANT":
                net -= e["btc"]
            elif e["dir"] == "ENTRANT":
                net += e["btc"]
    return net

# ------------------------- simulation --------------------------------
def run():
    jours, kl_jours = fetch_daily(200)
    fund = fetch_funding()
    evts = charger_flux()
    seuil_zm = charger_seuil_zone_morte()
    s50, s200 = regime_par_jour(jours)
    sigmas = [None] * len(jours)
    for i in range(31, len(jours)):
        rets = [math.log(jours[k]["c"] / jours[k - 1]["c"])
                for k in range(i - 30, i)]
        sigmas[i] = statistics.pstdev(rets)

    flux_masque_avant = FLUX_FIABLE_DES
    trades, pos, compteur_masks = [], None, {"r1_ofi": "masqué sur toute la fenêtre",
                                             "r2_flux_avant_14_08": 0,
                                             "r3_c2_purge": "masquée (branche trigger)"}

    def fermer(k, px, raison):
        nonlocal pos
        brut = pos["dir"] * (px - pos["entree"]) / pos["entree"] * NOTIONNEL
        trades.append({"entree_j": pos["jour"], "sortie_j": k["jour"], "side":
                       "LONG" if pos["dir"] > 0 else "SHORT", "entree": pos["entree"],
                       "sortie": px, "brut": round(brut, 2), "frais": round(FRAIS_AR, 2),
                       "net": round(brut - FRAIS_AR, 2), "raison": raison})
        pos = None

    for i in range(31, len(jours)):
        j = jours[i]
        jour = j["jour"]
        if jour >= FIN_FENETRE:
            break
        # ---- sorties d'abord (position existante) ----
        if pos:
            held = i - pos["i"]
            if held >= HOLD_MAX_J:
                fermer(j, j["o"], "filet_72h")
            elif pos["sortie_suivant_invalidation"]:
                fermer(j, j["o"], "invalidation")
                pos = None
            else:
                s = pos["sigma_px"]
                if pos["dir"] > 0:
                    pos["mfp"] = max(pos["mfp"], j["h"])
                    if pos["mfp"] >= pos["arm"] and pos["mfp"] - SIGMA_GIVEBACK * s >= j["l"]:
                        fermer(j, max(j["l"], pos["mfp"] - SIGMA_GIVEBACK * s), "trailing")
                    elif (j["c"] - jours[i - 1]["c"]) / jours[i - 1]["c"] <= -SIGMA_SHOCK * s:
                        fermer(j, j["c"], "shock_inversion")
                else:
                    pos["mfp"] = min(pos["mfp"], j["l"])
                    if pos["mfp"] <= pos["arm"] and pos["mfp"] + SIGMA_GIVEBACK * s <= j["h"]:
                        fermer(j, min(j["h"], pos["mfp"] + SIGMA_GIVEBACK * s), "trailing")
                    elif (j["c"] - jours[i - 1]["c"]) / jours[i - 1]["c"] >= SIGMA_SHOCK * s:
                        fermer(j, j["c"], "shock_inversion")
        # ---- décision à 00h00 (données ≤ i-1) — G + confirmations ----
        if pos is None and i > 31:
            regime = "HAUSSIER" if (s50[i] and s200[i] and s50[i] > s200[i]) else (
                     "BAISSIER" if (s50[i] and s200[i]) else None)
            dernier_f, avg30 = funding_etat(fund, jour)
            chg24 = (jours[i - 1]["c"] / jours[i - 2]["c"] - 1) * 100 if i >= 2 else 0.0
            masque_flux = jour < flux_masque_avant
            if masque_flux:
                compteur_masks["r2_flux_avant_14_08"] += 1
            net48 = 0.0 if masque_flux else flux_net_48h(evts, jour)
            confirm = {"sens": None, "c1": False, "c3": False, "preuves": []}
            if dernier_f is not None and avg30 is not None and not masque_flux:
                if regime == "HAUSSIER" and dernier_f > avg30:
                    confirm["c1"], confirm["sens"] = True, "LONG"
                    confirm["preuves"].append(f"C1 funding {dernier_f:.2e}>avg30 {avg30:.2e}")
                if net48 >= SEUIL_FLUX_BTC and chg24 <= -CHG24_MIN:
                    confirm["c3"] = True
                    confirm["sens"] = confirm["sens"] or "LONG"
                    confirm["preuves"].append(f"C3 flux {net48:+.1f} BTC + baisse {chg24:+.1f}%")
                if net48 <= -SEUIL_FLUX_BTC and chg24 >= CHG24_MIN:
                    confirm["c3"] = True
                    confirm["sens"] = "SHORT" if confirm["sens"] == "SHORT" or regime == "BAISSIER" else confirm["sens"]
                    confirm["preuves"].append(f"C3 flux {net48:+.1f} BTC + hausse {chg24:+.1f}%")
            # veto zone morte funding SUPPRIMÉ (décision superviseur D3 17/09) :
            # la porte C1 (funding > avg30) vérifie déjà cette mesure.
            # règle d'entrée : G + F1a ET F1b concordantes (R1/R3 masquent F2/F3)
            if confirm["c1"] and confirm["c3"] and confirm["sens"] == "LONG" and regime == "HAUSSIER":
                s = sigmas[i]
                pos = {"dir": 1, "jour": jour, "i": i, "entree": j["o"],
                       "sigma_px": s * j["o"], "mfp": j["o"],
                       "arm": j["o"] + SIGMA_ARM * s * j["o"],
                       "sortie_suivant_invalidation": False, "confirmations": confirm["preuves"]}
            elif confirm["c3"] and confirm["sens"] == "SHORT" and regime == "BAISSIER" and dernier_f is not None and avg30 is not None and dernier_f > avg30:
                s = sigmas[i]
                pos = {"dir": -1, "jour": jour, "i": i, "entree": j["o"],
                       "sigma_px": s * j["o"], "mfp": j["o"],
                       "arm": j["o"] - SIGMA_ARM * s * j["o"],
                       "sortie_suivant_invalidation": False, "confirmations": confirm["preuves"]}
        # ---- S3 : invalidation, détectée le jour suivant la bascule ----
        if pos:
            regime2 = "HAUSSIER" if (s50[i] and s200[i] and s50[i] > s200[i]) else "BAISSIER"
            bascule = (pos["dir"] > 0 and regime2 != "HAUSSIER") or (pos["dir"] < 0 and regime2 != "BAISSIER")
            pos["n_bascule"] = pos.get("n_bascule", 0) + (1 if bascule else 0)
            if pos.get("n_bascule", 0) >= 2:
                pos["sortie_suivant_invalidation"] = True
    if pos:
        j = jours[-1]
        fermer(j, j["c"], "fin_fenetre")

    # ------------------------- verdict mécanique -------------------------
    n = len(trades)
    nets = [t["net"] for t in trades]
    total_net = sum(nets)
    wins = sum(1 for x in nets if x > 0)
    pertes = [-x for x in nets if x < 0]
    pertes_tot = sum(pertes)
    part_raison = {}
    for t in trades:
        if t["net"] < 0:
            part_raison[t["raison"]] = part_raison.get(t["raison"], 0) + (-t["net"])
    pire_part = max((v / pertes_tot for v in part_raison.values()), default=0.0)
    crit = {
        "C1_n30": n >= 30,
        "C2_net_gt_frais": (n and (total_net / n) > (FRAIS_AR * n / n if n else 0) * 0 + (FRAIS_AR)) or False,
        "C3_wr50": n and wins / n > 0.50,
        "C4_pertes": pire_part <= 0.40,
    }
    net_par_trade = total_net / n if n else 0.0
    crit["C2_net_gt_frais"] = n and net_par_trade > FRAIS_AR
    verdict = "PASS" if all(crit.values()) else "ÉCHEC"
    clause = None
    if verdict == "ÉCHEC" and n < 30 and compteur_masks["r2_flux_avant_14_08"] > 0:
        nb_unmasked = sum(1 for t in trades if t["entree_j"] >= flux_masque_avant)
        if n == nb_unmasked:
            clause = ("hypothèse fenêtrée jamais mise à l'épreuve : tous les trades "
                      "viennent de la fenêtre non masquée (≥ 14/08) et n < 30 — "
                      "données trop courtes, constaté par la machine avant toute "
                      "lecture humaine (règle pré-enregistrée).")
    res = {
        "ts": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "spec": "VARIANTE v3 décisions superviseur 17/09 : veto funding SUPPRIMÉ (porte C1 funding>avg30 déjà présente) — reste = spec scellée 12/09",
        "masques": compteur_masks,
        "trades": trades,
        "stats": {"n": n, "wins": wins, "wr": round(wins / n, 3) if n else None,
                  "brut": round(sum(t["brut"] for t in trades), 2),
                  "frais": round(sum(t["frais"] for t in trades), 2),
                  "net": round(total_net, 2), "net_par_trade": round(net_par_trade, 2),
                  "part_pire_raison": round(pire_part, 3)},
        "criteres": crit,
        "verdict": verdict,
        "clause_pre_enregistree": clause,
    }
    OUT_JSON.write_text(json.dumps(res, indent=2, ensure_ascii=False))
    return res

if __name__ == "__main__":
    r = run()
    print(json.dumps({k: r[k] for k in ("ts", "verdict", "criteres", "stats", "clause_pre_enregistree")},
                     indent=2, ensure_ascii=False))
    print(f"\ntrades: {len(r['trades'])} -> {OUT_JSON}")
