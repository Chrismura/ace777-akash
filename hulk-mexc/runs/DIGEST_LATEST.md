# Hulk DIGEST — 2026-08-22T03:18:49Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.39 | 10.96 | 0.47 | 0.17 | 7670630.89 | 5.62 | tvl≈112,886,663 |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.29 | 11.77 | 0.0 | 0.2 | 161250287.79 | 1.28 | n/a |
| HBARUSDT | IDLE | 2.23 | 5.87 | 0.0 | 0.11 | 1007045.24 | 1.21 | empty_tvl |
| CCUSDT | IDLE | 1.98 | 8.96 | 1.67 | 0.17 | 679681.73 | 8.5 | no_map |
| BIOUSDT | IDLE | 3.04 | 7.36 | 2.84 | 0.06 | 197937.73 | 3.02 | n/a |
| CHIPUSDT | IDLE | 1.94 | 4.28 | 0.39 | -0.01 | 450826.89 | 11.93 | no_map |
| ZBCNUSDT | IDLE | 1.43 | 5.16 | 1.96 | 0.13 | 539975.12 | 26.38 | n/a |
| WUSDT | IDLE | 1.79 | 5.61 | 0.48 | 0.12 | 417814.66 | 12.85 | tvl≈1,646,654,250 |
| EDELUSDT | IDLE | 1.95 | 3.83 | 3.15 | -0.03 | 79971.04 | 33.65 | no_map |
| RIZEUSDT | IDLE | 1.81 | 7.71 | 4.24 | 0.1 | 59506.18 | 44.22 | no_map |
| REDUSDT | IDLE | 0.93 | 7.96 | 3.97 | 0.2 | 158001.91 | 10.27 | tvl≈2,314,909 |
| KITEUSDT | IDLE | 1.39 | 4.4 | 0.38 | 0.12 | 67588.17 | 13.42 | no_map |
| RWAINCUSDT | IDLE | 1.94 | 3.44 | 3.0 | 0.01 | 9365.24 | 59.57 | no_map |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | 0.0 | 3808.79 | 63.67 | no_map |
| QNTUSDT | IDLE | 1.68 | 3.97 | 0.04 | 0.09 | 174156.77 | 7.43 | n/a |
| TELUSDT | IDLE | 0.93 | 2.19 | 0.71 | 0.07 | 173388.28 | 15.42 | no_map |
| RWAUSDT | IDLE | 1.3 | 2.56 | 0.24 | 0.05 | 56164.3 | 24.2 | no_map |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.07 | 4710.05 | 20.26 | tvl≈2,599,456,799 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
