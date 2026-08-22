# Hulk DIGEST — 2026-08-22T05:59:13Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.13 | 19.14 | 8.63 | 0.08 | 17842363.15 | 15.67 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.28 | 23.87 | 10.05 | 0.16 | 206718026.32 | 8.52 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.26 | 15.8 | 8.99 | 0.05 | 1369748.39 | 6.32 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.28 | 24.54 | 11.74 | -0.09 | 709430.37 | 6.65 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.25 | 17.58 | 7.24 | 0.07 | 610219.83 | 7.19 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.39 | 45.06 | 13.7 | 0.09 | 164904.8 | 11.45 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.24 | 29.98 | 11.89 | -0.03 | 245259.24 | 16.37 | skipped_fast |
| CCUSDT | IDLE | 2.18 | 11.56 | 2.41 | 0.18 | 763134.06 | 7.47 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.21 | 8.47 | 5.94 | 0.04 | 547429.06 | 14.47 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.25 | 13.91 | 8.6 | 0.04 | 197137.69 | 1.54 | skipped_fast |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.87 | 9.68 | 5.74 | 0.08 | 74171.71 | 12.01 | skipped_fast |
| EDELUSDT | IDLE | 2.11 | 4.52 | 0.97 | 0.0 | 88080.42 | 10.95 | skipped_fast |
| RWAINCUSDT | IDLE | 2.49 | 4.48 | 3.35 | 0.01 | 11565.56 | 64.66 | skipped_fast |
| RIZEUSDT | IDLE | 1.72 | 6.91 | 6.18 | 0.07 | 59010.12 | 47.31 | skipped_fast |
| FLUIDUSDT | IDLE | 3.17 | 7.9 | 4.42 | 0.06 | 5386.26 | 22.51 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3283.04 | 7.99 | skipped_fast |
| TELUSDT | IDLE | 2.06 | 5.52 | 2.57 | 0.07 | 195762.76 | 40.53 | skipped_fast |
| RWAUSDT | IDLE | 1.83 | 3.38 | 1.83 | 0.05 | 57930.28 | 32.41 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
