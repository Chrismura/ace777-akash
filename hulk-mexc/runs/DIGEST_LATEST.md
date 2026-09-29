# Hulk DIGEST — 2026-09-29T08:45:02Z

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
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 2.57 | 26.71 | 7.23 | 0.03 | 11641709.28 | 10.03 | n/a |
| ETHUSDT | IDLE | 1.55 | 2.97 | 0.8 | 0.03 | 397105645.17 | 0.04 | no_map |
| XRPUSDT | IDLE | 1.42 | 2.71 | 0.89 | 0.02 | 58970634.44 | 0.67 | n/a |
| WUSDT | IDLE | 3.71 | 8.66 | 3.06 | 0.02 | 1127887.26 | 12.7 | tvl≈1,834,878,855 |
| HBARUSDT | IDLE | 0.93 | 4.54 | 3.66 | 0.09 | 11385348.58 | 5.98 | empty_tvl |
| BTCUSDT | IDLE | 0.92 | 1.76 | 0.51 | 0.01 | 669660350.0 | 0.0 | no_map |
| PYTHUSDT | IDLE | 2.1 | 3.85 | 2.31 | -0.0 | 1037001.3 | 3.77 | tvl≈180,706,208 |
| CCUSDT | IDLE | 0.95 | 3.51 | 2.31 | -0.03 | 1207557.8 | 7.57 | no_map |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 4.36 | 15.81 | 9.31 | -0.03 | 58743.18 | 93.1 | no_map |
| BIOUSDT | IDLE | 3.48 | 6.79 | 1.13 | 0.04 | 90462.84 | 9.8 | n/a |
| CHIPUSDT | IDLE | 2.94 | 6.66 | 1.51 | 0.01 | 73816.85 | 15.75 | no_map |
| ZBCNUSDT | IDLE | 1.5 | 4.69 | 0.3 | 0.1 | 250886.04 | 14.49 | n/a |
| KITEUSDT | IDLE | 2.19 | 4.05 | 2.2 | -0.0 | 75839.03 | 8.01 | no_map |
| TELUSDT | IDLE | 1.18 | 12.01 | 1.51 | 0.28 | 419488.68 | 43.57 | no_map |
| FLUIDUSDT | IDLE | 3.14 | 6.78 | 0.0 | 0.07 | 3805.76 | 21.76 | tvl≈2,609,352,782 |
| REDUSDT | IDLE | 1.35 | 2.71 | 0.0 | 0.0 | 57460.71 | 14.85 | tvl≈2,903,336 |
| RIZEUSDT | IDLE | 1.33 | 4.09 | 3.25 | 0.08 | 39208.68 | 70.57 | no_map |
| EDELUSDT | IDLE | 0.47 | 2.73 | 0.3 | 0.04 | 116331.56 | 7.63 | no_map |
| MNSRYUSDT | IDLE | 0.98 | 1.96 | 0.05 | -0.01 | 34697.23 | 5.16 | no_map |
| RWAUSDT | IDLE | 0.76 | 1.46 | 0.43 | -0.0 | 56703.49 | 7.22 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
