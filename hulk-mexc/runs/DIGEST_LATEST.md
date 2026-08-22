# Hulk DIGEST — 2026-08-22T09:43:06Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.2 | 19.14 | 10.85 | 0.02 | 44736248.72 | 2.01 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.84 | 23.87 | 11.11 | 0.09 | 218459243.73 | 2.65 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.38 | 15.8 | 9.96 | 0.03 | 1292894.54 | 5.12 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.2 | 23.96 | 12.29 | -0.1 | 665754.91 | 3.37 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.31 | 17.58 | 8.83 | 0.03 | 590615.08 | 5.23 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.21 | 29.98 | 10.48 | -0.03 | 237551.6 | 3.23 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.1 | 41.27 | 11.6 | 0.06 | 154555.98 | 9.71 | skipped_fast |
| CCUSDT | IDLE | 2.23 | 11.25 | 7.65 | 0.12 | 802644.2 | 10.38 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.13 | 8.0 | 6.57 | -0.01 | 439809.88 | 2.02 | skipped_fast |
| KITEUSDT | IDLE | 4.29 | 9.68 | 4.73 | 0.05 | 73113.76 | 9.15 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.38 | 13.91 | 8.83 | 0.01 | 192932.8 | 7.73 | skipped_fast |
| FLUIDUSDT | IDLE | 3.77 | 7.38 | 4.07 | 0.01 | 6941.81 | 13.92 | skipped_fast |
| EDELUSDT | IDLE | 2.52 | 4.52 | 3.46 | -0.03 | 79282.75 | 78.52 | skipped_fast |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.68 | 6.74 | 6.22 | -0.02 | 170895.05 | 21.06 | skipped_fast |
| RWAINCUSDT | IDLE | 2.42 | 4.36 | 3.14 | 0.01 | 11436.39 | 91.42 | skipped_fast |
| QAITUSDT | IDLE | 1.54 | 2.91 | 1.09 | 0.01 | 3199.56 | 66.45 | skipped_fast |
| RIZEUSDT | IDLE | 0.8 | 3.36 | 1.87 | -0.02 | 49367.35 | 25.95 | skipped_fast |
| RWAUSDT | IDLE | 1.73 | 3.29 | 1.12 | 0.03 | 57755.62 | 24.2 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
