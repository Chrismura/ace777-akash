# Hulk DIGEST — 2026-09-23T18:22:32Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 2.58 | 6.67 | 5.97 | -0.06 | 120946804.91 | 2.02 | skipped_fast |
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 3.71 | 11.74 | 7.35 | -0.07 | 1376316.31 | 4.82 | skipped_fast |
| ETHUSDT | IDLE | 1.83 | 3.32 | 2.33 | -0.03 | 504491822.1 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 1.59 | 2.87 | 2.07 | -0.03 | 886967672.08 | 0.43 | skipped_fast |
| HBARUSDT | IDLE | 2.12 | 6.6 | 5.11 | -0.07 | 1496578.17 | 1.11 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 3.43 | 8.79 | 7.1 | -0.06 | 396104.8 | 9.73 | skipped_fast |
| CCUSDT | IDLE | 2.91 | 6.58 | 4.87 | -0.05 | 524742.65 | 4.65 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.47 | 10.36 | 8.84 | -0.09 | 219753.9 | 21.47 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.39 | 9.46 | 8.05 | -0.11 | 191725.24 | 18.0 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 3.83 | 9.69 | 6.62 | -0.04 | 97195.39 | 10.63 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.41 | 6.14 | 5.26 | -0.04 | 57928.34 | 15.75 | skipped_fast |
| KITEUSDT | IDLE | 2.64 | 4.83 | 3.36 | -0.05 | 172476.0 | 8.3 | skipped_fast |
| ZBCNUSDT | IDLE | 2.03 | 4.91 | 4.04 | -0.02 | 253783.72 | 23.54 | skipped_fast |
| QNTUSDT | IDLE | 2.99 | 6.97 | 4.29 | -0.02 | 181377.15 | 1.41 | skipped_fast |
| RIZEUSDT | IDLE | 1.21 | 14.94 | 12.03 | 0.31 | 73507.08 | 43.91 | skipped_fast |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.47 | 7.2 | 5.5 | -0.04 | 4268.96 | 19.36 | skipped_fast |
| RWAINCUSDT | IDLE | 0.83 | 1.69 | 1.29 | 0.02 | 22868.4 | 5.43 | skipped_fast |
| RWAUSDT | IDLE | 1.63 | 2.9 | 2.46 | -0.03 | 54513.79 | 14.83 | skipped_fast |
| TELUSDT | IDLE | 1.35 | 3.61 | 2.63 | -0.04 | 156718.81 | 76.36 | skipped_fast |
| MNSRYUSDT | IDLE | 1.06 | 1.92 | 1.4 | -0.01 | 40616.09 | 45.56 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
