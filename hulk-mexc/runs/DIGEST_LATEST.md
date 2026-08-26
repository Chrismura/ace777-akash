# Hulk DIGEST — 2026-08-26T05:10:48Z

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
| PYTHUSDT | IDLE | 2.55 | 5.46 | 0.11 | -0.01 | 2602113.18 | 9.57 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.82 | 74.43 | 34.17 | 0.18 | 61294.5 | 36.52 | skipped_fast |
| XRPUSDT | IDLE | 1.03 | 1.88 | 1.33 | -0.06 | 60377368.72 | 2.1 | skipped_fast |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.91 | 31.72 | 11.11 | 0.13 | 15621.79 | 0.65 | skipped_fast |
| CHIPUSDT | IDLE | 1.69 | 4.71 | 2.76 | -0.04 | 379494.54 | 9.37 | skipped_fast |
| CCUSDT | IDLE | 1.11 | 2.13 | 1.87 | -0.05 | 511379.57 | 9.29 | skipped_fast |
| WUSDT | IDLE | 1.66 | 3.09 | 1.55 | -0.05 | 286442.21 | 8.51 | skipped_fast |
| REDUSDT | IDLE | 2.01 | 4.97 | 3.47 | -0.01 | 76332.24 | 11.39 | skipped_fast |
| BIOUSDT | IDLE | 1.89 | 3.33 | 2.99 | -0.05 | 95381.32 | 7.0 | skipped_fast |
| KITEUSDT | IDLE | 2.01 | 4.0 | 0.16 | 0.0 | 59237.94 | 9.48 | skipped_fast |
| HBARUSDT | IDLE | 0.98 | 1.84 | 0.86 | -0.05 | 560185.41 | 1.28 | skipped_fast |
| EDELUSDT | IDLE | 0.9 | 12.46 | 11.0 | -0.0 | 158225.51 | 76.34 | skipped_fast |
| ZBCNUSDT | IDLE | 1.54 | 2.99 | 0.6 | -0.0 | 159362.62 | 19.37 | skipped_fast |
| QAITUSDT | IDLE | 1.35 | 2.61 | 0.63 | 0.04 | 13942.51 | 59.26 | skipped_fast |
| RWAUSDT | IDLE | 1.05 | 1.84 | 1.72 | -0.05 | 56555.44 | 16.69 | skipped_fast |
| TELUSDT | IDLE | 0.85 | 1.61 | 0.66 | -0.04 | 93394.12 | 22.01 | skipped_fast |
| QNTUSDT | IDLE | 0.51 | 0.93 | 0.66 | -0.04 | 131353.69 | 4.74 | skipped_fast |
| RWAINCUSDT | IDLE | 0.78 | 1.37 | 1.3 | 0.01 | 1502.63 | 131.05 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
