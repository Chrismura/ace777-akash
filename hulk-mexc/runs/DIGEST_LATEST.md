# Hulk DIGEST — 2026-08-22T06:31:32Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.15 | 19.14 | 9.22 | 0.06 | 19925485.41 | 23.68 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.27 | 23.87 | 8.69 | 0.19 | 211165432.94 | 6.45 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.26 | 15.8 | 9.09 | 0.05 | 1387463.02 | 1.27 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.3 | 24.54 | 12.38 | -0.1 | 689320.53 | 6.72 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.27 | 17.58 | 7.91 | 0.06 | 614641.2 | 14.49 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.26 | 29.98 | 13.34 | -0.05 | 245736.1 | 3.34 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.19 | 42.58 | 11.18 | 0.09 | 166329.4 | 12.24 | skipped_fast |
| CCUSDT | IDLE | 1.99 | 11.25 | 3.19 | 0.19 | 776981.2 | 8.25 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.21 | 8.47 | 6.02 | 0.03 | 545791.06 | 26.53 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.38 | 13.91 | 8.83 | 0.04 | 200276.6 | 9.3 | skipped_fast |
| KITEUSDT | IDLE | 2.84 | 9.68 | 4.74 | 0.09 | 74874.37 | 11.89 | skipped_fast |
| EDELUSDT | IDLE | 2.3 | 4.52 | 3.68 | -0.03 | 88112.75 | 44.79 | skipped_fast |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.51 | 8.47 | 5.26 | 0.05 | 6989.9 | 21.28 | skipped_fast |
| RWAINCUSDT | IDLE | 2.49 | 4.48 | 3.29 | 0.01 | 11437.27 | 64.66 | skipped_fast |
| TELUSDT | IDLE | 2.14 | 5.52 | 3.95 | 0.06 | 196524.43 | 35.98 | skipped_fast |
| QAITUSDT | IDLE | 1.63 | 3.24 | 0.16 | -0.01 | 3303.04 | 63.67 | skipped_fast |
| RIZEUSDT | IDLE | 0.93 | 3.99 | 1.55 | 0.09 | 59533.29 | 46.34 | skipped_fast |
| RWAUSDT | IDLE | 1.83 | 3.38 | 1.91 | 0.04 | 58113.67 | 16.25 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
