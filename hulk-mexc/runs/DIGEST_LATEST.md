# Hulk DIGEST — 2026-10-18T21:07:07Z

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
| ETHUSDT | IDLE | 1.14 | 2.12 | 1.05 | -0.03 | 119054051.08 | 0.04 | skipped_fast |
| PYTHUSDT | IDLE | 1.71 | 5.89 | 4.98 | -0.14 | 1472012.65 | 2.79 | skipped_fast |
| XRPUSDT | IDLE | 0.92 | 1.7 | 0.92 | -0.03 | 29325981.52 | 2.37 | skipped_fast |
| BTCUSDT | IDLE | 0.38 | 0.71 | 0.37 | -0.01 | 228846640.81 | 0.0 | skipped_fast |
| WUSDT | IDLE | 1.95 | 4.69 | 4.06 | -0.1 | 918155.37 | 14.26 | skipped_fast |
| HBARUSDT | IDLE | 2.74 | 6.26 | 4.43 | -0.03 | 772080.57 | 3.62 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 4.04 | 11.43 | 10.16 | -0.04 | 53587.13 | 32.26 | skipped_fast |
| QNTUSDT | IDLE | 2.16 | 4.8 | 3.35 | -0.08 | 625971.63 | 1.63 | skipped_fast |
| WAXLUSDT | WATCH_PULLBACK — tension haute + reflux | 3.47 | 15.7 | 8.66 | -0.02 | 78416.59 | 51.04 | skipped_fast |
| EDELUSDT | IDLE | 1.85 | 4.42 | 3.26 | -0.09 | 246301.18 | 19.34 | skipped_fast |
| CCUSDT | IDLE | 1.67 | 3.11 | 2.22 | -0.07 | 239347.97 | 9.24 | skipped_fast |
| ZBCNUSDT | IDLE | 1.73 | 3.3 | 1.06 | -0.06 | 205358.34 | 30.17 | skipped_fast |
| CHIPUSDT | IDLE | 1.64 | 4.68 | 3.96 | -0.11 | 78899.8 | 2.56 | skipped_fast |
| REDUSDT | IDLE | 1.72 | 3.08 | 2.4 | -0.06 | 98635.53 | 13.55 | skipped_fast |
| BIOUSDT | IDLE | 1.59 | 2.97 | 2.06 | -0.07 | 84932.88 | 8.78 | skipped_fast |
| KITEUSDT | IDLE | 1.43 | 2.56 | 1.94 | -0.05 | 64706.72 | 14.36 | skipped_fast |
| RIZEUSDT | IDLE | 0.94 | 4.66 | 3.82 | -0.04 | 58560.87 | 61.44 | skipped_fast |
| FLUIDUSDT | IDLE | 2.1 | 3.87 | 3.58 | -0.08 | 4608.75 | 21.8 | skipped_fast |
| IOTAUSDT | IDLE | 1.75 | 3.77 | 2.85 | -0.08 | 73415.64 | 23.24 | skipped_fast |
| LAUSDT | IDLE | 1.18 | 2.81 | 2.17 | -0.1 | 58461.22 | 21.63 | skipped_fast |
| RWAUSDT | IDLE | 0.41 | 0.72 | 0.64 | -0.01 | 48673.3 | 16.06 | skipped_fast |
| MNSRYUSDT | IDLE | 0.41 | 0.73 | 0.61 | -0.01 | 34889.33 | 62.67 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
