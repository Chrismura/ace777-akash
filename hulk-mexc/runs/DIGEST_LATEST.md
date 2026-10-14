# Hulk DIGEST — 2026-10-14T16:19:40Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 3.93 | 8.7 | 7.69 | 0.0 | 2079002.46 | 2.53 | skipped_fast |
| WUSDT | IDLE | 1.95 | 8.09 | 6.86 | -0.12 | 3186462.52 | 9.96 | skipped_fast |
| XRPUSDT | IDLE | 2.47 | 4.34 | 4.06 | -0.03 | 41728833.65 | 1.51 | skipped_fast |
| ETHUSDT | IDLE | 2.38 | 4.22 | 3.65 | -0.04 | 186469122.19 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 1.61 | 2.81 | 2.73 | -0.02 | 416771612.08 | 0.0 | skipped_fast |
| QNTUSDT | IDLE | 1.94 | 4.8 | 1.99 | 0.01 | 1473836.81 | 1.93 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 4.18 | 22.88 | 17.9 | 0.03 | 62772.9 | 59.57 | skipped_fast |
| ZBCNUSDT | IDLE | 3.92 | 7.17 | 4.52 | -0.03 | 188389.7 | 24.27 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.35 | 9.7 | 7.9 | -0.08 | 109997.2 | 13.25 | skipped_fast |
| CCUSDT | IDLE | 1.51 | 3.9 | 2.83 | -0.08 | 448064.68 | 11.0 | skipped_fast |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.61 | 7.31 | 5.56 | 0.01 | 86701.46 | 8.5 | skipped_fast |
| HBARUSDT | IDLE | 2.31 | 4.11 | 3.36 | -0.03 | 464336.89 | 5.94 | skipped_fast |
| BIOUSDT | IDLE | 2.63 | 4.67 | 3.96 | -0.04 | 68569.11 | 3.77 | skipped_fast |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.84 | 13.1 | 8.75 | 0.05 | 18300.68 | 55.35 | skipped_fast |
| EDELUSDT | IDLE | 1.96 | 3.55 | 2.53 | -0.02 | 163566.46 | 20.85 | skipped_fast |
| REDUSDT | IDLE | 2.17 | 3.88 | 3.02 | -0.01 | 61019.44 | 15.83 | skipped_fast |
| RWAINCUSDT | IDLE | 1.54 | 4.94 | 4.45 | -0.09 | 31486.74 | 27.12 | skipped_fast |
| TELUSDT | IDLE | 2.29 | 4.39 | 1.27 | 0.02 | 115000.07 | 33.63 | skipped_fast |
| RWAUSDT | IDLE | 1.31 | 2.31 | 2.1 | -0.03 | 56336.88 | 7.94 | skipped_fast |
| MNSRYUSDT | IDLE | 0.62 | 1.13 | 0.68 | -0.01 | 38928.94 | 40.75 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
