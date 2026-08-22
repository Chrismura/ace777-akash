# Hulk DIGEST — 2026-08-22T06:50:44Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.13 | 19.14 | 8.85 | 0.05 | 20457648.45 | 3.93 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.24 | 23.87 | 7.02 | 0.21 | 214453187.08 | 3.8 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.23 | 15.8 | 8.22 | 0.06 | 1392354.41 | 2.51 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.3 | 24.54 | 12.32 | -0.11 | 702851.13 | 6.7 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.25 | 17.58 | 7.1 | 0.07 | 617570.25 | 15.39 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.26 | 29.98 | 13.05 | -0.05 | 246853.48 | 3.32 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.19 | 42.58 | 11.57 | 0.05 | 161554.12 | 9.61 | skipped_fast |
| CCUSDT | IDLE | 2.01 | 11.25 | 3.94 | 0.18 | 784586.13 | 6.66 | skipped_fast |
| ZBCNUSDT | IDLE | 3.16 | 8.47 | 4.97 | 0.04 | 546329.11 | 36.08 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.36 | 13.91 | 8.32 | 0.04 | 200303.31 | 9.22 | skipped_fast |
| KITEUSDT | IDLE | 2.78 | 9.68 | 3.38 | 0.11 | 74412.52 | 10.82 | skipped_fast |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.51 | 8.47 | 5.26 | 0.05 | 6989.9 | 21.11 | skipped_fast |
| EDELUSDT | IDLE | 2.26 | 4.52 | 3.14 | -0.04 | 87725.25 | 55.9 | skipped_fast |
| TELUSDT | IDLE | 2.14 | 5.52 | 3.95 | 0.06 | 196829.81 | 5.14 | skipped_fast |
| RWAINCUSDT | IDLE | 2.49 | 4.48 | 3.29 | 0.0 | 11421.15 | 91.72 | skipped_fast |
| QAITUSDT | IDLE | 1.71 | 3.24 | 1.18 | -0.02 | 3304.43 | 63.67 | skipped_fast |
| RIZEUSDT | IDLE | 0.91 | 3.99 | 1.13 | 0.09 | 59596.68 | 27.31 | skipped_fast |
| RWAUSDT | IDLE | 1.83 | 3.38 | 1.91 | 0.04 | 57954.32 | 8.11 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
