# Hulk DIGEST — 2026-09-11T07:17:41Z

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
| XRPUSDT | IDLE | 0.82 | 1.61 | 0.16 | -0.02 | 40595565.4 | 0.74 | skipped_fast |
| ETHUSDT | IDLE | 0.62 | 1.24 | 0.06 | -0.0 | 453814854.93 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.48 | 0.93 | 0.14 | -0.01 | 537479925.76 | 0.0 | skipped_fast |
| RIZEUSDT | IDLE | 1.92 | 48.6 | 30.36 | -0.06 | 155824.91 | 96.53 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 2.89 | 8.6 | 5.65 | -0.07 | 122863.43 | 13.15 | skipped_fast |
| CCUSDT | IDLE | 0.95 | 1.86 | 0.25 | -0.06 | 445155.8 | 6.07 | skipped_fast |
| PYTHUSDT | IDLE | 1.09 | 2.15 | 0.21 | -0.02 | 346367.25 | 1.93 | skipped_fast |
| WUSDT | IDLE | 1.47 | 2.76 | 1.16 | -0.01 | 152314.45 | 16.61 | skipped_fast |
| ZBCNUSDT | IDLE | 1.28 | 2.5 | 0.41 | -0.03 | 202070.42 | 20.95 | skipped_fast |
| EDELUSDT | IDLE | 0.87 | 3.71 | 3.03 | -0.08 | 199023.21 | 18.96 | skipped_fast |
| REDUSDT | IDLE | 1.19 | 2.19 | 1.2 | -0.01 | 60165.26 | 13.17 | skipped_fast |
| BIOUSDT | IDLE | 0.89 | 1.7 | 0.48 | -0.02 | 74048.27 | 7.98 | skipped_fast |
| KITEUSDT | IDLE | 0.9 | 1.6 | 1.28 | -0.03 | 58566.16 | 12.04 | skipped_fast |
| RWAINCUSDT | IDLE | 1.03 | 1.85 | 1.38 | -0.0 | 3346.14 | 27.94 | skipped_fast |
| TELUSDT | IDLE | 1.38 | 2.49 | 1.81 | -0.04 | 96347.61 | 34.58 | skipped_fast |
| HBARUSDT | IDLE | 0.63 | 1.14 | 0.79 | -0.02 | 174450.72 | 2.66 | skipped_fast |
| FLUIDUSDT | IDLE | 0.87 | 1.58 | 1.13 | -0.02 | 1839.17 | 13.92 | skipped_fast |
| QNTUSDT | IDLE | 0.66 | 1.32 | 0.0 | -0.03 | 35909.03 | 3.08 | skipped_fast |
| RWAUSDT | IDLE | 0.39 | 0.77 | 0.08 | -0.02 | 50407.99 | 7.6 | skipped_fast |
| MNSRYUSDT | IDLE | 0.3 | 0.6 | 0.04 | -0.01 | 35246.74 | 5.57 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
