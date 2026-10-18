# Hulk DIGEST — 2026-10-18T20:05:37Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| ETHUSDT | IDLE | 1.31 | 2.32 | 1.97 | -0.03 | 113618199.52 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 1.05 | 1.89 | 1.45 | -0.03 | 27624236.36 | 1.59 | skipped_fast |
| BTCUSDT | IDLE | 0.33 | 0.59 | 0.45 | -0.01 | 224117786.1 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.24 | 4.47 | 4.21 | -0.13 | 1406550.17 | 5.52 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 3.71 | 8.29 | 7.27 | -0.04 | 768635.66 | 11.0 | skipped_fast |
| WUSDT | IDLE | 1.71 | 4.48 | 4.11 | -0.11 | 913980.77 | 16.62 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 4.46 | 12.83 | 9.82 | -0.03 | 46102.38 | 5.36 | skipped_fast |
| QNTUSDT | IDLE | 2.37 | 5.27 | 4.7 | -0.09 | 622738.32 | 9.33 | skipped_fast |
| WAXLUSDT | WATCH_PULLBACK — tension haute + reflux | 3.64 | 16.5 | 9.03 | -0.02 | 77895.95 | 70.71 | skipped_fast |
| CCUSDT | IDLE | 1.7 | 3.11 | 2.81 | -0.08 | 251157.98 | 7.22 | skipped_fast |
| EDELUSDT | IDLE | 1.74 | 4.42 | 3.3 | -0.09 | 241755.62 | 38.67 | skipped_fast |
| ZBCNUSDT | IDLE | 2.03 | 3.92 | 2.66 | -0.06 | 206549.47 | 55.7 | skipped_fast |
| CHIPUSDT | IDLE | 1.89 | 5.51 | 5.23 | -0.11 | 78787.69 | 10.25 | skipped_fast |
| BIOUSDT | IDLE | 1.78 | 3.59 | 2.95 | -0.08 | 84513.14 | 8.81 | skipped_fast |
| REDUSDT | IDLE | 1.62 | 2.83 | 2.7 | -0.06 | 94998.49 | 9.82 | skipped_fast |
| RIZEUSDT | IDLE | 1.62 | 7.91 | 6.57 | -0.04 | 58736.61 | 63.44 | skipped_fast |
| KITEUSDT | IDLE | 1.5 | 2.62 | 2.54 | -0.06 | 69376.79 | 9.92 | skipped_fast |
| IOTAUSDT | IDLE | 1.91 | 4.24 | 3.39 | -0.08 | 71010.34 | 30.21 | skipped_fast |
| FLUIDUSDT | IDLE | 1.89 | 3.35 | 2.91 | -0.07 | 4487.41 | 21.47 | skipped_fast |
| LAUSDT | IDLE | 1.35 | 3.42 | 2.96 | -0.1 | 58394.34 | 23.65 | skipped_fast |
| RWAUSDT | IDLE | 0.58 | 1.05 | 0.72 | -0.01 | 48692.1 | 16.06 | skipped_fast |
| MNSRYUSDT | IDLE | 0.38 | 0.7 | 0.44 | -0.01 | 34744.64 | 54.1 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
