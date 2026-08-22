# Hulk DIGEST — 2026-08-22T15:01:44Z

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
| PYTHUSDT | IDLE | 1.58 | 7.62 | 1.34 | 0.05 | 51454081.67 | 1.97 | skipped_fast |
| XRPUSDT | IDLE | 1.35 | 7.49 | 5.35 | 0.04 | 213947537.57 | 2.76 | skipped_fast |
| CCUSDT | IDLE | 1.31 | 5.65 | 2.45 | 0.12 | 799718.81 | 9.4 | skipped_fast |
| HBARUSDT | IDLE | 0.81 | 2.85 | 2.26 | -0.01 | 1178459.7 | 5.23 | skipped_fast |
| CHIPUSDT | IDLE | 0.63 | 3.51 | 2.46 | -0.11 | 614363.99 | 6.81 | skipped_fast |
| WUSDT | IDLE | 0.79 | 3.17 | 2.08 | -0.02 | 563012.34 | 11.78 | skipped_fast |
| KITEUSDT | IDLE | 2.71 | 6.37 | 1.29 | 0.04 | 84587.58 | 10.66 | skipped_fast |
| ZBCNUSDT | IDLE | 1.25 | 3.49 | 0.65 | -0.06 | 322586.18 | 24.42 | skipped_fast |
| BIOUSDT | IDLE | 0.98 | 6.58 | 5.11 | -0.06 | 224462.13 | 6.65 | skipped_fast |
| EDELUSDT | IDLE | 1.39 | 2.52 | 1.79 | -0.04 | 78994.14 | 22.73 | skipped_fast |
| QAITUSDT | IDLE | 2.01 | 3.76 | 1.79 | -0.01 | 2374.33 | 67.45 | skipped_fast |
| REDUSDT | IDLE | 0.48 | 5.1 | 4.43 | -0.03 | 150670.83 | 19.25 | skipped_fast |
| RIZEUSDT | IDLE | 0.79 | 3.28 | 0.29 | 0.04 | 46490.53 | 43.92 | skipped_fast |
| QNTUSDT | IDLE | 0.87 | 2.69 | 2.17 | -0.01 | 188390.15 | 9.46 | skipped_fast |
| RWAINCUSDT | IDLE | 0.77 | 1.53 | 0.0 | 0.01 | 9946.26 | 80.62 | skipped_fast |
| TELUSDT | IDLE | 1.09 | 2.75 | 1.26 | 0.01 | 140173.4 | 53.13 | skipped_fast |
| FLUIDUSDT | IDLE | 0.98 | 1.87 | 1.32 | -0.04 | 4682.03 | 20.93 | skipped_fast |
| RWAUSDT | IDLE | 0.65 | 1.23 | 0.48 | 0.02 | 57305.49 | 16.23 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
