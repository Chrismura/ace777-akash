# 📌 FICHE VEILLE — QAIT (PLANCHER) — mise à jour 30/08/2026

> **Statut : 🟢 PLANCHER ACCESSIBLE** — QAIT (SEALCOIN) retiré de MEXC mais **toujours négociable**
> sur **Binance Alpha (swap)** et **BitMart (QAIT/USDT)**. Christophe attend qu'il atteigne son
> plancher pour un achat RÉEL. Cette fiche garde le contexte pour ne rien oublier.

---

## 🚨 L'ÉVÉNEMENT : QAIT delisted de MEXC

| Fait | Détail |
|---|---|
| **Premier échec API** | 29/08 2026 à **14:03:43Z** (HTTP 400 Bad Request) |
| **Dernier prix connu** | **0.001965 USDT** le 29/08 à 14:02:43Z |
| **Vérification exchangeInfo MEXC** | QAITUSDT **absent** (2072 symbols listés, QAIT non présent) |
| **Binance** | QAITUSDT aussi en HTTP 400 (pas listé non plus) |
| **Erreurs moteur accumulées** | 548 appels API 400 gaspillés en boucle (arrêté le 30/08) |

→ Le delisting n'est PAS un bug de nos sondes : la paire n'existe plus sur les exchanges testés.
→ **MAIS (découverte 30/08) : QAIT = SEALCOIN, toujours listé sur Binance Alpha + BitMart** —
  le delisting MEXC est un retrait local, pas la fin du token.

## 🦭 QAIT = SEALCOIN — OÙ ON L'ACHÈTE EN VRAI (vérifié 30/08)

| Marché | Comment | Preuve |
|---|---|---|
| **Binance Alpha** (pré-listing) | App Binance → Trade → **Swap** (Wallet), pas le spot classique | Binance « how to buy qait » + communiqué compétition $200K (04/06/2026) |
| **BitMart** | Paire **QAIT/USDT** listée 29/05/2026 | TradingView / CoinMarketCal |
| **Prix actuels** | $0.00189 (CoinGecko, 28/08) · $0.0025 (Phemex/LiveCoinWatch) · $0.0019 (CoinDesk 29/08) | CoinGecko, Phemex, CoinDesk |
| **Market cap / volume** | ~$2.64M · volume 24h ~$126-135K | Phemex, CoinDesk |
| **ATH / histoire** | ATH $0.03536 (06/06/2026) — lancé fin mai ~$0.006, +27% à $0.00729 le 22/07 (volume $5M) | Coingabbar, CMC |

→ **Le plancher que Christophe attend est PROCHE du niveau actuel** : notre dernier prix MEXC 0.001965,
  CoinGecko 0.001894 aujourd'hui. Le token est à ~-95% de son ATH — zone plancher potentielle.

## 🧹 Ce qu'on a fait (30/08, GO Christophe)

1. **Retiré QAITUSDT** de `PAPER_PAIRS` et `PAPER_EXTRA_PAIRS` (`config/defaults.env`) → le moteur
   Hulk ne tente plus la paire (fini les 548 erreurs/jour).
2. **Moteur relancé** (watchdog) pour recharger la config.
3. **Cette fiche** : QAIT reste en **veille plancher** — pas oublié, juste sorti de la rotation active.

## 🎯 L'OBJECTIF : achat réel au plancher

- Christophe attend que QAIT **atteigne son plancher** pour acheter en **vrai** (pas en paper).
- Le **creux historique du cycle** QAIT (profil 28-29/08) : zone **10h-13h UTC**, prix moyen creux ≈ **0.00195**.
- Dernier prix connu : **0.001965** (29/08 14:02Z).

## ⚠️ LE RISQUE (honnête)

- **Binance Alpha = zone pré-listing** : liquidité fine (~$130K/jour), risque élevé, pas de carnet
  classique — le swap se fait au prix du DEX sous-jacent.
- QAIT a déjà fait **-95% depuis l'ATH** ($0.035 → $0.002) : soit un plancher, soit un token qui
  continue de mourir. La ligne est fine.
- **Vérifier le prix réel au moment de l'achat** : nos données MEXC s'arrêtent au 29/08 14:02Z
  (0.001965) — le prix Alpha/BitMart peut diverger (frais de swap, slippage).
- La sonde `veille_presence_paires.py` surveille MEXC — QAIT n'y reviendra probablement pas ;
  pour le suivi du prix réel il faudrait une source externe (CoinGecko API, gratuit).

## 📎 Liens utiles

- Dernier état QAIT dans le portefeuille cockpit : figé au dernier prix (reel 29.14$ / hold 27.86$, seed 10$).
- Cycle QAIT (données figées au 29/08 14:02 — plus de points après le delisting) : `hulk-mexc/runs/CYCLE_QAIT_*.md`
- Source de données coupée : `hulk-mexc/runs/croisement_contexte.jsonl` (dernier point QAIT 29/08 14:02:43Z)
