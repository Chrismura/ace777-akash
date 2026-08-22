# Hulk DIGEST — 2026-08-22T04:07:59Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.82 | 12.59 | 0.73 | 0.19 | 9980866.56 | 7.4 | tvl≈112,886,663 |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.15 | 12.22 | 1.77 | 0.19 | 166702149.45 | 1.91 | n/a |
| CCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.08 | 11.33 | 0.0 | 0.22 | 717814.82 | 9.73 | no_map |
| HBARUSDT | IDLE | 2.11 | 6.03 | 0.63 | 0.1 | 1009420.32 | 1.2 | empty_tvl |
| CHIPUSDT | IDLE | 2.98 | 5.36 | 4.0 | -0.03 | 458643.57 | 9.22 | no_map |
| BIOUSDT | IDLE | 3.04 | 7.36 | 2.84 | 0.07 | 199608.07 | 3.02 | n/a |
| WUSDT | IDLE | 1.99 | 7.18 | 1.18 | 0.13 | 427691.86 | 12.7 | tvl≈1,672,612,247 |
| ZBCNUSDT | IDLE | 1.45 | 4.29 | 1.76 | 0.13 | 536764.64 | 20.06 | n/a |
| EDELUSDT | IDLE | 2.02 | 3.95 | 3.47 | -0.05 | 80456.25 | 22.47 | no_map |
| RIZEUSDT | IDLE | 1.86 | 7.71 | 5.04 | 0.09 | 59141.46 | 44.52 | no_map |
| REDUSDT | IDLE | 0.93 | 7.96 | 4.01 | 0.2 | 157818.83 | 18.21 | tvl≈2,314,909 |
| KITEUSDT | IDLE | 1.6 | 5.55 | 0.45 | 0.13 | 67584.27 | 10.62 | no_map |
| RWAINCUSDT | IDLE | 2.05 | 3.6 | 3.37 | 0.01 | 9366.1 | 43.55 | no_map |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3389.73 | 63.67 | no_map |
| QNTUSDT | IDLE | 1.56 | 3.8 | 0.86 | 0.09 | 178516.85 | 5.95 | n/a |
| RWAUSDT | IDLE | 1.54 | 3.05 | 0.24 | 0.06 | 56343.07 | 16.04 | no_map |
| TELUSDT | IDLE | 1.03 | 2.4 | 0.76 | 0.07 | 174266.14 | 46.0 | no_map |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.08 | 3702.43 | 18.84 | tvl≈2,594,231,317 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
