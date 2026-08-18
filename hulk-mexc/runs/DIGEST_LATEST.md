# Hulk DIGEST — 2026-08-18T12:28:43Z

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
| XRPUSDT | IDLE | 0.51 | 0.97 | 0.37 | -0.0 | 11575822.04 | 2.0 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 4.44 | 8.85 | 6.35 | -0.04 | 3544.05 | 17.79 | skipped_fast |
| CHIPUSDT | IDLE | 1.83 | 5.48 | 4.14 | -0.08 | 251677.71 | 3.54 | skipped_fast |
| CCUSDT | IDLE | 1.33 | 2.47 | 1.2 | -0.02 | 271833.68 | 6.53 | skipped_fast |
| REDUSDT | IDLE | 0.99 | 8.44 | 5.81 | 0.16 | 101257.67 | 22.42 | skipped_fast |
| RIZEUSDT | IDLE | 1.85 | 6.45 | 1.13 | -0.12 | 48979.88 | 47.42 | skipped_fast |
| ZBCNUSDT | IDLE | 0.99 | 1.88 | 0.71 | -0.0 | 211293.28 | 18.44 | skipped_fast |
| KITEUSDT | IDLE | 1.35 | 2.51 | 1.32 | -0.02 | 70303.86 | 17.5 | skipped_fast |
| PYTHUSDT | IDLE | 0.47 | 0.87 | 0.42 | -0.03 | 202954.21 | 2.63 | skipped_fast |
| WUSDT | IDLE | 0.65 | 1.19 | 0.71 | -0.03 | 153759.07 | 14.75 | skipped_fast |
| BIOUSDT | IDLE | 0.92 | 1.82 | 0.16 | -0.0 | 77395.36 | 8.15 | skipped_fast |
| EDELUSDT | IDLE | 0.78 | 1.98 | 1.29 | -0.04 | 80430.79 | 26.21 | skipped_fast |
| TELUSDT | IDLE | 1.48 | 2.8 | 1.05 | -0.03 | 124733.15 | 49.45 | skipped_fast |
| QAITUSDT | IDLE | 0.46 | 3.07 | 2.16 | -0.04 | 11405.95 | 50.14 | skipped_fast |
| HBARUSDT | IDLE | 0.49 | 0.92 | 0.35 | -0.0 | 116264.49 | 1.52 | skipped_fast |
| QNTUSDT | IDLE | 0.37 | 0.72 | 0.18 | 0.01 | 38402.32 | 7.14 | skipped_fast |
| RWAUSDT | IDLE | 0.31 | 0.61 | 0.09 | 0.0 | 50714.99 | 26.05 | skipped_fast |
| FLUIDUSDT | IDLE | 0.2 | 0.41 | 0.0 | -0.03 | 238.93 | 21.84 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
