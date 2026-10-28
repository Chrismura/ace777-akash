# Hulk DIGEST — 2026-10-28T16:40:22Z

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
| ETHUSDT | IDLE | 1.07 | 1.92 | 1.52 | -0.01 | 215100978.59 | 0.13 | skipped_fast |
| XRPUSDT | IDLE | 0.83 | 1.45 | 1.35 | -0.01 | 18665615.88 | 0.76 | skipped_fast |
| BTCUSDT | IDLE | 0.76 | 1.34 | 1.22 | -0.0 | 282284247.58 | 0.0 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.5 | 17.04 | 14.26 | -0.1 | 189510.26 | 20.36 | skipped_fast |
| CCUSDT | IDLE | 3.1 | 7.17 | 2.29 | 0.0 | 375788.28 | 4.0 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 4.14 | 9.65 | 8.56 | -0.01 | 37733.83 | 33.96 | skipped_fast |
| PYTHUSDT | IDLE | 1.56 | 2.74 | 2.58 | -0.02 | 388371.1 | 2.82 | skipped_fast |
| QNTUSDT | IDLE | 2.7 | 4.81 | 3.98 | -0.03 | 409256.71 | 2.58 | skipped_fast |
| WUSDT | IDLE | 1.46 | 2.74 | 1.2 | -0.01 | 440475.91 | 15.71 | skipped_fast |
| ZBCNUSDT | IDLE | 1.61 | 3.18 | 1.07 | -0.04 | 251061.09 | 34.68 | skipped_fast |
| EDELUSDT | IDLE | 1.52 | 2.83 | 1.42 | -0.0 | 200318.68 | 3.07 | skipped_fast |
| HBARUSDT | IDLE | 1.24 | 2.2 | 1.83 | -0.01 | 480727.32 | 6.65 | skipped_fast |
| BIOUSDT | IDLE | 1.62 | 3.02 | 1.49 | 0.0 | 83822.66 | 8.87 | skipped_fast |
| KITEUSDT | IDLE | 1.19 | 2.15 | 1.49 | -0.03 | 59002.42 | 9.58 | skipped_fast |
| REDUSDT | IDLE | 1.04 | 1.94 | 0.96 | -0.02 | 54097.89 | 14.54 | skipped_fast |
| RIZEUSDT | IDLE | 0.95 | 1.79 | 0.74 | 0.03 | 37672.8 | 61.36 | skipped_fast |
| IOTAUSDT | IDLE | 1.63 | 2.89 | 2.46 | -0.02 | 74335.67 | 24.19 | skipped_fast |
| LAUSDT | IDLE | 1.52 | 2.68 | 2.4 | -0.04 | 57740.14 | 20.75 | skipped_fast |
| FLUIDUSDT | IDLE | 1.15 | 3.48 | 2.59 | -0.01 | 6677.13 | 21.58 | skipped_fast |
| WAXLUSDT | IDLE | 1.35 | 2.38 | 2.18 | -0.03 | 56218.43 | 64.59 | skipped_fast |
| RWAUSDT | IDLE | 0.59 | 1.04 | 0.87 | -0.0 | 55587.88 | 40.05 | skipped_fast |
| MNSRYUSDT | IDLE | 0.28 | 0.51 | 0.31 | 0.0 | 36088.26 | 54.03 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
