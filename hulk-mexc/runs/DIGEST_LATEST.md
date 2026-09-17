# Hulk DIGEST — 2026-09-17T23:18:05Z

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
| ETHUSDT | IDLE | 0.59 | 1.08 | 0.63 | 0.02 | 301846553.37 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.55 | 1.04 | 0.35 | 0.0 | 38767544.95 | 2.31 | skipped_fast |
| BTCUSDT | IDLE | 0.37 | 0.68 | 0.37 | 0.01 | 420130372.06 | 0.0 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.99 | 35.39 | 10.14 | -0.16 | 277726.34 | 54.84 | skipped_fast |
| PYTHUSDT | IDLE | 1.8 | 3.72 | 2.44 | 0.08 | 552496.42 | 1.78 | skipped_fast |
| CCUSDT | IDLE | 1.33 | 2.66 | 0.01 | 0.05 | 553113.9 | 6.89 | skipped_fast |
| WUSDT | IDLE | 1.52 | 4.13 | 1.38 | 0.11 | 335035.05 | 10.04 | skipped_fast |
| HBARUSDT | IDLE | 1.33 | 2.39 | 1.79 | 0.02 | 556654.91 | 1.34 | skipped_fast |
| CHIPUSDT | IDLE | 1.71 | 4.36 | 3.35 | 0.05 | 143520.02 | 13.35 | skipped_fast |
| ZBCNUSDT | IDLE | 0.9 | 1.69 | 0.75 | 0.02 | 199546.3 | 27.29 | skipped_fast |
| KITEUSDT | IDLE | 1.05 | 2.02 | 0.49 | -0.0 | 60310.42 | 10.37 | skipped_fast |
| BIOUSDT | IDLE | 0.84 | 1.57 | 0.79 | 0.01 | 67505.57 | 7.97 | skipped_fast |
| REDUSDT | IDLE | 0.81 | 1.59 | 0.2 | 0.02 | 66746.44 | 15.26 | skipped_fast |
| TELUSDT | IDLE | 2.34 | 4.18 | 3.4 | -0.02 | 75268.98 | 70.27 | skipped_fast |
| RWAINCUSDT | IDLE | 0.72 | 1.25 | 1.23 | 0.0 | 14461.96 | 23.84 | skipped_fast |
| RIZEUSDT | IDLE | 0.83 | 5.65 | 3.33 | -0.04 | 42778.72 | 125.91 | skipped_fast |
| QNTUSDT | IDLE | 0.79 | 1.4 | 1.15 | -0.01 | 40754.33 | 3.28 | skipped_fast |
| RWAUSDT | IDLE | 0.17 | 0.3 | 0.22 | 0.01 | 57004.5 | 22.38 | skipped_fast |
| MNSRYUSDT | IDLE | 0.03 | 0.06 | 0.04 | 0.02 | 43241.76 | 4.19 | skipped_fast |
| FLUIDUSDT | IDLE | 0.0 | 0.0 | 0.0 | 0.03 | 146.13 | 21.78 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
