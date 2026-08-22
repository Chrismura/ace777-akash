# Hulk DIGEST — 2026-08-22T05:44:19Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.16 | 19.14 | 9.83 | 0.07 | 16968439.52 | 9.93 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.3 | 23.87 | 11.03 | 0.16 | 203802367.4 | 2.65 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.3 | 15.8 | 10.06 | 0.04 | 1366362.58 | 8.96 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.32 | 24.54 | 13.12 | -0.1 | 709185.21 | 10.12 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.3 | 17.58 | 8.79 | 0.05 | 601220.88 | 13.61 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.28 | 29.98 | 14.17 | -0.05 | 233940.09 | 3.36 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.4 | 45.06 | 14.23 | 0.09 | 164646.24 | 19.55 | skipped_fast |
| CCUSDT | IDLE | 2.23 | 11.56 | 4.18 | 0.17 | 764486.31 | 10.14 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.22 | 8.47 | 6.24 | 0.04 | 547387.63 | 32.54 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.28 | 13.91 | 9.52 | 0.03 | 197013.52 | 10.91 | skipped_fast |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.9 | 9.68 | 6.53 | 0.07 | 73540.38 | 20.55 | skipped_fast |
| EDELUSDT | IDLE | 2.12 | 4.52 | 1.08 | -0.02 | 88506.95 | 32.77 | skipped_fast |
| RIZEUSDT | IDLE | 1.72 | 6.91 | 6.28 | 0.06 | 58981.46 | 47.31 | skipped_fast |
| RWAINCUSDT | IDLE | 2.5 | 4.48 | 3.4 | 0.0 | 11498.71 | 70.06 | skipped_fast |
| FLUIDUSDT | IDLE | 3.18 | 7.9 | 4.66 | 0.06 | 5400.55 | 21.21 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3288.58 | 35.86 | skipped_fast |
| TELUSDT | IDLE | 2.07 | 5.52 | 2.62 | 0.07 | 195106.39 | 40.63 | skipped_fast |
| RWAUSDT | IDLE | 1.85 | 3.38 | 2.07 | 0.05 | 57955.39 | 24.4 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
