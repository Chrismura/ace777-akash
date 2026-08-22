# Hulk DIGEST — 2026-08-22T05:28:40Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.16 | 19.14 | 9.78 | 0.08 | 16456269.44 | 11.91 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.27 | 23.87 | 9.56 | 0.18 | 198999638.65 | 18.21 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.24 | 15.8 | 8.56 | 0.06 | 1348064.17 | 20.15 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.28 | 24.54 | 11.76 | -0.1 | 690747.73 | 20.09 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.28 | 17.58 | 8.1 | 0.07 | 587971.6 | 11.4 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.37 | 45.06 | 11.95 | 0.12 | 164578.29 | 12.06 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.24 | 29.98 | 12.07 | -0.03 | 218634.86 | 19.74 | skipped_fast |
| CCUSDT | IDLE | 2.19 | 11.56 | 2.85 | 0.18 | 760285.39 | 12.5 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.23 | 8.47 | 6.38 | 0.06 | 544145.63 | 35.54 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.28 | 13.91 | 9.35 | 0.04 | 195252.95 | 10.89 | skipped_fast |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.87 | 9.68 | 5.61 | 0.09 | 73366.27 | 12.04 | skipped_fast |
| EDELUSDT | IDLE | 2.16 | 4.52 | 1.62 | -0.02 | 88500.8 | 32.91 | skipped_fast |
| RWAINCUSDT | IDLE | 2.5 | 4.48 | 3.4 | 0.01 | 11525.01 | 64.66 | skipped_fast |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.22 | 7.9 | 5.34 | 0.05 | 5410.58 | 21.8 | skipped_fast |
| RIZEUSDT | IDLE | 1.22 | 4.9 | 4.57 | 0.08 | 58740.35 | 22.39 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3417.27 | 35.86 | skipped_fast |
| TELUSDT | IDLE | 2.06 | 5.52 | 2.47 | 0.08 | 195524.56 | 45.72 | skipped_fast |
| RWAUSDT | IDLE | 1.85 | 3.38 | 2.15 | 0.05 | 57551.96 | 24.44 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
