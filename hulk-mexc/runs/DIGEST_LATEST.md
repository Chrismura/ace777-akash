# Hulk DIGEST — 2026-08-22T09:10:47Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.19 | 19.14 | 10.57 | 0.04 | 37422486.38 | 8.01 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.82 | 23.87 | 10.36 | 0.13 | 220058604.28 | 3.28 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.39 | 15.8 | 10.14 | 0.03 | 1303294.19 | 2.56 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.2 | 23.96 | 12.32 | -0.1 | 668375.06 | 10.11 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.32 | 17.58 | 9.13 | 0.03 | 601024.81 | 13.63 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.22 | 29.98 | 11.23 | -0.04 | 239136.15 | 16.27 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.1 | 41.27 | 12.01 | 0.04 | 155160.19 | 18.63 | skipped_fast |
| CCUSDT | IDLE | 2.2 | 11.25 | 6.38 | 0.14 | 797429.17 | 10.25 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.12 | 8.0 | 6.34 | -0.01 | 468468.81 | 19.63 | skipped_fast |
| KITEUSDT | IDLE | 4.22 | 9.68 | 3.49 | 0.07 | 73147.0 | 10.84 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.39 | 13.91 | 9.17 | 0.02 | 193034.57 | 9.32 | skipped_fast |
| EDELUSDT | IDLE | 2.52 | 4.52 | 3.46 | -0.05 | 86139.89 | 11.2 | skipped_fast |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.84 | 7.38 | 5.05 | 0.01 | 6940.47 | 22.23 | skipped_fast |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.67 | 6.69 | 6.22 | -0.03 | 171078.25 | 10.53 | skipped_fast |
| RWAINCUSDT | IDLE | 2.32 | 4.36 | 1.88 | 0.03 | 11574.81 | 15.99 | skipped_fast |
| QAITUSDT | IDLE | 1.54 | 2.91 | 1.09 | 0.01 | 3209.57 | 66.45 | skipped_fast |
| RIZEUSDT | IDLE | 0.8 | 3.36 | 1.9 | -0.03 | 50475.96 | 29.42 | skipped_fast |
| RWAUSDT | IDLE | 1.76 | 3.29 | 1.59 | 0.03 | 57703.0 | 24.26 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
