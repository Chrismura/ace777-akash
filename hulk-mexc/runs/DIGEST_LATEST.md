# Hulk DIGEST — 2026-08-22T15:44:09Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : XRPUSDT, HBARUSDT, QAITUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT
- Watch only : QNTUSDT, FLUIDUSDT, RWAUSDT

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| PYTHUSDT | IDLE | 1.58 | 7.62 | 1.4 | 0.04 | 51498912.85 | 1.97 | tvl≈115,177,281 |
| XRPUSDT | IDLE | 1.39 | 7.64 | 6.06 | 0.02 | 216018872.52 | 2.09 | n/a |
| CCUSDT | IDLE | 1.33 | 5.65 | 3.21 | 0.08 | 790088.99 | 6.9 | no_map |
| HBARUSDT | IDLE | 0.85 | 3.03 | 2.22 | -0.02 | 1155786.6 | 1.31 | empty_tvl |
| CHIPUSDT | IDLE | 0.63 | 3.51 | 2.19 | -0.09 | 604957.38 | 6.8 | no_map |
| WUSDT | IDLE | 0.78 | 3.17 | 1.59 | -0.02 | 553334.18 | 11.75 | tvl≈1,556,368,553 |
| KITEUSDT | IDLE | 2.76 | 6.37 | 2.05 | 0.03 | 85395.29 | 8.96 | no_map |
| ZBCNUSDT | IDLE | 1.31 | 3.49 | 1.88 | -0.05 | 320040.08 | 16.97 | n/a |
| BIOUSDT | IDLE | 0.98 | 6.58 | 5.2 | -0.07 | 220947.94 | 6.65 | n/a |
| EDELUSDT | IDLE | 1.42 | 2.52 | 2.12 | -0.05 | 79058.97 | 22.78 | no_map |
| REDUSDT | IDLE | 0.53 | 5.67 | 5.15 | -0.13 | 143988.33 | 13.86 | tvl≈2,005,037 |
| QAITUSDT | IDLE | 1.99 | 3.76 | 1.48 | 0.01 | 2320.37 | 67.45 | no_map |
| RIZEUSDT | IDLE | 0.78 | 3.28 | 0.2 | 0.03 | 56478.94 | 21.94 | no_map |
| QNTUSDT | IDLE | 0.87 | 2.69 | 2.19 | -0.02 | 185112.21 | 4.73 | n/a |
| RWAINCUSDT | IDLE | 0.77 | 1.53 | 0.0 | 0.01 | 9767.54 | 75.23 | no_map |
| TELUSDT | IDLE | 1.11 | 2.75 | 1.63 | -0.01 | 140590.75 | 48.04 | no_map |
| FLUIDUSDT | IDLE | 0.98 | 1.87 | 1.32 | -0.04 | 4625.53 | 23.98 | tvl≈2,554,315,465 |
| RWAUSDT | IDLE | 0.65 | 1.23 | 0.4 | 0.02 | 57507.31 | 16.23 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
