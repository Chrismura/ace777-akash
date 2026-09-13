# Hulk DIGEST — 2026-09-13T15:40:20Z

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
| XRPUSDT | IDLE | 0.88 | 1.65 | 0.72 | -0.02 | 15026936.82 | 2.97 | n/a |
| ETHUSDT | IDLE | 0.7 | 1.35 | 0.29 | -0.02 | 240652435.77 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.51 | 0.98 | 0.23 | -0.0 | 292561086.42 | 0.0 | no_map |
| PYTHUSDT | IDLE | 2.28 | 4.38 | 1.26 | 0.0 | 432565.62 | 1.82 | tvl≈121,266,979 |
| CHIPUSDT | IDLE | 2.4 | 8.83 | 7.73 | -0.14 | 89261.8 | 13.85 | no_map |
| WUSDT | IDLE | 1.65 | 3.13 | 1.17 | 0.01 | 259432.82 | 13.02 | tvl≈1,471,657,497 |
| EDELUSDT | IDLE | 1.59 | 7.01 | 1.56 | 0.09 | 202996.88 | 15.82 | no_map |
| ZBCNUSDT | IDLE | 1.58 | 2.96 | 1.28 | -0.03 | 204433.11 | 13.49 | n/a |
| CCUSDT | IDLE | 0.84 | 1.6 | 0.52 | -0.03 | 287875.77 | 10.51 | no_map |
| REDUSDT | IDLE | 1.64 | 2.93 | 2.34 | 0.01 | 60961.32 | 18.41 | tvl≈2,363,783 |
| RIZEUSDT | IDLE | 0.76 | 12.36 | 3.41 | 0.06 | 92115.07 | 34.03 | no_map |
| BIOUSDT | IDLE | 1.12 | 2.03 | 1.36 | -0.02 | 69859.0 | 3.95 | n/a |
| KITEUSDT | IDLE | 1.08 | 1.89 | 1.85 | 0.01 | 63160.76 | 9.3 | no_map |
| RWAINCUSDT | IDLE | 0.86 | 1.65 | 0.45 | -0.01 | 6642.72 | 5.61 | no_map |
| HBARUSDT | IDLE | 1.15 | 2.12 | 1.18 | 0.01 | 191156.2 | 1.32 | empty_tvl |
| RWAUSDT | IDLE | 1.03 | 1.96 | 0.67 | -0.01 | 53549.04 | 7.45 | no_map |
| TELUSDT | IDLE | 0.88 | 1.65 | 0.75 | -0.05 | 89010.07 | 31.44 | no_map |
| QNTUSDT | IDLE | 0.81 | 1.49 | 0.87 | -0.01 | 36969.29 | 3.13 | n/a |
| FLUIDUSDT | IDLE | 0.63 | 1.11 | 1.05 | -0.0 | 1582.44 | 23.84 | tvl≈2,651,589,241 |
| MNSRYUSDT | IDLE | 0.15 | 0.29 | 0.04 | -0.0 | 32421.48 | 13.9 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
