# Hulk DIGEST — 2026-08-22T17:24:53Z

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
| PYTHUSDT | IDLE | 1.75 | 8.48 | 1.23 | 0.11 | 49131540.37 | 9.58 | skipped_fast |
| XRPUSDT | IDLE | 1.32 | 7.64 | 3.48 | 0.06 | 213734259.81 | 3.39 | skipped_fast |
| CCUSDT | IDLE | 0.94 | 4.25 | 0.43 | 0.12 | 768022.49 | 3.35 | skipped_fast |
| HBARUSDT | IDLE | 0.81 | 3.03 | 1.0 | 0.01 | 1096524.34 | 3.87 | skipped_fast |
| CHIPUSDT | IDLE | 0.57 | 3.36 | 0.73 | -0.09 | 631320.68 | 6.69 | skipped_fast |
| WUSDT | IDLE | 0.59 | 2.58 | 0.08 | 0.0 | 533574.41 | 8.41 | skipped_fast |
| BIOUSDT | IDLE | 1.19 | 7.96 | 6.52 | -0.08 | 228198.12 | 3.37 | skipped_fast |
| ZBCNUSDT | IDLE | 1.28 | 3.45 | 1.57 | -0.02 | 306513.4 | 14.86 | skipped_fast |
| EDELUSDT | IDLE | 1.76 | 3.11 | 2.68 | -0.02 | 74907.79 | 22.96 | skipped_fast |
| KITEUSDT | IDLE | 1.39 | 3.22 | 0.9 | 0.05 | 89116.62 | 7.08 | skipped_fast |
| REDUSDT | IDLE | 0.53 | 5.67 | 2.14 | -0.13 | 122069.56 | 11.63 | skipped_fast |
| RIZEUSDT | IDLE | 1.12 | 2.63 | 0.82 | 0.04 | 46138.79 | 45.71 | skipped_fast |
| QAITUSDT | IDLE | 1.39 | 2.71 | 0.47 | -0.01 | 2322.14 | 67.45 | skipped_fast |
| QNTUSDT | IDLE | 0.86 | 2.69 | 1.94 | -0.01 | 181260.17 | 6.29 | skipped_fast |
| TELUSDT | IDLE | 0.98 | 2.37 | 1.79 | 0.01 | 133987.12 | 37.46 | skipped_fast |
| RWAINCUSDT | IDLE | 0.8 | 1.53 | 0.43 | 0.01 | 7571.75 | 107.7 | skipped_fast |
| RWAUSDT | IDLE | 0.57 | 1.14 | 0.0 | 0.03 | 56228.0 | 16.16 | skipped_fast |
| FLUIDUSDT | IDLE | 0.1 | 0.19 | 0.19 | -0.03 | 4628.58 | 17.89 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
