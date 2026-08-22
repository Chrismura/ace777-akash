# Hulk DIGEST — 2026-08-22T15:16:12Z

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
| PYTHUSDT | IDLE | 1.58 | 7.62 | 1.48 | 0.04 | 51473735.83 | 3.95 | tvl≈110,752,782 |
| XRPUSDT | IDLE | 1.36 | 7.49 | 6.08 | 0.02 | 214637073.03 | 1.39 | n/a |
| CCUSDT | IDLE | 1.32 | 5.65 | 2.94 | 0.1 | 800857.53 | 7.73 | no_map |
| HBARUSDT | IDLE | 0.82 | 2.85 | 2.49 | -0.02 | 1172838.37 | 2.62 | empty_tvl |
| CHIPUSDT | IDLE | 0.64 | 3.51 | 2.92 | -0.11 | 613745.46 | 6.84 | no_map |
| KITEUSDT | IDLE | 2.82 | 6.37 | 3.0 | 0.02 | 85095.42 | 0.9 | no_map |
| WUSDT | IDLE | 0.8 | 3.17 | 2.24 | -0.03 | 559317.58 | 16.12 | tvl≈1,572,799,710 |
| ZBCNUSDT | IDLE | 1.32 | 3.49 | 1.92 | -0.07 | 324747.91 | 19.55 | n/a |
| BIOUSDT | IDLE | 0.98 | 6.58 | 5.36 | -0.07 | 226801.45 | 3.33 | n/a |
| REDUSDT | IDLE | 0.53 | 5.57 | 5.28 | -0.05 | 150615.83 | 12.02 | tvl≈2,031,082 |
| QAITUSDT | IDLE | 1.99 | 3.76 | 1.48 | 0.01 | 2320.37 | 67.45 | no_map |
| EDELUSDT | IDLE | 1.44 | 2.52 | 2.35 | -0.05 | 79097.4 | 45.66 | no_map |
| RIZEUSDT | IDLE | 0.79 | 3.28 | 0.35 | 0.03 | 46081.29 | 43.92 | no_map |
| QNTUSDT | IDLE | 0.87 | 2.69 | 2.34 | -0.02 | 188404.77 | 9.48 | n/a |
| RWAINCUSDT | IDLE | 0.77 | 1.53 | 0.0 | 0.01 | 9931.39 | 42.92 | no_map |
| TELUSDT | IDLE | 1.08 | 2.75 | 1.1 | 0.0 | 140657.35 | 42.51 | no_map |
| RWAUSDT | IDLE | 0.66 | 1.23 | 0.65 | 0.02 | 57227.94 | 16.23 | no_map |
| FLUIDUSDT | IDLE | 0.98 | 1.87 | 1.32 | -0.04 | 4682.03 | 46.47 | tvl≈2,554,943,805 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
