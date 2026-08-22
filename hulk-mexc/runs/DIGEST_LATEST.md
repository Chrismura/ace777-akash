# Hulk DIGEST — 2026-08-22T05:24:37Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.17 | 19.14 | 10.08 | 0.08 | 16156993.26 | 17.94 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.32 | 23.87 | 12.34 | 0.13 | 197078109.48 | 14.1 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.27 | 15.8 | 9.42 | 0.04 | 1342456.41 | 11.44 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.29 | 24.54 | 12.09 | -0.09 | 679324.74 | 20.02 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.29 | 17.58 | 8.47 | 0.06 | 581509.95 | 19.76 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.24 | 29.98 | 11.98 | -0.04 | 213904.86 | 19.71 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.37 | 45.06 | 12.08 | 0.1 | 164045.3 | 61.58 | skipped_fast |
| CCUSDT | IDLE | 2.23 | 11.56 | 4.2 | 0.16 | 757220.47 | 16.87 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.23 | 8.47 | 6.49 | 0.03 | 544074.75 | 38.66 | skipped_fast |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.9 | 9.68 | 6.39 | 0.08 | 73305.87 | 25.08 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.31 | 13.91 | 10.2 | 0.03 | 195303.82 | 141.04 | skipped_fast |
| RWAINCUSDT | IDLE | 2.38 | 4.48 | 1.83 | 0.03 | 11429.61 | 21.32 | skipped_fast |
| EDELUSDT | IDLE | 2.16 | 4.52 | 1.73 | -0.01 | 88470.79 | 65.72 | skipped_fast |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.22 | 7.9 | 5.34 | 0.05 | 5420.59 | 42.14 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3417.27 | 35.86 | skipped_fast |
| RIZEUSDT | IDLE | 1.1 | 4.41 | 3.99 | 0.09 | 58721.87 | 20.53 | skipped_fast |
| TELUSDT | IDLE | 2.05 | 5.52 | 2.32 | 0.08 | 192451.01 | 40.44 | skipped_fast |
| RWAUSDT | IDLE | 1.87 | 3.38 | 2.39 | 0.04 | 57571.09 | 40.8 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
