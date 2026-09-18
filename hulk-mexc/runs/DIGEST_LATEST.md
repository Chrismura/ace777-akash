# Hulk DIGEST — 2026-09-18T17:55:21Z

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
| XRPUSDT | IDLE | 2.88 | 6.26 | 0.95 | 0.07 | 56597238.25 | 2.16 | n/a |
| ETHUSDT | IDLE | 2.3 | 4.59 | 0.08 | 0.06 | 512917095.11 | 0.92 | no_map |
| BTCUSDT | IDLE | 2.14 | 4.21 | 0.46 | 0.06 | 670631205.65 | 0.0 | no_map |
| WUSDT | IDLE | 2.95 | 12.29 | 4.11 | 0.13 | 899324.88 | 9.15 | tvl≈1,589,625,579 |
| PYTHUSDT | IDLE | 1.75 | 4.06 | 2.04 | 0.05 | 686880.19 | 1.68 | tvl≈133,812,138 |
| RIZEUSDT | IDLE | 1.96 | 32.25 | 12.66 | -0.08 | 57294.4 | 92.72 | no_map |
| CCUSDT | IDLE | 0.78 | 2.67 | 0.26 | 0.09 | 642631.78 | 6.39 | no_map |
| HBARUSDT | IDLE | 1.81 | 3.49 | 0.87 | 0.04 | 595724.89 | 1.27 | empty_tvl |
| ZBCNUSDT | IDLE | 1.93 | 3.53 | 2.22 | 0.03 | 238870.47 | 27.55 | n/a |
| CHIPUSDT | IDLE | 1.43 | 6.91 | 2.28 | 0.12 | 190398.91 | 13.84 | no_map |
| EDELUSDT | IDLE | 0.92 | 8.46 | 3.44 | -0.0 | 257477.86 | 20.73 | no_map |
| FLUIDUSDT | IDLE | 2.92 | 11.14 | 3.72 | 0.11 | 1905.69 | 21.88 | tvl≈2,647,458,765 |
| REDUSDT | IDLE | 1.55 | 5.0 | 1.46 | 0.11 | 64421.94 | 15.22 | tvl≈2,549,905 |
| BIOUSDT | IDLE | 1.2 | 3.28 | 0.47 | 0.08 | 87278.71 | 3.66 | n/a |
| KITEUSDT | IDLE | 1.19 | 2.18 | 1.38 | 0.05 | 78160.84 | 12.69 | no_map |
| RWAINCUSDT | IDLE | 1.23 | 2.45 | 0.0 | 0.01 | 7552.09 | 5.83 | no_map |
| QNTUSDT | IDLE | 1.83 | 3.45 | 1.46 | 0.04 | 72479.8 | 11.01 | n/a |
| TELUSDT | IDLE | 1.61 | 4.59 | 2.23 | 0.05 | 95466.17 | 58.54 | no_map |
| RWAUSDT | IDLE | 1.29 | 2.46 | 0.8 | 0.02 | 59745.69 | 22.03 | no_map |
| MNSRYUSDT | IDLE | 1.66 | 3.27 | 0.38 | 0.06 | 43349.58 | 56.9 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
