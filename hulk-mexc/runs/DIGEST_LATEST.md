# Hulk DIGEST — 2026-10-16T15:01:13Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 2.65 | 8.3 | 5.17 | -0.01 | 3483697.0 | 1.13 | tvl≈206,072,259 |
| WUSDT | IDLE | 2.32 | 4.38 | 1.75 | 0.01 | 1720973.24 | 16.22 | tvl≈1,663,326,925 |
| XRPUSDT | IDLE | 1.11 | 1.94 | 1.88 | 0.0 | 23409373.03 | 2.26 | n/a |
| ETHUSDT | IDLE | 1.08 | 1.96 | 1.33 | 0.03 | 220036916.29 | 0.2 | no_map |
| BTCUSDT | IDLE | 0.83 | 1.49 | 1.16 | 0.0 | 365040169.72 | 0.02 | no_map |
| QNTUSDT | IDLE | 2.2 | 3.89 | 3.39 | -0.0 | 1079089.83 | 4.86 | n/a |
| CCUSDT | IDLE | 1.88 | 3.49 | 1.81 | -0.04 | 402893.96 | 7.65 | no_map |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 2.99 | 8.9 | 7.78 | -0.11 | 26058.01 | 10.72 | no_map |
| RIZEUSDT | IDLE | 2.73 | 8.3 | 2.28 | 0.03 | 53008.33 | 26.57 | no_map |
| CHIPUSDT | IDLE | 1.87 | 5.65 | 5.07 | 0.01 | 158131.67 | 12.68 | no_map |
| ZBCNUSDT | IDLE | 1.64 | 2.99 | 1.93 | 0.04 | 192697.74 | 2.67 | n/a |
| EDELUSDT | IDLE | 1.18 | 3.15 | 0.29 | 0.0 | 215158.64 | 16.27 | no_map |
| REDUSDT | IDLE | 1.5 | 4.3 | 1.41 | -0.01 | 91517.07 | 7.91 | tvl≈3,681,377 |
| KITEUSDT | IDLE | 1.55 | 2.74 | 2.42 | -0.01 | 68519.07 | 13.17 | no_map |
| BIOUSDT | IDLE | 1.46 | 2.59 | 2.25 | 0.01 | 61322.95 | 7.82 | n/a |
| HBARUSDT | IDLE | 1.1 | 1.92 | 1.88 | 0.03 | 290075.46 | 10.52 | empty_tvl |
| TELUSDT | IDLE | 1.05 | 2.03 | 0.5 | 0.04 | 92664.35 | 38.9 | no_map |
| FLUIDUSDT | IDLE | 1.16 | 2.12 | 1.29 | -0.02 | 6284.09 | 21.43 | tvl≈2,260,925,316 |
| RWAUSDT | IDLE | 0.26 | 0.47 | 0.31 | 0.01 | 51937.62 | 7.89 | no_map |
| MNSRYUSDT | IDLE | 0.11 | 0.21 | 0.11 | 0.01 | 38644.54 | 11.3 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
