#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""generer_fiches_setup.py — Fiches de set-up individuelles par actif (30/08/2026).

À partir des profils JSON générés par analyse_pattern_actif.py, crée une fiche de set-up
INDIVIDUELLE par actif dans Crypto_Projet/. Chaque set-up est adapté au comportement
réel de l'actif (pattern intraday, volatilité, corrélations, signal) — jamais copié.

Usage : python3 generer_fiches_setup.py [PAIRE1 ...]   (défaut : tous les profils)
"""
import json
import os
import sys

RUNS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "runs")
PROFILS = os.path.join(RUNS, "profils_actifs")
CRYPTO = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..",
                      "Index_Maison", "OUTBOX_OBSIDIAN", "Crypto_Projet")
os.makedirs(CRYPTO, exist_ok=True)

# Noms des projets réels (vérifiés dans nos deepdives) — reste à compléter au fur et à mesure
NOMS = {
    "BTCUSDT": "Bitcoin (socle)",
    "ETHUSDT": "Ethereum (socle)",
    "XRPUSDT": "XRP (Ripple)",
    "HBARUSDT": "Hedera",
    "CCUSDT": "CC (Canton Network)",
    "REDUSDT": "RedStone (oracle)",
    "CHIPUSDT": "CHIP (USD.AI, compute)",
    "EDELUSDT": "EDEL",
    "PYTHUSDT": "Pyth (oracle)",
    "RIZEUSDT": "RIZE (T-RIZE, RWA)",
    "ZBCNUSDT": "Zebec",
    "WUSDT": "W (Wormhole)",
    "BIOUSDT": "BIO (Bioprotocol)",
    "KITEUSDT": "KITE",
    "TELUSDT": "Telos",
    "RWAINCUSDT": "RWA Inc.",
    "RWAUSDT": "Allo (RWA)",
    "QNTUSDT": "Quant",
    "FLUIDUSDT": "Fluid",
    "MNSRYUSDT": "Mansory",
}


def decide_setup(p):
    """Décide un set-up INDIVIDUEL à partir du profil. Règles validées (famille + Cortana)."""
    h_creux, h_pic = p.get("h_creux"), p.get("h_pic")
    ecart = p.get("ecart_nuit_creux_pct") or 0.0
    dd15 = p.get("dd15_moy") or 0.0
    corr_btc = p.get("corr_btc")
    signal = p.get("signal_div") or "neutre"
    range_pct = p.get("range_total_pct") or 0.0

    # Fenêtre d'entrée : 3h centrées sur l'heure de creux
    def win(h):
        if h is None:
            return [14, 15, 16]
        return [(h - 1) % 24, h % 24, (h + 1) % 24]
    entree_win = win(int(h_creux))
    sortie_win = win(int(h_pic)) if h_pic is not None else [1, 2, 3]
    entree_txt = " / ".join(f"{h}h" for h in entree_win)
    sortie_txt = " / ".join(f"{h}h" for h in sortie_win)

    # Lecture du pattern jour/nuit
    if ecart < -1.5:
        lecture = f"Pattern INVERSE (nuit < creux de {abs(ecart):.1f}%) — l'actif vit le JOUR, pas la nuit"
        regime_txt = "jour > nuit"
    elif ecart > 1.5:
        lecture = f"Pattern nuit > creux ({ecart:.1f}%) — cycle de nuit (type QAIT/EDEL)"
        regime_txt = "nuit > jour"
    else:
        lecture = f"Pattern faible ({ecart:.1f}%) — cycle horaire peu marqué, prudent"
        regime_txt = "distribué"

    # Risque volatilité
    if dd15 > 25:
        risque = f"TRÈS ÉLEVÉ — dd15 moyen {dd15:.0f}% (rafales brutales, stops serrés obligatoires)"
        n_tranches = "50% au contact / 50% si poussière <10%"
    elif dd15 > 15:
        risque = f"ÉLEVÉ — dd15 moyen {dd15:.0f}% (volatile, stops à respecter)"
        n_tranches = "50% au contact / 50% si poussière <10%"
    else:
        risque = f"MODÉRÉ — dd15 moyen {dd15:.0f}%"
        n_tranches = "3 tranches (−1/−2/−3%)"

    # Corrélation BTC
    if corr_btc is not None:
        if corr_btc > 0.8:
            corr_txt = f"fortement corrélé BTC ({corr_btc:+.2f}) → suit le marché"
            endogene = "NON — actif de marché (filtre macro >1.5% BTC/ETH indispensable)"
        elif corr_btc > 0.4:
            corr_txt = f"moyennement corrélé BTC ({corr_btc:+.2f})"
            endogene = "PARTIEL — attention aux secousses macro"
        elif corr_btc < -0.2:
            corr_txt = f"ANTI-corrélé BTC ({corr_btc:+.2f}) → bouge en sens inverse du marché"
            endogene = "OUI mais anti-corrélé — ne pas lire les signaux BTC au premier degré"
        else:
            corr_txt = f"faiblement corrélé BTC ({corr_btc:+.2f}) → plutôt endogène"
            endogene = "OUI (dé-corrélé) — mais vérifier si c'est de la liquidité fine"
    else:
        corr_txt, endogene = "corrélation non calculée", "à mesurer"

    return {
        "entree_txt": entree_txt, "sortie_txt": sortie_txt,
        "lecture": lecture, "regime_txt": regime_txt,
        "risque": risque, "n_tranches": n_tranches,
        "corr_txt": corr_txt, "endogene": endogene,
        "range_pct": range_pct, "signal": signal,
    }


def render_fiche(p, s):
    nom = NOMS.get(p["pair"], p["pair"].replace("USDT", ""))
    poussiere = p.get("poussiere_moy")
    mur = p.get("mur_max_usd")
    spoof = p.get("spoof_moy")
    return f"""# 🎯 FICHE SET-UP INDIVIDUEL — {p['pair']} ({nom}) — 30/08/2026

