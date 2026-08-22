# Hulk DIGEST — 2026-08-22T14:59:15Z

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
| PYTHUSDT | IDLE | 1.59 | 7.62 | 1.81 | 0.04 | 51452920.95 | 3.96 | tvl≈110,752,782 |
| XRPUSDT | IDLE | 1.36 | 7.58 | 5.28 | 0.03 | 213839466.91 | 6.21 | n/a |
| CCUSDT | IDLE | 1.38 | 6.16 | 3.21 | 0.11 | 797976.05 | 8.57 | no_map |
| HBARUSDT | IDLE | 0.96 | 3.34 | 2.91 | -0.01 | 1178459.55 | 5.24 | empty_tvl |
| WUSDT | IDLE | 1.11 | 4.43 | 3.02 | -0.02 | 563089.2 | 13.91 | tvl≈1,572,799,710 |
| CHIPUSDT | IDLE | 0.63 | 3.51 | 2.23 | -0.1 | 614406.03 | 3.4 | no_map |
| KITEUSDT | IDLE | 2.72 | 6.37 | 1.48 | 0.04 | 84549.9 | 22.27 | no_map |
| ZBCNUSDT | IDLE | 1.54 | 4.21 | 1.35 | -0.06 | 323833.14 | 18.29 | n/a |
| BIOUSDT | IDLE | 0.98 | 6.58 | 5.36 | -0.06 | 226342.81 | 6.66 | n/a |
| EDELUSDT | IDLE | 1.46 | 2.63 | 1.9 | -0.04 | 78994.17 | 22.73 | no_map |
| QAITUSDT | IDLE | 2.01 | 3.76 | 1.79 | -0.01 | 2374.33 | 67.45 | no_map |
| REDUSDT | IDLE | 0.42 | 5.1 | 4.45 | -0.03 | 150674.95 | 20.17 | tvl≈2,031,082 |
| RIZEUSDT | IDLE | 0.79 | 3.28 | 0.47 | 0.03 | 46758.8 | 43.92 | no_map |
| RWAINCUSDT | IDLE | 1.26 | 2.4 | 0.85 | 0.01 | 9946.26 | 75.23 | no_map |
| QNTUSDT | IDLE | 0.87 | 2.69 | 2.17 | -0.01 | 188438.57 | 6.31 | n/a |
| TELUSDT | IDLE | 1.3 | 3.24 | 1.78 | 0.01 | 140177.18 | 37.26 | no_map |
| RWAUSDT | IDLE | 0.82 | 1.55 | 0.56 | 0.02 | 57242.87 | 16.22 | no_map |
| FLUIDUSDT | IDLE | 0.98 | 1.87 | 1.32 | -0.04 | 4682.03 | 20.9 | tvl≈2,554,943,805 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
