# Hulk DIGEST — 2026-10-17T16:20:45Z

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
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 2.84 | 7.33 | 5.96 | -0.05 | 1231470.02 | 8.71 | skipped_fast |
| XRPUSDT | IDLE | 0.87 | 1.54 | 1.37 | -0.01 | 18490392.83 | 1.55 | skipped_fast |
| ETHUSDT | IDLE | 0.79 | 1.38 | 1.36 | -0.01 | 100661465.04 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.26 | 0.45 | 0.45 | -0.0 | 204842621.39 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.22 | 3.9 | 3.56 | -0.05 | 1099589.51 | 1.21 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 3.12 | 12.81 | 6.88 | 0.02 | 24899.65 | 21.07 | skipped_fast |
| CHIPUSDT | IDLE | 2.92 | 5.19 | 4.36 | -0.06 | 88742.4 | 11.41 | skipped_fast |
| ZBCNUSDT | IDLE | 2.44 | 4.47 | 2.68 | -0.04 | 221043.31 | 19.91 | skipped_fast |
| QNTUSDT | IDLE | 1.54 | 2.68 | 2.61 | -0.02 | 627548.49 | 2.01 | skipped_fast |
| KITEUSDT | IDLE | 2.36 | 4.26 | 3.37 | -0.03 | 63837.91 | 12.73 | skipped_fast |
| CCUSDT | IDLE | 1.35 | 2.56 | 0.9 | 0.02 | 271216.57 | 4.79 | skipped_fast |
| BIOUSDT | IDLE | 1.61 | 2.85 | 2.45 | -0.04 | 70313.36 | 8.24 | skipped_fast |
| EDELUSDT | IDLE | 0.95 | 1.71 | 1.27 | -0.04 | 151848.51 | 13.89 | skipped_fast |
| FLUIDUSDT | IDLE | 2.74 | 4.89 | 4.17 | 0.01 | 3749.75 | 21.18 | skipped_fast |
| REDUSDT | IDLE | 1.14 | 2.08 | 1.39 | -0.05 | 60814.21 | 14.99 | skipped_fast |
| RIZEUSDT | IDLE | 0.31 | 0.61 | 0.08 | -0.04 | 42878.68 | 35.88 | skipped_fast |
| RWAUSDT | IDLE | 1.5 | 2.92 | 0.47 | -0.0 | 51488.46 | 39.67 | skipped_fast |
| HBARUSDT | IDLE | 0.75 | 1.32 | 1.19 | -0.02 | 141835.2 | 6.04 | skipped_fast |
| TELUSDT | IDLE | 1.04 | 1.86 | 1.53 | -0.06 | 88568.37 | 23.95 | skipped_fast |
| MNSRYUSDT | IDLE | 0.35 | 0.68 | 0.07 | 0.0 | 27859.89 | 11.31 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
