# Hulk DIGEST — 2026-08-22T10:17:32Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 3.73 | 16.77 | 11.29 | 0.01 | 51601960.11 | 2.06 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.9 | 23.87 | 13.65 | 0.06 | 216081729.82 | 7.5 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.43 | 15.8 | 11.24 | 0.01 | 1246949.03 | 3.89 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.05 | 22.93 | 12.96 | -0.11 | 664542.89 | 3.43 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.18 | 16.84 | 10.18 | 0.01 | 595272.41 | 11.75 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.23 | 29.98 | 11.58 | -0.04 | 236787.61 | 3.26 | skipped_fast |
| CCUSDT | IDLE | 2.26 | 11.25 | 8.95 | 0.11 | 814828.51 | 8.77 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 2.86 | 37.92 | 11.66 | 0.04 | 155575.69 | 13.56 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.4 | 8.58 | 7.77 | -0.02 | 429096.58 | 9.21 | skipped_fast |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 4.2 | 9.28 | 5.92 | 0.03 | 73072.28 | 9.29 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 3.1 | 9.75 | 6.85 | -0.01 | 189393.06 | 7.86 | skipped_fast |
| EDELUSDT | IDLE | 2.7 | 4.76 | 4.32 | -0.04 | 79021.01 | 33.88 | skipped_fast |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.17 | 7.96 | 7.32 | -0.04 | 169012.31 | 32.02 | skipped_fast |
| FLUIDUSDT | IDLE | 3.77 | 7.38 | 4.07 | 0.01 | 5824.3 | 20.1 | skipped_fast |
| QAITUSDT | IDLE | 1.66 | 2.91 | 2.68 | -0.02 | 3179.19 | 67.05 | skipped_fast |
| RIZEUSDT | IDLE | 0.76 | 3.18 | 1.77 | -0.01 | 49243.84 | 45.14 | skipped_fast |
| RWAUSDT | IDLE | 1.81 | 3.29 | 2.15 | 0.02 | 57550.92 | 8.14 | skipped_fast |
| RWAINCUSDT | IDLE | 1.21 | 2.11 | 2.07 | -0.0 | 11436.39 | 81.15 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
