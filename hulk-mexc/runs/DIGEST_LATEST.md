# Hulk DIGEST — 2026-10-13T06:56:47Z

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
| PYTHUSDT | IDLE | 3.09 | 12.26 | 2.34 | 0.07 | 3795480.15 | 3.48 | tvl≈187,461,878 |
| WUSDT | IDLE | 0.67 | 11.65 | 4.52 | -0.34 | 10540972.62 | 11.24 | tvl≈1,772,943,912 |
| ETHUSDT | IDLE | 2.42 | 4.82 | 0.08 | -0.01 | 265015985.16 | 0.35 | no_map |
| XRPUSDT | IDLE | 2.16 | 4.38 | 0.02 | -0.03 | 35423530.34 | 0.73 | n/a |
| BTCUSDT | IDLE | 1.52 | 3.02 | 0.15 | -0.0 | 374940682.4 | 0.0 | no_map |
| CCUSDT | IDLE | 2.94 | 6.66 | 0.44 | -0.02 | 406220.31 | 7.22 | no_map |
| QNTUSDT | IDLE | 1.69 | 4.41 | 1.08 | -0.05 | 919263.4 | 2.19 | n/a |
| KITEUSDT | IDLE | 2.56 | 7.42 | 0.23 | 0.01 | 66206.7 | 7.76 | no_map |
| ZBCNUSDT | IDLE | 2.11 | 4.15 | 0.41 | -0.02 | 221154.74 | 17.94 | n/a |
| BIOUSDT | IDLE | 2.22 | 7.89 | 0.88 | -0.05 | 75115.78 | 7.09 | n/a |
| REDUSDT | IDLE | 1.03 | 7.52 | 0.96 | -0.01 | 312659.09 | 15.15 | tvl≈3,962,951 |
| HBARUSDT | IDLE | 1.41 | 4.24 | 0.59 | -0.07 | 550548.3 | 2.27 | empty_tvl |
| CHIPUSDT | IDLE | 1.76 | 7.98 | 0.0 | -0.06 | 146525.39 | 13.19 | no_map |
| FLUIDUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.8 | 8.59 | 0.0 | 0.07 | 13936.54 | 22.93 | tvl≈2,397,820,079 |
| EDELUSDT | IDLE | 0.91 | 3.88 | 1.14 | -0.12 | 279276.54 | 21.14 | no_map |
| RWAINCUSDT | IDLE | 1.76 | 5.01 | 0.43 | 0.05 | 40718.49 | 9.71 | no_map |
| TELUSDT | IDLE | 2.47 | 4.81 | 0.89 | 0.03 | 112425.28 | 28.21 | no_map |
| RIZEUSDT | IDLE | 0.47 | 3.02 | 0.44 | -0.12 | 67267.81 | 8.34 | no_map |
| RWAUSDT | IDLE | 0.87 | 1.72 | 0.15 | 0.0 | 53471.6 | 7.71 | no_map |
| MNSRYUSDT | IDLE | 1.01 | 1.97 | 0.29 | -0.01 | 39917.33 | 52.52 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
