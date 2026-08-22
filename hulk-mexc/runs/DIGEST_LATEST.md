# Hulk DIGEST — 2026-08-22T00:30:39Z

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
| PYTHUSDT | IDLE | 1.76 | 6.39 | 1.23 | 0.1 | 6383135.27 | 2.04 | tvl≈107,253,350 |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.0 | 8.23 | 0.73 | 0.15 | 144510969.0 | 2.05 | n/a |
| HBARUSDT | IDLE | 2.81 | 6.36 | 1.76 | 0.07 | 937377.57 | 2.52 | empty_tvl |
| ZBCNUSDT | IDLE | 2.87 | 11.25 | 2.3 | 0.12 | 533887.96 | 37.09 | n/a |
| CCUSDT | IDLE | 1.94 | 7.42 | 0.89 | 0.13 | 647831.66 | 8.88 | no_map |
| WUSDT | IDLE | 2.74 | 6.91 | 1.09 | 0.08 | 385623.14 | 11.23 | tvl≈1,638,353,418 |
| CHIPUSDT | IDLE | 1.62 | 3.56 | 1.25 | 0.02 | 552879.47 | 6.16 | no_map |
| BIOUSDT | IDLE | 2.29 | 5.04 | 1.02 | 0.02 | 185891.15 | 6.21 | n/a |
| EDELUSDT | IDLE | 2.62 | 5.5 | 1.95 | -0.02 | 79740.56 | 22.12 | no_map |
| RIZEUSDT | IDLE | 2.21 | 9.82 | 2.52 | 0.13 | 59818.43 | 45.1 | no_map |
| QAITUSDT | IDLE | 2.27 | 4.22 | 2.14 | -0.01 | 3715.41 | 19.88 | no_map |
| TELUSDT | IDLE | 2.84 | 6.89 | 0.61 | 0.05 | 186403.08 | 41.17 | no_map |
| QNTUSDT | IDLE | 2.56 | 5.42 | 1.42 | 0.06 | 170452.96 | 6.05 | n/a |
| REDUSDT | IDLE | 0.54 | 4.91 | 0.71 | 0.22 | 157851.51 | 17.34 | tvl≈2,226,572 |
| KITEUSDT | IDLE | 1.07 | 3.12 | 0.35 | 0.1 | 61058.46 | 9.19 | no_map |
| RWAINCUSDT | IDLE | 1.69 | 2.99 | 2.54 | 0.04 | 9704.24 | 59.19 | no_map |
| RWAUSDT | IDLE | 1.09 | 2.08 | 0.65 | 0.03 | 54688.28 | 16.42 | no_map |
| FLUIDUSDT | IDLE | 1.17 | 2.87 | 0.66 | 0.09 | 4845.77 | 21.77 | tvl≈2,603,605,946 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
