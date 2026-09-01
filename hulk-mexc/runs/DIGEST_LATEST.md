# Hulk DIGEST — 2026-09-01T21:27:14Z

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
| XRPUSDT | IDLE | 1.67 | 3.01 | 2.24 | -0.03 | 34398724.29 | 1.48 | n/a |
| ETHUSDT | IDLE | 1.51 | 2.8 | 1.42 | -0.02 | 331204880.74 | 0.04 | no_map |
| BTCUSDT | IDLE | 1.09 | 2.04 | 0.98 | -0.02 | 534710969.57 | 0.0 | no_map |
| CHIPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.2 | 11.2 | 1.81 | 0.16 | 631411.68 | 6.64 | no_map |
| PYTHUSDT | IDLE | 2.0 | 3.94 | 0.41 | 0.04 | 661512.97 | 3.92 | tvl≈113,597,849 |
| ZBCNUSDT | IDLE | 3.53 | 6.37 | 4.6 | 0.01 | 201364.46 | 1.62 | n/a |
| WUSDT | IDLE | 1.99 | 4.18 | 1.31 | 0.08 | 395001.04 | 19.37 | tvl≈1,517,233,965 |
| CCUSDT | IDLE | 1.56 | 3.39 | 3.01 | -0.08 | 334474.07 | 10.6 | no_map |
| REDUSDT | IDLE | 1.92 | 5.97 | 3.15 | 0.09 | 115291.46 | 13.08 | tvl≈2,090,812 |
| BIOUSDT | IDLE | 1.96 | 3.43 | 3.24 | -0.04 | 70441.83 | 3.94 | n/a |
| RIZEUSDT | IDLE | 2.63 | 4.92 | 3.34 | -0.05 | 43738.28 | 75.1 | no_map |
| EDELUSDT | IDLE | 0.85 | 6.39 | 5.66 | -0.09 | 134645.11 | 9.23 | no_map |
| KITEUSDT | IDLE | 1.58 | 3.03 | 0.86 | 0.04 | 68570.91 | 10.56 | no_map |
| TELUSDT | IDLE | 2.66 | 4.83 | 3.27 | -0.05 | 93967.58 | 42.18 | no_map |
| RWAINCUSDT | IDLE | 1.48 | 2.8 | 1.04 | -0.02 | 6420.69 | 17.56 | no_map |
| FLUIDUSDT | IDLE | 2.52 | 4.41 | 4.22 | -0.03 | 129.84 | 21.91 | tvl≈2,577,163,826 |
| HBARUSDT | IDLE | 0.89 | 1.66 | 0.84 | 0.0 | 250406.87 | 1.35 | empty_tvl |
| QNTUSDT | IDLE | 1.56 | 2.79 | 2.19 | 0.03 | 47421.08 | 7.94 | n/a |
| MNSRYUSDT | IDLE | 0.94 | 1.66 | 1.45 | -0.03 | 34325.81 | 44.05 | no_map |
| RWAUSDT | IDLE | 0.41 | 0.93 | 0.69 | -0.01 | 59349.19 | 7.72 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
