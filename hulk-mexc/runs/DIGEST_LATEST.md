# Hulk DIGEST — 2026-08-22T03:38:32Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.41 | 11.15 | 0.47 | 0.18 | 7970521.61 | 1.87 | tvl≈112,886,663 |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.47 | 14.16 | 1.15 | 0.2 | 164467182.99 | 6.33 | n/a |
| HBARUSDT | IDLE | 2.4 | 6.93 | 0.38 | 0.11 | 1032653.99 | 3.61 | empty_tvl |
| CCUSDT | IDLE | 1.95 | 8.96 | 0.84 | 0.18 | 687569.38 | 6.72 | no_map |
| CHIPUSDT | IDLE | 2.5 | 5.36 | 1.56 | -0.02 | 452708.16 | 11.93 | no_map |
| BIOUSDT | IDLE | 3.0 | 7.36 | 2.2 | 0.08 | 198710.23 | 3.0 | n/a |
| ZBCNUSDT | IDLE | 1.4 | 5.16 | 1.15 | 0.12 | 537146.15 | 17.6 | n/a |
| WUSDT | IDLE | 1.82 | 5.83 | 0.41 | 0.12 | 424009.05 | 8.87 | tvl≈1,672,612,247 |
| RIZEUSDT | IDLE | 1.82 | 7.71 | 4.42 | 0.1 | 59543.14 | 44.22 | no_map |
| REDUSDT | IDLE | 0.93 | 7.96 | 4.39 | 0.21 | 157919.25 | 10.34 | tvl≈2,314,909 |
| EDELUSDT | IDLE | 1.96 | 3.95 | 2.5 | -0.03 | 80429.19 | 66.82 | no_map |
| KITEUSDT | IDLE | 1.41 | 4.59 | 0.04 | 0.12 | 67786.27 | 11.57 | no_map |
| RWAINCUSDT | IDLE | 1.94 | 3.44 | 2.9 | 0.01 | 9343.86 | 54.47 | no_map |
| QNTUSDT | IDLE | 1.85 | 4.68 | 0.19 | 0.1 | 174252.15 | 7.39 | n/a |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | 0.0 | 3808.79 | 63.67 | no_map |
| RWAUSDT | IDLE | 1.5 | 2.97 | 0.16 | 0.06 | 56254.02 | 16.04 | no_map |
| TELUSDT | IDLE | 1.02 | 2.45 | 0.46 | 0.07 | 173585.67 | 30.67 | no_map |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.07 | 4710.05 | 20.89 | tvl≈2,594,231,317 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
