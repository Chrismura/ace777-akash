# Hulk DIGEST — 2026-09-06T13:30:59Z

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
| XRPUSDT | IDLE | 0.5 | 0.88 | 0.86 | -0.0 | 25440811.75 | 1.41 | skipped_fast |
| ETHUSDT | IDLE | 0.32 | 0.55 | 0.55 | 0.01 | 230999872.84 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.19 | 0.33 | 0.28 | 0.0 | 399001724.21 | 0.0 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.66 | 6.82 | 6.06 | 0.03 | 402636.96 | 1.73 | skipped_fast |
| PYTHUSDT | IDLE | 1.51 | 2.65 | 2.46 | 0.0 | 454584.13 | 3.65 | skipped_fast |
| WUSDT | IDLE | 2.39 | 4.58 | 1.38 | 0.04 | 236563.5 | 13.53 | skipped_fast |
| RWAINCUSDT | IDLE | 2.47 | 5.39 | 2.51 | 0.05 | 6374.45 | 10.28 | skipped_fast |
| RIZEUSDT | IDLE | 1.92 | 10.46 | 9.23 | -0.08 | 74037.76 | 70.92 | skipped_fast |
| CCUSDT | IDLE | 0.97 | 1.72 | 1.52 | -0.0 | 326129.36 | 6.38 | skipped_fast |
| EDELUSDT | IDLE | 1.97 | 3.61 | 2.2 | 0.0 | 68287.92 | 37.56 | skipped_fast |
| ZBCNUSDT | IDLE | 1.39 | 2.48 | 2.06 | -0.01 | 197297.82 | 39.89 | skipped_fast |
| REDUSDT | IDLE | 1.71 | 3.15 | 1.8 | 0.03 | 62209.3 | 10.11 | skipped_fast |
| KITEUSDT | IDLE | 1.53 | 2.75 | 2.06 | 0.0 | 61739.03 | 9.48 | skipped_fast |
| HBARUSDT | IDLE | 0.6 | 1.04 | 1.03 | -0.01 | 451616.21 | 1.24 | skipped_fast |
| BIOUSDT | IDLE | 0.77 | 1.38 | 1.04 | -0.0 | 91695.86 | 3.61 | skipped_fast |
| TELUSDT | IDLE | 0.92 | 1.65 | 1.21 | 0.0 | 67567.02 | 17.58 | skipped_fast |
| MNSRYUSDT | IDLE | 0.58 | 1.08 | 0.52 | 0.02 | 42288.81 | 14.77 | skipped_fast |
| RWAUSDT | IDLE | 0.48 | 0.86 | 0.64 | -0.01 | 52113.13 | 14.29 | skipped_fast |
| QNTUSDT | IDLE | 0.7 | 1.25 | 0.95 | 0.02 | 38238.9 | 42.75 | skipped_fast |
| FLUIDUSDT | IDLE | 0.0 | 0.0 | 0.0 | 0.02 | 353.17 | 21.98 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
