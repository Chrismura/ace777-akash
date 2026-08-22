# Hulk DIGEST — 2026-08-22T08:24:48Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.15 | 19.14 | 9.42 | 0.04 | 27582808.26 | 7.91 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.76 | 23.87 | 9.44 | 0.15 | 222786618.03 | 5.85 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.31 | 15.8 | 9.76 | 0.03 | 1343784.92 | 5.1 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.29 | 24.54 | 12.18 | -0.1 | 684840.03 | 10.04 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.28 | 17.58 | 7.96 | 0.04 | 599796.8 | 13.45 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.18 | 29.98 | 8.92 | -0.03 | 250699.21 | 3.17 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.15 | 42.01 | 11.31 | 0.08 | 155106.8 | 4.38 | skipped_fast |
| CCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.04 | 11.25 | 1.92 | 0.2 | 823273.9 | 8.14 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.27 | 8.47 | 6.1 | 0.02 | 537048.24 | 36.92 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.37 | 13.91 | 8.7 | 0.03 | 194063.97 | 6.18 | skipped_fast |
| KITEUSDT | IDLE | 3.81 | 9.68 | 3.97 | 0.07 | 73046.12 | 12.7 | skipped_fast |
| FLUIDUSDT | IDLE | 3.75 | 7.38 | 4.01 | 0.04 | 6888.1 | 21.75 | skipped_fast |
| EDELUSDT | IDLE | 2.27 | 4.52 | 3.35 | -0.02 | 86841.83 | 66.96 | skipped_fast |
| RWAINCUSDT | IDLE | 2.48 | 4.48 | 3.24 | 0.02 | 11182.34 | 118.15 | skipped_fast |
| TELUSDT | IDLE | 1.85 | 4.7 | 3.95 | -0.0 | 173603.55 | 10.28 | skipped_fast |
| QAITUSDT | IDLE | 1.49 | 2.91 | 0.43 | 0.02 | 3212.56 | 66.45 | skipped_fast |
| RIZEUSDT | IDLE | 0.84 | 3.73 | 0.78 | 0.01 | 52285.48 | 46.13 | skipped_fast |
| RWAUSDT | IDLE | 1.74 | 3.29 | 1.2 | 0.04 | 58174.97 | 24.14 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
