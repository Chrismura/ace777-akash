# Hulk DIGEST — 2026-08-18T23:45:36Z

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
| XRPUSDT | IDLE | 0.24 | 0.46 | 0.12 | -0.0 | 10906193.79 | 2.0 | skipped_fast |
| CHIPUSDT | IDLE | 1.71 | 5.28 | 3.44 | -0.05 | 192994.38 | 3.8 | skipped_fast |
| PYTHUSDT | IDLE | 1.52 | 2.69 | 2.29 | -0.0 | 174897.15 | 2.6 | skipped_fast |
| RIZEUSDT | IDLE | 2.34 | 4.47 | 3.55 | -0.04 | 29926.14 | 54.09 | skipped_fast |
| CCUSDT | IDLE | 1.01 | 1.99 | 0.14 | 0.01 | 240846.74 | 6.56 | skipped_fast |
| REDUSDT | IDLE | 0.64 | 4.67 | 3.38 | 0.07 | 159879.41 | 12.85 | skipped_fast |
| ZBCNUSDT | IDLE | 0.63 | 1.22 | 0.28 | -0.0 | 146360.24 | 14.01 | skipped_fast |
| WUSDT | IDLE | 0.59 | 1.11 | 0.41 | -0.02 | 129949.11 | 13.6 | skipped_fast |
| RWAINCUSDT | IDLE | 0.95 | 2.1 | 0.0 | -0.01 | 10505.43 | 17.81 | skipped_fast |
| BIOUSDT | IDLE | 0.54 | 1.02 | 0.41 | -0.0 | 64238.99 | 4.07 | skipped_fast |
| EDELUSDT | IDLE | 0.72 | 2.17 | 1.06 | -0.03 | 73874.95 | 40.08 | skipped_fast |
| KITEUSDT | IDLE | 0.38 | 0.76 | 0.04 | -0.0 | 64162.04 | 16.33 | skipped_fast |
| FLUIDUSDT | IDLE | 1.72 | 3.05 | 2.58 | -0.02 | 212.15 | 21.99 | skipped_fast |
| HBARUSDT | IDLE | 1.06 | 2.09 | 0.15 | 0.02 | 110861.67 | 1.49 | skipped_fast |
| QAITUSDT | IDLE | 0.24 | 3.32 | 1.45 | -0.16 | 16123.66 | 63.49 | skipped_fast |
| TELUSDT | IDLE | 0.97 | 1.82 | 0.75 | 0.04 | 90382.61 | 41.52 | skipped_fast |
| QNTUSDT | IDLE | 0.46 | 0.84 | 0.53 | -0.01 | 34620.01 | 7.16 | skipped_fast |
| RWAUSDT | IDLE | 0.23 | 0.44 | 0.17 | -0.01 | 51136.47 | 8.71 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
