# Hulk DIGEST — 2026-09-28T23:43:22Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| HBARUSDT | IDLE | 1.63 | 14.78 | 7.16 | 0.27 | 11732194.77 | 1.65 | skipped_fast |
| QNTUSDT | IDLE | 0.88 | 12.95 | 7.41 | -0.19 | 15019996.79 | 10.2 | skipped_fast |
| XRPUSDT | IDLE | 1.42 | 2.65 | 1.31 | -0.01 | 66006306.23 | 2.67 | skipped_fast |
| WUSDT | IDLE | 0.69 | 3.21 | 0.5 | -0.13 | 1779909.96 | 8.78 | skipped_fast |
| ETHUSDT | IDLE | 0.67 | 1.29 | 0.31 | 0.0 | 398785453.06 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.61 | 1.14 | 0.53 | -0.01 | 829605309.41 | 0.0 | skipped_fast |
| CCUSDT | IDLE | 1.41 | 5.38 | 2.44 | -0.04 | 1358671.16 | 6.13 | skipped_fast |
| PYTHUSDT | IDLE | 1.82 | 4.0 | 0.66 | -0.03 | 1184794.54 | 1.23 | skipped_fast |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.83 | 28.41 | 5.47 | 0.26 | 361250.64 | 38.44 | skipped_fast |
| EDELUSDT | IDLE | 1.86 | 11.4 | 8.73 | 0.06 | 159526.13 | 11.22 | skipped_fast |
| RWAINCUSDT | IDLE | 2.65 | 5.88 | 4.65 | -0.03 | 17000.3 | 12.35 | skipped_fast |
| ZBCNUSDT | IDLE | 1.58 | 3.05 | 0.73 | -0.01 | 219024.62 | 17.24 | skipped_fast |
| RIZEUSDT | IDLE | 1.53 | 5.52 | 2.04 | 0.11 | 47039.58 | 45.77 | skipped_fast |
| CHIPUSDT | IDLE | 1.3 | 3.17 | 1.02 | -0.05 | 75459.07 | 18.28 | skipped_fast |
| KITEUSDT | IDLE | 0.94 | 3.49 | 1.73 | -0.1 | 100296.45 | 9.48 | skipped_fast |
| BIOUSDT | IDLE | 0.81 | 2.59 | 0.0 | -0.07 | 114900.65 | 10.1 | skipped_fast |
| REDUSDT | IDLE | 1.02 | 2.12 | 0.28 | -0.05 | 58512.65 | 14.87 | skipped_fast |
| FLUIDUSDT | IDLE | 0.93 | 2.23 | 1.24 | -0.06 | 4428.24 | 21.99 | skipped_fast |
| RWAUSDT | IDLE | 0.41 | 0.72 | 0.64 | -0.01 | 57650.78 | 7.2 | skipped_fast |
| MNSRYUSDT | IDLE | 0.24 | 0.45 | 0.22 | -0.02 | 33839.67 | 15.48 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
