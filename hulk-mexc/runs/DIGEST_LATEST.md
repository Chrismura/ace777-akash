# Hulk DIGEST — 2026-10-18T20:08:18Z

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
| ETHUSDT | IDLE | 1.3 | 2.32 | 1.93 | -0.03 | 113892991.91 | 0.3 | skipped_fast |
| XRPUSDT | IDLE | 1.05 | 1.89 | 1.38 | -0.03 | 27694027.61 | 2.38 | skipped_fast |
| BTCUSDT | IDLE | 0.33 | 0.59 | 0.47 | -0.01 | 224139675.04 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.22 | 4.47 | 3.84 | -0.13 | 1410909.69 | 2.75 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 3.69 | 8.29 | 7.04 | -0.03 | 764126.8 | 4.88 | skipped_fast |
| WUSDT | IDLE | 1.7 | 4.48 | 3.91 | -0.1 | 914398.81 | 16.61 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 4.46 | 12.83 | 9.82 | -0.03 | 46102.38 | 5.36 | skipped_fast |
| QNTUSDT | IDLE | 2.36 | 5.27 | 4.58 | -0.09 | 622759.33 | 1.64 | skipped_fast |
| WAXLUSDT | WATCH_PULLBACK — tension haute + reflux | 3.64 | 16.5 | 9.01 | -0.02 | 77992.54 | 46.02 | skipped_fast |
| ZBCNUSDT | IDLE | 2.05 | 3.92 | 2.94 | -0.06 | 206361.54 | 26.17 | skipped_fast |
| CCUSDT | IDLE | 1.68 | 3.11 | 2.59 | -0.08 | 251267.72 | 8.23 | skipped_fast |
| EDELUSDT | IDLE | 1.74 | 4.42 | 3.41 | -0.09 | 241926.22 | 27.16 | skipped_fast |
| CHIPUSDT | IDLE | 1.89 | 5.57 | 5.13 | -0.11 | 78807.01 | 10.24 | skipped_fast |
| BIOUSDT | IDLE | 1.77 | 3.59 | 2.78 | -0.08 | 84523.45 | 8.79 | skipped_fast |
| REDUSDT | IDLE | 1.68 | 2.93 | 2.82 | -0.06 | 95060.9 | 12.1 | skipped_fast |
| RIZEUSDT | IDLE | 1.62 | 7.91 | 6.49 | -0.04 | 58685.22 | 63.44 | skipped_fast |
| KITEUSDT | IDLE | 1.5 | 2.64 | 2.4 | -0.06 | 69447.6 | 9.89 | skipped_fast |
| IOTAUSDT | IDLE | 1.91 | 4.24 | 3.24 | -0.08 | 71078.58 | 20.92 | skipped_fast |
| FLUIDUSDT | IDLE | 1.89 | 3.35 | 2.91 | -0.07 | 4487.41 | 21.44 | skipped_fast |
| LAUSDT | IDLE | 1.36 | 3.42 | 3.12 | -0.1 | 58385.23 | 43.47 | skipped_fast |
| RWAUSDT | IDLE | 0.58 | 1.05 | 0.8 | -0.01 | 48724.33 | 24.09 | skipped_fast |
| MNSRYUSDT | IDLE | 0.39 | 0.7 | 0.54 | -0.01 | 34716.95 | 62.65 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
