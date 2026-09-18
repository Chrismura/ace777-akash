#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""v2_duo_replay_4h.py — SIMULATION DUO ORIGINEL (BETA Scout + ALPHA Hunter Revenge)
sur signaux V2 4H. GO superviseur Christophe 17/09. Zéro ordre, zéro euro.
L'original scellé v2_confirmation_replay.py n'est PAS modifié. Le champion lu :
LE_VRAI_CHAMPION_CERTIFIE_37FCA367.txt (SHA 7d1ed5f6… = copie scellée 01/09).

SPÉCIFICATION FIGÉE AVANT LE RUN (directive superviseur 17/09 + règles originelles) :
  SIGNAL D'ENTRÉE (V2 4H) : régime macro 1D (SMA 50/200 causale sur clôtures
     journalières) + au moins 2 confirmations/3 au sens de la directive :
       G1 funding > avg30 (sens = celui du régime)
       G2 flux baleines 48 h ≥ +5 BTC (LONG) / ≤ −5 BTC (SHORT)
       G3 chute 4H ≤ −0,5 % (LONG) / hausse 4H ≥ +0,5 % (SHORT)
     Les 2+ confirmations doivent être ACCORDÉES sur le même sens (conflit →
     silence, compté). LONG seulement si HAUSSIER, SHORT seulement si BAISSIER.
     None-safe : porte indisponible ≠ porte fausse ; le compte se fait sur les
     portes DISPONIBLES (masque R2 flux avant 14/08 conservé → porte indispo).
     VETO négatif seul (règle du GO 4H précédent, maintenue) : funding ≤ 0 → rien.
     Décision à la clôture 4H, exécution à l'ouverture de la bougie suivante.
  DUO ORIGINEL (règles du champion certifié, lignes citées) :
     BETA SCOUT : engagement 200 $ (BUY_USDT_BETA l.68). Stop-Loss 16 bps
        (STOP_LOSS_BPS l.55). Sortie en gain : trailing σ4h (arm 1,0σ, giveback
        0,4σ — convention maison, directive « trailing σ »). Sorties vérifiées
        DÈS la bougie d'entrée ; ordre pessimiste (SL avant trailing). Pas de
        shock ni de filet (non spécifiés par la directive Duo). fin_fenetre si
        encore ouvert à la fin.
     ALPHA HUNTER REVENGE : si et seulement si le Scout ferme en PERTE PAR
        STOP-LOSS (DUO_HUNTER_REQUIRE_STOP_LOSS=TRUE l.320 ; directive), le
        Hunter entre DANS LES 120 s (= à l'instant, résolution 4H) au PRIX DU
        STOP du Scout, à 800 $ (directive ; le « ×1,5 » = DUO_HUNTER_REVENGE_MULT
        l.318, 800/200=4× nominal — le chiffre concret de la directive gagne),
        dans le sens OPPOSÉ au Scout (DUO_FORCE_OPPOSITE=TRUE l.321 — capturer
        l'impulsion qui a stoppé le Scout).
        Sorties (durée originelle DUO_HUNTER_MAX_HOLD_SEC=240 s < 1 bougie 4H →
        tout se joue DANS la bougie d'entrée) :
          - hard stop 2×16 = 32 bps contre (DUO_HUNTER_HARD_STOP_MULT=2.0 l.323)
          - trail agressif arm +2 bps / giveback +1 bp
            (DUO_HUNTER_AGGR_TRAIL_ARM_BPS=2 / GIVEBACK_BPS=1 l.334-335)
          - sinon clôture de la bougie d'entrée (proxy de la durée max)
        Ordre pessimiste : hard stop vérifié avant trail.
  ÉCONOMIE : frais 16 bps AR → Scout 0,32 $ · Hunter 1,28 $ (directive).
  UNE POSITION À LA FOIS (Scout ou Hunter). Le Hunter ne tire qu'une fois par
     stop du Scout. Pas de nouvelle entrée sur une bougie occupée.
  VERDICT PRÉ-ENREGISTRÉ (critères maison, appliqués au COMBINÉ) :
     C1 n_total ≥ 30 · C2 net/trade > frais/trade · C3 WR combiné > 50 % ·
     C4 aucune cause de sortie > 40 % des pertes totales → PASS sinon ÉCHEC.
     Pas de 3e verdict.
"""
import json
import math
import statistics
import subprocess
from datetime import datetime, timedelta, timezone
from pathlib import Path

# ------------------------- constantes figées -------------------------
NOTIONNEL_SCOUT = 200.0
NOTIONNEL_HUNTER = 800.0
FRAIS_SCOUT = 0.32            # 16 bps AR sur 200 $
FRAIS_HUNTER = 1.28           # 16 bps AR sur 800 $
SL_SCOUT_BPS = 16.0           # STOP_LOSS_BPS (l.55)
HARD_STOP_MULT = 2.0          # DUO_HUNTER_HARD_STOP_MULT (l.323)
TRAIL_ARM_BPS = 2.0           # DUO_HUNTER_AGGR_TRAIL_ARM_BPS (l.334)
TRAIL_GIVE_BPS = 1.0          # DUO_HUNTER_AGGR_TRAIL_GIVEBACK_BPS (l.335)
SIGMA_ARM, SIGMA_GIVEBACK = 1.0, 0.4          # trailing σ du Scout (directive)
SEUIL_FLUX_BTC = 5.0
CHG4H_PCT = 0.5               # chute/hausse 4H en %
VETO_FUNDING_NEG = 0.0
FLUX_FIABLE_DES = "2026-08-14"
FIN_FENETRE = "2026-09-12"
SPOT_URL = "https://api.binance.com/api/v3/klines"
FUT_URL = "https://fapi.binance.com/fapi/v1/klines"
FUND_URL = "https://fapi.binance.com/fapi/v1/fundingRate"
BASE = Path.home() / "ace777-test-day1"
OUT_JSON = BASE / "Index_Maison/thermo/v2_duo_replay_4h_resultat.json"

# ------------------------- acquisition (identique variante 4H) -------
def http_json(url, tag):
    h = str(abs(hash(url)))[:12]
    cache = Path("/tmp") / f"v2duo_{tag}_{h}.json"
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
    """Copie fidèle de l'original scellé (dédup txid, direction vs registre)."""
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
def simuler_duo(kl4h, fund, evts, i_debut=1, i_fin=None):
    """Cœur PUR de la simulation duo (aucune E/S). Les indicateurs restent
    CAUSAUX (calculés sur le passé seul) ; seule la boucle de trading est bornée
    à [i_debut, i_fin). i_fin=None => fin de série.

    Extrait de run() le 18/09 (P1 du plan ACE) pour permettre le walk-forward et
    la mesure de drawdown. REFACTOR SANS CHANGEMENT DE COMPORTEMENT : la sortie
    sur la série complète est identique au JSON scellé E32 (vérifié par diff)."""
    if i_fin is None:
        i_fin = len(kl4h)
    clos_par_jour = {}
    for k in kl4h:
        clos_par_jour[jour_de(k["t"])] = k["c"]
    jours_tri = sorted(clos_par_jour)
    def sma(n, avant_jour):
        vals = [clos_par_jour[j] for j in jours_tri if j < avant_jour][-n:]
        return sum(vals) / len(vals) if len(vals) == n else None

    rets4h = [math.log(kl4h[i]["c"] / kl4h[i - 1]["c"]) for i in range(1, len(kl4h))]
    def sigma4h(i):
        seg = rets4h[max(0, i - 180):i]
        return statistics.pstdev(seg) if len(seg) >= 120 else None

    scouts, hunters = [], []
    pos = None                      # scout ouvert
    indispo = {"flux_masque": 0, "funding_absent": 0}
    refus = {"veto_funding_neg": 0, "conflit_direction": 0,
             "confirmations_insuffisantes": 0, "regime_neutre": 0}
    chasseur_tirs = {"tires": 0, "pas_tires_sans_stop": 0}

    def cloture_scout(i, px, raison):
        """ferme le scout ; tire le Hunter si stop-loss (même bougie)."""
        nonlocal pos
        s = pos
        brut = s["dir"] * (px - s["entree"]) / s["entree"] * NOTIONNEL_SCOUT
        scouts.append({"entree_t": s["t_entree"], "sortie_t": kl4h[i]["t"],
                       "side": "LONG" if s["dir"] > 0 else "SHORT",
                       "entree": s["entree"], "sortie": px,
                       "brut": round(brut, 2), "frais": FRAIS_SCOUT,
                       "net": round(brut - FRAIS_SCOUT, 2), "raison": raison})
        pos = None
        if raison == "stop_loss":
            chasseur_tirs["tires"] += 1
            hunter(s, i, px)

    def hunter(s, i, p0):
        """ALPHA : sens opposé, 800 $, dans la bougie du stop (règles originelles).
        giveback = 1 bp EN ARIÈRE depuis le meilleur prix (fill dans la bougie)."""
        k = kl4h[i]
        d = -s["dir"]
        # BUG CORRIGÉ (20:27Z) : le hard stop se déclenche quand le prix va CONTRE
        # la position → prix de stop = p0 × (1 − d×32bps) : en DESSOUS pour un LONG,
        # AU-DESSUS pour un SHORT. L'ancien signe (+) déclenchait le stop dans le
        # sens FAVORABLE et fabriquait un gain garanti de 32 bps par trade
        # (artefact : brut = 47 × 2,56 $ exactement, WR 1.0). Tableau précédent INVALIDE.
        dur = (1 - d * HARD_STOP_MULT * SL_SCOUT_BPS / 10000.0)      # hard stop (contre)
        arm = (1 + d * TRAIL_ARM_BPS / 10000.0)                      # arm trail
        gvb = (1 - d * TRAIL_GIVE_BPS / 10000.0)                     # giveback (ARRIÈRE)
        if d < 0:   # SHORT (sortie = rachat, giveback AU-DESSUS du plus bas)
            if k["h"] >= p0 * dur:
                px = p0 * dur
            elif k["l"] <= p0 * arm:
                px = k["l"] * gvb if k["l"] * gvb <= k["h"] else k["c"]
            else:
                px = k["c"]
        else:       # LONG (sortie = vente, giveback EN DESSOUS du plus haut)
            if k["l"] <= p0 * dur:
                px = p0 * dur
            elif k["h"] >= p0 * arm:
                px = k["h"] * gvb if k["h"] * gvb >= k["l"] else k["c"]
            else:
                px = k["c"]
        brut = d * (px - p0) / p0 * NOTIONNEL_HUNTER
        hunters.append({"entree_t": k["t"], "side": "LONG" if d > 0 else "SHORT",
                        "entree": p0, "sortie": px, "brut": round(brut, 2),
                        "frais": FRAIS_HUNTER, "net": round(brut - FRAIS_HUNTER, 2),
                        "raison": "hard_stop" if px == p0 * dur else
                                  ("trail_agressif" if px != k["c"] else "close_bougie"),
                        "scout_stop_t": s["t_entree"]})

    for i in range(i_debut, i_fin):
        k = kl4h[i]
        jour = jour_de(k["t"])
        # ---- gestion du Scout ouvert (sorties dès la bougie d'entrée) ----
        if pos:
            s = pos
            if s["dir"] > 0:
                stop_px = s["entree"] * (1 - SL_SCOUT_BPS / 10000.0)
                if k["l"] <= stop_px:                       # pessimiste : SL d'abord
                    cloture_scout(i, stop_px, "stop_loss")
                else:
                    s["mfp"] = max(s["mfp"], k["h"])
                    if s["mfp"] >= s["arm"] and s["mfp"] - SIGMA_GIVEBACK * s["sig_px"] >= k["l"]:
                        cloture_scout(i, s["mfp"] - SIGMA_GIVEBACK * s["sig_px"], "trailing")
            else:
                stop_px = s["entree"] * (1 + SL_SCOUT_BPS / 10000.0)
                if k["h"] >= stop_px:
                    cloture_scout(i, stop_px, "stop_loss")
                else:
                    s["mfp"] = min(s["mfp"], k["l"])
                    if s["mfp"] <= s["arm"] and s["mfp"] + SIGMA_GIVEBACK * s["sig_px"] <= k["h"]:
                        cloture_scout(i, s["mfp"] + SIGMA_GIVEBACK * s["sig_px"], "trailing")
        # ---- décision à la clôture 4H (si à plat) ----
        if pos is None:
            a, b = sma(50, jour), sma(200, jour)
            regime = ("HAUSSIER" if (a and b and a > b) else
                      "BAISSIER" if (a and b) else None)
            if regime is None:
                refus["regime_neutre"] += 1
                continue
            dernier_f, avg30 = funding_etat(fund, k["t"])
            s4h = sigma4h(i)
            chg4h = (k["c"] / kl4h[i - 1]["c"] - 1) * 100.0
            masque = jour < FLUX_FIABLE_DES
            if dernier_f is not None and dernier_f <= VETO_FUNDING_NEG:
                refus["veto_funding_neg"] += 1
                continue
            votes = []                        # portes DISPONIBLES qui votent
            if dernier_f is not None and avg30 is not None:
                votes.append(("LONG" if regime == "HAUSSIER" else "SHORT"))     # G1
            else:
                indispo["funding_absent"] += 1
            if not masque:
                net48 = flux_net_48h(evts, k["t"])
                if net48 >= SEUIL_FLUX_BTC:
                    votes.append("LONG")
                elif net48 <= -SEUIL_FLUX_BTC:
                    votes.append("SHORT")
            else:
                indispo["flux_masque"] += 1
            if chg4h <= -CHG4H_PCT:
                votes.append("LONG")
            elif chg4h >= CHG4H_PCT:
                votes.append("SHORT")
            nl, ns = votes.count("LONG"), votes.count("SHORT")
            if nl >= 2 and ns >= 2:
                refus["conflit_direction"] += 1
                continue
            sens = "LONG" if nl >= 2 else ("SHORT" if ns >= 2 else None)
            if sens is None:
                refus["confirmations_insuffisantes"] += 1
                continue
            if sens == "LONG" and regime != "HAUSSIER":
                continue
            if sens == "SHORT" and regime != "BAISSIER":
                continue
            e = kl4h[i + 1] if i + 1 < i_fin else None
            if e is None:
                break
            d = 1 if sens == "LONG" else -1
            sig_px = (s4h or 0.0) * e["o"]
            pos = {"dir": d, "t_entree": e["t"], "i_entree": i + 1,
                   "entree": e["o"], "sig_px": sig_px, "mfp": e["o"],
                   "arm": e["o"] + d * SIGMA_ARM * sig_px}
    if pos:
        k = kl4h[i_fin - 1]
        cloture_scout(i_fin - 1, k["c"], "fin_fenetre")

    return {"scouts": scouts, "hunters": hunters, "indispo": indispo,
            "refus": refus, "chasseur": chasseur_tirs}


def run():
    kl4h = fetch_4h()
    fund = fetch_funding()
    evts = charger_flux()
    sim = simuler_duo(kl4h, fund, evts)
    scouts, hunters = sim["scouts"], sim["hunters"]
    indispo, refus, chasseur_tirs = sim["indispo"], sim["refus"], sim["chasseur"]

    # ------------------------- verdict mécanique -------------------------
    def resume(trades):
        n = len(trades)
        nets = [t["net"] for t in trades]
        wins = sum(1 for x in nets if x > 0)
        return {"n": n, "brut": round(sum(t["brut"] for t in trades), 2),
                "frais": round(sum(t["frais"] for t in trades), 2),
                "net": round(sum(nets), 2),
                "wr": round(wins / n, 3) if n else None}
    sc, hu = resume(scouts), resume(hunters)
    n_tot = sc["n"] + hu["n"]
    brut_tot = round(sc["brut"] + hu["brut"], 2)
    net_tot = round(sc["net"] + hu["net"], 2)
    frais_tot = round(sc["frais"] + hu["frais"], 2)
    wins_tot = sum(1 for t in scouts + hunters if t["net"] > 0)
    wr_tot = round(wins_tot / n_tot, 3) if n_tot else None
    pertes_tot = sum(-t["net"] for t in scouts + hunters if t["net"] < 0)
    part = {}
    for t in scouts + hunters:
        if t["net"] < 0:
            part[t["raison"]] = part.get(t["raison"], 0) + (-t["net"])
    pire = max((v / pertes_tot for v in part.values()), default=0.0)
    crit = {"C1_n30": n_tot >= 30,
            "C2_net_par_trade_gt_frais": bool(n_tot) and (net_tot / n_tot) > (frais_tot / n_tot),
            "C3_wr50": bool(n_tot) and wins_tot / n_tot > 0.50,
            "C4_pertes": pire <= 0.40}
    verdict = "PASS" if all(crit.values()) else "ÉCHEC"
    res = {"ts": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
           "spec": "DUO ORIGINEL (BETA 200$ SL16bps trail σ4h · ALPHA 800$ sens opposé "
                   "hard-stop 32bps trail 2/1bps) sur signaux V2 4H (2/3 : funding/flux/chute), "
                   "veto funding<=0, None-safe, frais 16bps AR — GO superviseur 17/09",
           "scout": sc, "hunter": hu,
           "combine": {"n": n_tot, "brut": brut_tot, "frais": frais_tot,
                       "net": net_tot, "wr": wr_tot},
           "chasseur": chasseur_tirs,
           "pertes_par_raison": {k: round(v, 2) for k, v in part.items()},
           "indispo": indispo, "refus": refus,
           "criteres": crit, "verdict": verdict,
           "trades_scout": scouts, "trades_hunter": hunters}
    OUT_JSON.write_text(json.dumps(res, indent=2, ensure_ascii=False))
    return res

if __name__ == "__main__":
    r = run()
    print("═══ RÉSUMÉ DUO ORIGINEL (Scout + Hunter Revenge) ═══")
    print(f"BETA Scout   : n={r['scout']['n']} · brut {r['scout']['brut']} $ · net {r['scout']['net']} $ · WR {r['scout']['wr']}")
    print(f"ALPHA Hunter : n={r['hunter']['n']} · brut {r['hunter']['brut']} $ · net {r['hunter']['net']} $ · WR {r['hunter']['wr']}")
    print(f"COMBINÉ      : n={r['combine']['n']} · brut {r['combine']['brut']} $ · frais {r['combine']['frais']} $ · net {r['combine']['net']} $ · WR {r['combine']['wr']}")
    print(f"chasseur     : {r['chasseur']}")
    print(f"pertes/raison: {r['pertes_par_raison']}")
    print(f"refus        : {r['refus']} · indispo: {r['indispo']}")
    print(f"VERDICT      : {r['verdict']} · critères: {r['criteres']}")
    print(f"-> {OUT_JSON}")