> **Système unique, set-up propre à CET actif** (doctrine : même système, pas même set-up).
> Profil automatique : `hulk-mexc/runs/profils_actifs/PROFIL_{p['pair']}.md` ({p['pts']} points).
> Suivi quotidien : `hulk-mexc/runs/SUIVI_SETUP_{p['pair']}.md` (mesure jour par jour, plist 16:35 locale).

---

## 📊 LE PROFIL (mesuré, 27-30/08)

| Élément | Valeur | Lecture |
|---|---|---|
| **Range total** | {p['range_total_pct']}% | Amplitude sur la fenêtre |
| **Creux intraday** | **{p['h_creux']}h UTC** | Fenêtre d'entrée : **{s['entree_txt']}** |
| **Pic intraday** | **{p['h_pic']}h UTC** | Fenêtre de sortie : **{s['sortie_txt']}** |
| **Pattern jour/nuit** | {s['regime_txt']} | {s['lecture']} |
| **Volatilité (dd15 moy)** | {p['dd15_moy']}% | {s['risque']} |
| **Mur bid max** | {mur}$ (spoof {spoof}%) | Mur = INFO, spoof = TENSION |
| **Poussière moyenne** | {poussiere}% | Déclencheur entrée : < 15% |
| **Corrélation BTC** | {p['corr_btc']} | {s['corr_txt']} |
| **Signal divergence** | {p['signal_div']} | Référence panier |

---

## 🎯 LE SET-UP INDIVIDUEL (adapté à ce comportement — à faire évoluer)

### Entrée (tout doit être vrai)
1. **Fenêtre** : uniquement **{s['entree_txt']} UTC** (le creux de CET actif).
2. **Déclencheur** : poussière < 15% + mur testé qui tient.
3. **{s['endogene']}** — {s['corr_txt']}.
4. Garde-fou volume 15min < 3× moyenne 24h · FPOB ratio bid/ask ±2% > 1.2.
5. **Exécution** : {s['n_tranches']} · stop dynamique 1,5× range 15min.

### Sortie
- Scaling out vers la fenêtre de pic **{s['sortie_txt']} UTC**, reste derrière le trailing Hulk.

### Invalidation / risques
- **{s['risque']}**.
- Arrêter si frais réels + slippage > 1% (marge trop fine).
- Signal divergence : {p['signal_div']} — à surveiller (instable sur small caps).

---

## ⏱️ ÉTAT ACTUEL
- **{p['pair']} est suivie en observation** (doctrine : tous les actifs sous observation).
- Rien n'est câblé de neuf dans Hulk : ce set-up est la **cible d'observation**, à valider
  sur les prochains jours de mesure (jour 1 → jour 2 → ... différence ou pas ?).
- Fiche à réviser avec l'évolution des données (jamais statique).

## Archives
- Profil : `hulk-mexc/runs/profils_actifs/PROFIL_{p['pair']}.md`
- Suivi : `hulk-mexc/runs/SUIVI_SETUP_{p['pair']}.jsonl` + `.md`
"""


def main():
    pairs = sys.argv[1:] or [f.replace("PROFIL_", "").replace(".json", "")
                             for f in sorted(os.listdir(PROFILS)) if f.endswith(".json")]
    n = 0
    for pair in pairs:
        jf = os.path.join(PROFILS, f"PROFIL_{pair}.json")
        if not os.path.exists(jf):
            print(f"[SKIP] pas de profil JSON {pair}")
            continue
        p = json.load(open(jf, encoding="utf-8"))
        s = decide_setup(p)
        fn = os.path.join(CRYPTO, f"FICHE_SETUP_{pair}_20260830.md")
        with open(fn, "w", encoding="utf-8") as fh:
            fh.write(render_fiche(p, s))
        print(f"[OK] {pair}: entrée {s['entree_txt']} · sortie {s['sortie_txt']} · {s['regime_txt']} · {s['risque']}")
        n += 1
    print(f"== {n} fiches générées dans Crypto_Projet/")


if __name__ == "__main__":
    main()