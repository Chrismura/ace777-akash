# Hulk DIGEST — 2026-08-22T12:23:55Z

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
| XRPUSDT | IDLE | 2.46 | 14.26 | 6.15 | 0.12 | 215850008.87 | 3.93 | n/a |
| PYTHUSDT | IDLE | 1.66 | 7.83 | 2.45 | 0.05 | 51600644.13 | 7.96 | tvl≈110,752,782 |
| HBARUSDT | IDLE | 1.25 | 4.63 | 1.92 | 0.03 | 1260572.34 | 6.4 | empty_tvl |
| CCUSDT | IDLE | 1.6 | 8.38 | 3.54 | 0.14 | 774402.21 | 8.43 | no_map |
| WUSDT | IDLE | 1.54 | 6.27 | 3.13 | 0.02 | 577864.8 | 13.68 | tvl≈1,571,378,489 |
| ZBCNUSDT | IDLE | 2.2 | 5.77 | 3.62 | -0.03 | 371098.85 | 12.28 | n/a |
| CHIPUSDT | IDLE | 0.71 | 4.16 | 1.19 | -0.09 | 607453.73 | 6.68 | no_map |
| KITEUSDT | IDLE | 2.6 | 6.24 | 0.32 | 0.05 | 83347.5 | 3.53 | no_map |
| EDELUSDT | IDLE | 2.14 | 3.89 | 2.54 | -0.02 | 78079.07 | 45.15 | no_map |
| BIOUSDT | IDLE | 0.77 | 5.65 | 0.94 | -0.02 | 241842.18 | 15.8 | n/a |
| QAITUSDT | IDLE | 2.2 | 4.16 | 1.63 | -0.0 | 2384.15 | 63.29 | no_map |
| REDUSDT | IDLE | 0.46 | 6.02 | 2.14 | 0.03 | 153246.78 | 21.05 | tvl≈2,031,082 |
| TELUSDT | IDLE | 2.17 | 5.61 | 3.88 | -0.03 | 164429.65 | 58.53 | no_map |
| RWAINCUSDT | IDLE | 1.38 | 2.4 | 2.34 | -0.01 | 10075.72 | 76.09 | no_map |
| QNTUSDT | IDLE | 1.03 | 3.47 | 0.84 | 0.01 | 187888.93 | 4.63 | n/a |
| RIZEUSDT | IDLE | 0.46 | 1.91 | 0.29 | -0.04 | 48007.46 | 15.37 | no_map |
| RWAUSDT | IDLE | 1.0 | 1.8 | 1.29 | 0.02 | 57773.14 | 32.49 | no_map |
| FLUIDUSDT | IDLE | 1.01 | 1.93 | 1.38 | -0.01 | 5711.25 | 21.43 | tvl≈2,552,552,396 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
