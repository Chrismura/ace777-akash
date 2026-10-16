# Hulk DIGEST — 2026-10-16T18:03:21Z

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
| PYTHUSDT | IDLE | 2.13 | 7.52 | 6.11 | -0.1 | 2207945.08 | 2.37 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 3.06 | 7.35 | 5.82 | -0.04 | 1667103.54 | 11.28 | skipped_fast |
| XRPUSDT | IDLE | 2.14 | 3.81 | 3.14 | -0.03 | 25698064.59 | 0.77 | skipped_fast |
| ETHUSDT | IDLE | 2.01 | 3.61 | 2.69 | -0.01 | 210747203.58 | 0.54 | skipped_fast |
| BTCUSDT | IDLE | 1.13 | 2.05 | 1.42 | -0.01 | 358442817.42 | 0.0 | skipped_fast |
| QNTUSDT | IDLE | 2.58 | 4.55 | 4.12 | -0.04 | 890538.51 | 5.52 | skipped_fast |
| CCUSDT | IDLE | 2.42 | 4.35 | 3.21 | -0.04 | 391347.19 | 5.82 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 3.27 | 10.73 | 9.24 | -0.1 | 24252.41 | 5.47 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 3.41 | 6.0 | 5.52 | -0.02 | 313315.37 | 10.94 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 2.92 | 6.95 | 5.47 | -0.09 | 97620.52 | 15.18 | skipped_fast |
| ZBCNUSDT | IDLE | 2.61 | 4.58 | 4.31 | -0.02 | 218744.49 | 23.99 | skipped_fast |
| CHIPUSDT | IDLE | 2.32 | 8.31 | 6.36 | -0.02 | 152702.61 | 13.18 | skipped_fast |
| EDELUSDT | IDLE | 2.37 | 4.3 | 2.89 | 0.03 | 182577.93 | 20.04 | skipped_fast |
| BIOUSDT | IDLE | 2.37 | 4.24 | 3.33 | -0.03 | 61965.39 | 4.01 | skipped_fast |
| RIZEUSDT | IDLE | 2.37 | 5.54 | 0.83 | 0.05 | 47518.5 | 57.14 | skipped_fast |
| KITEUSDT | IDLE | 1.9 | 3.4 | 2.63 | -0.03 | 56775.99 | 11.64 | skipped_fast |
| RWAUSDT | IDLE | 2.07 | 3.9 | 1.64 | 0.0 | 54140.09 | 31.77 | skipped_fast |
| TELUSDT | IDLE | 1.19 | 2.09 | 1.94 | -0.0 | 90559.17 | 39.51 | skipped_fast |
| FLUIDUSDT | IDLE | 1.26 | 2.36 | 1.12 | -0.03 | 6135.25 | 21.48 | skipped_fast |
| MNSRYUSDT | IDLE | 0.4 | 0.7 | 0.68 | -0.01 | 35874.19 | 26.98 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
