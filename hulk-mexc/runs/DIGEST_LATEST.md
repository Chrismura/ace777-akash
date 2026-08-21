# Hulk DIGEST — 2026-08-21T21:57:33Z

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
| PYTHUSDT | IDLE | 1.22 | 4.74 | 0.35 | 0.1 | 5686006.57 | 4.11 | tvl≈107,253,350 |
| XRPUSDT | IDLE | 1.09 | 3.73 | 0.74 | 0.12 | 129719983.6 | 1.43 | n/a |
| HBARUSDT | IDLE | 2.1 | 4.71 | 0.59 | 0.08 | 834168.64 | 1.27 | empty_tvl |
| CHIPUSDT | IDLE | 1.87 | 5.61 | 3.58 | 0.04 | 526940.01 | 6.19 | no_map |
| ZBCNUSDT | IDLE | 1.91 | 8.19 | 2.53 | 0.11 | 492691.5 | 28.29 | n/a |
| CCUSDT | IDLE | 1.3 | 3.92 | 0.0 | 0.11 | 636552.21 | 8.2 | no_map |
| WUSDT | IDLE | 2.11 | 4.19 | 0.25 | 0.07 | 367608.25 | 10.39 | tvl≈1,602,784,605 |
| BIOUSDT | IDLE | 2.36 | 5.2 | 1.11 | 0.04 | 186053.74 | 3.11 | n/a |
| REDUSDT | IDLE | 1.33 | 11.01 | 8.3 | 0.19 | 153814.55 | 8.92 | tvl≈2,226,572 |
| RIZEUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.03 | 10.4 | 1.07 | 0.05 | 56173.37 | 45.14 | no_map |
| TELUSDT | IDLE | 2.55 | 6.45 | 1.28 | 0.05 | 191831.86 | 10.41 | no_map |
| QAITUSDT | IDLE | 2.37 | 4.38 | 2.37 | -0.02 | 3827.91 | 59.7 | no_map |
| EDELUSDT | IDLE | 1.99 | 4.12 | 1.87 | -0.04 | 83425.1 | 67.04 | no_map |
| RWAINCUSDT | IDLE | 2.22 | 4.3 | 0.9 | 0.03 | 10238.87 | 53.39 | no_map |
| KITEUSDT | IDLE | 1.27 | 4.0 | 1.08 | 0.11 | 61321.17 | 11.01 | no_map |
| QNTUSDT | IDLE | 1.34 | 2.65 | 0.17 | 0.05 | 62428.37 | 4.62 | n/a |
| RWAUSDT | IDLE | 0.67 | 1.33 | 0.08 | 0.04 | 54144.07 | 8.23 | no_map |
| FLUIDUSDT | IDLE | 0.51 | 1.15 | 0.09 | 0.09 | 4171.26 | 20.37 | tvl≈2,562,752,708 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
