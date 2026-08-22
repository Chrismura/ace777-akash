# Hulk DIGEST — 2026-08-22T10:07:33Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 3.71 | 16.77 | 10.67 | 0.02 | 51586699.42 | 2.05 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.89 | 23.87 | 13.29 | 0.04 | 215264577.31 | 8.15 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.43 | 15.8 | 11.27 | 0.01 | 1256333.77 | 1.3 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.04 | 22.93 | 12.4 | -0.11 | 663775.12 | 3.4 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.17 | 16.84 | 9.67 | 0.02 | 594816.98 | 12.74 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.21 | 29.98 | 10.59 | -0.03 | 236852.38 | 3.23 | skipped_fast |
| CCUSDT | IDLE | 2.26 | 11.25 | 8.7 | 0.11 | 812983.19 | 9.64 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 2.85 | 37.92 | 10.86 | 0.05 | 155588.77 | 11.67 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.12 | 7.87 | 7.29 | -0.02 | 432760.8 | 19.34 | skipped_fast |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 4.18 | 9.28 | 5.59 | 0.03 | 73253.5 | 9.25 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 3.07 | 9.75 | 6.29 | -0.0 | 189410.02 | 9.38 | skipped_fast |
| EDELUSDT | IDLE | 2.71 | 4.76 | 4.43 | -0.03 | 79228.49 | 33.84 | skipped_fast |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.01 | 7.55 | 7.02 | -0.04 | 170969.61 | 31.88 | skipped_fast |
| FLUIDUSDT | IDLE | 3.77 | 7.38 | 4.07 | 0.01 | 5824.3 | 20.77 | skipped_fast |
| QAITUSDT | IDLE | 1.54 | 2.91 | 1.09 | -0.01 | 3179.54 | 66.45 | skipped_fast |
| RIZEUSDT | IDLE | 0.76 | 3.18 | 1.91 | -0.01 | 49323.04 | 46.77 | skipped_fast |
| RWAINCUSDT | IDLE | 1.21 | 2.11 | 2.07 | 0.0 | 11462.91 | 70.29 | skipped_fast |
| RWAUSDT | IDLE | 1.78 | 3.29 | 1.83 | 0.02 | 57479.24 | 16.22 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
