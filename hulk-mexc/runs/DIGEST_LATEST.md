# Hulk DIGEST — 2026-08-22T02:23:12Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.45 | 9.18 | 0.1 | 0.15 | 6952833.7 | 15.37 | tvl≈112,886,663 |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.31 | 10.26 | 0.19 | 0.17 | 154529685.14 | 1.99 | n/a |
| HBARUSDT | IDLE | 2.3 | 4.99 | 0.0 | 0.08 | 962058.21 | 1.24 | empty_tvl |
| ZBCNUSDT | IDLE | 2.49 | 9.63 | 2.79 | 0.09 | 544132.12 | 11.13 | n/a |
| CCUSDT | IDLE | 1.69 | 6.27 | 0.0 | 0.15 | 656516.4 | 6.96 | no_map |
| CHIPUSDT | IDLE | 2.24 | 5.07 | 0.75 | -0.01 | 503722.31 | 3.02 | no_map |
| BIOUSDT | IDLE | 3.05 | 7.64 | 0.18 | 0.09 | 192802.73 | 14.69 | n/a |
| WUSDT | IDLE | 1.85 | 5.07 | 0.12 | 0.1 | 402116.13 | 7.01 | tvl≈1,646,654,250 |
| EDELUSDT | IDLE | 2.49 | 5.02 | 3.15 | -0.03 | 79693.18 | 67.04 | no_map |
| RIZEUSDT | IDLE | 1.98 | 8.52 | 3.95 | 0.11 | 61312.43 | 45.71 | no_map |
| REDUSDT | IDLE | 1.0 | 8.27 | 6.6 | 0.17 | 157025.27 | 8.14 | tvl≈2,314,909 |
| QNTUSDT | IDLE | 2.23 | 4.89 | 0.15 | 0.08 | 171100.77 | 5.98 | n/a |
| KITEUSDT | IDLE | 1.35 | 4.09 | 0.74 | 0.11 | 61750.45 | 12.61 | no_map |
| QAITUSDT | IDLE | 1.86 | 3.57 | 0.94 | 0.0 | 3916.13 | 39.49 | no_map |
| RWAINCUSDT | IDLE | 1.82 | 3.27 | 2.48 | 0.0 | 9379.52 | 54.17 | no_map |
| TELUSDT | IDLE | 2.15 | 5.11 | 1.23 | 0.04 | 178545.94 | 57.04 | no_map |
| FLUIDUSDT | IDLE | 1.44 | 3.69 | 2.03 | 0.07 | 4710.05 | 19.67 | tvl≈2,599,456,799 |
| RWAUSDT | IDLE | 1.06 | 2.08 | 0.24 | 0.04 | 54870.42 | 16.37 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
