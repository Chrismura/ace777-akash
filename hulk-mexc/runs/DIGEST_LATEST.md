# Hulk DIGEST — 2026-08-22T09:05:39Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.2 | 19.14 | 11.07 | 0.04 | 36043638.2 | 8.06 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.85 | 23.87 | 11.61 | 0.11 | 221284757.15 | 5.33 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.41 | 15.8 | 10.72 | 0.02 | 1302970.45 | 2.58 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.22 | 23.96 | 12.91 | -0.11 | 673865.71 | 10.17 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.34 | 17.58 | 9.86 | 0.02 | 602051.73 | 11.65 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.23 | 29.98 | 11.69 | -0.04 | 242376.6 | 13.05 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.11 | 41.27 | 12.43 | 0.05 | 155051.14 | 23.2 | skipped_fast |
| CCUSDT | IDLE | 2.18 | 11.25 | 5.95 | 0.14 | 796910.16 | 14.47 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.15 | 8.0 | 6.96 | -0.01 | 477638.29 | 8.61 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.42 | 13.91 | 9.7 | 0.01 | 192964.33 | 3.12 | skipped_fast |
| KITEUSDT | IDLE | 4.26 | 9.68 | 4.27 | 0.05 | 73314.05 | 19.11 | skipped_fast |
| EDELUSDT | IDLE | 2.54 | 4.52 | 3.68 | -0.05 | 86393.8 | 33.58 | skipped_fast |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.84 | 7.38 | 5.05 | 0.01 | 6940.47 | 22.27 | skipped_fast |
| RWAINCUSDT | IDLE | 2.32 | 4.36 | 1.88 | 0.03 | 11599.81 | 15.99 | skipped_fast |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.67 | 6.69 | 6.27 | -0.03 | 170765.96 | 21.04 | skipped_fast |
| QAITUSDT | IDLE | 1.54 | 2.91 | 1.09 | 0.01 | 3209.57 | 66.45 | skipped_fast |
| RIZEUSDT | IDLE | 0.8 | 3.36 | 1.87 | -0.03 | 50813.17 | 46.77 | skipped_fast |
| RWAUSDT | IDLE | 1.74 | 3.29 | 1.27 | 0.03 | 57797.47 | 32.34 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
