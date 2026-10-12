# Hulk DIGEST — 2026-10-12T10:28:49Z

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
| WUSDT | IDLE | 0.82 | 15.49 | 11.21 | 0.61 | 14211453.84 | 15.59 | tvl≈1,756,543,167 |
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.93 | 9.68 | 1.08 | 0.11 | 1487953.62 | 3.51 | tvl≈188,677,247 |
| XRPUSDT | IDLE | 0.84 | 1.48 | 1.38 | 0.01 | 23748821.78 | 2.14 | n/a |
| BTCUSDT | IDLE | 0.68 | 1.22 | 0.95 | 0.01 | 239433086.67 | 0.0 | no_map |
| ETHUSDT | IDLE | 0.65 | 1.17 | 0.89 | 0.02 | 251608516.27 | 0.04 | no_map |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.68 | 25.76 | 5.76 | 0.21 | 122759.14 | 64.88 | tvl≈4,030,883 |
| QNTUSDT | IDLE | 2.16 | 3.88 | 2.99 | -0.03 | 823046.71 | 1.27 | n/a |
| CHIPUSDT | IDLE | 2.55 | 7.86 | 3.96 | -0.05 | 193292.4 | 12.38 | no_map |
| CCUSDT | IDLE | 0.9 | 1.61 | 1.27 | 0.04 | 393951.36 | 8.77 | no_map |
| HBARUSDT | IDLE | 1.41 | 2.46 | 2.4 | 0.02 | 473912.46 | 6.46 | empty_tvl |
| ZBCNUSDT | IDLE | 0.94 | 1.91 | 0.62 | 0.07 | 278688.21 | 11.64 | n/a |
| BIOUSDT | IDLE | 1.52 | 2.66 | 2.59 | 0.0 | 102092.35 | 3.41 | n/a |
| EDELUSDT | IDLE | 1.31 | 2.5 | 0.81 | -0.02 | 244195.18 | 45.06 | no_map |
| RIZEUSDT | IDLE | 1.13 | 6.93 | 3.58 | 0.11 | 47647.08 | 39.28 | no_map |
| KITEUSDT | IDLE | 1.25 | 2.48 | 0.17 | 0.03 | 62300.33 | 11.51 | no_map |
| TELUSDT | IDLE | 1.84 | 3.49 | 1.24 | 0.02 | 184297.83 | 5.68 | no_map |
| RWAINCUSDT | IDLE | 0.71 | 1.99 | 1.5 | -0.01 | 18858.99 | 15.17 | no_map |
| MNSRYUSDT | IDLE | 0.73 | 1.28 | 1.25 | 0.0 | 37866.29 | 4.1 | no_map |
| FLUIDUSDT | IDLE | 0.36 | 2.76 | 0.66 | 0.05 | 63453.83 | 21.69 | tvl≈2,427,449,782 |
| RWAUSDT | IDLE | 0.3 | 0.54 | 0.38 | 0.03 | 52404.23 | 7.72 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
