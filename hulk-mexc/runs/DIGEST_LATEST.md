# Hulk DIGEST — 2026-08-21T08:14:14Z

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
| PYTHUSDT | IDLE | 2.84 | 12.1 | 2.34 | 0.15 | 2829008.92 | 8.07 | skipped_fast |
| XRPUSDT | IDLE | 1.13 | 4.98 | 0.22 | 0.2 | 125148949.24 | 2.23 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.72 | 18.43 | 6.2 | -0.0 | 41146.29 | 13.72 | skipped_fast |
| CHIPUSDT | IDLE | 1.09 | 6.22 | 4.44 | 0.12 | 491986.48 | 15.06 | skipped_fast |
| ZBCNUSDT | IDLE | 1.91 | 7.31 | 1.25 | 0.07 | 306353.87 | 22.14 | skipped_fast |
| WUSDT | IDLE | 2.15 | 4.09 | 1.46 | 0.06 | 283355.98 | 14.09 | skipped_fast |
| CCUSDT | IDLE | 1.2 | 2.32 | 0.5 | -0.0 | 492678.29 | 9.81 | skipped_fast |
| BIOUSDT | IDLE | 2.23 | 6.52 | 1.07 | 0.04 | 212840.91 | 24.73 | skipped_fast |
| REDUSDT | IDLE | 2.01 | 6.07 | 2.01 | -0.05 | 120329.64 | 13.08 | skipped_fast |
| EDELUSDT | IDLE | 2.03 | 3.61 | 2.96 | 0.02 | 75909.61 | 32.59 | skipped_fast |
| KITEUSDT | IDLE | 1.95 | 3.86 | 0.24 | 0.07 | 62709.34 | 15.53 | skipped_fast |
| HBARUSDT | IDLE | 1.0 | 2.0 | 0.0 | 0.06 | 535670.32 | 1.32 | skipped_fast |
| TELUSDT | IDLE | 1.71 | 8.98 | 0.66 | 0.21 | 221099.59 | 55.94 | skipped_fast |
| QAITUSDT | IDLE | 1.26 | 2.95 | 2.29 | -0.05 | 5526.94 | 67.45 | skipped_fast |
| RWAINCUSDT | IDLE | 0.82 | 1.6 | 0.33 | 0.04 | 8584.28 | 32.97 | skipped_fast |
| QNTUSDT | IDLE | 1.1 | 2.19 | 0.03 | 0.05 | 74169.05 | 14.32 | skipped_fast |
| RWAUSDT | IDLE | 0.91 | 1.79 | 0.25 | 0.03 | 54883.13 | 8.41 | skipped_fast |
| FLUIDUSDT | IDLE | 0.88 | 1.71 | 0.32 | 0.05 | 2720.67 | 29.6 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
