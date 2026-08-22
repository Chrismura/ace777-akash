# Hulk DIGEST — 2026-08-22T12:25:12Z

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
| PYTHUSDT | IDLE | 1.65 | 7.83 | 2.2 | 0.05 | 51601691.38 | 1.99 | skipped_fast |
| XRPUSDT | IDLE | 2.47 | 14.26 | 6.52 | 0.12 | 215881264.7 | 4.6 | skipped_fast |
| HBARUSDT | IDLE | 1.25 | 4.63 | 1.96 | 0.03 | 1261091.97 | 5.12 | skipped_fast |
| CCUSDT | IDLE | 1.59 | 8.38 | 3.1 | 0.14 | 775143.59 | 6.72 | skipped_fast |
| WUSDT | IDLE | 1.53 | 6.27 | 3.0 | 0.02 | 577782.41 | 12.61 | skipped_fast |
| ZBCNUSDT | IDLE | 2.2 | 5.77 | 3.55 | -0.02 | 371021.76 | 12.28 | skipped_fast |
| CHIPUSDT | IDLE | 0.71 | 4.16 | 1.19 | -0.09 | 606237.43 | 3.34 | skipped_fast |
| KITEUSDT | IDLE | 2.6 | 6.24 | 0.36 | 0.05 | 83454.9 | 3.53 | skipped_fast |
| EDELUSDT | IDLE | 2.12 | 3.89 | 2.32 | -0.02 | 78079.1 | 11.28 | skipped_fast |
| BIOUSDT | IDLE | 0.76 | 5.65 | 0.57 | -0.02 | 241888.29 | 6.32 | skipped_fast |
| QAITUSDT | IDLE | 2.25 | 4.16 | 2.33 | -0.01 | 2396.75 | 43.59 | skipped_fast |
| REDUSDT | IDLE | 0.46 | 6.02 | 2.09 | 0.02 | 153162.61 | 14.05 | skipped_fast |
| TELUSDT | IDLE | 2.17 | 5.61 | 3.93 | -0.03 | 164438.7 | 63.8 | skipped_fast |
| RWAINCUSDT | IDLE | 1.38 | 2.4 | 2.34 | -0.01 | 10075.72 | 76.09 | skipped_fast |
| QNTUSDT | IDLE | 1.04 | 3.47 | 0.9 | 0.01 | 187947.91 | 4.63 | skipped_fast |
| RIZEUSDT | IDLE | 0.47 | 1.91 | 0.44 | -0.04 | 48032.07 | 46.13 | skipped_fast |
| RWAUSDT | IDLE | 0.98 | 1.8 | 1.04 | 0.02 | 57757.78 | 24.38 | skipped_fast |
| FLUIDUSDT | IDLE | 1.01 | 1.93 | 1.38 | -0.01 | 5711.25 | 22.18 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
