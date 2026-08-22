# Hulk DIGEST — 2026-08-22T09:07:15Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.2 | 19.14 | 11.09 | 0.03 | 36564549.06 | 10.07 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.84 | 23.87 | 11.0 | 0.12 | 220783382.08 | 4.63 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.4 | 15.8 | 10.61 | 0.03 | 1303073.34 | 5.15 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.21 | 23.96 | 12.77 | -0.1 | 673945.72 | 3.39 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.34 | 17.58 | 9.75 | 0.03 | 602597.39 | 16.9 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.23 | 29.98 | 11.49 | -0.03 | 241959.26 | 3.26 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.1 | 41.27 | 12.23 | 0.05 | 155114.91 | 14.25 | skipped_fast |
| CCUSDT | IDLE | 2.19 | 11.25 | 6.01 | 0.14 | 797482.11 | 9.35 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.14 | 8.0 | 6.7 | -0.01 | 476841.56 | 30.32 | skipped_fast |
| KITEUSDT | IDLE | 4.26 | 9.68 | 4.21 | 0.06 | 73300.78 | 13.66 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.42 | 13.91 | 9.7 | 0.01 | 193009.89 | 10.92 | skipped_fast |
| EDELUSDT | IDLE | 2.52 | 4.52 | 3.46 | -0.05 | 86444.95 | 22.4 | skipped_fast |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.84 | 7.38 | 5.05 | 0.01 | 6940.47 | 20.06 | skipped_fast |
| RWAINCUSDT | IDLE | 2.32 | 4.36 | 1.88 | 0.03 | 11599.81 | 15.99 | skipped_fast |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.63 | 6.69 | 5.58 | -0.03 | 171498.49 | 36.79 | skipped_fast |
| QAITUSDT | IDLE | 1.54 | 2.91 | 1.09 | 0.01 | 3209.57 | 66.45 | skipped_fast |
| RIZEUSDT | IDLE | 0.8 | 3.36 | 1.87 | -0.04 | 50542.63 | 46.77 | skipped_fast |
| RWAUSDT | IDLE | 1.74 | 3.29 | 1.27 | 0.03 | 57862.83 | 40.44 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
