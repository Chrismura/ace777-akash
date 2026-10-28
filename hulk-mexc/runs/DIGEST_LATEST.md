# Hulk DIGEST — 2026-10-28T09:32:12Z

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
| ETHUSDT | IDLE | 0.84 | 1.57 | 0.74 | 0.03 | 249720534.24 | 0.21 | skipped_fast |
| XRPUSDT | IDLE | 0.67 | 1.24 | 0.66 | 0.02 | 20574970.94 | 0.75 | skipped_fast |
| BTCUSDT | IDLE | 0.6 | 1.15 | 0.37 | 0.02 | 305509311.47 | 0.0 | skipped_fast |
| WUSDT | IDLE | 0.7 | 1.36 | 1.04 | 0.03 | 619311.7 | 21.11 | skipped_fast |
| CCUSDT | IDLE | 1.95 | 3.9 | 0.02 | 0.05 | 274099.78 | 6.84 | skipped_fast |
| PYTHUSDT | IDLE | 1.22 | 2.23 | 1.43 | -0.0 | 388064.88 | 1.38 | skipped_fast |
| EDELUSDT | IDLE | 1.48 | 2.63 | 2.23 | 0.01 | 327524.52 | 33.85 | skipped_fast |
| RWAINCUSDT | IDLE | 2.29 | 4.59 | 0.0 | 0.01 | 57106.67 | 6.53 | skipped_fast |
| QNTUSDT | IDLE | 1.4 | 2.75 | 0.3 | -0.02 | 543229.4 | 2.48 | skipped_fast |
| RIZEUSDT | IDLE | 2.46 | 4.52 | 2.68 | 0.03 | 36300.32 | 61.57 | skipped_fast |
| ZBCNUSDT | IDLE | 1.29 | 2.51 | 1.12 | -0.05 | 214292.06 | 45.31 | skipped_fast |
| CHIPUSDT | IDLE | 1.03 | 2.59 | 1.53 | 0.07 | 123121.8 | 20.3 | skipped_fast |
| KITEUSDT | IDLE | 0.89 | 1.56 | 1.49 | 0.03 | 60472.27 | 11.17 | skipped_fast |
| REDUSDT | IDLE | 0.9 | 1.81 | 1.38 | 0.04 | 55077.27 | 15.71 | skipped_fast |
| HBARUSDT | IDLE | 0.71 | 1.32 | 0.7 | 0.0 | 388843.02 | 10.47 | skipped_fast |
| BIOUSDT | IDLE | 0.7 | 1.37 | 0.26 | 0.04 | 83264.82 | 8.75 | skipped_fast |
| IOTAUSDT | IDLE | 0.76 | 1.43 | 0.66 | 0.01 | 70840.09 | 25.99 | skipped_fast |
| LAUSDT | IDLE | 0.69 | 1.38 | 0.37 | 0.04 | 59630.71 | 26.96 | skipped_fast |
| WAXLUSDT | IDLE | 0.83 | 1.63 | 0.24 | 0.01 | 55963.98 | 44.93 | skipped_fast |
| RWAUSDT | IDLE | 0.48 | 0.88 | 0.56 | 0.01 | 55940.43 | 16.03 | skipped_fast |
| MNSRYUSDT | IDLE | 0.69 | 1.37 | 0.03 | 0.01 | 35770.07 | 54.03 | skipped_fast |
| FLUIDUSDT | IDLE | 0.46 | 1.42 | 0.46 | 0.01 | 6681.88 | 21.15 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
