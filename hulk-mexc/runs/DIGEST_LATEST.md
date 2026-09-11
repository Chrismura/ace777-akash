# Hulk DIGEST — 2026-09-11T06:15:05Z

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
| ETHUSDT | IDLE | 0.6 | 1.21 | 0.0 | -0.0 | 451562820.63 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.57 | 1.14 | 0.04 | -0.02 | 40511858.43 | 2.22 | skipped_fast |
| BTCUSDT | IDLE | 0.45 | 0.89 | 0.0 | -0.01 | 546252549.77 | 0.0 | skipped_fast |
| RIZEUSDT | IDLE | 1.68 | 47.43 | 28.01 | -0.53 | 166182.09 | 92.17 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 2.62 | 5.89 | 5.38 | -0.07 | 101712.97 | 17.47 | skipped_fast |
| CCUSDT | IDLE | 0.87 | 1.79 | 0.16 | -0.05 | 462278.87 | 9.11 | skipped_fast |
| PYTHUSDT | IDLE | 1.1 | 2.15 | 0.27 | -0.02 | 356655.7 | 1.93 | skipped_fast |
| ZBCNUSDT | IDLE | 1.2 | 2.36 | 0.29 | -0.03 | 203726.79 | 3.86 | skipped_fast |
| WUSDT | IDLE | 1.45 | 2.76 | 0.89 | -0.01 | 159160.85 | 15.52 | skipped_fast |
| EDELUSDT | IDLE | 0.87 | 3.7 | 2.56 | -0.05 | 201080.96 | 28.18 | skipped_fast |
| REDUSDT | IDLE | 1.12 | 2.19 | 0.3 | -0.01 | 60292.76 | 17.96 | skipped_fast |
| BIOUSDT | IDLE | 0.87 | 1.7 | 0.32 | -0.02 | 73908.74 | 7.97 | skipped_fast |
| KITEUSDT | IDLE | 0.81 | 1.47 | 0.94 | -0.03 | 57618.84 | 13.86 | skipped_fast |
| RWAINCUSDT | IDLE | 1.03 | 1.85 | 1.43 | 0.0 | 3644.13 | 33.59 | skipped_fast |
| TELUSDT | IDLE | 1.5 | 2.73 | 1.81 | -0.03 | 96391.28 | 45.95 | skipped_fast |
| HBARUSDT | IDLE | 0.59 | 1.14 | 0.3 | -0.02 | 177526.48 | 1.33 | skipped_fast |
| QNTUSDT | IDLE | 0.6 | 1.17 | 0.15 | -0.03 | 35972.13 | 6.17 | skipped_fast |
| FLUIDUSDT | IDLE | 0.82 | 1.65 | 0.0 | -0.02 | 1877.67 | 13.79 | skipped_fast |
| RWAUSDT | IDLE | 0.4 | 0.77 | 0.15 | -0.02 | 50130.49 | 7.61 | skipped_fast |
| MNSRYUSDT | IDLE | 0.26 | 0.46 | 0.36 | -0.02 | 35118.72 | 4.2 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
