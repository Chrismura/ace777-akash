# Hulk DIGEST — 2026-08-22T10:49:37Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 3.74 | 16.77 | 11.68 | 0.0 | 51652018.19 | 2.07 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.87 | 23.87 | 12.39 | 0.08 | 218357104.77 | 2.69 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.42 | 15.8 | 11.18 | 0.0 | 1250375.8 | 5.18 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.02 | 22.93 | 11.65 | -0.1 | 663341.94 | 3.38 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.17 | 16.84 | 9.79 | 0.01 | 596519.09 | 11.7 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.23 | 29.98 | 11.69 | -0.05 | 240514.22 | 3.27 | skipped_fast |
| CCUSDT | IDLE | 2.24 | 11.25 | 8.17 | 0.12 | 817317.48 | 5.22 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 2.85 | 37.92 | 11.47 | 0.03 | 154265.12 | 9.92 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.8 | 9.72 | 7.86 | -0.03 | 423996.93 | 25.62 | skipped_fast |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 4.15 | 9.28 | 5.02 | 0.03 | 73420.91 | 11.05 | skipped_fast |
| EDELUSDT | IDLE | 3.32 | 5.96 | 4.54 | -0.04 | 78976.57 | 67.87 | skipped_fast |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.6 | 9.12 | 7.81 | -0.04 | 168768.29 | 42.9 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 3.08 | 9.75 | 6.38 | -0.0 | 189253.89 | 6.26 | skipped_fast |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.86 | 7.38 | 5.33 | -0.01 | 5711.25 | 22.41 | skipped_fast |
| QAITUSDT | IDLE | 1.82 | 3.41 | 1.47 | 0.04 | 2991.92 | 67.45 | skipped_fast |
| RWAINCUSDT | IDLE | 1.5 | 2.62 | 2.55 | 0.0 | 11326.93 | 65.18 | skipped_fast |
| RIZEUSDT | IDLE | 0.75 | 3.18 | 1.45 | 0.0 | 49230.72 | 44.83 | skipped_fast |
| RWAUSDT | IDLE | 1.82 | 3.29 | 2.31 | 0.01 | 57360.58 | 16.3 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
