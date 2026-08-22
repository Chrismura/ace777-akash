# Hulk DIGEST — 2026-08-22T09:30:31Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.18 | 19.14 | 10.37 | 0.05 | 41477119.21 | 7.99 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.83 | 23.87 | 10.75 | 0.1 | 219380237.05 | 2.64 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.37 | 15.8 | 9.77 | 0.04 | 1298821.71 | 6.37 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.19 | 23.96 | 11.88 | -0.08 | 667115.62 | 6.71 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.29 | 17.58 | 8.5 | 0.04 | 594762.93 | 11.45 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.21 | 29.98 | 10.74 | -0.03 | 237892.22 | 3.23 | skipped_fast |
| CCUSDT | IDLE | 2.22 | 11.25 | 7.12 | 0.14 | 795424.15 | 7.74 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.09 | 41.27 | 11.39 | 0.06 | 154723.11 | 40.44 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.13 | 8.0 | 6.56 | -0.01 | 462579.17 | 17.65 | skipped_fast |
| KITEUSDT | IDLE | 4.27 | 9.68 | 4.39 | 0.05 | 73121.94 | 10.02 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.37 | 13.91 | 8.76 | 0.02 | 193213.64 | 4.64 | skipped_fast |
| EDELUSDT | IDLE | 2.52 | 4.52 | 3.46 | -0.02 | 79291.8 | 44.79 | skipped_fast |
| FLUIDUSDT | IDLE | 3.77 | 7.38 | 4.07 | 0.02 | 6973.73 | 19.72 | skipped_fast |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.65 | 6.69 | 5.92 | -0.01 | 171187.93 | 10.49 | skipped_fast |
| RWAINCUSDT | IDLE | 2.42 | 4.36 | 3.14 | 0.01 | 11525.92 | 91.42 | skipped_fast |
| QAITUSDT | IDLE | 1.54 | 2.91 | 1.09 | 0.01 | 3209.57 | 66.45 | skipped_fast |
| RIZEUSDT | IDLE | 0.8 | 3.36 | 1.84 | -0.03 | 49850.1 | 46.77 | skipped_fast |
| RWAUSDT | IDLE | 1.75 | 3.29 | 1.35 | 0.03 | 57739.44 | 8.08 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
