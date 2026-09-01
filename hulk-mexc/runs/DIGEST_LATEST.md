# Hulk DIGEST — 2026-09-01T10:23:52Z

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
| XRPUSDT | IDLE | 1.41 | 2.56 | 1.68 | 0.0 | 29341358.79 | 2.19 | skipped_fast |
| BTCUSDT | IDLE | 1.04 | 1.85 | 1.55 | -0.01 | 572795347.76 | 0.05 | skipped_fast |
| ETHUSDT | IDLE | 1.01 | 1.85 | 1.19 | 0.0 | 300764963.06 | 0.04 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 4.18 | 27.51 | 19.23 | -0.03 | 176595.2 | 17.11 | skipped_fast |
| CHIPUSDT | IDLE | 3.05 | 6.71 | 3.52 | -0.03 | 349262.54 | 12.77 | skipped_fast |
| PYTHUSDT | IDLE | 1.94 | 4.9 | 1.79 | 0.05 | 562759.07 | 2.01 | skipped_fast |
| CCUSDT | IDLE | 2.45 | 4.33 | 3.77 | -0.0 | 385404.23 | 6.7 | skipped_fast |
| REDUSDT | IDLE | 3.21 | 6.02 | 2.71 | 0.01 | 59947.71 | 10.07 | skipped_fast |
| WUSDT | IDLE | 1.69 | 3.09 | 1.92 | 0.03 | 235268.46 | 13.68 | skipped_fast |
| RWAUSDT | WATCH_PULLBACK — tension haute + reflux | 3.13 | 8.32 | 7.4 | 0.04 | 64487.02 | 15.37 | skipped_fast |
| BIOUSDT | IDLE | 1.85 | 3.33 | 2.43 | -0.01 | 61860.57 | 3.84 | skipped_fast |
| ZBCNUSDT | IDLE | 1.24 | 2.38 | 0.66 | 0.04 | 182498.28 | 0.53 | skipped_fast |
| KITEUSDT | IDLE | 1.45 | 2.66 | 1.55 | -0.02 | 61450.58 | 11.02 | skipped_fast |
| RIZEUSDT | IDLE | 1.52 | 5.19 | 1.62 | -0.07 | 37920.43 | 71.37 | skipped_fast |
| RWAINCUSDT | IDLE | 1.4 | 2.62 | 1.16 | -0.02 | 4763.54 | 40.95 | skipped_fast |
| HBARUSDT | IDLE | 1.07 | 1.99 | 1.0 | 0.0 | 217462.3 | 1.34 | skipped_fast |
| TELUSDT | IDLE | 1.42 | 2.52 | 2.12 | -0.01 | 83276.64 | 17.56 | skipped_fast |
| QNTUSDT | IDLE | 0.73 | 1.41 | 0.39 | -0.0 | 47251.1 | 6.51 | skipped_fast |
| MNSRYUSDT | IDLE | 0.38 | 0.69 | 0.5 | 0.0 | 29151.32 | 29.83 | skipped_fast |
| FLUIDUSDT | IDLE | 0.0 | 0.0 | 0.0 | -0.01 | 1146.31 | 21.29 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
