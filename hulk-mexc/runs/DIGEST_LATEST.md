# Hulk DIGEST — 2026-10-24T16:29:17Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| ETHUSDT | IDLE | 2.2 | 3.93 | 3.17 | -0.04 | 133411001.77 | 0.65 | skipped_fast |
| XRPUSDT | IDLE | 1.45 | 2.62 | 1.89 | -0.03 | 31099855.74 | 0.79 | skipped_fast |
| BTCUSDT | IDLE | 1.1 | 1.97 | 1.48 | -0.02 | 275204017.51 | 0.0 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 4.26 | 10.49 | 8.23 | -0.08 | 643974.39 | 36.93 | skipped_fast |
| WUSDT | IDLE | 1.66 | 4.49 | 3.52 | -0.09 | 1059813.28 | 21.46 | skipped_fast |
| PYTHUSDT | IDLE | 2.35 | 5.03 | 4.25 | -0.06 | 683272.55 | 2.97 | skipped_fast |
| LAUSDT | WATCH_PULLBACK — tension haute + reflux | 3.56 | 20.14 | 15.27 | 0.08 | 106657.95 | 17.84 | skipped_fast |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.17 | 5.96 | 5.46 | -0.07 | 61202.43 | 10.78 | skipped_fast |
| CCUSDT | IDLE | 2.46 | 4.43 | 3.23 | -0.05 | 239417.95 | 7.07 | skipped_fast |
| BIOUSDT | IDLE | 2.53 | 5.2 | 4.94 | -0.08 | 70643.36 | 4.52 | skipped_fast |
| REDUSDT | IDLE | 2.23 | 7.95 | 5.03 | 0.02 | 92840.91 | 16.44 | skipped_fast |
| QNTUSDT | IDLE | 2.56 | 4.51 | 4.06 | -0.04 | 358747.7 | 1.72 | skipped_fast |
| RWAINCUSDT | IDLE | 2.47 | 4.42 | 3.44 | 0.01 | 49321.53 | 5.47 | skipped_fast |
| CHIPUSDT | IDLE | 2.0 | 5.07 | 4.53 | -0.07 | 71723.31 | 14.59 | skipped_fast |
| ZBCNUSDT | IDLE | 1.63 | 4.39 | 2.41 | -0.07 | 195077.93 | 29.23 | skipped_fast |
| WAXLUSDT | WATCH_PULLBACK — tension haute + reflux | 2.8 | 8.17 | 7.01 | -0.02 | 60632.93 | 39.6 | skipped_fast |
| IOTAUSDT | IDLE | 2.68 | 4.76 | 4.0 | -0.06 | 72166.38 | 30.71 | skipped_fast |
| HBARUSDT | IDLE | 1.59 | 2.96 | 1.45 | -0.03 | 179426.92 | 9.22 | skipped_fast |
| FLUIDUSDT | IDLE | 2.11 | 5.72 | 5.41 | -0.07 | 17326.74 | 21.33 | skipped_fast |
| RIZEUSDT | IDLE | 1.02 | 1.78 | 1.68 | -0.04 | 29694.54 | 26.97 | skipped_fast |
| RWAUSDT | IDLE | 0.69 | 1.2 | 1.18 | -0.02 | 52856.47 | 31.95 | skipped_fast |
| MNSRYUSDT | IDLE | 0.92 | 1.61 | 1.48 | -0.02 | 38396.1 | 77.07 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
