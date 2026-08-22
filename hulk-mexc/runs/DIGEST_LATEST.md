# Hulk DIGEST — 2026-08-22T05:05:23Z

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
| PYTHUSDT | IDLE | 3.24 | 15.45 | 3.92 | 0.16 | 13801668.46 | 22.37 | tvl≈112,886,663 |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.51 | 19.3 | 0.69 | 0.29 | 182915325.41 | 4.15 | n/a |
| HBARUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.57 | 10.33 | 0.05 | 0.16 | 1123006.39 | 2.3 | empty_tvl |
| CCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.14 | 11.56 | 0.96 | 0.21 | 743854.99 | 5.72 | no_map |
| CHIPUSDT | IDLE | 2.8 | 5.36 | 1.56 | 0.01 | 446784.49 | 2.99 | no_map |
| WUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.13 | 8.22 | 0.83 | 0.15 | 450213.26 | 10.57 | tvl≈1,672,612,247 |
| BIOUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.03 | 9.0 | 0.12 | 0.1 | 203381.84 | 2.89 | n/a |
| ZBCNUSDT | IDLE | 1.53 | 4.29 | 1.26 | 0.11 | 537593.16 | 20.89 | n/a |
| QNTUSDT | IDLE | 2.73 | 9.16 | 3.98 | 0.1 | 187025.78 | 19.09 | n/a |
| RWAINCUSDT | IDLE | 2.48 | 4.48 | 3.24 | 0.01 | 10345.47 | 21.57 | no_map |
| REDUSDT | IDLE | 1.01 | 7.96 | 6.19 | 0.18 | 158145.43 | 12.16 | tvl≈2,314,909 |
| KITEUSDT | IDLE | 1.82 | 6.62 | 0.41 | 0.15 | 68335.27 | 14.0 | no_map |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3417.27 | 35.86 | no_map |
| TELUSDT | IDLE | 1.95 | 5.52 | 0.44 | 0.1 | 184076.65 | 29.75 | no_map |
| RIZEUSDT | IDLE | 1.08 | 4.41 | 3.53 | 0.09 | 58620.92 | 46.02 | no_map |
| EDELUSDT | IDLE | 1.49 | 3.28 | 0.11 | -0.02 | 80250.28 | 88.4 | no_map |
| RWAUSDT | IDLE | 1.69 | 3.38 | 0.0 | 0.07 | 56824.41 | 15.96 | no_map |
| FLUIDUSDT | IDLE | 0.88 | 2.07 | 2.03 | 0.08 | 3692.42 | 37.29 | tvl≈2,594,231,317 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
