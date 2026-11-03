#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""hack_actif_mesure.py — REGIME HACK_ACTIF SANS TIMING FIXE (GO 02/11, recâblé 03/11).

Mesure, 0 ordre, stdlib. Ecrit thermo/hack_actif.json.
Formule : niveau 0-3 mesuré, pas de date d'expiration.

03/11 (GO Christophe « go sur toute la ligne ») — corrections de la boucle source :
1. ÉQUITY ET CASH VRAIS : lit thermo/equity_reconcilie.json (le moteur et son
   journal ne disent pas le même chiffre : 797,21 $ vs 892,42 $ au 03/11).
   `cash_reel_usd` = cash du journal (194,10 $), `cash_cible_usd` = equity × pct,
   `cash_ecart_usd` = l'écart à combler. Avant : une cible de 399,52 $ annoncée
   sur un compte qui n'en portait pas la moitié.
2. QUANTILES AU LIEU DE CONSTANTES : funding (p80), L/S (p70), Fear (p30),
   alts↓ (p70) sont lus sur thermo/history.jsonl (n>=100 exigé). Si l'historique
   manque, repli explicite sur la valeur du 02/11 + drapeau `mesure=False` —
   jamais un défaut silencieux (R26).
3. LE SIGNAL QUI A VU LE 29/10 ENTRE DANS LE SCORE : murs L2 qui s'évaporent
   (aspiration_live : drop_*_pct_per_s) et dépôts exchange dominants
   (flux_nets_latest : btc_entrant > btc_sortant). Avant : dehors.
4. HISTORIQUE : chaque run ajoute une ligne à thermo/hack_actif_hist.jsonl
   (score, composantes, quantiles utilisés) — sans ça, les seuils de niveau
   ne pourront jamais être calibrés.

Entrées : flux_nets_latest.json · ofi_latest.json · veille_institutionnelle_etat.json
          geopol_gratuit_live.json · THERMO_DERNIER.md · history.jsonl
          mur_mesure.json · m_kelly_live.json · equity_reconcilie.json
          aspiration_live.json · PORTEFEUILLE_LATEST.md
