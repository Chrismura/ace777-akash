# Hulk DIGEST — 2026-10-26T03:12:43Z

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
| ETHUSDT | IDLE | 1.32 | 2.38 | 1.71 | -0.02 | 100409088.65 | 0.61 | skipped_fast |
| XRPUSDT | IDLE | 0.96 | 1.71 | 1.43 | -0.02 | 16018052.81 | 0.78 | skipped_fast |
| BTCUSDT | IDLE | 0.93 | 1.67 | 1.22 | -0.01 | 184150114.49 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.46 | 3.08 | 2.32 | 0.04 | 736349.51 | 2.7 | skipped_fast |
| WUSDT | IDLE | 1.33 | 2.4 | 1.67 | -0.03 | 604539.68 | 17.84 | skipped_fast |
| ZBCNUSDT | IDLE | 2.47 | 4.46 | 3.7 | 0.01 | 180278.45 | 14.21 | skipped_fast |
| CHIPUSDT | IDLE | 2.45 | 4.71 | 2.87 | -0.04 | 87828.12 | 18.45 | skipped_fast |
| RWAINCUSDT | IDLE | 2.34 | 4.15 | 3.55 | -0.05 | 64444.99 | 5.74 | skipped_fast |
| QNTUSDT | IDLE | 0.8 | 2.24 | 1.41 | 0.05 | 682796.85 | 2.63 | skipped_fast |
| KITEUSDT | IDLE | 1.74 | 3.13 | 2.38 | -0.02 | 54292.22 | 14.36 | skipped_fast |
| EDELUSDT | IDLE | 0.86 | 2.07 | 1.43 | 0.05 | 239856.98 | 15.73 | skipped_fast |
| CCUSDT | IDLE | 1.09 | 1.98 | 1.38 | -0.01 | 180320.43 | 10.92 | skipped_fast |
| REDUSDT | IDLE | 1.56 | 2.9 | 1.52 | -0.02 | 60196.87 | 9.74 | skipped_fast |
| BIOUSDT | IDLE | 1.16 | 2.09 | 1.47 | -0.03 | 60442.89 | 9.05 | skipped_fast |
| WAXLUSDT | IDLE | 2.09 | 3.69 | 3.3 | -0.02 | 53639.85 | 29.31 | skipped_fast |
| LAUSDT | IDLE | 1.81 | 4.86 | 3.59 | -0.08 | 61329.87 | 23.41 | skipped_fast |
| RIZEUSDT | IDLE | 1.02 | 1.99 | 0.3 | 0.0 | 33007.65 | 48.38 | skipped_fast |
| HBARUSDT | IDLE | 1.13 | 2.04 | 1.42 | -0.02 | 181415.27 | 6.5 | skipped_fast |
| IOTAUSDT | IDLE | 1.58 | 2.84 | 2.11 | -0.03 | 60492.93 | 28.41 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 4.86 | 4.56 | -0.03 | 19214.62 | 21.76 | skipped_fast |
| RWAUSDT | IDLE | 0.17 | 0.32 | 0.16 | -0.0 | 53300.24 | 15.92 | skipped_fast |
| MNSRYUSDT | IDLE | 0.33 | 0.59 | 0.41 | -0.01 | 38041.15 | 60.17 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
