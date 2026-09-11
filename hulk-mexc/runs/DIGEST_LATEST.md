# Hulk DIGEST — 2026-09-11T15:20:17Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.61 | 130.41 | 30.1 | 0.46 | 144869.69 | 64.31 | no_map |
| XRPUSDT | IDLE | 4.2 | 8.82 | 3.03 | 0.02 | 50870035.45 | 1.44 | n/a |
| ETHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 4.06 | 9.44 | 1.99 | 0.07 | 570461243.34 | 0.04 | no_map |
| BTCUSDT | IDLE | 2.58 | 4.93 | 1.49 | 0.02 | 524423966.49 | 0.0 | no_map |
| CCUSDT | IDLE | 4.02 | 7.68 | 2.37 | -0.01 | 476962.07 | 9.03 | no_map |
| PYTHUSDT | IDLE | 3.93 | 7.72 | 0.93 | 0.03 | 370306.5 | 1.87 | tvl≈114,862,105 |
| EDELUSDT | IDLE | 4.06 | 7.66 | 3.11 | -0.01 | 195348.2 | 9.16 | no_map |
| WUSDT | IMPULSE_WAIT — spike en cours, pas chase | 4.06 | 8.01 | 0.7 | 0.04 | 173390.15 | 12.08 | tvl≈1,491,265,667 |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 4.08 | 8.51 | 6.13 | 0.02 | 10003.35 | 27.63 | no_map |
| REDUSDT | IDLE | 3.84 | 7.46 | 1.43 | 0.03 | 61177.53 | 18.33 | tvl≈2,189,903 |
| BIOUSDT | IDLE | 3.33 | 6.49 | 1.08 | 0.02 | 81172.01 | 11.68 | n/a |
| CHIPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.91 | 9.52 | 0.08 | 0.03 | 138074.15 | 20.45 | no_map |
| ZBCNUSDT | IDLE | 2.87 | 5.61 | 0.86 | 0.03 | 175347.89 | 16.45 | n/a |
| TELUSDT | IDLE | 4.15 | 8.79 | 2.21 | 0.01 | 103937.51 | 55.25 | no_map |
| KITEUSDT | IDLE | 2.09 | 4.0 | 1.23 | 0.0 | 59462.88 | 12.76 | no_map |
| HBARUSDT | IDLE | 2.61 | 5.04 | 1.25 | 0.01 | 207383.9 | 1.31 | empty_tvl |
| QNTUSDT | IDLE | 2.77 | 5.19 | 2.39 | 0.0 | 40860.93 | 7.63 | n/a |
| FLUIDUSDT | IDLE | 2.47 | 4.94 | 0.0 | 0.03 | 1301.56 | 22.06 | tvl≈2,667,882,720 |
| RWAUSDT | IDLE | 1.63 | 3.2 | 0.44 | 0.02 | 51172.62 | 29.72 | no_map |
| MNSRYUSDT | IDLE | 1.62 | 3.1 | 0.95 | 0.02 | 38243.64 | 49.64 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
