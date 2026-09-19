# Hulk DIGEST — 2026-09-19T11:02:16Z

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
| ETHUSDT | IDLE | 0.82 | 1.52 | 0.78 | 0.05 | 564218239.6 | 0.04 | no_map |
| XRPUSDT | IDLE | 0.72 | 1.5 | 0.78 | 0.07 | 67886549.81 | 2.11 | n/a |
| BTCUSDT | IDLE | 0.38 | 0.7 | 0.35 | 0.04 | 633007441.67 | 0.0 | no_map |
| WUSDT | IDLE | 1.08 | 3.15 | 1.09 | 0.06 | 979481.92 | 9.16 | tvl≈1,591,350,724 |
| PYTHUSDT | IDLE | 1.04 | 2.01 | 0.45 | 0.01 | 720196.47 | 9.98 | tvl≈135,130,786 |
| EDELUSDT | IDLE | 2.3 | 12.85 | 10.19 | -0.14 | 192274.84 | 24.6 | no_map |
| HBARUSDT | IDLE | 1.66 | 3.25 | 0.47 | 0.04 | 597364.51 | 1.24 | empty_tvl |
| CCUSDT | IDLE | 0.75 | 1.44 | 0.45 | 0.02 | 417021.18 | 4.52 | no_map |
| KITEUSDT | IDLE | 2.27 | 4.34 | 1.36 | 0.05 | 70439.84 | 9.48 | no_map |
| CHIPUSDT | IDLE | 1.34 | 4.45 | 3.09 | 0.04 | 143549.0 | 20.07 | no_map |
| REDUSDT | IDLE | 1.1 | 5.45 | 2.91 | 0.07 | 131585.12 | 8.68 | tvl≈2,684,962 |
| ZBCNUSDT | IDLE | 1.18 | 2.27 | 0.64 | 0.01 | 178700.06 | 5.46 | n/a |
| BIOUSDT | IDLE | 1.39 | 2.73 | 0.29 | 0.02 | 76099.19 | 7.3 | n/a |
| QNTUSDT | IDLE | 1.53 | 3.02 | 0.31 | 0.02 | 75494.08 | 3.09 | n/a |
| RWAINCUSDT | IDLE | 0.71 | 1.26 | 1.02 | 0.03 | 5364.76 | 39.85 | no_map |
| TELUSDT | IDLE | 0.86 | 2.52 | 2.27 | 0.03 | 122089.19 | 45.23 | no_map |
| RIZEUSDT | IDLE | 0.25 | 2.07 | 1.0 | -0.07 | 38753.92 | 101.01 | no_map |
| FLUIDUSDT | IDLE | 0.89 | 3.21 | 0.0 | 0.14 | 11039.52 | 21.89 | tvl≈2,642,420,208 |
| RWAUSDT | IDLE | 0.54 | 0.96 | 0.81 | 0.0 | 56791.79 | 29.52 | no_map |
| MNSRYUSDT | IDLE | 0.29 | 0.55 | 0.17 | 0.04 | 39727.71 | 2.62 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
