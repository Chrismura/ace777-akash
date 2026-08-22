# Hulk DIGEST — 2026-08-22T10:31:51Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 3.73 | 16.77 | 11.33 | 0.01 | 51639489.58 | 2.06 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.89 | 23.87 | 13.31 | 0.07 | 217065383.83 | 6.79 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.45 | 15.8 | 11.72 | 0.01 | 1246839.21 | 6.51 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.02 | 22.93 | 11.77 | -0.1 | 666648.28 | 10.15 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.18 | 16.84 | 10.2 | 0.01 | 598815.14 | 11.75 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.24 | 29.98 | 12.01 | -0.06 | 238752.91 | 6.56 | skipped_fast |
| CCUSDT | IDLE | 2.23 | 11.25 | 7.49 | 0.12 | 811741.54 | 10.37 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 2.85 | 37.92 | 11.18 | 0.03 | 154828.73 | 11.7 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.83 | 9.72 | 8.43 | -0.03 | 426327.71 | 21.62 | skipped_fast |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 4.17 | 9.28 | 5.45 | 0.03 | 73172.2 | 9.25 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.39 | 5.96 | 5.41 | -0.05 | 78867.53 | 45.61 | skipped_fast |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.62 | 9.12 | 8.16 | -0.05 | 168569.57 | 43.08 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 3.11 | 9.75 | 7.13 | -0.01 | 189385.7 | 6.3 | skipped_fast |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.89 | 7.38 | 5.83 | -0.01 | 5710.05 | 22.48 | skipped_fast |
| QAITUSDT | IDLE | 1.82 | 3.41 | 1.47 | -0.01 | 3242.83 | 67.45 | skipped_fast |
| RIZEUSDT | IDLE | 0.74 | 3.18 | 1.26 | 0.0 | 49252.19 | 43.21 | skipped_fast |
| RWAUSDT | IDLE | 1.8 | 3.29 | 2.07 | 0.02 | 57347.55 | 24.42 | skipped_fast |
| RWAINCUSDT | IDLE | 1.21 | 2.11 | 2.07 | 0.01 | 11327.59 | 92.07 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
