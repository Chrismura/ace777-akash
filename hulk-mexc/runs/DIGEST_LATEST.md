# Hulk DIGEST — 2026-08-22T10:45:08Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 3.72 | 16.77 | 11.07 | 0.02 | 51653404.29 | 2.06 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.85 | 23.87 | 11.56 | 0.1 | 217820284.15 | 4.66 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.41 | 15.8 | 10.9 | 0.01 | 1250581.22 | 5.17 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.02 | 22.93 | 11.62 | -0.09 | 661629.8 | 3.37 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.15 | 16.84 | 9.31 | 0.02 | 596550.64 | 13.75 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.22 | 29.98 | 11.26 | -0.05 | 240452.13 | 3.25 | skipped_fast |
| CCUSDT | IDLE | 2.23 | 11.25 | 7.61 | 0.13 | 816942.64 | 6.92 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 2.85 | 37.92 | 11.15 | 0.03 | 154326.5 | 11.7 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.78 | 9.72 | 7.47 | -0.02 | 424278.86 | 29.06 | skipped_fast |
| KITEUSDT | IDLE | 4.12 | 9.28 | 4.55 | 0.04 | 73325.24 | 12.84 | skipped_fast |
| EDELUSDT | IDLE | 3.35 | 5.96 | 4.97 | -0.04 | 78976.5 | 22.7 | skipped_fast |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.6 | 9.12 | 7.86 | -0.04 | 168681.84 | 42.94 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 3.07 | 9.75 | 6.15 | 0.0 | 189277.1 | 9.36 | skipped_fast |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.86 | 7.38 | 5.33 | -0.01 | 5711.25 | 21.54 | skipped_fast |
| QAITUSDT | IDLE | 1.82 | 3.41 | 1.47 | -0.01 | 3239.82 | 67.45 | skipped_fast |
| RWAINCUSDT | IDLE | 1.5 | 2.62 | 2.55 | 0.0 | 11326.93 | 59.77 | skipped_fast |
| RIZEUSDT | IDLE | 0.74 | 3.18 | 1.38 | -0.0 | 49204.29 | 46.66 | skipped_fast |
| RWAUSDT | IDLE | 1.81 | 3.29 | 2.15 | 0.01 | 57461.2 | 16.3 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
