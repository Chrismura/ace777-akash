# Hulk DIGEST — 2026-08-22T06:42:16Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.13 | 19.14 | 8.65 | 0.06 | 20199917.06 | 1.96 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.23 | 23.87 | 6.87 | 0.21 | 213486875.63 | 11.37 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.23 | 15.8 | 8.21 | 0.06 | 1389572.66 | 3.76 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.29 | 24.54 | 12.09 | -0.11 | 704679.73 | 3.36 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.24 | 17.58 | 6.95 | 0.07 | 617289.83 | 11.26 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.25 | 29.98 | 12.53 | -0.04 | 245616.18 | 6.61 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.2 | 42.58 | 12.02 | 0.07 | 163699.57 | 21.96 | skipped_fast |
| CCUSDT | IDLE | 2.02 | 11.25 | 4.26 | 0.17 | 783001.25 | 5.84 | skipped_fast |
| ZBCNUSDT | IDLE | 3.15 | 8.47 | 4.87 | 0.04 | 546281.99 | 19.77 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.35 | 13.91 | 8.25 | 0.04 | 200356.93 | 7.7 | skipped_fast |
| KITEUSDT | IDLE | 2.8 | 9.68 | 3.69 | 0.11 | 74595.1 | 11.76 | skipped_fast |
| EDELUSDT | IDLE | 2.22 | 4.52 | 2.59 | -0.02 | 88034.78 | 33.31 | skipped_fast |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.51 | 8.47 | 5.26 | 0.05 | 6989.9 | 18.94 | skipped_fast |
| RWAINCUSDT | IDLE | 2.49 | 4.48 | 3.29 | 0.0 | 11421.15 | 64.66 | skipped_fast |
| TELUSDT | IDLE | 2.13 | 5.52 | 3.85 | 0.06 | 196518.35 | 30.8 | skipped_fast |
| QAITUSDT | IDLE | 1.71 | 3.24 | 1.18 | -0.02 | 3304.43 | 63.67 | skipped_fast |
| RIZEUSDT | IDLE | 0.92 | 3.99 | 1.45 | 0.09 | 59551.94 | 46.34 | skipped_fast |
| RWAUSDT | IDLE | 1.83 | 3.38 | 1.83 | 0.04 | 58163.71 | 16.23 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
