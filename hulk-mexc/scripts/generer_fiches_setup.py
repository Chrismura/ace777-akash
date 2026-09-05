#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""generer_fiches_setup.py — Fiches de set-up individuelles par actif (30/08/2026, v2 06/09/2026).

À partir des profils JSON générés par analyse_pattern_actif.py, crée une fiche de set-up
INDIVIDUELLE par actif dans Crypto_Projet/. Chaque set-up est adapté au comportement
réel de l'actif (pattern intraday, volatilité, corrélations, signal) — jamais copié.

v2 (06/09/2026) — améliorations après audit :
- date dynamique + nom de fichier versionné (FICHE_SETUP_<PAIRE>_<AAAAMMJJ>.md)
- section STATUT OBSERVATION depuis hulk-mexc/strategie/paires_croisement.json
- résumé du SUIVI quotidien (nb mesures + dernière ligne)
- labels honnêtes : poussière = indicateur PANIER (pas par paire), mur max = max du run
- déclencheur d'entrée basé régime + mur courant (la poussière n'est plus un déclencheur)

Usage : python3 generer_fiches_setup.py [PAIRE1 ...]   (défaut : tous les profils)
"""
import datetime
import json
import os
import sys

RUNS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "runs")
PROFILS = os.path.join(RUNS, "profils_actifs")
STRAT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "strategie")
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


def charger_statuts():
    """Statut observation/deepdive par paire depuis hulk-mexc/strategie/paires_croisement.json."""
    fn = os.path.join(STRAT, "paires_croisement.json")
    try:
        d = json.load(open(fn, encoding="utf-8"))
    except Exception:
        return {}
    out = {}
    for grp, label in (("deepdive_validees", "DEEPDIVE VALIDÉE"),
                       ("observation_setup", "OBSERVATION"),
                       ("exclues_prudence", "EXCLUE (prudence)"),
                       ("ejectees", "ÉJECTÉE")):
        for pair, note in (d.get(grp) or {}).items():
            out[pair] = (label, note or "")
    return out


def charger_grille():
    """Grille de corrélation (runs/grille_correlation.json) — lead-lag, décorrélation, copains."""
    fn = os.path.join(RUNS, "grille_correlation.json")
    try:
        return json.load(open(fn, encoding="utf-8"))
    except Exception:
        return None


def charger_poussiere_indiv():
    """Poussière INDIVIDUELLE par paire (runs/poussiere_paires.json, poussiere_paire.py)."""
    fn = os.path.join(RUNS, "poussiere_paires.json")
    try:
        d = json.load(open(fn, encoding="utf-8"))
        return d.get("ts"), d.get("paires") or {}
    except Exception:
        return None, {}


def suivi_recap(pair):
    """Résumé du suivi quotidien : nb de mesures + dernière ligne (None si absent)."""
    jl = os.path.join(RUNS, f"SUIVI_SETUP_{pair}.jsonl")
    if not os.path.exists(jl):
        return None
    rows = []
    for l in open(jl, encoding="utf-8"):
        try:
            rows.append(json.loads(l))
        except Exception:
            continue
    if not rows:
        return None
    # Comparaison à heure fixe (amélioration #2 audit 06/09) : on retient la dernière
    # mesure prise à l'heure MODALE de suivi (comparable d'un jour sur l'autre).
    from collections import Counter
    heures = Counter(r.get("heure_utc") for r in rows if r.get("heure_utc") is not None)
    h_modale = heures.most_common(1)[0][0] if heures else None
    last_modale = next((r for r in reversed(rows) if r.get("heure_utc") == h_modale), None)
    return {"n": len(rows), "last": rows[-1], "h_modale": h_modale, "last_modale": last_modale}


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
        n_tranches = "50% au contact / 50% si le creux tient sur 2 bougies 15min"
    elif dd15 > 15:
        risque = f"ÉLEVÉ — dd15 moyen {dd15:.0f}% (volatile, stops à respecter)"
        n_tranches = "50% au contact / 50% si le creux tient sur 2 bougies 15min"
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


GARDE_FOU = {
    # verdicts famille : interdiction de trade, prix croisé SEUL (MNSRY/RWA = NON 30/08)
    "MNSRYUSDT": "⛔ NON famille (1/10, usurpation de marque) — prix croisé SEUL, jamais de position",
    "RWAUSDT": "⛔ NON famille (1.7/10, rebranding trompeur, liquidité mortifère) — prix croisé SEUL, ne pas agrandir",
    "EDELUSDT": "⚠️ NON deepdive (2-3.5/10, loterie assumée) — seed gardée uniquement, veille delisting",
}


def render_fiche(p, s, date_str, date_tag, statut, suivi, grille=None, pouss_ts=None, pouss=None):
    nom = NOMS.get(p["pair"], p["pair"].replace("USDT", ""))
    poussiere = p.get("poussiere_moy")
    mur = p.get("mur_max_usd")
    spoof = p.get("spoof_moy")
    statut_label = statut[0] if statut else "—"
    statut_note = statut[1] if statut else ""

    # ---- Grille de corrélation (v3) ----
    g_lag = (grille or {}).get("lag_panier", {}).get(p["pair"]) or {}
    g_deco = (grille or {}).get("decorrelation_moy", {}).get(p["pair"])
    g_copains = (grille or {}).get("copains", {}).get(p["pair"]) or []
    g_sig = (grille or {}).get("signal_directionnel_9j", {}).get(p["pair"])
    short = lambda x: x.replace("USDT", "")
    copains_txt = ", ".join(f"{short(b)} ({c:+.2f})" for b, c in g_copains[:3]) if g_copains else "—"
    lag_h, lag_c = g_lag.get("lag_h"), g_lag.get("corr_max")
    if lag_h is not None and lag_h < 0 and (lag_c or 0) >= 0.30:
        role_txt = f"🟢 ANTICIPATEUR (précède le panier de {abs(lag_h)}h, corr {lag_c:+.2f})"
    elif lag_h == 0 and (lag_c or 0) >= 0.30:
        role_txt = f"⚪ SYNCHRONISÉ au groupe (corr {lag_c:+.2f}) — baromètre, pas un précurseur"
    elif lag_h is not None and lag_h > 0:
        role_txt = f"🔶 SUIVEUR (lag {lag_h:+d}h)"
    else:
        role_txt = "· lien faible au panier"
    if g_deco is not None and g_deco < 0.25:
        deco_txt = f"🟣 ENDOGÈNE (décorr moy {g_deco:.2f}) — moteur propre, signaux du panier peu utiles"
    elif g_deco is not None and g_deco < 0.45:
        deco_txt = f"🟡 semi-endogène (décorr moy {g_deco:.2f})"
    elif g_deco is not None:
        deco_txt = f"🟠 corrélationné au groupe (décorr moy {g_deco:.2f}) — filtre macro indispensable"
    else:
        deco_txt = "—"
    sig_txt = (f"{g_sig:+.2f}" if isinstance(g_sig, (int, float)) else "—")

    # ---- Poussière individuelle (v3) ----
    if pouss:
        pb = pouss.get("poussiere_bid_pct")
        ev = pouss.get("evanescence_bid_pct")
        mur_top = pouss.get("mur_bid_top_usd")
        prof = pouss.get("profondeur_bid_usd")
        if pb is not None and pb < 5:
            lect_p = "carnet sain (peu de poussière)"
        elif pb is not None and pb < 30:
            lect_p = "carnet mixte"
        elif pb is not None:
            lect_p = "carnet dominé par la poussière (fragile)"
        else:
            lect_p = "—"
        pouss_txt = (f"**{pb}%** bid / {pouss.get('poussiere_ask_pct')}% ask · "
                     f"évanescence 75s : **{ev}%** · profondeur ±2% : {prof}$ · mur top : {mur_top}$ ({lect_p})")
    else:
        pouss_txt = "— (relancer `poussiere_paire.py`)"

    garde = GARDE_FOU.get(p["pair"])
    garde_bloc = ("**🚧 GARDE-FOU FAMILLE : " + garde + "**\n\n---\n") if garde else ""

    # Résumé du suivi quotidien
    if suivi:
        last = suivi["last"]
        mur_moy_last = last.get("mur_bid_moy_usd")
        mur_txt = f"{mur_moy_last:,.0f}$" if isinstance(mur_moy_last, (int, float)) else "—"
        suivi_txt = (
            f"- Dernière mesure : **{last.get('ts', '?')}** — prix {last.get('prix', '?')}, "
            f"régime {last.get('regime', '?')}, mur bid moy {mur_txt}.\n"
            f"- {suivi['n']} mesures depuis le 30/08 — comparer d'une ligne à l'autre "
            f"(même heure de mesure = comparable)."
        )
    else:
        suivi_txt = "- Aucune mesure de suivi — relancer `suivi_setup_actif.py`."

    return f"""# 🎯 FICHE SET-UP INDIVIDUEL — {p['pair']} ({nom}) — {date_str}

