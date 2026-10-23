# Hulk DIGEST — 2026-10-23T15:49:30Z

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
| XRPUSDT | IDLE | 0.93 | 1.71 | 0.97 | -0.01 | 28380958.2 | 0.76 | skipped_fast |
| ETHUSDT | IDLE | 0.84 | 1.6 | 0.47 | 0.01 | 221889688.5 | 0.33 | skipped_fast |
| BTCUSDT | IDLE | 0.61 | 1.15 | 0.53 | 0.0 | 312455023.92 | 0.0 | skipped_fast |
| QNTUSDT | IDLE | 2.15 | 4.05 | 1.72 | -0.04 | 1195325.38 | 6.04 | skipped_fast |
| EDELUSDT | IDLE | 2.82 | 5.36 | 1.85 | 0.0 | 471479.96 | 18.51 | skipped_fast |
| PYTHUSDT | IDLE | 1.39 | 2.71 | 0.46 | -0.02 | 703615.26 | 4.16 | skipped_fast |
| WUSDT | IDLE | 1.79 | 3.45 | 0.81 | 0.02 | 611790.89 | 13.36 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.96 | 11.8 | 5.66 | -0.05 | 39063.26 | 30.96 | skipped_fast |
| CHIPUSDT | IDLE | 2.23 | 4.3 | 2.82 | 0.02 | 116573.26 | 20.4 | skipped_fast |
| ZBCNUSDT | IDLE | 1.8 | 3.34 | 2.33 | 0.01 | 197663.17 | 13.46 | skipped_fast |
| CCUSDT | IDLE | 1.66 | 3.27 | 0.36 | 0.03 | 192134.05 | 6.66 | skipped_fast |
| RWAINCUSDT | IDLE | 1.87 | 3.48 | 1.68 | 0.02 | 52506.18 | 27.53 | skipped_fast |
| REDUSDT | IDLE | 1.44 | 2.87 | 0.0 | 0.0 | 61035.15 | 18.3 | skipped_fast |
| BIOUSDT | IDLE | 1.16 | 2.24 | 0.54 | 0.02 | 70962.81 | 8.32 | skipped_fast |
| KITEUSDT | IDLE | 1.12 | 2.09 | 0.98 | 0.01 | 57955.58 | 10.78 | skipped_fast |
| HBARUSDT | IDLE | 1.21 | 2.16 | 1.79 | -0.01 | 303928.95 | 1.27 | skipped_fast |
| LAUSDT | IDLE | 1.59 | 3.02 | 1.12 | 0.04 | 56626.05 | 22.99 | skipped_fast |
| WAXLUSDT | IDLE | 1.51 | 2.98 | 0.23 | 0.01 | 57612.33 | 45.27 | skipped_fast |
| IOTAUSDT | IDLE | 1.1 | 2.17 | 0.24 | 0.01 | 70933.7 | 28.8 | skipped_fast |
| FLUIDUSDT | IDLE | 1.12 | 2.05 | 1.27 | -0.03 | 8394.26 | 21.53 | skipped_fast |
| RWAUSDT | IDLE | 0.4 | 0.79 | 0.08 | 0.02 | 51879.45 | 23.54 | skipped_fast |
| MNSRYUSDT | IDLE | 0.71 | 1.32 | 0.64 | -0.0 | 36430.02 | 74.39 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