Sortie : thermo/hack_actif.json (+ hack_actif_hist.jsonl)
"""
import json
import os
import re
from datetime import datetime, timezone

BASE = os.path.expanduser("~/ace777-test-day1")
INDEX = os.path.join(BASE, "Index_Maison")
THERMO = os.path.join(INDEX, "thermo")
DATA = os.path.join(INDEX, "data")
OUT = os.path.join(THERMO, "hack_actif.json")
HIST = os.path.join(THERMO, "hack_actif_hist.jsonl")
RUNS = os.path.join(BASE, "hulk-mexc", "runs")

HIST_THERMO = os.path.join(THERMO, "history.jsonl")
N_MIN_QUANTILE = 100
# Repli documenté (02/11) — utilisé SEULEMENT si l'historique est insuffisant,
# et alors `mesure=False` le dit à voix haute.
REPLI = {"funding": 0.00009, "ls": 2.0, "fear": 40.0, "alts_down": 65.0}
# Seuils en FRACTION du score maximum possible. Leçon du 03/11 : ajouter des
# composantes (dépôts, murs L2) à des seuils ABSOLUS a fait monter le score de
# 3,00 à 5,50 dès le premier run -> tout le monde en FORTRESSE sans que le
# marché ait changé. Le ratio est insensible à la taille de l'échelle ; les
# fractions elles-mêmes se calibreront sur thermo/hack_actif_hist.jsonl.
SEUILS_RATIO = {"fortresse": 0.75, "hack": 0.50, "vigilance": 0.25}
MAX_COMPOSANTES = {"flux": 2.0, "depots": 0.5, "ofi": 1.0, "foule": 1.0,
                   "fear": 1.0, "alts": 0.5, "veille": 2.0, "geopol": 1.0,
                   "murs_l2": 1.0}


def load_json(p, d=None):
    try:
        with open(p, encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return d if d is not None else {}


def lire_thermo():
    txt = ""
    try:
        txt = open(os.path.join(INDEX, "THERMO_DERNIER.md"), encoding="utf-8").read()
    except Exception:
        pass

    def grab(pat):
        m = re.search(pat, txt)
        return float(m.group(1)) if m else None

    return {"funding": grab(r"Funding \| ([-\d\.eE\+]+)"),
            "ls": grab(r"L/S 1h \| ([\d\.]+)"),
            "fear": grab(r"Fear & Greed (\d+)"),
            "alts_down": grab(r"Alts.*?([\d\.]+) ?%"),
            "btc24": grab(r"BTC 24h ([-\d\.]+)"),
            "txt": txt}


def quantiles():
    """p80 funding, p70 L/S, p30 Fear, p70 alts↓ sur thermo/history.jsonl."""
    vals = {"funding": [], "ls": [], "fear": [], "alts_down": []}
    try:
        with open(HIST_THERMO, encoding="utf-8", errors="ignore") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    r = json.loads(line)
                except Exception:
                    continue
                for cle_json, cle_out in (("funding", "funding"), ("longShort", "ls"),
                                          ("fearGreed", "fear"),
                                          ("panierDownPct", "alts_down")):
                    v = r.get(cle_json)
                    if v is not None:
                        try:
                            vals[cle_out].append(float(v))
                        except Exception:
                            pass
    except Exception:
        pass

    def q(v, p):
        v = sorted(v)
        if not v:
            return None
        i = min(len(v) - 1, max(0, int(round(p * (len(v) - 1)))))
        return v[i]

    out = {}
    for cle, p in (("funding", 0.80), ("ls", 0.70), ("fear", 0.30), ("alts_down", 0.70)):
        n = len(vals[cle])
        m = q(vals[cle], p) if n >= N_MIN_QUANTILE else None
        out[cle] = {"n": n, "p": p, "valeur": (round(m, 8) if m is not None else REPLI[cle]),
                    "mesure": m is not None}
    return out


def murs_l2():
    """Part des paires dont un des deux côtés de murs s'évapore (drop/s > 0)."""
    a = load_json(os.path.join(RUNS, "aspiration_live.json"), {})
    paires = a.get("paires") or {}
    tot = casse = 0
    for p in paires.values():
        if not isinstance(p, dict):
            continue
        d = p.get("max_drop_pct_per_s")
        if d is None:
            d = max(float(p.get("drop_bid_pct_per_s") or 0.0),
                    float(p.get("drop_ask_pct_per_s") or 0.0))
        tot += 1
        if float(d or 0.0) > 0.0:
            casse += 1
    return {"n": tot, "casse": casse,
            "pct": round(100.0 * casse / tot, 1) if tot else None,
            "ts": a.get("ts")}


