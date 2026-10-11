# Hulk DIGEST — 2026-10-11T17:24:17Z

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
| XRPUSDT | IDLE | 1.21 | 2.38 | 0.21 | 0.01 | 13548602.04 | 1.41 | n/a |
| ETHUSDT | IDLE | 1.09 | 2.14 | 0.3 | 0.02 | 212609142.7 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.61 | 1.21 | 0.06 | 0.01 | 149194861.55 | 0.0 | no_map |
| WUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.39 | 8.15 | 1.22 | 0.05 | 928843.7 | 10.85 | tvl≈1,674,589,277 |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 4.4 | 11.9 | 8.01 | -0.0 | 28167.1 | 4.92 | no_map |
| PYTHUSDT | IDLE | 1.33 | 2.51 | 0.99 | -0.03 | 769386.25 | 3.89 | tvl≈172,259,825 |
| CCUSDT | IDLE | 2.75 | 5.44 | 0.75 | 0.06 | 324439.44 | 7.14 | no_map |
| CHIPUSDT | IDLE | 1.68 | 9.0 | 3.89 | 0.22 | 410133.84 | 16.2 | no_map |
| EDELUSDT | IDLE | 1.77 | 3.17 | 2.41 | -0.0 | 404460.59 | 5.21 | no_map |
| QNTUSDT | IDLE | 1.09 | 2.06 | 0.76 | 0.0 | 858287.98 | 0.82 | n/a |
| ZBCNUSDT | IDLE | 2.63 | 5.23 | 0.25 | 0.04 | 176005.44 | 15.55 | n/a |
| TELUSDT | IDLE | 3.89 | 7.16 | 4.14 | -0.03 | 143244.66 | 11.52 | no_map |
| RIZEUSDT | IDLE | 2.01 | 5.52 | 1.02 | -0.03 | 31857.66 | 12.33 | no_map |
| REDUSDT | IDLE | 1.89 | 3.69 | 0.56 | 0.01 | 57934.05 | 14.39 | tvl≈3,713,830 |
| BIOUSDT | IDLE | 1.66 | 3.24 | 0.59 | 0.04 | 85672.96 | 6.63 | n/a |
| KITEUSDT | IDLE | 1.05 | 2.09 | 0.05 | -0.01 | 70449.27 | 10.92 | no_map |
| HBARUSDT | IDLE | 1.42 | 2.79 | 0.31 | 0.01 | 249001.48 | 3.2 | empty_tvl |
| RWAUSDT | IDLE | 1.3 | 2.54 | 0.39 | 0.01 | 50967.48 | 7.77 | no_map |
| FLUIDUSDT | IDLE | 0.73 | 5.76 | 0.25 | 0.09 | 55691.0 | 41.53 | tvl≈2,422,137,643 |
| MNSRYUSDT | IDLE | 0.86 | 1.66 | 0.39 | -0.01 | 30579.73 | 17.72 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
