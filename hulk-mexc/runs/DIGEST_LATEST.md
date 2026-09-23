# Hulk DIGEST — 2026-09-23T02:06:52Z

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
| PYTHUSDT | IDLE | 1.09 | 4.83 | 4.08 | 0.04 | 1777190.06 | 3.05 | tvl≈147,506,051 |
| XRPUSDT | IDLE | 1.55 | 2.92 | 1.26 | 0.05 | 104225245.53 | 3.16 | n/a |
| ETHUSDT | IDLE | 0.77 | 1.41 | 0.85 | 0.0 | 408623549.26 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.52 | 0.95 | 0.55 | 0.01 | 894109298.76 | 0.0 | no_map |
| HBARUSDT | IDLE | 0.91 | 2.27 | 0.7 | 0.09 | 1761675.72 | 1.0 | empty_tvl |
| WUSDT | IDLE | 1.96 | 3.56 | 2.45 | 0.02 | 318575.74 | 8.29 | tvl≈1,802,144,998 |
| CCUSDT | IDLE | 1.4 | 2.5 | 2.01 | -0.03 | 416699.93 | 10.54 | no_map |
| CHIPUSDT | IDLE | 2.37 | 4.74 | 1.73 | -0.02 | 122907.91 | 19.38 | no_map |
| BIOUSDT | IDLE | 2.1 | 3.82 | 2.5 | 0.02 | 129372.72 | 10.1 | n/a |
| EDELUSDT | IDLE | 1.31 | 6.49 | 1.52 | 0.01 | 263031.81 | 26.36 | no_map |
| RIZEUSDT | IDLE | 1.51 | 25.28 | 3.77 | 0.26 | 45362.11 | 94.2 | no_map |
| ZBCNUSDT | IDLE | 1.83 | 3.61 | 0.3 | 0.02 | 205563.23 | 34.9 | n/a |
| REDUSDT | IDLE | 1.14 | 1.98 | 1.95 | 0.01 | 59353.92 | 13.99 | tvl≈2,865,884 |
| RWAINCUSDT | IDLE | 1.26 | 3.01 | 2.82 | 0.02 | 19853.9 | 21.49 | no_map |
| KITEUSDT | IDLE | 0.68 | 2.75 | 1.5 | 0.15 | 125448.89 | 9.41 | no_map |
| QNTUSDT | IDLE | 1.18 | 4.09 | 2.3 | 0.12 | 212224.71 | 9.39 | n/a |
| TELUSDT | IDLE | 0.87 | 3.6 | 1.92 | 0.13 | 109435.48 | 21.81 | no_map |
| FLUIDUSDT | IDLE | 0.92 | 1.83 | 0.0 | 0.02 | 5475.4 | 19.69 | tvl≈2,641,875,696 |
| RWAUSDT | IDLE | 0.55 | 1.02 | 0.5 | 0.01 | 52682.33 | 14.42 | no_map |
| MNSRYUSDT | IDLE | 0.38 | 0.72 | 0.28 | 0.0 | 40160.45 | 24.37 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
