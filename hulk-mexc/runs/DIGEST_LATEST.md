# Hulk DIGEST — 2026-08-21T22:30:11Z

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
| PYTHUSDT | IDLE | 1.36 | 5.17 | 0.33 | 0.11 | 5789395.14 | 2.05 | tvl≈107,253,350 |
| XRPUSDT | IDLE | 1.56 | 5.68 | 0.61 | 0.14 | 134040498.78 | 0.7 | n/a |
| CCUSDT | IDLE | 1.76 | 6.48 | 0.28 | 0.13 | 656013.72 | 6.24 | no_map |
| HBARUSDT | IDLE | 2.21 | 4.71 | 0.77 | 0.08 | 857971.26 | 1.27 | empty_tvl |
| WUSDT | IDLE | 2.46 | 5.3 | 0.25 | 0.08 | 370384.24 | 10.28 | tvl≈1,602,784,605 |
| CHIPUSDT | IDLE | 1.48 | 4.54 | 1.18 | 0.06 | 534256.9 | 3.05 | no_map |
| ZBCNUSDT | IDLE | 1.59 | 6.77 | 0.54 | 0.11 | 503513.75 | 23.15 | n/a |
| BIOUSDT | IDLE | 2.29 | 5.04 | 1.08 | 0.02 | 188057.23 | 3.11 | n/a |
| REDUSDT | IDLE | 1.32 | 11.01 | 7.99 | 0.18 | 156035.3 | 11.31 | tvl≈2,226,572 |
| EDELUSDT | IDLE | 2.3 | 5.04 | 0.33 | -0.03 | 82603.12 | 32.84 | no_map |
| RWAINCUSDT | IDLE | 2.22 | 4.07 | 2.43 | 0.02 | 10246.23 | 21.56 | no_map |
| TELUSDT | IDLE | 2.53 | 6.45 | 0.87 | 0.05 | 187115.04 | 10.36 | no_map |
| QAITUSDT | IDLE | 2.37 | 4.38 | 2.37 | -0.02 | 3827.91 | 63.67 | no_map |
| KITEUSDT | IDLE | 1.22 | 3.58 | 1.09 | 0.11 | 61390.54 | 10.14 | no_map |
| RIZEUSDT | IDLE | 0.95 | 4.7 | 1.69 | 0.06 | 56367.3 | 45.14 | no_map |
| QNTUSDT | IDLE | 1.85 | 3.71 | 0.0 | 0.05 | 65342.05 | 3.04 | n/a |
| RWAUSDT | IDLE | 0.89 | 1.75 | 0.16 | 0.04 | 54167.66 | 8.21 | no_map |
| FLUIDUSDT | IDLE | 0.51 | 1.15 | 0.08 | 0.09 | 4171.26 | 18.24 | tvl≈2,590,200,853 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