def main():
    flux = load_json(os.path.join(DATA, "flux_nets_latest.json"), {})
    ofi = load_json(os.path.join(DATA, "ofi_latest.json"), {})
    veille = load_json(os.path.join(DATA, "veille_institutionnelle_etat.json"), {})
    geopol = load_json(os.path.join(THERMO, "geopol_gratuit_live.json"), {})
    mur = load_json(os.path.join(THERMO, "mur_mesure.json"), {})
    kelly = load_json(os.path.join(THERMO, "m_kelly_live.json"), {})
    recon = load_json(os.path.join(THERMO, "equity_reconcilie.json"), {})
    th = lire_thermo()
    qt = quantiles()
    l2 = murs_l2()

    signaux = []
    comp = {}
    score = 0.0

    # 1. Flux nets : seule preuve onchain gratuite d'un dépôt massif
    verdict = (flux.get("verdict") or "INCONNU").upper()
    if verdict == "DISTRIBUTION":
        score += 2; signaux.append("flux DISTRIBUTION +2 (dépôts dominants : possible vente)")
        comp["flux"] = 2
    elif verdict == "ACCUMULATION":
        signaux.append("flux ACCUMULATION +0")
        comp["flux"] = 0
    elif verdict == "EQUILIBRE":
        signaux.append("flux EQUILIBRE +0 (pas de dump visible)")
        comp["flux"] = 0
    else:
        signaux.append("flux %s +0 (fail-open, pas de conclusion)" % verdict)
        comp["flux"] = 0

    # 1bis. Dépôts exchange dominants (48h) — mesuré, pas un seuil inventé
    f48 = flux.get("fenetre_48h") or {}
    ent, sor = float(f48.get("btc_entrant") or 0), float(f48.get("btc_sortant") or 0)
    if ent + sor > 0 and ent > sor:
        score += 0.5
        signaux.append("dépôts exchange dominants 48h %.0f vs %.0f BTC +0.5" % (ent, sor))
        comp["depots"] = 0.5
    else:
        comp["depots"] = 0.0

    # 2. OFI vendeur (p95 mesuré 02/11 = -0.07)
    try:
        ofi_n = float(ofi.get("fenetre_globale", {}).get("ofi_norm", 0))
    except Exception:
        ofi_n = 0.0
    if ofi_n < -0.07:
        score += 1; signaux.append("OFI vendeur %.4f +1 (seuil p95 02/11)" % ofi_n)
        comp["ofi"] = 1
    else:
        signaux.append("OFI %.4f neutre +0" % ofi_n)
        comp["ofi"] = 0

    # 3. Foule piégée : funding >= p80 ET L/S >= p70 (mesurés)
    qf, ql = qt["funding"]["valeur"], qt["ls"]["valeur"]
    if th["funding"] is not None and th["ls"] is not None and th["funding"] >= qf and th["ls"] >= ql:
        score += 1
        signaux.append("foule longue piégée funding %s≥%.6f L/S %.2f≥%.2f +1"
                       % (th["funding"], qf, th["ls"], ql))
        comp["foule"] = 1
    else:
        signaux.append("foule OK +0 (funding %s / p80 %.6f · L/S %s / p70 %.2f)"
                       % (th["funding"], qf, th["ls"], ql))
        comp["foule"] = 0

    # 4. Fear + breadth (quantiles)
    if th["fear"] is not None and th["fear"] <= qt["fear"]["valeur"]:
        score += 1
        signaux.append("Fear %.0f ≤ p30 %.0f +1" % (th["fear"], qt["fear"]["valeur"]))
        comp["fear"] = 1
    else:
        comp["fear"] = 0
    if th["alts_down"] is not None and th["alts_down"] >= qt["alts_down"]["valeur"]:
        score += 0.5
        signaux.append("alts↓ %.0f%% ≥ p70 %.0f%% +0.5"
                       % (th["alts_down"], qt["alts_down"]["valeur"]))
        comp["alts"] = 0.5
    else:
        comp["alts"] = 0.0

    # 5. Institutionnel
    n_act = len(veille.get("signaux_actifs", [])) if isinstance(veille.get("signaux_actifs"), list) else 0
    if n_act > 0:
        score += min(2, n_act)
        signaux.append("veille %d signaux +%d" % (n_act, min(2, n_act)))
        comp["veille"] = min(2, n_act)
    else:
        signaux.append("veille SURVEILLANCE +0")
        comp["veille"] = 0

    # 6. Géopol : contexte, jamais déclencheur seul
    try:
        gscore = float(geopol.get("notre_geopol", {}).get("score", 0))
    except Exception:
        gscore = 0.0
    if gscore >= 0.5:
        score += 1; comp["geopol"] = 1
        signaux.append("geopol %.4f +1" % gscore)
    elif gscore >= 0.3:
        score += 0.5; comp["geopol"] = 0.5
        signaux.append("geopol attention %.4f +0.5" % gscore)
    else:
        comp["geopol"] = 0.0
        signaux.append("geopol %.4f +0" % gscore)

    # 7. MURS L2 QUI S'ÉVAPORENT (le signal du 29/10, mesuré maison)
    if l2["pct"] is not None:
        if l2["pct"] >= 30.0:
            score += 1; comp["murs_l2"] = 1
        elif l2["pct"] >= 15.0:
            score += 0.5; comp["murs_l2"] = 0.5
        else:
            comp["murs_l2"] = 0.0
        signaux.append("murs L2 s'évaporent %d/%d paires (%.1f%%) +%s"
                       % (l2["casse"], l2["n"], l2["pct"], comp["murs_l2"]))
    else:
        comp["murs_l2"] = 0.0
        signaux.append("murs L2 : sonde muette +0 (fail-open)")

    signaux.append("contexte hack 29/10 6.3Mds (3Mds gelés, 3Mds mobiles) + midterms US : "
                   "pas de compte à rebours, la sortie se mesure")

    # Niveau : ratio du maximum possible (insensible à l'échelle du score)
    score_max = sum(MAX_COMPOSANTES.values())
    ratio = (score / score_max) if score_max > 0 else 0.0
    if ratio >= SEUILS_RATIO["fortresse"]:
        niveau, label = 3, "FORTRESSE"
    elif ratio >= SEUILS_RATIO["hack"]:
        niveau, label = 2, "HACK_ACTIF"
    elif ratio >= SEUILS_RATIO["vigilance"]:
        niveau, label = 1, "VIGILANCE"
    else:
        niveau, label = 0, "CALME"

    # --- équity et cash VRAIS (equity_reconcilie) ---
    equity = None
    cash_reel = None
    src_eq = "mur_mesure"
    if recon.get("ok") is not None and recon.get("equity_moteur"):
        equity = float(recon["equity_moteur"])
        cash_reel = float(recon.get("cash_journal") or 0.0)
        src_eq = "equity_reconcilie"
    if not equity:
        equity = float(mur.get("equity", 893.78) or 893.78)
        cash_reel = None

    latent = -83.39
    try:
        txt_pf = open(os.path.join(RUNS, "PORTEFEUILLE_LATEST.md"), encoding="utf-8").read()
        m = re.search(r"LATENT : ([-\d\.]+)", txt_pf)
        if m:
            latent = float(m.group(1))
    except Exception:
        pass
    stress = min(15.0, round(abs(latent) / max(equity, 1) * 100 / 2, 1))
    cash_pct = min(60.0, round(20 + 10 * niveau + stress, 1))
    mult = {0: 1.0, 1: 0.75, 2: 0.5, 3: 0.25}[niveau]
    cash_cible = round(equity * cash_pct / 100, 2)
    cash_ecart = round(cash_cible - cash_reel, 2) if cash_reel is not None else None
    try:
        base_cap = float(kelly.get("maxS2", 4.84) or 4.84)
    except Exception:
        base_cap = 4.84
    cap_trade = round(base_cap * mult, 2)

    res = {
        "ts": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "score": round(score, 2),
        "score_max": round(score_max, 2),
        "score_ratio": round(ratio, 3),
        "seuils_ratio": SEUILS_RATIO,
        "niveau": niveau,
        "label": label,
        "signaux": signaux,
        "composantes": comp,
        "flux_verdict": verdict,
        "ofi_norm": ofi_n,
        "foule": {"funding": th["funding"], "ls": th["ls"], "fear": th["fear"]},
        "geopol_score": gscore,
        "murs_l2": l2,
        "quantiles": qt,
        "equity": round(equity, 2),
        "equity_source": src_eq,
        "latent": latent,
        "cash_reserve_pct": cash_pct,
        "cash_reserve_usd": cash_cible,
        "cash_reel_usd": (round(cash_reel, 2) if cash_reel is not None else None),
        "cash_ecart_usd": cash_ecart,
        "taille_multiplier": mult,
        "cap_trade_usd": cap_trade,
        "regle_spread": "niveau>=2 : INTERDIT nouveau bag si spread>20bps (BIO/RIZE/RED/WAXL/CHIP) — mesurer spread digest, pas deviner",
        "regle_sortie": "décrue UNIQUEMENT si score<1.5 sur 2 runs consécutifs + flux EQUILIBRE/ACCUMULATION — jamais à date fixe",
        "conduite": "TENIR bags, garder cash, laisser shorts BTC/ETH/XRP couvrir ; racheter la chute par paliers OFI+mur, pas au feeling",
        "ok": True,
    }
    tmp = OUT + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(res, f, ensure_ascii=False, indent=1)
    os.replace(tmp, OUT)

    # --- historique (calibration future des seuils) ---
    try:
        ligne = {"ts": res["ts"], "score": res["score"],
                 "score_ratio": round(ratio, 3), "niveau": niveau,
                 "label": label, "composantes": comp,
                 "quantiles": {k: v["valeur"] for k, v in qt.items()},
                 "quantiles_mesures": {k: v["mesure"] for k, v in qt.items()},
                 "murs_l2_pct": l2["pct"], "equity": res["equity"],
                 "cash_reel_usd": res["cash_reel_usd"],
                 "cash_cible_usd": cash_cible, "cap_trade_usd": cap_trade}
        with open(HIST, "a", encoding="utf-8") as f:
            f.write(json.dumps(ligne, ensure_ascii=False) + "\n")
    except Exception:
        pass

    print("[hack-actif] score=%.2f niveau=%d %s cash cible=%.2f$ réel=%s$ écart=%s$ "
          "mult=%.2f cap=%.2f$"
          % (res["score"], niveau, label, cash_cible,
             ("%.2f" % cash_reel) if cash_reel is not None else "?",
             ("%.2f" % cash_ecart) if cash_ecart is not None else "?", mult, cap_trade))
    for s in signaux:
        print("  ·", s)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
