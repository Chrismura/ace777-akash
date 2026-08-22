# Hulk DIGEST — 2026-08-22T09:41:00Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.19 | 19.14 | 10.75 | 0.02 | 44288621.57 | 2.01 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.84 | 23.87 | 11.21 | 0.09 | 218407936.29 | 2.65 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.38 | 15.8 | 10.01 | 0.03 | 1291436.07 | 1.28 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.2 | 23.96 | 12.26 | -0.1 | 666551.27 | 3.36 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.31 | 17.58 | 8.98 | 0.03 | 591100.96 | 12.56 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.21 | 29.98 | 10.62 | -0.04 | 237626.63 | 3.23 | skipped_fast |
| CCUSDT | IDLE | 2.23 | 11.25 | 7.84 | 0.12 | 802238.0 | 4.33 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.09 | 41.27 | 11.46 | 0.06 | 154583.82 | 21.16 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.14 | 8.0 | 6.7 | -0.01 | 439791.31 | 9.59 | skipped_fast |
| KITEUSDT | IDLE | 4.31 | 9.68 | 4.94 | 0.05 | 73156.42 | 9.17 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.39 | 13.91 | 9.04 | 0.01 | 192990.71 | 7.75 | skipped_fast |
| EDELUSDT | IDLE | 2.5 | 4.52 | 3.14 | -0.02 | 79319.18 | 11.18 | skipped_fast |
| FLUIDUSDT | IDLE | 3.77 | 7.38 | 4.07 | 0.01 | 6941.81 | 21.22 | skipped_fast |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.67 | 6.69 | 6.22 | -0.02 | 171352.2 | 26.32 | skipped_fast |
| RWAINCUSDT | IDLE | 2.42 | 4.36 | 3.14 | 0.01 | 11436.39 | 91.42 | skipped_fast |
| QAITUSDT | IDLE | 1.54 | 2.91 | 1.09 | 0.01 | 3209.57 | 66.45 | skipped_fast |
| RIZEUSDT | IDLE | 0.79 | 3.36 | 1.72 | -0.01 | 49378.43 | 46.77 | skipped_fast |
| RWAUSDT | IDLE | 1.75 | 3.29 | 1.35 | 0.03 | 57802.23 | 24.2 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
