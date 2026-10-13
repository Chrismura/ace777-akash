# Hulk DIGEST — 2026-10-13T15:02:50Z

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
| WUSDT | IDLE | 1.58 | 12.65 | 11.02 | -0.25 | 5689654.55 | 15.59 | skipped_fast |
| PYTHUSDT | IDLE | 1.14 | 3.81 | 2.55 | -0.04 | 2375264.75 | 10.97 | skipped_fast |
| XRPUSDT | IDLE | 1.22 | 2.35 | 0.54 | -0.0 | 38741274.66 | 1.46 | skipped_fast |
| ETHUSDT | IDLE | 0.82 | 1.57 | 0.53 | -0.0 | 235327746.44 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.45 | 0.85 | 0.4 | 0.01 | 379587148.51 | 0.0 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 3.08 | 10.84 | 7.08 | -0.09 | 1200921.92 | 4.35 | skipped_fast |
| CCUSDT | IDLE | 2.85 | 8.94 | 2.78 | 0.05 | 579539.65 | 13.31 | skipped_fast |
| EDELUSDT | IDLE | 3.59 | 7.67 | 2.28 | 0.02 | 319000.03 | 20.39 | skipped_fast |
| REDUSDT | IDLE | 2.59 | 5.08 | 3.77 | -0.09 | 188523.5 | 13.83 | skipped_fast |
| RWAINCUSDT | IDLE | 2.73 | 4.9 | 3.72 | -0.02 | 32372.9 | 4.96 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.67 | 8.66 | 5.11 | -0.03 | 63237.36 | 87.62 | skipped_fast |
| ZBCNUSDT | IDLE | 1.43 | 2.72 | 0.94 | -0.02 | 250511.13 | 23.52 | skipped_fast |
| HBARUSDT | IDLE | 1.95 | 3.65 | 1.66 | -0.03 | 360465.01 | 2.29 | skipped_fast |
| CHIPUSDT | IDLE | 1.53 | 3.26 | 2.7 | -0.03 | 121704.87 | 20.74 | skipped_fast |
| BIOUSDT | IDLE | 1.29 | 3.0 | 1.51 | -0.04 | 74229.43 | 7.29 | skipped_fast |
| KITEUSDT | IDLE | 1.06 | 2.25 | 0.73 | 0.01 | 60925.2 | 11.81 | skipped_fast |
| TELUSDT | IDLE | 1.56 | 2.95 | 1.18 | 0.0 | 110876.91 | 51.24 | skipped_fast |
| FLUIDUSDT | IDLE | 1.58 | 3.17 | 2.72 | 0.03 | 16238.39 | 21.49 | skipped_fast |
| MNSRYUSDT | IDLE | 0.6 | 1.09 | 0.71 | -0.02 | 38166.44 | 13.94 | skipped_fast |
| RWAUSDT | IDLE | 0.24 | 0.46 | 0.15 | 0.0 | 53132.85 | 23.14 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
