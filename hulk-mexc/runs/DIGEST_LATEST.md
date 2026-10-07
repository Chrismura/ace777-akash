# Hulk DIGEST — 2026-10-07T02:41:01Z

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
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 3.65 | 6.52 | 5.15 | -0.04 | 2365635.82 | 9.77 | skipped_fast |
| ETHUSDT | IDLE | 2.35 | 4.24 | 3.06 | -0.03 | 387023649.89 | 0.57 | skipped_fast |
| XRPUSDT | IDLE | 2.17 | 3.92 | 2.85 | -0.03 | 37255056.98 | 1.37 | skipped_fast |
| BTCUSDT | IDLE | 1.36 | 2.42 | 2.05 | -0.02 | 582208999.66 | 0.0 | skipped_fast |
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 3.14 | 9.87 | 6.6 | -0.06 | 1026064.72 | 2.74 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.05 | 18.99 | 9.78 | -0.14 | 501108.97 | 68.29 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.01 | 15.45 | 9.58 | -0.07 | 89204.2 | 6.88 | skipped_fast |
| CCUSDT | IDLE | 3.17 | 5.78 | 3.74 | -0.04 | 436200.88 | 6.51 | skipped_fast |
| WUSDT | IDLE | 2.99 | 5.7 | 1.9 | 0.03 | 465640.81 | 15.84 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.55 | 7.56 | 5.74 | -0.03 | 199308.56 | 15.4 | skipped_fast |
| HBARUSDT | IDLE | 3.0 | 5.38 | 4.16 | -0.05 | 509121.0 | 8.33 | skipped_fast |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.73 | 16.23 | 5.61 | 0.09 | 188248.16 | 43.51 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.04 | 6.17 | 5.33 | -0.08 | 61678.19 | 15.55 | skipped_fast |
| ZBCNUSDT | IDLE | 2.42 | 4.26 | 3.91 | -0.02 | 203793.6 | 14.36 | skipped_fast |
| KITEUSDT | IDLE | 2.28 | 4.29 | 1.78 | -0.0 | 58336.75 | 10.02 | skipped_fast |
| RWAINCUSDT | IDLE | 2.48 | 6.92 | 1.49 | -0.03 | 32929.96 | 82.23 | skipped_fast |
| RIZEUSDT | IDLE | 0.88 | 8.39 | 3.8 | 0.2 | 86723.93 | 53.99 | skipped_fast |
| FLUIDUSDT | IDLE | 1.91 | 5.57 | 3.99 | -0.13 | 62758.2 | 20.92 | skipped_fast |
| RWAUSDT | IDLE | 1.15 | 2.02 | 1.9 | -0.02 | 52739.76 | 7.46 | skipped_fast |
| MNSRYUSDT | IDLE | 1.19 | 2.12 | 1.76 | -0.02 | 38094.93 | 63.68 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
