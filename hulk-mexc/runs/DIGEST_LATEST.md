# Hulk DIGEST — 2026-08-22T10:47:33Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 3.73 | 16.77 | 11.44 | 0.01 | 51652218.41 | 4.13 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.86 | 23.87 | 11.95 | 0.08 | 217984738.9 | 4.01 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.42 | 15.8 | 11.03 | 0.0 | 1250429.3 | 5.18 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.01 | 22.93 | 11.47 | -0.1 | 663274.28 | 6.73 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.16 | 16.84 | 9.6 | 0.01 | 595959.45 | 12.74 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.23 | 29.98 | 11.46 | -0.06 | 240511.61 | 3.26 | skipped_fast |
| CCUSDT | IDLE | 2.23 | 11.25 | 7.65 | 0.13 | 816936.66 | 17.32 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 2.85 | 37.92 | 11.23 | 0.03 | 154330.08 | 9.92 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.77 | 9.72 | 7.37 | -0.02 | 424435.49 | 25.5 | skipped_fast |
| KITEUSDT | IDLE | 4.12 | 9.28 | 4.66 | 0.04 | 73360.22 | 11.93 | skipped_fast |
| EDELUSDT | IDLE | 3.34 | 5.96 | 4.86 | -0.04 | 78976.52 | 22.7 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 3.07 | 9.75 | 6.28 | -0.0 | 189250.81 | 6.25 | skipped_fast |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.58 | 9.12 | 7.52 | -0.04 | 168863.52 | 53.62 | skipped_fast |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.86 | 7.38 | 5.33 | -0.01 | 5711.25 | 22.36 | skipped_fast |
| QAITUSDT | IDLE | 1.82 | 3.41 | 1.47 | -0.01 | 3237.82 | 67.45 | skipped_fast |
| RWAINCUSDT | IDLE | 1.5 | 2.62 | 2.55 | 0.0 | 11326.93 | 59.77 | skipped_fast |
| RIZEUSDT | IDLE | 0.74 | 3.18 | 1.4 | -0.0 | 49212.21 | 46.66 | skipped_fast |
| RWAUSDT | IDLE | 1.81 | 3.29 | 2.15 | 0.01 | 57410.56 | 16.3 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
