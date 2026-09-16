# Hulk DIGEST — 2026-09-16T20:14:11Z

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
| XRPUSDT | IDLE | 2.79 | 5.48 | 0.7 | 0.02 | 63194873.28 | 0.76 | skipped_fast |
| ETHUSDT | IDLE | 1.33 | 2.56 | 0.65 | 0.0 | 378686729.37 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 1.01 | 1.96 | 0.44 | 0.0 | 514545580.59 | 0.0 | skipped_fast |
| CCUSDT | IDLE | 4.03 | 7.82 | 1.63 | 0.03 | 473664.39 | 8.48 | skipped_fast |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 4.27 | 14.7 | 8.72 | -0.01 | 65829.27 | 14.7 | skipped_fast |
| PYTHUSDT | IDLE | 2.15 | 4.01 | 1.92 | -0.01 | 431254.68 | 1.92 | skipped_fast |
| CHIPUSDT | IDLE | 2.49 | 5.22 | 3.59 | -0.05 | 87515.3 | 19.59 | skipped_fast |
| ZBCNUSDT | IDLE | 2.02 | 3.8 | 1.64 | 0.01 | 193715.36 | 27.21 | skipped_fast |
| WUSDT | IDLE | 1.83 | 3.55 | 0.79 | -0.03 | 199026.73 | 9.0 | skipped_fast |
| BIOUSDT | IDLE | 2.09 | 4.13 | 0.36 | 0.0 | 77832.97 | 8.05 | skipped_fast |
| EDELUSDT | IDLE | 0.54 | 4.71 | 1.12 | 0.07 | 336704.17 | 26.34 | skipped_fast |
| REDUSDT | IDLE | 1.8 | 3.64 | 1.66 | -0.05 | 66803.77 | 18.04 | skipped_fast |
| RIZEUSDT | IDLE | 0.87 | 13.44 | 4.63 | 0.31 | 59427.96 | 17.95 | skipped_fast |
| HBARUSDT | IDLE | 1.47 | 2.9 | 0.31 | -0.02 | 268066.07 | 2.72 | skipped_fast |
| TELUSDT | IDLE | 2.09 | 4.87 | 0.82 | -0.05 | 113404.04 | 20.64 | skipped_fast |
| RWAINCUSDT | IDLE | 1.2 | 2.1 | 2.0 | -0.04 | 12145.3 | 24.07 | skipped_fast |
| RWAUSDT | IDLE | 2.0 | 3.87 | 0.89 | -0.0 | 53482.93 | 22.58 | skipped_fast |
| QNTUSDT | IDLE | 1.34 | 2.67 | 0.13 | -0.02 | 37930.82 | 3.31 | skipped_fast |
| FLUIDUSDT | IDLE | 0.95 | 1.9 | 0.0 | -0.02 | 1583.22 | 22.26 | skipped_fast |
| MNSRYUSDT | IDLE | 0.43 | 0.77 | 0.56 | -0.01 | 31037.7 | 24.14 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
