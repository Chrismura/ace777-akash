# Thermo — sources (FREE d’abord · ZeroGEX = exemple)

**Statut :** 🟢 doctrine hygiène · **0 € d’abo API**  
**Règle S14 :** économies = pas d’API payante sans GO explicite rare.  
**Automatique :** `scripts/thermo_quotidien_free.py` → [[THERMO_DERNIER]] (branché journal soir).

> **ZeroGEX** = *exemple* du concept (gamma flip / walls). On n’achète pas le dashboard.  
> Le **top dont on a besoin** pour ACE/Hulk = **stress levier crypto gratuit** (OI, funding, L/S) + plus tard lecture humaine free delayed si utile.

---

## Stack FREE (canon — automatisée)

| Besoin thermo | Source **gratuite** | Comment |
|---------------|---------------------|---------|
| OI BTC | Binance `GET /fapi/v1/openInterest` | **C13** · sans clé |
| Funding / mark | `GET /fapi/v1/premiumIndex` + `fundingRate` | **C14** soft |
| Crowding | `GET /futures/data/globalLongShortAccountRatio` | proxy sentiment |
| 24h move / vol | `GET /fapi/v1/ticker/24hr` | **B7 / B10** |
| Whales ≥500k$ (proxy) | Binance `GET /fapi/v1/aggTrades` | **C15** · gros prints · pas Whale Alert |
| Dark / OTC (proxy) | OI + `takerlongshortRatio` | **C23** · **pas** dark pool US temps réel |
| Top traders L/S | `topLongShortAccountRatio` | crowding pros |

**Commande manuelle :**
```bash
python3 ~/ace777-test-day1/Index_Maison/scripts/thermo_quotidien_free.py
```

**Auto :** appelé par `journal_soir_launchd.sh` (avec le journal).

---

## Concepts (exemples) — pas d’abo

| Exemple marché | Ce qu’on en garde | Proxy free chez nous |
|----------------|-------------------|----------------------|
| **ZeroGEX** / SpotGamma | Flip, walls, régime gamma | Funding extrême + OI qui gonfle = « dealers stress » soft — **pas** vrai GEX |
| Dark pools US / OTC | Gros prints cachés | **Pas free temps réel** fiable · **REFUS abo** · proxy = **C23** OI + taker B/S |
| Whale Alert / payant | Gros wallets | **C15** = gros *trades* Binance ≥500k$ (proxy) |
| FlashAlpha / UW / Quant Data | APIs GEX/dark | 🔴 **REFUS** hygiène (payant) sauf GO rare |

---

## IDs Index

| ID | Statut | Preuve |
|----|--------|--------|
| C13 OI | 🟢 via thermo free | [[THERMO_DERNIER]] |
| C14 levier/funding | 🟢 soft auto | idem |
| C15 whales | 🟢 proxy aggTrades ≥500k$ | idem · pas Whale Alert |
| C23 dark/OTC | 🟢 proxy OI+taker | pas FINRA / pas abo |
| C24–C25 GEX/walls | 🔵 concept ZeroGEX-style | proxy funding/OI · pas dashboard payant |

---

## Liens
[[OSSATURE_INDEX]] · [[PREFS_STACK]] · [[00_INDICATEURS_V1]] · [[VALEUR_INFORMATION]]
