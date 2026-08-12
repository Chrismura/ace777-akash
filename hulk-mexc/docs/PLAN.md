# Plan Hulk MEXC — dip & rip

## Stratégie (v0 — simple)

Sur chaque symbole **admis** (filtre liquidité) :

1. **Buy dip** : prix baisse ≥ `DIP_PCT` vs référence courte (ex. high 1h ou SMA)  
2. **Sell rip / spike** : rebond ≥ `RIP_PCT` depuis entry **ou** take-profit / stop  
3. Une position à la fois par symbole (v0)  
4. Notionnel petit (paper d’abord)

## Liquidité vs spike

| Risque | Garde-fou v0 |
|--------|----------------|
| Spread large | `MAX_SPREAD_BPS` |
| Volume mort | `MIN_QUOTE_VOL_USDT` 24h |
| Spike sans exit | size plafonnée ; stop obligatoire |
| Liste trop large (50) | tiers A (liquide) / B (spike illiquide, paper only) |

## Tiers

- **A — tradeable test** : volume/spread OK sur MEXC  
- **B — watch spike** : faible volume, paper ou taille microscopique  
- **C — skip** : pas de paire USDT MEXC

## Cadence

0. Inventaire MEXC ✓ (`scripts/inventory_mexc.py`)  
1. **Paper v1.4** → `scripts/paper_diprip.py`  
   - Pleine mise (20$) → à **2× (40$)** vend **50%** (récupère la mise)  
   - Reste = **bag maison** ; lent → DCA ; crash → vend **90%**  
   - Cash récupéré → redeploy 100% sur dip  
   - Volume sniffer small-caps + sense + compound  
2. Mesurer fills / bags dans `runs/PAPER_V1_*.csv`  
2b. **Veille** : `scripts/digest_watch.py` → Qwen lit `DIGEST_LATEST.md` (`docs/VEILLE_QWEN.md`)  
3. Ajuster SPIKE / IMPULSE / mult cadence  
4. Tiny live MEXC (clés `~/.mexc.env`)  
5. Tier B illiquide en dernier (QAIT déjà en paper watch)

## Séparation ACE

Aucun import du genesis NUAGE. API MEXC seule. Clés dans `~/.mexc.env` (à créer) — jamais commit.
