# Hulk DIGEST — 2026-10-19T08:57:04Z

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
| XRPUSDT | IDLE | 0.55 | 1.02 | 0.54 | 0.02 | 31605093.01 | 1.52 | skipped_fast |
| ETHUSDT | IDLE | 0.54 | 1.03 | 0.32 | 0.01 | 141824248.94 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.43 | 0.81 | 0.28 | 0.01 | 324386306.92 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.09 | 3.02 | 1.58 | -0.04 | 1017218.68 | 1.33 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.19 | 11.35 | 5.24 | 0.02 | 316138.09 | 26.66 | skipped_fast |
| QNTUSDT | IDLE | 2.02 | 5.46 | 1.25 | 0.02 | 687557.88 | 9.52 | skipped_fast |
| WUSDT | IDLE | 1.34 | 2.45 | 2.05 | -0.04 | 532683.51 | 15.63 | skipped_fast |
| HBARUSDT | IDLE | 0.71 | 1.69 | 0.68 | -0.04 | 820915.62 | 4.72 | skipped_fast |
| EDELUSDT | IDLE | 1.98 | 3.92 | 3.13 | 0.02 | 235782.22 | 40.64 | skipped_fast |
| CCUSDT | IDLE | 0.88 | 1.62 | 0.9 | 0.02 | 318688.44 | 9.75 | skipped_fast |
| RWAINCUSDT | IDLE | 1.68 | 5.06 | 2.18 | -0.02 | 80996.86 | 63.66 | skipped_fast |
| CHIPUSDT | IDLE | 0.99 | 2.54 | 2.13 | -0.0 | 78276.18 | 14.19 | skipped_fast |
| KITEUSDT | IDLE | 0.97 | 1.83 | 0.69 | 0.02 | 64185.8 | 11.23 | skipped_fast |
| REDUSDT | IDLE | 0.77 | 1.43 | 0.77 | -0.0 | 94267.66 | 16.02 | skipped_fast |
| BIOUSDT | IDLE | 0.74 | 1.45 | 0.17 | 0.0 | 80534.27 | 4.2 | skipped_fast |
| FLUIDUSDT | IDLE | 2.24 | 6.06 | 1.87 | 0.02 | 7651.86 | 16.15 | skipped_fast |
| RIZEUSDT | IDLE | 0.35 | 1.85 | 1.0 | -0.03 | 58364.8 | 63.44 | skipped_fast |
| RWAUSDT | IDLE | 1.08 | 1.91 | 1.64 | 0.0 | 54921.68 | 15.89 | skipped_fast |
| IOTAUSDT | IDLE | 0.97 | 1.88 | 0.42 | -0.0 | 66368.24 | 28.79 | skipped_fast |
| LAUSDT | IDLE | 0.94 | 1.79 | 0.64 | -0.01 | 58551.25 | 24.47 | skipped_fast |
| WAXLUSDT | IDLE | 0.79 | 3.7 | 1.24 | -0.02 | 85593.09 | 61.86 | skipped_fast |
| MNSRYUSDT | IDLE | 0.26 | 0.51 | 0.11 | -0.0 | 38712.38 | 24.21 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
