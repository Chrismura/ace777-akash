# Hulk DIGEST — 2026-08-22T10:56:36Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 3.76 | 16.77 | 12.15 | -0.01 | 51654935.23 | 2.08 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.88 | 23.87 | 12.95 | 0.07 | 218177487.08 | 10.82 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.43 | 15.8 | 11.24 | -0.0 | 1250576.5 | 6.49 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.03 | 22.93 | 11.95 | -0.11 | 662241.72 | 3.38 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.17 | 16.84 | 9.82 | 0.01 | 593267.9 | 7.45 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.23 | 29.98 | 11.72 | -0.06 | 240638.85 | 3.28 | skipped_fast |
| CCUSDT | IDLE | 2.23 | 11.25 | 7.81 | 0.12 | 819088.07 | 9.53 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.8 | 9.72 | 7.86 | -0.04 | 423606.01 | 15.91 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 2.85 | 37.92 | 10.78 | 0.03 | 153985.0 | 20.56 | skipped_fast |
| KITEUSDT | IDLE | 4.11 | 9.28 | 4.51 | 0.03 | 73343.11 | 11.91 | skipped_fast |
| EDELUSDT | IDLE | 3.34 | 5.96 | 4.86 | -0.04 | 78929.54 | 22.7 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 3.08 | 9.75 | 6.53 | -0.01 | 189102.62 | 7.84 | skipped_fast |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.57 | 9.12 | 7.32 | -0.03 | 169009.94 | 64.1 | skipped_fast |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.86 | 7.38 | 5.33 | -0.01 | 5711.25 | 23.14 | skipped_fast |
| QAITUSDT | IDLE | 1.82 | 3.41 | 1.47 | 0.01 | 2438.25 | 67.45 | skipped_fast |
| RWAINCUSDT | IDLE | 1.5 | 2.62 | 2.55 | 0.0 | 11326.93 | 59.83 | skipped_fast |
| RIZEUSDT | IDLE | 0.74 | 3.18 | 1.4 | -0.0 | 49232.55 | 46.66 | skipped_fast |
| RWAUSDT | IDLE | 1.82 | 3.29 | 2.31 | 0.01 | 57470.44 | 16.31 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
