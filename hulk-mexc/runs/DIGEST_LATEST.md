# Hulk DIGEST — 2026-10-18T06:08:04Z

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
| XRPUSDT | IDLE | 0.59 | 1.06 | 0.74 | -0.01 | 18529358.58 | 1.54 | skipped_fast |
| ETHUSDT | IDLE | 0.57 | 1.03 | 0.73 | -0.01 | 91094640.79 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.35 | 0.65 | 0.4 | 0.0 | 185750753.65 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.21 | 3.01 | 2.62 | -0.08 | 1281577.54 | 1.3 | skipped_fast |
| WUSDT | IDLE | 1.25 | 4.03 | 2.77 | -0.07 | 1266630.79 | 17.04 | skipped_fast |
| QNTUSDT | IDLE | 1.88 | 3.47 | 1.93 | -0.05 | 587015.0 | 2.56 | skipped_fast |
| CCUSDT | IDLE | 1.6 | 2.9 | 2.0 | -0.02 | 250307.39 | 6.87 | skipped_fast |
| EDELUSDT | IDLE | 1.42 | 4.47 | 1.94 | -0.09 | 182352.06 | 7.45 | skipped_fast |
| REDUSDT | IDLE | 1.86 | 3.33 | 2.6 | -0.04 | 61364.92 | 16.12 | skipped_fast |
| ZBCNUSDT | IDLE | 1.3 | 2.33 | 1.83 | -0.04 | 176324.63 | 11.5 | skipped_fast |
| BIOUSDT | IDLE | 1.48 | 2.64 | 2.17 | -0.04 | 70627.24 | 4.18 | skipped_fast |
| CHIPUSDT | IDLE | 1.17 | 3.15 | 1.62 | -0.07 | 75089.68 | 11.59 | skipped_fast |
| KITEUSDT | IDLE | 0.99 | 2.32 | 1.94 | -0.08 | 70365.9 | 12.22 | skipped_fast |
| HBARUSDT | IDLE | 1.23 | 2.3 | 1.02 | 0.02 | 274302.91 | 9.31 | skipped_fast |
| RIZEUSDT | IDLE | 1.25 | 2.2 | 2.03 | -0.0 | 45559.35 | 57.61 | skipped_fast |
| LAUSDT | IDLE | 1.95 | 3.46 | 2.92 | -0.06 | 54984.01 | 25.8 | skipped_fast |
| IOTAUSDT | IDLE | 1.79 | 3.22 | 2.37 | -0.04 | 64435.6 | 21.91 | skipped_fast |
| RWAINCUSDT | IDLE | 0.35 | 1.06 | 0.42 | 0.04 | 17835.85 | 5.26 | skipped_fast |
| WAXLUSDT | IDLE | 0.8 | 2.88 | 1.15 | -0.0 | 65255.68 | 29.94 | skipped_fast |
| RWAUSDT | IDLE | 0.41 | 0.8 | 0.16 | 0.0 | 50721.52 | 15.94 | skipped_fast |
| MNSRYUSDT | IDLE | 0.6 | 1.09 | 0.78 | -0.01 | 29098.02 | 37.05 | skipped_fast |
| FLUIDUSDT | IDLE | 0.46 | 0.85 | 0.52 | -0.02 | 1708.17 | 21.55 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
