# Hulk DIGEST — 2026-10-29T18:49:44Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.53 | 11.89 | 10.52 | -0.05 | 1093142.73 | 2.93 | skipped_fast |
| XRPUSDT | IDLE | 1.73 | 3.06 | 2.68 | -0.03 | 24805792.49 | 0.78 | skipped_fast |
| ETHUSDT | IDLE | 1.58 | 2.84 | 2.11 | -0.01 | 271521091.92 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 1.38 | 2.53 | 1.5 | -0.0 | 371589579.75 | 0.0 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 3.28 | 5.78 | 5.25 | -0.04 | 515773.41 | 1.58 | skipped_fast |
| WUSDT | IDLE | 2.58 | 4.6 | 3.69 | -0.05 | 392454.68 | 16.46 | skipped_fast |
| CCUSDT | IDLE | 2.31 | 4.89 | 4.44 | 0.01 | 378162.65 | 9.96 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.07 | 8.59 | 7.46 | -0.0 | 134096.13 | 12.31 | skipped_fast |
| HBARUSDT | IDLE | 2.62 | 4.67 | 3.8 | -0.03 | 442646.12 | 5.48 | skipped_fast |
| EDELUSDT | IDLE | 1.64 | 2.92 | 2.46 | -0.05 | 349977.35 | 22.66 | skipped_fast |
| BIOUSDT | IDLE | 2.68 | 5.1 | 2.81 | 0.0 | 76923.01 | 8.76 | skipped_fast |
| KITEUSDT | IDLE | 1.77 | 3.1 | 2.94 | -0.03 | 60580.76 | 14.25 | skipped_fast |
| ZBCNUSDT | IDLE | 1.11 | 2.05 | 1.2 | -0.0 | 225935.14 | 19.89 | skipped_fast |
| REDUSDT | IDLE | 1.69 | 2.97 | 2.77 | -0.02 | 63916.82 | 17.48 | skipped_fast |
| LAUSDT | IDLE | 2.49 | 4.49 | 3.31 | -0.01 | 60714.05 | 22.83 | skipped_fast |
| RWAINCUSDT | IDLE | 1.21 | 2.2 | 1.53 | -0.02 | 33622.5 | 7.06 | skipped_fast |
| IOTAUSDT | IDLE | 2.03 | 3.67 | 3.28 | -0.04 | 96123.62 | 17.42 | skipped_fast |
| FLUIDUSDT | IDLE | 2.16 | 5.88 | 5.56 | -0.09 | 7847.9 | 21.54 | skipped_fast |
| RIZEUSDT | IDLE | 0.82 | 1.55 | 0.58 | -0.02 | 67771.17 | 67.67 | skipped_fast |
| WAXLUSDT | IDLE | 1.55 | 3.49 | 3.04 | -0.05 | 53163.31 | 34.35 | skipped_fast |
| MNSRYUSDT | IDLE | 1.05 | 2.04 | 0.42 | -0.0 | 38268.78 | 40.93 | skipped_fast |
| RWAUSDT | IDLE | 0.91 | 1.7 | 0.8 | -0.0 | 55855.3 | 40.14 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
