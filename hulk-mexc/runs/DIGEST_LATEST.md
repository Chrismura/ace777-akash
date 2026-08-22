# Hulk DIGEST — 2026-08-22T01:02:16Z

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
| PYTHUSDT | IDLE | 2.2 | 7.24 | 0.12 | 0.13 | 6551277.76 | 2.0 | tvl≈107,253,350 |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.21 | 8.4 | 1.44 | 0.15 | 148149908.71 | 1.37 | n/a |
| HBARUSDT | IDLE | 3.04 | 6.36 | 1.24 | 0.08 | 951661.28 | 1.25 | empty_tvl |
| ZBCNUSDT | IDLE | 2.6 | 10.08 | 2.87 | 0.11 | 543507.46 | 17.0 | n/a |
| CCUSDT | IDLE | 1.65 | 6.26 | 0.42 | 0.15 | 651471.52 | 10.61 | no_map |
| WUSDT | IDLE | 2.72 | 6.65 | 0.94 | 0.09 | 391980.9 | 8.16 | tvl≈1,638,353,418 |
| CHIPUSDT | IDLE | 1.55 | 3.56 | 0.18 | 0.02 | 536918.08 | 3.05 | no_map |
| BIOUSDT | IDLE | 2.32 | 5.18 | 0.55 | 0.04 | 186513.51 | 3.08 | n/a |
| EDELUSDT | IDLE | 2.64 | 5.5 | 2.28 | -0.02 | 79748.11 | 22.17 | no_map |
| RIZEUSDT | IDLE | 1.98 | 8.52 | 3.92 | 0.12 | 60301.52 | 45.71 | no_map |
| REDUSDT | IDLE | 0.94 | 8.27 | 2.93 | 0.2 | 159790.25 | 19.62 | tvl≈2,226,572 |
| QNTUSDT | IDLE | 2.42 | 5.18 | 0.94 | 0.07 | 170535.07 | 4.52 | n/a |
| TELUSDT | IDLE | 2.56 | 6.19 | 0.66 | 0.06 | 183845.62 | 41.26 | no_map |
| KITEUSDT | IDLE | 1.35 | 3.86 | 0.31 | 0.11 | 60779.76 | 12.7 | no_map |
| QAITUSDT | IDLE | 2.09 | 4.02 | 1.01 | 0.01 | 3850.39 | 67.05 | no_map |
| RWAINCUSDT | IDLE | 1.33 | 2.45 | 1.43 | 0.03 | 9646.54 | 16.16 | no_map |
| RWAUSDT | IDLE | 1.09 | 2.08 | 0.73 | 0.03 | 54868.6 | 16.45 | no_map |
| FLUIDUSDT | IDLE | 1.17 | 2.87 | 0.66 | 0.09 | 4845.77 | 12.55 | tvl≈2,603,605,946 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
