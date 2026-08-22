# Hulk DIGEST — 2026-08-22T07:27:41Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.13 | 19.14 | 8.63 | 0.04 | 22009815.63 | 11.76 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.37 | 23.87 | 5.53 | 0.21 | 219072577.98 | 3.74 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.27 | 15.8 | 8.82 | 0.05 | 1352482.54 | 6.31 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.28 | 24.54 | 11.59 | -0.09 | 696163.99 | 6.65 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.26 | 17.58 | 7.34 | 0.06 | 618488.92 | 11.31 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.24 | 29.98 | 12.15 | -0.04 | 246470.56 | 13.13 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.13 | 42.01 | 9.96 | 0.08 | 160590.77 | 12.08 | skipped_fast |
| CCUSDT | IDLE | 2.05 | 11.25 | 3.57 | 0.19 | 799083.92 | 5.8 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.24 | 8.47 | 5.53 | 0.05 | 541946.71 | 8.45 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.35 | 13.91 | 8.21 | 0.04 | 198745.43 | 6.14 | skipped_fast |
| KITEUSDT | IDLE | 3.39 | 9.68 | 2.73 | 0.1 | 74199.24 | 11.66 | skipped_fast |
| EDELUSDT | IDLE | 2.24 | 4.52 | 2.92 | -0.04 | 87180.29 | 44.59 | skipped_fast |
| FLUIDUSDT | IDLE | 3.33 | 7.38 | 4.01 | 0.04 | 6900.29 | 21.84 | skipped_fast |
| RWAINCUSDT | IDLE | 2.39 | 4.48 | 2.04 | 0.03 | 11367.66 | 75.03 | skipped_fast |
| TELUSDT | IDLE | 2.06 | 5.36 | 3.5 | 0.04 | 193434.78 | 35.81 | skipped_fast |
| QAITUSDT | IDLE | 1.71 | 3.24 | 1.18 | -0.01 | 3225.39 | 63.67 | skipped_fast |
| RIZEUSDT | IDLE | 0.93 | 3.99 | 1.52 | 0.0 | 55974.7 | 25.77 | skipped_fast |
| RWAUSDT | IDLE | 1.76 | 3.29 | 1.59 | 0.04 | 58144.34 | 16.18 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
