# Hulk DIGEST — 2026-09-07T20:47:48Z

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
| XRPUSDT | IDLE | 0.92 | 1.79 | 0.31 | -0.01 | 36422072.58 | 2.14 | skipped_fast |
| ETHUSDT | IDLE | 0.68 | 1.31 | 0.27 | -0.0 | 345310083.6 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.47 | 0.91 | 0.26 | -0.01 | 457814569.59 | 0.0 | skipped_fast |
| ZBCNUSDT | IDLE | 3.49 | 9.56 | 3.68 | -0.03 | 214920.05 | 18.9 | skipped_fast |
| PYTHUSDT | IDLE | 1.61 | 3.02 | 1.38 | -0.0 | 563908.03 | 1.82 | skipped_fast |
| CCUSDT | IDLE | 1.99 | 3.5 | 3.2 | -0.06 | 475674.7 | 9.6 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 3.27 | 10.08 | 9.16 | -0.01 | 4791.7 | 5.28 | skipped_fast |
| CHIPUSDT | IDLE | 1.98 | 8.01 | 1.79 | -0.07 | 233568.78 | 9.23 | skipped_fast |
| HBARUSDT | IDLE | 1.61 | 3.14 | 0.49 | 0.02 | 588385.89 | 1.21 | skipped_fast |
| WUSDT | IDLE | 1.36 | 2.6 | 0.75 | -0.0 | 263204.6 | 13.64 | skipped_fast |
| RIZEUSDT | IDLE | 2.08 | 6.16 | 3.62 | -0.05 | 59932.66 | 46.19 | skipped_fast |
| EDELUSDT | IDLE | 1.49 | 5.62 | 1.67 | -0.05 | 99512.65 | 10.01 | skipped_fast |
| REDUSDT | IDLE | 1.43 | 2.64 | 1.4 | 0.03 | 58884.27 | 9.88 | skipped_fast |
| KITEUSDT | IDLE | 1.39 | 2.53 | 1.65 | -0.04 | 60539.7 | 12.56 | skipped_fast |
| BIOUSDT | IDLE | 1.21 | 2.35 | 0.51 | -0.01 | 67676.37 | 7.32 | skipped_fast |
| QNTUSDT | IDLE | 1.08 | 2.11 | 0.31 | 0.0 | 48179.42 | 1.5 | skipped_fast |
| TELUSDT | IDLE | 1.02 | 1.89 | 0.99 | -0.01 | 112440.19 | 35.19 | skipped_fast |
| RWAUSDT | IDLE | 0.52 | 0.95 | 0.65 | -0.01 | 53819.66 | 14.55 | skipped_fast |
| FLUIDUSDT | IDLE | 0.77 | 1.54 | 0.0 | 0.01 | 1643.72 | 21.78 | skipped_fast |
| MNSRYUSDT | IDLE | 0.38 | 0.7 | 0.37 | -0.01 | 37368.29 | 9.54 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
