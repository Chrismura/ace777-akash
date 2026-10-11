# Hulk DIGEST — 2026-10-11T21:24:59Z

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
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 3.64 | 32.38 | 10.89 | 0.16 | 4039263.85 | 18.26 | skipped_fast |
| XRPUSDT | IDLE | 1.1 | 1.95 | 1.7 | -0.0 | 15767433.78 | 1.43 | skipped_fast |
| ETHUSDT | IDLE | 0.86 | 1.54 | 1.24 | 0.01 | 212273113.67 | 0.08 | skipped_fast |
| BTCUSDT | IDLE | 0.6 | 1.07 | 0.92 | 0.0 | 155160789.45 | 0.09 | skipped_fast |
| PYTHUSDT | IDLE | 2.42 | 4.34 | 3.37 | -0.02 | 898010.98 | 9.04 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.48 | 21.63 | 10.63 | 0.03 | 39910.97 | 50.71 | skipped_fast |
| EDELUSDT | IDLE | 2.79 | 4.96 | 4.12 | -0.03 | 401485.4 | 26.48 | skipped_fast |
| QNTUSDT | IDLE | 2.13 | 3.75 | 3.41 | -0.01 | 769338.76 | 1.26 | skipped_fast |
| ZBCNUSDT | IDLE | 2.49 | 4.44 | 3.57 | 0.0 | 199624.34 | 12.6 | skipped_fast |
| CCUSDT | IDLE | 1.44 | 2.76 | 2.6 | 0.04 | 343930.6 | 7.23 | skipped_fast |
| CHIPUSDT | IDLE | 1.08 | 4.13 | 3.35 | -0.0 | 291233.78 | 13.35 | skipped_fast |
| BIOUSDT | IDLE | 1.44 | 2.54 | 2.28 | -0.0 | 89212.32 | 6.75 | skipped_fast |
| TELUSDT | IDLE | 2.63 | 4.8 | 3.11 | -0.05 | 180119.62 | 52.46 | skipped_fast |
| RWAINCUSDT | IDLE | 1.42 | 3.82 | 2.72 | 0.01 | 28731.93 | 4.92 | skipped_fast |
| KITEUSDT | IDLE | 1.03 | 1.83 | 1.52 | -0.01 | 75225.07 | 8.7 | skipped_fast |
| REDUSDT | IDLE | 1.1 | 1.94 | 1.79 | -0.0 | 57699.05 | 15.92 | skipped_fast |
| HBARUSDT | IDLE | 1.19 | 2.13 | 1.68 | 0.0 | 298259.7 | 7.51 | skipped_fast |
| RWAUSDT | IDLE | 1.68 | 3.05 | 2.05 | 0.02 | 52557.57 | 15.5 | skipped_fast |
| MNSRYUSDT | IDLE | 0.97 | 1.79 | 1.04 | -0.01 | 32244.88 | 15.06 | skipped_fast |
| FLUIDUSDT | IDLE | 0.38 | 2.63 | 2.47 | 0.05 | 61253.99 | 20.62 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
