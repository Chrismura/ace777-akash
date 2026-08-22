# Hulk DIGEST — 2026-08-22T10:28:30Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 3.75 | 16.77 | 11.84 | 0.0 | 51635935.28 | 16.58 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.92 | 23.87 | 14.75 | 0.05 | 216485115.81 | 2.76 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.47 | 15.8 | 12.27 | -0.0 | 1250392.18 | 6.56 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.04 | 22.93 | 12.43 | -0.11 | 667103.11 | 13.6 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.2 | 16.84 | 10.73 | -0.01 | 599109.45 | 13.96 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.24 | 29.98 | 12.27 | -0.05 | 238034.34 | 16.4 | skipped_fast |
| CCUSDT | IDLE | 2.23 | 11.25 | 7.76 | 0.12 | 810520.16 | 10.37 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.85 | 9.72 | 8.79 | -0.03 | 428651.14 | 15.54 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 2.86 | 37.92 | 11.99 | 0.03 | 155409.96 | 19.86 | skipped_fast |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 4.19 | 9.28 | 5.7 | 0.02 | 73159.65 | 19.49 | skipped_fast |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.62 | 9.12 | 8.16 | -0.05 | 168612.36 | 32.26 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 3.11 | 9.75 | 7.2 | -0.01 | 189342.77 | 9.46 | skipped_fast |
| EDELUSDT | IDLE | 3.33 | 5.96 | 4.65 | -0.05 | 78867.69 | 102.56 | skipped_fast |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.89 | 7.38 | 5.83 | -0.01 | 5825.49 | 11.98 | skipped_fast |
| QAITUSDT | IDLE | 1.82 | 3.41 | 1.47 | -0.01 | 3242.83 | 67.45 | skipped_fast |
| RWAUSDT | IDLE | 1.81 | 3.29 | 2.23 | 0.01 | 57381.44 | 8.15 | skipped_fast |
| RIZEUSDT | IDLE | 0.74 | 3.18 | 1.36 | 0.0 | 49248.15 | 46.66 | skipped_fast |
| RWAINCUSDT | IDLE | 1.21 | 2.11 | 2.07 | 0.01 | 11368.82 | 70.48 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
