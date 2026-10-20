# Hulk DIGEST — 2026-10-20T06:10:02Z

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
| ETHUSDT | IDLE | 0.97 | 1.8 | 0.95 | -0.02 | 122528992.83 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.87 | 1.66 | 0.53 | -0.01 | 20170898.68 | 0.77 | skipped_fast |
| BTCUSDT | IDLE | 0.69 | 1.28 | 0.72 | -0.01 | 301703715.29 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.8 | 3.21 | 2.66 | -0.05 | 1082987.79 | 2.78 | skipped_fast |
| WUSDT | IDLE | 2.24 | 3.98 | 3.27 | -0.01 | 742319.85 | 13.98 | skipped_fast |
| EDELUSDT | IDLE | 3.9 | 15.22 | 2.46 | 0.09 | 239649.54 | 36.83 | skipped_fast |
| CCUSDT | IDLE | 2.47 | 4.35 | 3.88 | 0.01 | 470266.82 | 4.83 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.58 | 13.3 | 10.91 | -0.07 | 66923.25 | 39.79 | skipped_fast |
| QNTUSDT | IDLE | 2.24 | 3.97 | 3.43 | -0.03 | 723815.38 | 3.64 | skipped_fast |
| CHIPUSDT | IDLE | 3.3 | 7.85 | 1.42 | 0.03 | 90214.45 | 11.42 | skipped_fast |
| BIOUSDT | IDLE | 1.63 | 3.03 | 1.51 | -0.01 | 67975.43 | 4.26 | skipped_fast |
| KITEUSDT | IDLE | 1.61 | 3.41 | 1.81 | 0.07 | 78602.98 | 12.23 | skipped_fast |
| ZBCNUSDT | IDLE | 1.21 | 2.14 | 1.93 | -0.02 | 154728.86 | 18.79 | skipped_fast |
| HBARUSDT | IDLE | 1.4 | 2.62 | 1.22 | -0.01 | 369485.94 | 4.81 | skipped_fast |
| REDUSDT | IDLE | 1.52 | 2.93 | 0.71 | 0.0 | 58345.58 | 15.23 | skipped_fast |
| RWAINCUSDT | IDLE | 0.98 | 2.09 | 0.1 | 0.06 | 72179.09 | 10.25 | skipped_fast |
| IOTAUSDT | IDLE | 1.94 | 3.71 | 1.13 | 0.01 | 89278.77 | 21.91 | skipped_fast |
| FLUIDUSDT | IDLE | 2.26 | 4.4 | 0.8 | -0.01 | 4203.05 | 20.92 | skipped_fast |
| LAUSDT | IDLE | 1.79 | 3.32 | 1.73 | -0.02 | 55244.94 | 28.71 | skipped_fast |
| WAXLUSDT | IDLE | 1.57 | 3.59 | 2.19 | -0.05 | 56656.11 | 73.6 | skipped_fast |
| RWAUSDT | IDLE | 0.22 | 0.39 | 0.31 | 0.01 | 51958.4 | 23.54 | skipped_fast |
| MNSRYUSDT | IDLE | 0.14 | 0.27 | 0.1 | -0.0 | 40189.16 | 14.25 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
