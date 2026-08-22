# Hulk DIGEST — 2026-08-22T03:10:24Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.38 | 10.96 | 0.11 | 0.18 | 7561865.49 | 13.06 | tvl≈112,886,663 |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.27 | 11.43 | 0.36 | 0.21 | 160483470.28 | 3.22 | n/a |
| HBARUSDT | IDLE | 2.15 | 5.29 | 0.24 | 0.1 | 996940.9 | 1.22 | empty_tvl |
| CCUSDT | IDLE | 1.94 | 8.96 | 0.46 | 0.19 | 671222.52 | 10.08 | no_map |
| BIOUSDT | IDLE | 3.02 | 7.36 | 2.4 | 0.06 | 195648.66 | 3.0 | n/a |
| CHIPUSDT | IDLE | 1.92 | 4.28 | 0.15 | -0.0 | 448882.7 | 2.98 | no_map |
| ZBCNUSDT | IDLE | 1.44 | 5.16 | 2.3 | 0.12 | 540860.19 | 24.05 | n/a |
| WUSDT | IDLE | 1.78 | 5.61 | 0.4 | 0.12 | 417355.1 | 10.86 | tvl≈1,646,654,250 |
| EDELUSDT | IDLE | 1.94 | 3.83 | 3.04 | -0.03 | 80070.92 | 11.19 | no_map |
| RIZEUSDT | IDLE | 1.82 | 7.71 | 4.26 | 0.1 | 59510.55 | 44.22 | no_map |
| REDUSDT | IDLE | 0.93 | 7.96 | 4.04 | 0.2 | 157935.38 | 12.67 | tvl≈2,314,909 |
| RWAINCUSDT | IDLE | 1.94 | 3.44 | 3.0 | -0.0 | 9452.18 | 32.45 | no_map |
| KITEUSDT | IDLE | 1.32 | 4.17 | 0.02 | 0.12 | 63770.6 | 13.41 | no_map |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.01 | 3813.17 | 63.67 | no_map |
| QNTUSDT | IDLE | 1.69 | 3.97 | 0.19 | 0.09 | 172854.43 | 4.46 | n/a |
| RWAUSDT | IDLE | 1.18 | 2.31 | 0.32 | 0.05 | 56171.21 | 8.09 | no_map |
| TELUSDT | IDLE | 0.91 | 2.19 | 0.36 | 0.07 | 173226.65 | 56.28 | no_map |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.07 | 4710.05 | 21.67 | tvl≈2,599,456,799 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
