# Hulk DIGEST — 2026-10-13T17:05:22Z

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
| WUSDT | IDLE | 2.13 | 16.19 | 13.32 | -0.24 | 5367584.2 | 16.49 | skipped_fast |
| PYTHUSDT | IDLE | 2.67 | 8.61 | 4.54 | -0.07 | 2140071.25 | 12.44 | skipped_fast |
| XRPUSDT | IDLE | 1.06 | 1.96 | 1.07 | 0.0 | 37290051.26 | 1.46 | skipped_fast |
| ETHUSDT | IDLE | 0.74 | 1.36 | 0.78 | -0.0 | 237119765.48 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.48 | 0.85 | 0.68 | 0.01 | 385754645.97 | 0.0 | skipped_fast |
| QNTUSDT | IDLE | 1.21 | 4.18 | 3.22 | -0.11 | 1290751.5 | 1.47 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 4.46 | 14.13 | 10.78 | -0.1 | 77114.69 | 60.67 | skipped_fast |
| CCUSDT | IDLE | 2.32 | 7.41 | 1.27 | 0.06 | 588296.13 | 5.4 | skipped_fast |
| EDELUSDT | IDLE | 2.45 | 5.03 | 2.88 | 0.05 | 306948.39 | 23.49 | skipped_fast |
| ZBCNUSDT | IDLE | 1.74 | 3.31 | 1.14 | -0.01 | 236410.21 | 13.01 | skipped_fast |
| CHIPUSDT | IDLE | 2.04 | 4.31 | 3.84 | -0.02 | 108794.27 | 14.01 | skipped_fast |
| REDUSDT | IDLE | 1.51 | 3.24 | 0.41 | -0.01 | 152630.01 | 15.6 | skipped_fast |
| HBARUSDT | IDLE | 1.81 | 3.37 | 1.7 | -0.02 | 351776.78 | 6.87 | skipped_fast |
| RWAINCUSDT | IDLE | 1.88 | 3.75 | 0.0 | 0.01 | 30297.85 | 28.99 | skipped_fast |
| BIOUSDT | IDLE | 1.37 | 3.0 | 1.33 | -0.03 | 72041.19 | 7.27 | skipped_fast |
| KITEUSDT | IDLE | 1.13 | 2.33 | 1.26 | 0.0 | 60583.58 | 10.27 | skipped_fast |
| TELUSDT | IDLE | 1.58 | 2.89 | 1.74 | -0.0 | 106797.4 | 34.31 | skipped_fast |
| FLUIDUSDT | IDLE | 1.38 | 2.93 | 1.19 | 0.04 | 26423.78 | 16.9 | skipped_fast |
| MNSRYUSDT | IDLE | 0.57 | 1.04 | 0.68 | -0.02 | 38363.51 | 15.34 | skipped_fast |
| RWAUSDT | IDLE | 0.26 | 0.46 | 0.38 | 0.0 | 52405.46 | 7.72 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
