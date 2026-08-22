# Hulk DIGEST — 2026-08-22T05:32:20Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.16 | 19.14 | 9.73 | 0.08 | 16613766.41 | 5.95 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.31 | 23.87 | 11.6 | 0.15 | 200925753.1 | 0.67 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.32 | 15.8 | 10.72 | 0.04 | 1355120.84 | 42.57 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.3 | 24.54 | 12.41 | -0.1 | 698883.79 | 13.39 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.31 | 17.58 | 8.87 | 0.06 | 592089.12 | 12.56 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.39 | 45.06 | 13.18 | 0.11 | 164215.87 | 21.74 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.25 | 29.98 | 12.7 | -0.04 | 218840.41 | 23.05 | skipped_fast |
| CCUSDT | IDLE | 2.19 | 11.56 | 2.65 | 0.19 | 759665.1 | 5.81 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.18 | 8.47 | 5.44 | 0.06 | 545586.68 | 47.14 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.29 | 13.91 | 9.56 | 0.04 | 195253.92 | 9.34 | skipped_fast |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.88 | 9.68 | 5.99 | 0.08 | 73238.55 | 25.02 | skipped_fast |
| EDELUSDT | IDLE | 2.15 | 4.52 | 1.51 | -0.02 | 88509.69 | 54.73 | skipped_fast |
| RWAINCUSDT | IDLE | 2.5 | 4.48 | 3.4 | 0.01 | 11525.01 | 70.06 | skipped_fast |
| FLUIDUSDT | IDLE | 3.18 | 7.9 | 4.66 | 0.06 | 5410.56 | 32.82 | skipped_fast |
| RIZEUSDT | IDLE | 1.23 | 4.9 | 4.62 | 0.08 | 58749.88 | 22.39 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3288.58 | 35.86 | skipped_fast |
| TELUSDT | IDLE | 2.08 | 5.52 | 2.86 | 0.07 | 194911.18 | 40.67 | skipped_fast |
| RWAUSDT | IDLE | 1.85 | 3.38 | 2.15 | 0.05 | 57506.15 | 16.3 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