> **Système unique, set-up propre à CET actif** (doctrine : même système, pas même set-up).
> Profil automatique : `hulk-mexc/runs/profils_actifs/PROFIL_{p['pair']}.md` ({p['pts']} points, {p['first']} → {p['last']}).
> Suivi quotidien : `hulk-mexc/runs/SUIVI_SETUP_{p['pair']}.md` (CORE-20 mesuré systématiquement, plist 16:35 locale).
> Version précédente : 30/08/2026 (archive `_traites/`).

---

## 🏛️ STATUT OBSERVATION (paires_croisement.json)

**{statut_label}** — {statut_note or "pas de statut enregistré"}

---

{garde_bloc}## 🕸️ RÔLE DANS LE GROUPE (grille 20×20, 06/09)

| Élément | Valeur |
|---|---|
| **Lead-lag vs panier** | {role_txt} |
| **Décorrélation** | {deco_txt} |
| **Top copains** | {copains_txt} |
| **Signal directionnel (m6→panier +4h)** | {sig_txt} |

---

## 📊 LE PROFIL (mesuré, {p['first']} → {p['last']})

| Élément | Valeur | Lecture |
|---|---|---|
| **Range total** | {p['range_total_pct']}% | Amplitude sur la fenêtre |
| **Creux intraday** | **{p['h_creux']}h UTC** | Fenêtre d'entrée : **{s['entree_txt']}** |
| **Pic intraday** | **{p['h_pic']}h UTC** | Fenêtre de sortie : **{s['sortie_txt']}** |
| **Pattern jour/nuit** | {s['regime_txt']} | {s['lecture']} |
| **Volatilité (dd15 moy)** | {p['dd15_moy']}% | {s['risque']} |
| **Mur bid max (run)** | {mur}$ (spoof {spoof}%) | Max historique du run = plafond observé ; mur COURANT à lire dans le suivi |
| **Poussière INDIVIDUELLE** | {pouss_txt} | Mesure carnet MEXC ±2% ({pouss_ts or 'date ?'}) — remplace l'ancien indicateur panier ({poussiere}%) |
| **Corrélation BTC** | {p['corr_btc']} | {s['corr_txt']} |
| **Signal divergence** | {p['signal_div']} | Référence panier |

