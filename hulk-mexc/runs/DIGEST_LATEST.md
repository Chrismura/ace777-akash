# Hulk DIGEST — 2026-09-18T00:17:29Z

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
| XRPUSDT | IDLE | 0.54 | 1.01 | 0.45 | -0.0 | 37000605.72 | 2.32 | n/a |
| ETHUSDT | IDLE | 0.49 | 0.88 | 0.65 | 0.01 | 291502080.22 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.34 | 0.62 | 0.42 | 0.0 | 416180897.5 | 0.0 | no_map |
| EDELUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.5 | 29.67 | 1.46 | -0.13 | 274991.15 | 26.04 | no_map |
| CCUSDT | IDLE | 1.77 | 3.51 | 0.18 | -0.0 | 508743.23 | 8.81 | no_map |
| PYTHUSDT | IDLE | 1.29 | 2.89 | 0.25 | 0.07 | 555586.11 | 3.52 | tvl≈125,357,356 |
| WUSDT | IDLE | 1.4 | 3.82 | 1.09 | 0.09 | 336315.45 | 17.01 | tvl≈1,469,713,968 |
| HBARUSDT | IDLE | 1.32 | 2.39 | 1.64 | 0.01 | 528788.17 | 1.34 | empty_tvl |
| REDUSDT | IDLE | 1.89 | 3.62 | 1.12 | 0.02 | 67062.27 | 27.94 | tvl≈2,360,052 |
| CHIPUSDT | IDLE | 1.11 | 3.04 | 0.44 | 0.05 | 175859.0 | 23.72 | no_map |
| ZBCNUSDT | IDLE | 0.9 | 1.69 | 0.76 | 0.01 | 201624.96 | 20.49 | n/a |
| KITEUSDT | IDLE | 1.06 | 2.02 | 0.62 | -0.01 | 60934.17 | 14.17 | no_map |
| BIOUSDT | IDLE | 0.79 | 1.57 | 0.04 | 0.01 | 67946.43 | 7.92 | n/a |
| TELUSDT | IDLE | 1.85 | 3.26 | 2.88 | -0.03 | 73757.32 | 42.43 | no_map |
| RWAINCUSDT | IDLE | 0.41 | 0.71 | 0.71 | -0.02 | 14029.11 | 23.85 | no_map |
| RIZEUSDT | IDLE | 0.81 | 5.38 | 3.95 | -0.04 | 42784.4 | 148.87 | no_map |
| QNTUSDT | IDLE | 0.67 | 1.23 | 0.72 | -0.0 | 40505.03 | 6.56 | n/a |
| RWAUSDT | IDLE | 0.33 | 0.6 | 0.37 | 0.0 | 56858.44 | 22.4 | no_map |
| MNSRYUSDT | IDLE | 0.11 | 0.21 | 0.06 | 0.01 | 42977.51 | 2.79 | no_map |
| FLUIDUSDT | IDLE | 0.22 | 0.39 | 0.39 | 0.02 | 148.34 | 23.48 | tvl≈2,607,123,588 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
