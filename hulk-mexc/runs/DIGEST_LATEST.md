# Hulk DIGEST — 2026-08-22T10:29:03Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 3.73 | 16.77 | 11.35 | 0.01 | 51638672.77 | 8.25 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.9 | 23.87 | 13.83 | 0.05 | 216570058.07 | 5.47 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.45 | 15.8 | 11.89 | -0.0 | 1249915.6 | 7.83 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.04 | 22.93 | 12.4 | -0.11 | 666502.64 | 6.8 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.19 | 16.84 | 10.33 | 0.0 | 598994.41 | 13.9 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.24 | 29.98 | 12.15 | -0.05 | 238049.39 | 3.27 | skipped_fast |
| CCUSDT | IDLE | 2.22 | 11.25 | 7.28 | 0.12 | 810740.86 | 8.62 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 2.85 | 37.92 | 11.22 | 0.04 | 154850.5 | 15.31 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.83 | 9.72 | 8.45 | -0.03 | 426224.65 | 29.91 | skipped_fast |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 4.18 | 9.28 | 5.64 | 0.03 | 73309.26 | 13.91 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.4 | 5.96 | 5.62 | -0.05 | 78867.64 | 79.68 | skipped_fast |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.62 | 9.12 | 8.16 | -0.05 | 168623.63 | 37.69 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 3.11 | 9.75 | 7.2 | -0.01 | 189367.48 | 1.58 | skipped_fast |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.89 | 7.38 | 5.83 | -0.01 | 5825.49 | 21.69 | skipped_fast |
| QAITUSDT | IDLE | 1.82 | 3.41 | 1.47 | -0.01 | 3242.83 | 67.45 | skipped_fast |
| RIZEUSDT | IDLE | 0.75 | 3.18 | 1.48 | -0.0 | 49250.67 | 25.9 | skipped_fast |
| RWAINCUSDT | IDLE | 1.21 | 2.11 | 2.07 | 0.01 | 11368.82 | 70.48 | skipped_fast |
| RWAUSDT | IDLE | 1.8 | 3.29 | 2.07 | 0.02 | 57435.2 | 24.44 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
