# Hulk DIGEST — 2026-08-22T07:37:59Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.12 | 19.14 | 8.33 | 0.03 | 22354439.9 | 1.95 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.37 | 23.87 | 5.84 | 0.22 | 221910086.72 | 8.13 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.27 | 15.8 | 8.78 | 0.05 | 1357630.72 | 1.26 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.27 | 24.54 | 11.24 | -0.09 | 695219.24 | 6.63 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.26 | 17.58 | 7.42 | 0.06 | 616503.37 | 11.31 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.18 | 29.98 | 9.18 | -0.02 | 248270.58 | 3.19 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.14 | 42.01 | 10.48 | 0.08 | 160700.54 | 11.27 | skipped_fast |
| CCUSDT | IDLE | 2.05 | 11.25 | 3.44 | 0.19 | 803600.08 | 3.31 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.24 | 8.47 | 5.56 | 0.05 | 538760.22 | 4.47 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.34 | 13.91 | 7.87 | 0.04 | 195547.31 | 7.65 | skipped_fast |
| KITEUSDT | IDLE | 3.4 | 9.68 | 2.93 | 0.1 | 74222.33 | 10.79 | skipped_fast |
| FLUIDUSDT | IDLE | 3.33 | 7.38 | 4.01 | 0.04 | 6890.3 | 21.82 | skipped_fast |
| EDELUSDT | IDLE | 2.25 | 4.52 | 3.03 | -0.04 | 87148.74 | 78.08 | skipped_fast |
| RWAINCUSDT | IDLE | 2.48 | 4.48 | 3.24 | 0.01 | 11302.57 | 118.15 | skipped_fast |
| TELUSDT | IDLE | 2.08 | 5.36 | 4.0 | -0.0 | 181216.95 | 41.11 | skipped_fast |
| QAITUSDT | IDLE | 1.71 | 3.24 | 1.18 | -0.01 | 3225.39 | 59.7 | skipped_fast |
| RIZEUSDT | IDLE | 0.92 | 3.99 | 1.49 | -0.05 | 52692.4 | 46.34 | skipped_fast |
| RWAUSDT | IDLE | 1.76 | 3.29 | 1.51 | 0.04 | 58467.29 | 16.17 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
