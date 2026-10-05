# Hulk DIGEST — 2026-10-05T13:35:39Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| QNTUSDT | IDLE | 2.36 | 5.38 | 2.95 | 0.01 | 2921804.77 | 8.2 | n/a |
| XRPUSDT | IDLE | 0.66 | 1.2 | 0.85 | 0.01 | 32043748.52 | 1.32 | n/a |
| ETHUSDT | IDLE | 0.48 | 0.88 | 0.59 | 0.01 | 242915586.93 | 0.4 | no_map |
| BTCUSDT | IDLE | 0.46 | 0.84 | 0.59 | 0.01 | 558804835.64 | 0.0 | no_map |
| PYTHUSDT | IDLE | 2.09 | 3.72 | 3.05 | 0.01 | 545712.15 | 5.09 | tvl≈179,164,173 |
| WUSDT | IDLE | 1.55 | 2.73 | 2.48 | -0.03 | 517886.81 | 16.74 | tvl≈1,892,688,241 |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.3 | 24.98 | 6.85 | 0.22 | 42063.17 | 21.4 | tvl≈2,539,550,016 |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 3.05 | 7.15 | 6.56 | -0.05 | 8164.65 | 12.49 | no_map |
| EDELUSDT | IDLE | 1.59 | 2.86 | 2.17 | 0.0 | 374095.36 | 20.56 | no_map |
| ZBCNUSDT | IDLE | 1.9 | 3.86 | 2.81 | 0.03 | 214613.41 | 10.21 | n/a |
| CCUSDT | IDLE | 1.33 | 2.34 | 2.2 | 0.0 | 299000.92 | 0.8 | no_map |
| CHIPUSDT | IDLE | 1.56 | 3.65 | 3.05 | 0.06 | 142849.45 | 12.23 | no_map |
| BIOUSDT | IDLE | 1.79 | 3.28 | 2.03 | 0.03 | 89055.26 | 9.54 | n/a |
| HBARUSDT | IDLE | 1.26 | 2.25 | 1.75 | 0.01 | 471313.09 | 6.83 | empty_tvl |
| REDUSDT | IDLE | 1.06 | 1.85 | 1.78 | -0.02 | 88556.47 | 12.33 | tvl≈4,281,961 |
| KITEUSDT | IDLE | 0.99 | 1.75 | 1.54 | -0.05 | 66465.54 | 4.21 | no_map |
| TELUSDT | IDLE | 2.08 | 3.67 | 3.29 | 0.0 | 142637.33 | 26.17 | no_map |
| RIZEUSDT | IDLE | 1.09 | 7.51 | 0.13 | 0.18 | 38975.76 | 75.57 | no_map |
| RWAUSDT | IDLE | 0.25 | 0.44 | 0.44 | -0.01 | 52013.62 | 7.33 | no_map |
| MNSRYUSDT | IDLE | 0.19 | 0.37 | 0.06 | -0.0 | 40311.36 | 6.44 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
