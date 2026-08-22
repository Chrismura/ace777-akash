# Hulk DIGEST — 2026-08-22T11:17:13Z

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
| PYTHUSDT | IDLE | 2.19 | 9.66 | 7.76 | 0.0 | 51649066.44 | 2.07 | skipped_fast |
| XRPUSDT | IDLE | 2.33 | 14.26 | 8.31 | 0.07 | 217578862.15 | 2.01 | skipped_fast |
| CCUSDT | IDLE | 2.05 | 10.24 | 7.71 | 0.11 | 811789.62 | 7.8 | skipped_fast |
| HBARUSDT | IDLE | 1.47 | 5.26 | 3.63 | 0.0 | 1257498.6 | 6.48 | skipped_fast |
| WUSDT | IDLE | 1.56 | 6.27 | 3.87 | 0.02 | 584223.17 | 7.42 | skipped_fast |
| ZBCNUSDT | IDLE | 2.33 | 5.93 | 5.11 | -0.04 | 397126.7 | 17.15 | skipped_fast |
| CHIPUSDT | IDLE | 0.74 | 4.16 | 2.48 | -0.11 | 645617.34 | 3.38 | skipped_fast |
| EDELUSDT | IDLE | 2.78 | 4.93 | 4.26 | -0.04 | 78848.23 | 34.19 | skipped_fast |
| BIOUSDT | IDLE | 0.96 | 6.64 | 3.52 | -0.04 | 237586.7 | 3.26 | skipped_fast |
| KITEUSDT | IDLE | 1.87 | 4.3 | 1.54 | 0.03 | 73671.04 | 9.09 | skipped_fast |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.66 | 6.75 | 5.71 | -0.04 | 169179.14 | 48.22 | skipped_fast |
| QAITUSDT | IDLE | 2.16 | 4.16 | 1.12 | 0.01 | 2502.14 | 67.45 | skipped_fast |
| REDUSDT | IDLE | 0.49 | 6.02 | 4.97 | 0.02 | 154548.71 | 9.96 | skipped_fast |
| RWAINCUSDT | IDLE | 1.38 | 2.4 | 2.34 | -0.01 | 11324.46 | 59.83 | skipped_fast |
| QNTUSDT | IDLE | 1.09 | 3.47 | 2.27 | -0.0 | 188711.27 | 6.27 | skipped_fast |
| RIZEUSDT | IDLE | 0.67 | 2.89 | 0.95 | 0.0 | 49257.21 | 46.44 | skipped_fast |
| FLUIDUSDT | IDLE | 1.87 | 3.68 | 1.96 | -0.01 | 5711.25 | 22.37 | skipped_fast |
| RWAUSDT | IDLE | 1.03 | 1.8 | 1.69 | 0.01 | 57499.78 | 8.17 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
