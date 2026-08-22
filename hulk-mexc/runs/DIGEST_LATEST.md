# Hulk DIGEST — 2026-08-22T03:56:36Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.49 | 11.77 | 1.48 | 0.17 | 9010592.04 | 3.76 | tvl≈112,886,663 |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.49 | 14.16 | 1.8 | 0.19 | 166161439.62 | 3.19 | n/a |
| HBARUSDT | IDLE | 2.4 | 6.93 | 0.44 | 0.1 | 1034573.46 | 1.2 | empty_tvl |
| CCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.07 | 10.39 | 0.31 | 0.2 | 702533.02 | 13.23 | no_map |
| CHIPUSDT | IDLE | 2.47 | 5.36 | 1.21 | -0.03 | 459405.4 | 2.98 | no_map |
| BIOUSDT | IDLE | 3.01 | 7.36 | 2.32 | 0.07 | 199238.51 | 3.0 | n/a |
| ZBCNUSDT | IDLE | 1.45 | 5.37 | 1.35 | 0.13 | 537827.7 | 23.8 | n/a |
| WUSDT | IDLE | 1.87 | 6.27 | 0.09 | 0.13 | 425277.21 | 13.69 | tvl≈1,672,612,247 |
| EDELUSDT | IDLE | 2.0 | 3.95 | 3.15 | -0.04 | 80633.65 | 33.69 | no_map |
| RIZEUSDT | IDLE | 1.82 | 7.71 | 4.46 | 0.1 | 59297.53 | 46.02 | no_map |
| REDUSDT | IDLE | 0.91 | 7.96 | 2.69 | 0.23 | 157679.23 | 18.75 | tvl≈2,314,909 |
| KITEUSDT | IDLE | 1.55 | 5.3 | 0.42 | 0.13 | 67556.55 | 12.42 | no_map |
| RWAINCUSDT | IDLE | 2.02 | 3.6 | 2.95 | 0.01 | 9351.15 | 43.55 | no_map |
| QNTUSDT | IDLE | 1.87 | 4.68 | 0.47 | 0.09 | 178469.26 | 4.45 | n/a |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3389.73 | 63.67 | no_map |
| RWAUSDT | IDLE | 1.62 | 3.22 | 0.16 | 0.06 | 56309.92 | 16.01 | no_map |
| TELUSDT | IDLE | 1.01 | 2.45 | 0.31 | 0.07 | 174048.57 | 40.86 | no_map |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.07 | 4710.05 | 18.09 | tvl≈2,594,231,317 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
