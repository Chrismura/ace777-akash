# Hulk DIGEST — 2026-08-21T22:26:42Z

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
| PYTHUSDT | IDLE | 1.36 | 5.17 | 0.16 | 0.11 | 5773887.62 | 4.09 | tvl≈107,253,350 |
| XRPUSDT | IDLE | 1.56 | 5.68 | 0.51 | 0.13 | 133819713.2 | 3.49 | n/a |
| CCUSDT | IDLE | 1.76 | 6.48 | 0.2 | 0.13 | 650070.85 | 9.79 | no_map |
| HBARUSDT | IDLE | 2.2 | 4.71 | 0.63 | 0.08 | 857851.05 | 2.53 | empty_tvl |
| WUSDT | IDLE | 2.46 | 5.3 | 0.26 | 0.08 | 370950.99 | 10.28 | tvl≈1,602,784,605 |
| CHIPUSDT | IDLE | 1.48 | 4.54 | 1.21 | 0.06 | 534172.37 | 6.1 | no_map |
| ZBCNUSDT | IDLE | 1.55 | 6.64 | 0.23 | 0.11 | 502579.64 | 20.66 | n/a |
| BIOUSDT | IDLE | 2.28 | 5.04 | 0.89 | 0.03 | 187913.5 | 3.1 | n/a |
| REDUSDT | IDLE | 1.32 | 11.01 | 8.04 | 0.19 | 156165.84 | 11.31 | tvl≈2,226,572 |
| EDELUSDT | IDLE | 2.03 | 4.47 | 0.11 | -0.03 | 82605.25 | 10.97 | no_map |
| QAITUSDT | IDLE | 2.37 | 4.38 | 2.37 | -0.02 | 3827.91 | 63.67 | no_map |
| TELUSDT | IDLE | 2.53 | 6.45 | 0.92 | 0.05 | 186900.61 | 41.49 | no_map |
| RWAINCUSDT | IDLE | 2.13 | 4.07 | 1.27 | 0.03 | 10238.87 | 64.76 | no_map |
| KITEUSDT | IDLE | 1.22 | 3.58 | 1.23 | 0.11 | 61373.96 | 12.92 | no_map |
| RIZEUSDT | IDLE | 0.95 | 4.7 | 1.69 | 0.06 | 56358.01 | 45.14 | no_map |
| QNTUSDT | IDLE | 1.84 | 3.69 | 0.0 | 0.05 | 65346.1 | 3.04 | n/a |
| RWAUSDT | IDLE | 0.91 | 1.75 | 0.49 | 0.03 | 54115.49 | 8.23 | no_map |
| FLUIDUSDT | IDLE | 0.51 | 1.15 | 0.08 | 0.09 | 4171.26 | 0.7 | tvl≈2,590,200,853 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
