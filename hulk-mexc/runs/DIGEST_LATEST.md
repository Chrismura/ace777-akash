# Hulk DIGEST — 2026-09-18T19:55:16Z

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
| ETHUSDT | IDLE | 1.68 | 3.56 | 0.24 | 0.08 | 584152517.26 | 0.08 | no_map |
| XRPUSDT | IDLE | 1.52 | 3.47 | 0.53 | 0.08 | 59819084.93 | 2.86 | n/a |
| BTCUSDT | IDLE | 0.85 | 1.67 | 0.15 | 0.06 | 715009006.86 | 0.0 | no_map |
| WUSDT | IDLE | 2.8 | 11.09 | 2.32 | 0.12 | 868240.78 | 6.28 | tvl≈1,582,338,243 |
| PYTHUSDT | IDLE | 1.18 | 2.82 | 0.86 | 0.08 | 685891.18 | 3.32 | tvl≈133,812,138 |
| CCUSDT | IDLE | 0.9 | 2.99 | 0.76 | 0.11 | 669030.22 | 4.55 | no_map |
| RIZEUSDT | IDLE | 1.95 | 32.04 | 13.18 | -0.12 | 57764.89 | 118.56 | no_map |
| ZBCNUSDT | IDLE | 1.86 | 3.53 | 1.25 | 0.03 | 230417.23 | 11.46 | n/a |
| HBARUSDT | IDLE | 1.11 | 2.19 | 0.2 | 0.05 | 596245.58 | 2.53 | empty_tvl |
| EDELUSDT | IDLE | 0.93 | 8.04 | 6.72 | 0.18 | 206238.27 | 21.4 | no_map |
| CHIPUSDT | IDLE | 0.88 | 4.08 | 2.59 | 0.14 | 188411.31 | 20.82 | no_map |
| RWAINCUSDT | IDLE | 1.64 | 3.28 | 0.0 | 0.02 | 7890.34 | 5.77 | no_map |
| BIOUSDT | IDLE | 1.13 | 3.06 | 0.65 | 0.09 | 87081.58 | 7.29 | n/a |
| FLUIDUSDT | IDLE | 2.52 | 9.71 | 2.74 | 0.12 | 2376.06 | 21.99 | tvl≈2,647,767,179 |
| KITEUSDT | IDLE | 1.18 | 2.15 | 1.38 | 0.05 | 77203.97 | 20.86 | no_map |
| REDUSDT | IDLE | 1.1 | 3.51 | 1.23 | 0.12 | 63248.41 | 22.08 | tvl≈2,630,264 |
| QNTUSDT | IDLE | 1.14 | 2.09 | 1.33 | 0.04 | 71358.7 | 7.85 | n/a |
| MNSRYUSDT | IDLE | 1.54 | 3.03 | 0.27 | 0.06 | 42849.57 | 39.43 | no_map |
| TELUSDT | IDLE | 1.19 | 3.35 | 1.84 | 0.07 | 98905.95 | 45.38 | no_map |
| RWAUSDT | IDLE | 0.89 | 1.63 | 0.95 | 0.01 | 58574.46 | 29.54 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
