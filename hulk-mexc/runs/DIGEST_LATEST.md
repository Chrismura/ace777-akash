# Hulk DIGEST — 2026-10-19T12:58:35Z

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
| XRPUSDT | IDLE | 0.98 | 1.83 | 0.83 | 0.01 | 33533152.82 | 2.29 | skipped_fast |
| ETHUSDT | IDLE | 0.77 | 1.39 | 0.94 | 0.0 | 151284641.98 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.67 | 1.24 | 0.71 | 0.01 | 337953207.12 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.75 | 3.94 | 3.33 | -0.07 | 1027549.22 | 4.1 | skipped_fast |
| QNTUSDT | IDLE | 1.28 | 3.55 | 3.13 | 0.01 | 843669.19 | 2.02 | skipped_fast |
| WUSDT | IDLE | 1.34 | 2.67 | 0.05 | -0.03 | 531697.39 | 13.9 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 2.95 | 8.56 | 6.09 | -0.01 | 93980.1 | 31.85 | skipped_fast |
| EDELUSDT | IDLE | 2.25 | 4.55 | 2.95 | 0.01 | 238540.69 | 11.1 | skipped_fast |
| HBARUSDT | IDLE | 1.46 | 2.97 | 1.61 | -0.05 | 654006.61 | 4.77 | skipped_fast |
| CCUSDT | IDLE | 1.43 | 3.05 | 0.0 | 0.04 | 324767.07 | 8.57 | skipped_fast |
| KITEUSDT | IDLE | 2.25 | 4.38 | 0.84 | 0.03 | 61784.19 | 9.29 | skipped_fast |
| CHIPUSDT | IDLE | 1.49 | 3.85 | 2.99 | -0.01 | 87153.2 | 14.35 | skipped_fast |
| ZBCNUSDT | IDLE | 0.53 | 1.86 | 0.96 | 0.02 | 279834.36 | 12.2 | skipped_fast |
| BIOUSDT | IDLE | 1.36 | 2.54 | 1.17 | -0.01 | 73002.95 | 4.24 | skipped_fast |
| REDUSDT | IDLE | 1.2 | 2.28 | 0.77 | -0.01 | 76912.2 | 10.22 | skipped_fast |
| RIZEUSDT | IDLE | 0.92 | 4.84 | 3.64 | -0.07 | 60095.14 | 64.04 | skipped_fast |
| IOTAUSDT | IDLE | 1.69 | 3.11 | 1.74 | -0.01 | 76156.93 | 20.16 | skipped_fast |
| LAUSDT | IDLE | 1.36 | 2.58 | 0.95 | -0.01 | 59189.94 | 22.58 | skipped_fast |
| WAXLUSDT | IDLE | 1.03 | 4.2 | 1.44 | 0.03 | 79286.55 | 46.38 | skipped_fast |
| FLUIDUSDT | IDLE | 1.09 | 2.69 | 2.62 | 0.01 | 6404.42 | 20.99 | skipped_fast |
| RWAUSDT | IDLE | 0.61 | 1.19 | 0.16 | 0.01 | 55394.08 | 55.14 | skipped_fast |
| MNSRYUSDT | IDLE | 0.28 | 0.53 | 0.24 | -0.0 | 40299.04 | 18.52 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
