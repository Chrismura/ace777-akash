# Hulk DIGEST — 2026-08-22T01:50:07Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.88 | 10.86 | 1.18 | 0.15 | 6835599.01 | 1.96 | tvl≈112,886,663 |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.36 | 10.52 | 0.01 | 0.16 | 152977315.49 | 5.3 | n/a |
| HBARUSDT | IDLE | 2.99 | 6.36 | 0.4 | 0.08 | 960303.31 | 3.73 | empty_tvl |
| ZBCNUSDT | IDLE | 2.6 | 10.08 | 2.74 | 0.08 | 554232.7 | 6.29 | n/a |
| CCUSDT | IDLE | 1.79 | 7.36 | 0.32 | 0.16 | 661358.34 | 7.87 | no_map |
| WUSDT | IDLE | 2.68 | 6.65 | 0.31 | 0.08 | 391706.25 | 12.17 | tvl≈1,638,353,418 |
| CHIPUSDT | IDLE | 1.6 | 3.56 | 0.91 | 0.01 | 512274.45 | 3.07 | no_map |
| BIOUSDT | IDLE | 2.59 | 5.86 | 0.09 | 0.06 | 185941.63 | 3.05 | n/a |
| EDELUSDT | IDLE | 2.63 | 5.5 | 2.06 | -0.02 | 79516.16 | 22.15 | no_map |
| RIZEUSDT | IDLE | 1.97 | 8.52 | 3.89 | 0.11 | 60974.5 | 45.71 | no_map |
| REDUSDT | IDLE | 0.98 | 8.27 | 4.94 | 0.17 | 157335.39 | 16.79 | tvl≈2,226,572 |
| QNTUSDT | IDLE | 2.44 | 5.18 | 1.25 | 0.06 | 171666.54 | 4.54 | n/a |
| KITEUSDT | IDLE | 1.6 | 5.17 | 0.16 | 0.12 | 61356.52 | 10.76 | no_map |
| TELUSDT | IDLE | 2.61 | 6.19 | 1.59 | 0.04 | 182082.05 | 41.58 | no_map |
| QAITUSDT | IDLE | 2.04 | 4.02 | 0.43 | 0.01 | 3870.41 | 31.31 | no_map |
| RWAINCUSDT | IDLE | 1.77 | 3.27 | 1.79 | 0.03 | 9235.4 | 90.93 | no_map |
| FLUIDUSDT | IDLE | 1.35 | 3.74 | 0.0 | 0.1 | 4798.05 | 21.27 | tvl≈2,603,605,946 |
| RWAUSDT | IDLE | 1.07 | 2.08 | 0.41 | 0.03 | 54605.05 | 8.2 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
