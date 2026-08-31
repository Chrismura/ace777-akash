# 🩳 SPEC SHORT BTC PAPER — ceinture de sécurité contre-tendance (31/08/2026)

> **GO Christophe, 31/08** : « implémente short btc ». Décision fondée sur l'audit du
> même jour : il n'existe AUCUN actif long qui monte quand BTC baisse (tout est
> corrélé, beta positif partout — vérifié sur le portefeuille ET sur le top 180
> Binance). La seule vraie contre-tendance exploitable = **short BTC quand le
> marché est en sommet**. Ce module la teste en PAPER (zéro argent réel).

---

## 1. Pourquoi ce module existe

Christophe cherchait un actif « contre BTC » → l'audit a prouvé que ça n'existe pas
en actif long dans ce régime de marché. Le protocole divergence (29/08) a par
contre montré un signal de **sommet** : quand les cryptos pompent, le panier
baisse 4h après (POMPE-PIÈGE). Ce module transforme ce signal en **short BTC
paper** — c'est la ceinture de sécurité : si le marché corrige, la ligne short
compense.

## 2. Le signal (score composite /10) — entrée short si score ≥ 5

| Composante | Règle | Points |
|---|---|---|
| **A. Contexte sommet** (protocole divergence) | corr(m6 BTC → delta panier +4h) ≤ −0.15 / −0.10 / −0.05 | 3 / 2 / 1 |
| **B. Surchauffe instantanée** | % paires (dernier point frais) avec m6 > +3% : ≥60% / ≥40% / ≥25% | 3 / 2 / 1 |
| **C. BTC en surchauffe** | dernier m6 BTC ≥ +2.0% / ≥ +1.0% | 2 / 1 |
| **D. Momentum 24h BTC** | move24 ≥ +3.0% / ≥ +1.5% | 2 / 1 |

**Entrée** : score ≥ 5 **ET** session 08-17h UTC (gating temporel validé) **ET**
données fraîches (< 15 min). Pas de levier : notional **5 $** (1/4 de la base 20 $).

## 3. Sortie (première condition atteinte)

| Condition | Règle |
|---|---|
| **TP** | prix ≤ entrée × (1 − 2%) |
| **SL** | prix ≥ entrée × (1 + 1.5%) |
| **Signal éteint** | score < 2 (le sommet s'est dissipé) |
| **Time-out** | position ouverte depuis > 24h |

## 4. Gardes-fous (non négociables)

- **Paper uniquement** : capital virtuel 100 $, notional 5 $. AUCUN argent réel.
- **Zéro appel réseau** : lit `runs/croisement_contexte.jsonl` (même source de
  prix que le moteur Hulk → cohérence garantie).
- **Fail-open** : données périmées (> 15 min) → ni entrée ni sortie forcée.
- **Gating temporel** : pas d'entrée la nuit (08-17h UTC, thèse Cortana validée).
- **Taille plafonnée** : c'est une ceinture, pas un moteur de PnL.

## 5. Fichiers

| Fichier | Rôle |
|---|---|
| `scripts/short_btc.py` | La machine (signal + position + journal) |
| `runs/short_btc_state.json` | État persistant (position, capital, trades) |
| `runs/short_btc_live.json` | État courant → cockpit (pont `/shortbtc`) |
| `runs/short_btc_journal.csv` | Journal des trades |
| `runs/short_btc_signaux.jsonl` | **TOUS les signaux calculés (audit)** |
| `~/Library/LaunchAgents/com.ace777.short-btc.plist` | Lancement toutes les 5 min |
| `Index_Maison/cockpit/index.html` (onglet STRATÉGIE) | Carte SHORT BTC |

## 6. Protocole de validation (comme le protocole divergence — 29/08)

> Christophe : « rien n'est statique — tant que les chiffres le montrent on
> valide. » Le seuil de confiance est **3 jours de comportement stable** avant
> toute idée de passage réel (jamais sans GO Christophe).

1. **Jour 1-3** : laisser tourner en paper. Chaque signal est journalisé dans
   `short_btc_signaux.jsonl` (score, composantes, prix) → on peut mesurer la
   QUALITÉ du signal même sans trade (ex. : quand le score ≥ 5, BTC a-t-il
   vraiment baissé dans les 24h ?).
2. **Point d'étape** : comparer les entrées/sorties au comportement réel du
   marché. Un TP sur 2+ ? Le signal prédit-il les sommets ?
3. **Décision** : garder en paper, ajuster les seuils (score, TP/SL), ou
   abandonner — jamais de passage réel sans GO explicite.
4. **Ré-évaluation permanente** : le signal vit et meurt selon les chiffres
   (principe de validité dynamique, 29/08).

## 7. Lecture dans le cockpit

Onglet **STRATÉGIE** → carte « SHORT BTC — CEINTURE DE SÉCURITÉ (PAPER) » :
score /10 en direct, position (entrée, prix actuel, PnL %), PnL total, derniers
trades clos. Données servies par le pont `GET /shortbtc` (lecture seule de
`short_btc_live.json`).

## 8. État au lancement (31/08 09:20 UTC)

Position short paper **ouverte @ 78 690 $** (score 5 = contexte 2 + surchauffe
40% + BTC m6 +1.7%). C'est le premier test réel du module.
