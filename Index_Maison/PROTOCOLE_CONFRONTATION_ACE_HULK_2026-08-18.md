# PROTOCOLE — Confrontation ACE ↔ Hulk (données synchronisées)

> Créé le 18/08/2026 à la demande de Christophe — « on superpose les données Hulk avec ACE et on voit ce que ça donne ».
> État : **PRÉPARÉ** — l'analyse se lance à la fin du run ACE 96h (22/08 09:41 UTC) ou quand on a assez de cycles BTC.

---

## 🎯 Objectif

Utiliser les **données déjà collectées** (pas de nouvelle sonde) pour répondre à :
1. **Quand les murs des small caps bougent (signal Hulk), ACE trade-t-il le BTC pareil ?**
2. **Quand ACE détecte un mur BTC qui tombe, les small caps Hulk réagissent-elles ?**
3. **Le bruit BTC (btc_delta_pct) explique-t-il les trades perdants d'ACE ?**

## 📊 Les 2 sources de données (déjà en cours)

| Source | Fichier | Ce qu'elle mesure |
|---|---|---|
| **Sonde Hulk** | `hulk-mexc/runs/ASPIRATION_CALIB_20260816_214411.csv` | murs bid/ask small caps (drop %/s), spread, spoof, **+ btc_price + btc_delta_pct** |
| **ACE (logs moteur)** | `ace777-test-day1/runs/MASTER_VORTEX_V2_COLLAB_4H_*_X5.csv` | chaque trade : entrée/sortie, PnL, **bid_drop / ask_drop / tension** (4 211 trades avec murs non nuls dans l'historique) |

**Point clé** : les deux ont le **même horodatage BTC** → superposition possible par timestamp.

## ⚠️ Limite honnête (à documenter dans l'analyse)

- Hulk scanne les carnets **MEXC spot** des small caps — elle ne voit **pas** le carnet BTCUSDT
- ACE trade le carnet **BTCUSDT futures testnet** — il ne voit **pas** les carnets small caps
- → La superposition est **temporelle** (corrélation de comportement), PAS une lecture du même carnet.
- Si l'analyse révèle un trou (besoin de lire le carnet BTC entre les trades ACE), **là** on ajoute une micro-sonde — seulement si nécessaire.

## 🔗 Fenêtre d'observation synchronisée (parfaite)

Le run ACE **96h** a démarré le 18/08 09:41 UTC et la sonde Hulk tourne en continu.
→ On aura **96 h de données synchronisées** (18/08 09:41 → 22/08 09:41 UTC).

## 📋 KPI à comparer

1. **Corrélation temporelle** : signaux Hulk (drop mur ≥ X %/s) vs trades ACE (mêmes fenêtres ± 5 min)
2. **btc_delta_pct vs PnL ACE** : les trades perdants d'ACE coïncident-ils avec des mouvements BTC ?
3. **Murs ACE (bid_drop/ask_drop) vs sorties** : l'aspiration d'ACE (1.618 @ 37.8°) sort-elle quand les murs tombent ?
4. **Régimes Hulk (IDLE/IMPULSE/WATCH_PULLBACK) vs activité ACE** : les small caps en impulse = ACE actif sur BTC ?

## 🚀 Déclencheur d'analyse

- **Minimum** : fin du run ACE 96h (22/08 09:41 UTC)
- **Idéal** : 1 semaine complète de sonde Hulk (25/08 21:45 UTC) = ~7 cycles BTC
- La **veilleuse** (`VEILLE_CONFRONTATION_ACE_HULK.md` + rappel auto) surveille la date.

## 📁 Livrables

- Analyse : `Index_Maison/CONFRONTATION_ACE_HULK_ANALYSE.md`
- Proposition d'action (si un pattern émerge) : soumission à la famille AVANT toute activation.

---
> « On n'est pas pressés — on fait au mieux. Plus on voit de cycles BTC, plus le calibrage est fiable. »
