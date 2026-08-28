# Hulk DIGEST — 2026-08-28T19:07:58Z

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
| XRPUSDT | IDLE | 3.11 | 5.57 | 4.33 | -0.05 | 55009650.16 | 1.45 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 2.94 | 17.89 | 13.03 | 0.04 | 1021991.45 | 7.31 | skipped_fast |
| PYTHUSDT | IDLE | 2.81 | 5.81 | 3.8 | -0.06 | 853655.84 | 2.14 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.79 | 7.41 | 5.7 | -0.07 | 196944.68 | 26.32 | skipped_fast |
| CCUSDT | IDLE | 2.46 | 4.39 | 3.51 | -0.03 | 365676.56 | 3.66 | skipped_fast |
| WUSDT | IDLE | 2.76 | 5.91 | 4.54 | -0.06 | 207133.21 | 12.14 | skipped_fast |
| HBARUSDT | IDLE | 3.07 | 5.77 | 2.53 | -0.03 | 443047.52 | 1.31 | skipped_fast |
| BIOUSDT | IDLE | 2.71 | 5.99 | 4.2 | -0.06 | 95626.93 | 3.62 | skipped_fast |
| REDUSDT | IDLE | 2.59 | 6.25 | 2.87 | -0.02 | 67660.25 | 12.39 | skipped_fast |
| KITEUSDT | IDLE | 2.61 | 5.04 | 1.15 | -0.0 | 80004.07 | 8.67 | skipped_fast |
| EDELUSDT | IDLE | 2.63 | 4.63 | 4.26 | -0.05 | 69589.0 | 17.76 | skipped_fast |
| QAITUSDT | IDLE | 1.67 | 22.24 | 15.36 | -0.18 | 74284.86 | 149.14 | skipped_fast |
| RWAUSDT | IDLE | 3.27 | 5.9 | 4.3 | -0.0 | 55025.07 | 16.64 | skipped_fast |
| RIZEUSDT | IDLE | 1.58 | 4.58 | 1.66 | -0.03 | 43094.49 | 55.08 | skipped_fast |
| QNTUSDT | IDLE | 2.12 | 3.76 | 3.15 | -0.04 | 42295.63 | 6.6 | skipped_fast |
| FLUIDUSDT | IDLE | 2.31 | 4.19 | 2.88 | -0.05 | 4475.04 | 21.6 | skipped_fast |
| TELUSDT | IDLE | 1.96 | 5.02 | 4.29 | -0.1 | 104499.09 | 56.79 | skipped_fast |
| RWAINCUSDT | IDLE | 0.93 | 3.1 | 1.18 | -0.0 | 18584.93 | 70.52 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
