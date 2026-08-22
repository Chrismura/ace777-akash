# Hulk DIGEST — 2026-08-22T10:40:05Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 3.71 | 16.77 | 10.78 | 0.02 | 51650937.61 | 12.3 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.87 | 23.87 | 12.22 | 0.09 | 217753601.78 | 2.68 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.42 | 15.8 | 11.09 | 0.01 | 1250183.62 | 5.18 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.02 | 22.93 | 11.53 | -0.09 | 661978.74 | 3.37 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.15 | 16.84 | 9.25 | 0.02 | 597680.32 | 13.75 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.22 | 29.98 | 10.94 | -0.05 | 239235.48 | 16.21 | skipped_fast |
| CCUSDT | IDLE | 2.22 | 11.25 | 7.37 | 0.13 | 810584.35 | 8.64 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 2.85 | 37.92 | 11.49 | 0.03 | 154334.12 | 11.7 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.78 | 9.72 | 7.44 | -0.02 | 423824.89 | 28.06 | skipped_fast |
| KITEUSDT | IDLE | 4.12 | 9.28 | 4.66 | 0.04 | 73280.96 | 9.19 | skipped_fast |
| EDELUSDT | IDLE | 3.34 | 5.96 | 4.76 | -0.04 | 78968.96 | 22.7 | skipped_fast |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.61 | 9.12 | 8.01 | -0.05 | 168524.49 | 37.66 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 3.08 | 9.75 | 6.47 | 0.0 | 189400.36 | 6.26 | skipped_fast |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.89 | 7.38 | 5.83 | -0.01 | 5710.05 | 22.31 | skipped_fast |
| QAITUSDT | IDLE | 1.82 | 3.41 | 1.47 | -0.01 | 3241.83 | 67.45 | skipped_fast |
| RWAINCUSDT | IDLE | 1.5 | 2.62 | 2.55 | 0.0 | 11326.93 | 65.18 | skipped_fast |
| RWAUSDT | IDLE | 1.81 | 3.29 | 2.15 | 0.01 | 57495.26 | 8.15 | skipped_fast |
| RIZEUSDT | IDLE | 0.74 | 3.18 | 1.38 | -0.0 | 49234.23 | 46.66 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