---

## 🎯 LE SET-UP INDIVIDUEL (adapté à ce comportement — à faire évoluer)

### Entrée (tout doit être vrai)
1. **Fenêtre** : uniquement **{s['entree_txt']} UTC** (le creux de CET actif).
2. **Déclencheur** : régime COOLING/IMPULSE_WAIT (pas WATCH) + mur bid courant qui tient sur 24h.
3. **{s['endogene']}** — {s['corr_txt']}.
4. Garde-fou volume 15min < 3× moyenne 24h · FPOB ratio bid/ask ±2% > 1.2.
5. **Exécution** : {s['n_tranches']} · stop dynamique 1,5× range 15min.

### Sortie
- Scaling out vers la fenêtre de pic **{s['sortie_txt']} UTC**, reste derrière le trailing Hulk.

### Invalidation / risques
- **{s['risque']}**.
- Arrêter si frais réels + slippage > 1% (marge trop fine).
- Signal divergence : {p['signal_div']} — à surveiller (instable sur small caps).
- Poussière = indicateur panier : ne PAS l'utiliser comme déclencheur individuel (v2 06/09).

---

## ⏱️ SUIVI QUOTIDIEN

{suivi_txt}

## ⏱️ ÉTAT ACTUEL
- **{p['pair']} est suivie en observation** (doctrine : tous les actifs sous observation).
- Rien n'est câblé de neuf dans Hulk : ce set-up est la **cible d'observation**, à valider
  sur les prochains jours de mesure (jour 1 → jour 2 → ... différence ou pas ?).
- Fiche à réviser avec l'évolution des données (jamais statique).

## Archives
- Profil : `hulk-mexc/runs/profils_actifs/PROFIL_{p['pair']}.md`
- Suivi : `hulk-mexc/runs/SUIVI_SETUP_{p['pair']}.jsonl` + `.md`
- Version 30/08/2026 : `Index_Maison/OUTBOX_OBSIDIAN/_traites/FICHE_SETUP_{p['pair']}_20260830.md`
"""


def main():
    today = datetime.date.today()
    date_str = today.strftime("%d/%m/%Y")
    date_tag = today.strftime("%Y%m%d")
    statuts = charger_statuts()
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
        statut = statuts.get(pair)
        suivi = suivi_recap(pair)
        grille = charger_grille()
        pouss_ts, pouss_map = charger_poussiere_indiv()
        fn = os.path.join(CRYPTO, f"FICHE_SETUP_{pair}_{date_tag}.md")
        with open(fn, "w", encoding="utf-8") as fh:
            fh.write(render_fiche(p, s, date_str, date_tag, statut, suivi, grille, pouss_ts,
                                  (pouss_map or {}).get(pair)))
        print(f"[OK] {pair}: entrée {s['entree_txt']} · sortie {s['sortie_txt']} · {s['regime_txt']} · "
              f"{s['risque']} · {statut[0] if statut else '—'} · suivi {suivi['n'] if suivi else 0} mesures")
        n += 1
    print(f"== {n} fiches générées dans Crypto_Projet/")


if __name__ == "__main__":
    main()
