#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""hack_actif_mesure.py — REGIME HACK_ACTIF SANS TIMING FIXE (GO 02/11).
Lecture seule, 0 ordre, stdlib. Ecrit thermo/hack_actif.json.
Formule : niveau 0-3 mesure, pas de date d'expiration.
Cash reserve dynamique pour racheter la chute, taille bridee en consequence.

Entrees (toutes mesurees, fail-open si absent):
- flux_nets_latest.json (DISTRIBUTION=+2, EQUILIBRE=0)
- ofi_latest.json (vendeur si ofi_norm < -0.07 p95 02/11)
- THERMO_DERNIER.md (funding vs moyenne, L/S, fear, alts↓, ETF moy)
- veille_institutionnelle_etat.json (SURVEILLANCE=0, signaux actifs=+)
- geopol_gratuit_live.json (score maison >0.5 = +1, attention=0.5)
- mur_mesure.json + m_kelly_live.json + PORTEFEUILLE_LATEST.md (stress latent)
- calendrier : hack 29/10 et elections US = contexte, JAMAIS un compte a rebours

Sorties:
- niveau: 0 calme / 1 vigilance / 2 HACK_ACTIF / 3 FORTRESSE
- cash_reserve_pct = 20 + 10*niveau + stress_latent (cap 60)
- taille_multiplier = {0:1.0, 1:0.75, 2:0.5, 3:0.25}
- interdiction nouveaux bags si spread>20bps quand niveau>=2
- decrue UNIQUEMENT quand les mesures retombent, pas quand X jours passent.
"""
import json, os, re
from datetime import datetime, timezone

BASE = os.path.expanduser("~/ace777-test-day1")
INDEX = os.path.join(BASE, "Index_Maison")
THERMO = os.path.join(INDEX, "thermo")
DATA = os.path.join(INDEX, "data")
OUT = os.path.join(THERMO, "hack_actif.json")

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
    funding = grab(r"Funding \| ([\d\.]+)")
    ls = grab(r"L/S 1h \| ([\d\.]+)")
    fear = grab(r"Fear & Greed (\d+)")
    alts = grab(r"Alts.*?(\d+\.\d+) ?%")
    btc24 = grab(r"BTC 24h ([-\d\.]+)")
    return {"funding": funding, "ls": ls, "fear": fear, "alts_down": alts, "btc24": btc24, "txt": txt}

def main():
    flux = load_json(os.path.join(DATA, "flux_nets_latest.json"), {})
    ofi = load_json(os.path.join(DATA, "ofi_latest.json"), {})
    veille = load_json(os.path.join(DATA, "veille_institutionnelle_etat.json"), {})
    geopol = load_json(os.path.join(THERMO, "geopol_gratuit_live.json"), {})
    mur = load_json(os.path.join(THERMO, "mur_mesure.json"), {})
    kelly = load_json(os.path.join(THERMO, "m_kelly_live.json"), {})
    th = lire_thermo()

    signaux = []
    score = 0.0

    # 1. Flux nets : seule preuve onchain gratuite d'un depot massif (vente voleur)
    verdict = (flux.get("verdict") or "INCONNU").upper()
    if verdict == "DISTRIBUTION":
        score += 2; signaux.append("flux DISTRIBUTION +2 (depots dominent : possible vente)")
    elif verdict == "EQUILIBRE":
        signaux.append("flux EQUILIBRE +0 (pas de dump visible)")
    else:
        signaux.append(f"flux {verdict} +0 (fail-open, pas de conclusion)")

    # 2. OFI vendeur : pression carnet immediate
    try:
        ofi_n = float(ofi.get("fenetre_globale", {}).get("ofi_norm", 0))
    except Exception:
        ofi_n = 0.0
    if ofi_n < -0.07:
        score += 1; signaux.append(f"OFI vendeur {ofi_n} +1")
    else:
        signaux.append(f"OFI {ofi_n} neutre +0 (pas d'absorption)")

    # 3. Foule piegee : funding >2x moyenne 30j (0.0001 vs 0.000046) + L/S>2
    if th["funding"] and th["funding"] >= 0.00009 and th["ls"] and th["ls"] >= 2.0:
        score += 1; signaux.append(f"foule longue piegee funding {th['funding']} L/S {th['ls']} +1")
    else:
        signaux.append("foule OK +0")

    # 4. Fear + breadth : Fear<40 et alts>65% down = journee sous tension
    if th["fear"] is not None and th["fear"] <= 40:
        score += 1; signaux.append(f"Fear {th['fear']} +1")
    if th["alts_down"] and th["alts_down"] >= 65:
        score += 0.5; signaux.append(f"alts down {th['alts_down']}% +0.5")

    # 5. Institutionnel : signaux actifs = +1 chacun (aujourd'hui 0 = SURVEILLANCE)
    n_act = len(veille.get("signaux_actifs", [])) if isinstance(veille.get("signaux_actifs"), list) else 0
    if n_act > 0:
        score += n_act; signaux.append(f"veille {n_act} signaux +{n_act}")
    else:
        signaux.append("veille SURVEILLANCE +0")

    # 6. Geopol/elections : contexte, pas declencheur seul
    try:
        gscore = float(geopol.get("notre_geopol", {}).get("score", 0))
    except Exception:
        gscore = 0.0
    if gscore >= 0.5:
        score += 1; signaux.append(f"geopol {gscore} +1")
    elif gscore >= 0.3:
        score += 0.5; signaux.append(f"geopol attention {gscore} +0.5")
    else:
        signaux.append(f"geopol {gscore} +0")
    signaux.append("contexte hack 29/10 6.3Mds (3Mds gelés, 3Mds mobiles) + midterms US 03/11 : pas de compte à rebours, la sortie se mesure")

    # Niveau sans timing fixe : seuils sur score mesure
    if score >= 4.5:
        niveau, label = 3, "FORTRESSE"
    elif score >= 3.0:
        niveau, label = 2, "HACK_ACTIF"
    elif score >= 1.5:
        niveau, label = 1, "VIGILANCE"
    else:
        niveau, label = 0, "CALME"

    # Stress latent : |latent| / equity -> coussin supplementaire (max +15)
    equity = float(mur.get("equity", 893.78) or 893.78)
    latent = -83.39
    try:
        txt_pf = open(os.path.join(BASE, "hulk-mexc", "runs", "PORTEFEUILLE_LATEST.md"), encoding="utf-8").read()
        m = re.search(r"LATENT : ([-\d\.]+)", txt_pf)
        if m:
            latent = float(m.group(1))
    except Exception:
        pass
    stress = min(15.0, round(abs(latent) / max(equity, 1) * 100 / 2, 1))
    cash_pct = min(60.0, round(20 + 10 * niveau + stress, 1))
    mult = {0: 1.0, 1: 0.75, 2: 0.5, 3: 0.25}[niveau]
    # Cash $ sur equity : ce qu'on garde pour racheter la chute
    cash_usd = round(equity * cash_pct / 100, 2)
    # Cap par trade : m_kelly maxS2 * multiplier (mesure x regime, pas fixe)
    try:
        base_cap = float(kelly.get("maxS2", 4.84) or 4.84)
    except Exception:
        base_cap = 4.84
    cap_trade = round(base_cap * mult, 2)

    res = {
        "ts": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "score": round(score, 2),
        "niveau": niveau,
        "label": label,
        "signaux": signaux,
        "flux_verdict": verdict,
        "ofi_norm": ofi_n,
        "foule": {"funding": th["funding"], "ls": th["ls"], "fear": th["fear"]},
        "geopol_score": gscore,
        "equity": equity,
        "latent": latent,
        "cash_reserve_pct": cash_pct,
        "cash_reserve_usd": cash_usd,
        "taille_multiplier": mult,
        "cap_trade_usd": cap_trade,
        "regle_spread": "niveau>=2 : INTERDIT nouveau bag si spread>20bps (BIO/RIZE/RED/WAXL/CHIP) — mesurer spread digest, pas deviner",
        "regle_sortie": "décrue UNIQUEMENT si score<1.5 sur 2 runs consécutifs + flux EQUILIBRE/ACCUMULATION — jamais à date fixe",
        "conduite": "TENIR bags, garder cash, laisser shorts BTC/ETH/XRP couvrir ; racheter la chute par paliers OFI+mur, pas au feeling",
        "ok": True,
    }
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(res, f, ensure_ascii=False, indent=1)
    print(f"[hack-actif] score={res['score']} niveau={niveau} {label} cash={cash_pct}% ({cash_usd}$) mult={mult} cap={cap_trade}$")
    print(" | ".join(signaux))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
