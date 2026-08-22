# Hulk DIGEST — 2026-08-22T09:13:16Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.18 | 19.14 | 10.44 | 0.04 | 38065888.02 | 4.0 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.82 | 23.87 | 10.3 | 0.12 | 219618864.29 | 3.28 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.38 | 15.8 | 9.99 | 0.03 | 1303592.53 | 5.12 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.2 | 23.96 | 12.06 | -0.09 | 668355.91 | 3.36 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.31 | 17.58 | 8.98 | 0.03 | 600958.53 | 13.61 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.21 | 29.98 | 10.68 | -0.03 | 239257.36 | 3.23 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.1 | 41.27 | 11.9 | 0.04 | 155108.03 | 9.75 | skipped_fast |
| CCUSDT | IDLE | 2.2 | 11.25 | 6.5 | 0.14 | 797235.55 | 11.12 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.11 | 8.0 | 6.18 | -0.01 | 467263.78 | 15.56 | skipped_fast |
| KITEUSDT | IDLE | 4.2 | 9.68 | 3.27 | 0.06 | 73131.47 | 11.72 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.38 | 13.91 | 8.97 | 0.02 | 193030.43 | 6.2 | skipped_fast |
| EDELUSDT | IDLE | 2.52 | 4.52 | 3.46 | -0.05 | 86164.78 | 22.42 | skipped_fast |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.84 | 7.38 | 5.05 | 0.01 | 6940.47 | 17.71 | skipped_fast |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.67 | 6.69 | 6.27 | -0.03 | 171397.11 | 15.8 | skipped_fast |
| RWAINCUSDT | IDLE | 2.32 | 4.36 | 1.88 | 0.03 | 11574.81 | 15.99 | skipped_fast |
| QAITUSDT | IDLE | 1.54 | 2.91 | 1.09 | 0.01 | 3209.57 | 66.45 | skipped_fast |
| RIZEUSDT | IDLE | 0.79 | 3.36 | 1.68 | -0.02 | 50464.12 | 46.77 | skipped_fast |
| RWAUSDT | IDLE | 1.76 | 3.29 | 1.51 | 0.03 | 57680.26 | 32.34 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
