# Hulk DIGEST — 2026-09-14T12:42:27Z

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
| XRPUSDT | IDLE | 1.08 | 2.06 | 0.62 | 0.05 | 36563136.58 | 0.71 | skipped_fast |
| ETHUSDT | IDLE | 0.65 | 1.16 | 0.95 | 0.01 | 314600130.93 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.59 | 1.09 | 0.66 | 0.01 | 410586642.95 | 0.0 | skipped_fast |
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 3.61 | 6.36 | 5.78 | 0.01 | 517918.01 | 5.45 | skipped_fast |
| WUSDT | IDLE | 1.86 | 3.26 | 3.02 | 0.0 | 230512.39 | 12.1 | skipped_fast |
| EDELUSDT | IDLE | 1.44 | 6.96 | 0.96 | 0.18 | 239351.88 | 27.64 | skipped_fast |
| REDUSDT | IDLE | 1.79 | 4.33 | 0.89 | 0.06 | 163267.35 | 16.64 | skipped_fast |
| CHIPUSDT | IDLE | 1.75 | 5.38 | 0.93 | -0.07 | 105174.12 | 16.48 | skipped_fast |
| CCUSDT | IDLE | 0.94 | 1.85 | 0.24 | 0.01 | 233319.61 | 11.42 | skipped_fast |
| ZBCNUSDT | IDLE | 1.02 | 1.9 | 0.94 | 0.0 | 210045.69 | 19.21 | skipped_fast |
| RWAINCUSDT | IDLE | 1.49 | 2.83 | 0.97 | 0.04 | 8658.99 | 5.46 | skipped_fast |
| BIOUSDT | IDLE | 1.06 | 1.89 | 1.55 | 0.01 | 75985.28 | 7.84 | skipped_fast |
| KITEUSDT | IDLE | 1.14 | 2.13 | 1.04 | -0.02 | 61243.79 | 10.33 | skipped_fast |
| RIZEUSDT | IDLE | 0.84 | 9.88 | 3.63 | 0.19 | 68583.86 | 91.79 | skipped_fast |
| HBARUSDT | IDLE | 0.97 | 1.87 | 0.44 | 0.03 | 288725.03 | 1.3 | skipped_fast |
| TELUSDT | IDLE | 1.81 | 3.38 | 1.66 | 0.0 | 89836.05 | 37.62 | skipped_fast |
| FLUIDUSDT | IDLE | 1.1 | 2.06 | 0.93 | 0.02 | 815.22 | 21.76 | skipped_fast |
| QNTUSDT | IDLE | 0.69 | 1.31 | 0.44 | 0.0 | 38668.57 | 7.8 | skipped_fast |
| RWAUSDT | IDLE | 0.17 | 0.3 | 0.22 | 0.01 | 53657.92 | 14.81 | skipped_fast |
| MNSRYUSDT | IDLE | 0.25 | 0.46 | 0.32 | -0.01 | 29235.4 | 33.52 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
