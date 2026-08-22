# Hulk DIGEST — 2026-08-22T14:55:14Z

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
| PYTHUSDT | IDLE | 1.61 | 7.62 | 2.28 | 0.04 | 51453048.8 | 1.99 | skipped_fast |
| XRPUSDT | IDLE | 1.36 | 7.58 | 5.52 | 0.03 | 213444642.98 | 2.77 | skipped_fast |
| CCUSDT | IDLE | 1.38 | 6.16 | 3.27 | 0.11 | 795926.67 | 6.01 | skipped_fast |
| HBARUSDT | IDLE | 0.96 | 3.34 | 3.12 | -0.02 | 1175524.99 | 1.31 | skipped_fast |
| WUSDT | IDLE | 1.13 | 4.43 | 3.45 | -0.02 | 562984.49 | 13.97 | skipped_fast |
| CHIPUSDT | IDLE | 0.64 | 3.51 | 2.96 | -0.11 | 614160.77 | 6.85 | skipped_fast |
| KITEUSDT | IDLE | 2.74 | 6.37 | 1.72 | 0.04 | 84422.32 | 8.92 | skipped_fast |
| ZBCNUSDT | IDLE | 1.57 | 4.21 | 1.99 | -0.08 | 324048.08 | 13.29 | skipped_fast |
| BIOUSDT | IDLE | 0.99 | 6.58 | 5.8 | -0.06 | 226147.67 | 6.69 | skipped_fast |
| EDELUSDT | IDLE | 1.43 | 2.63 | 1.56 | -0.04 | 78916.32 | 34.07 | skipped_fast |
| QAITUSDT | IDLE | 2.01 | 3.76 | 1.79 | -0.01 | 2374.33 | 67.45 | skipped_fast |
| REDUSDT | IDLE | 0.42 | 5.06 | 4.78 | -0.03 | 150413.98 | 12.87 | skipped_fast |
| RIZEUSDT | IDLE | 0.78 | 3.28 | 0.2 | 0.03 | 46765.46 | 45.5 | skipped_fast |
| RWAINCUSDT | IDLE | 1.26 | 2.4 | 0.85 | 0.01 | 9946.26 | 75.23 | skipped_fast |
| QNTUSDT | IDLE | 0.87 | 2.69 | 2.31 | -0.01 | 188446.23 | 9.48 | skipped_fast |
| TELUSDT | IDLE | 1.3 | 3.24 | 1.78 | 0.01 | 140085.62 | 42.6 | skipped_fast |
| RWAUSDT | IDLE | 0.84 | 1.55 | 0.81 | 0.02 | 57279.89 | 8.11 | skipped_fast |
| FLUIDUSDT | IDLE | 0.98 | 1.87 | 1.32 | -0.04 | 4682.03 | 21.7 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
