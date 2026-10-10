# Hulk DIGEST — 2026-10-10T07:51:14Z

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
| WUSDT | IDLE | 1.83 | 4.55 | 4.1 | -0.03 | 1826745.08 | 13.06 | skipped_fast |
| PYTHUSDT | IDLE | 1.86 | 4.6 | 3.79 | -0.07 | 1411691.22 | 6.32 | skipped_fast |
| XRPUSDT | IDLE | 0.49 | 0.89 | 0.57 | 0.0 | 24103579.49 | 2.14 | skipped_fast |
| BTCUSDT | IDLE | 0.2 | 0.39 | 0.12 | 0.0 | 246871194.63 | 0.0 | skipped_fast |
| ETHUSDT | IDLE | 0.2 | 0.37 | 0.2 | -0.0 | 131521343.37 | 0.04 | skipped_fast |
| QNTUSDT | IDLE | 1.2 | 2.21 | 1.33 | 0.02 | 1158474.38 | 2.03 | skipped_fast |
| CCUSDT | IDLE | 0.94 | 1.9 | 1.69 | 0.03 | 575656.1 | 10.77 | skipped_fast |
| ZBCNUSDT | IDLE | 0.98 | 2.62 | 0.7 | -0.07 | 263866.46 | 23.24 | skipped_fast |
| REDUSDT | IDLE | 1.46 | 2.56 | 2.46 | 0.01 | 57542.42 | 8.79 | skipped_fast |
| CHIPUSDT | IDLE | 1.21 | 4.04 | 2.05 | 0.07 | 99137.61 | 15.11 | skipped_fast |
| EDELUSDT | IDLE | 0.64 | 2.32 | 1.77 | 0.12 | 207882.82 | 12.52 | skipped_fast |
| BIOUSDT | IDLE | 1.16 | 2.02 | 1.98 | 0.01 | 72415.54 | 3.48 | skipped_fast |
| RIZEUSDT | IDLE | 1.06 | 5.68 | 5.05 | 0.05 | 64890.19 | 39.85 | skipped_fast |
| KITEUSDT | IDLE | 1.12 | 2.21 | 0.2 | -0.02 | 76386.58 | 13.0 | skipped_fast |
| HBARUSDT | IDLE | 1.02 | 1.9 | 0.95 | 0.01 | 296715.74 | 3.24 | skipped_fast |
| RWAINCUSDT | IDLE | 1.28 | 2.29 | 1.81 | 0.01 | 9358.51 | 87.0 | skipped_fast |
| RWAUSDT | IDLE | 1.66 | 2.92 | 2.61 | -0.01 | 52782.3 | 23.61 | skipped_fast |
| TELUSDT | IDLE | 1.43 | 2.67 | 1.33 | -0.01 | 114770.27 | 26.89 | skipped_fast |
| MNSRYUSDT | IDLE | 0.75 | 1.42 | 0.54 | 0.01 | 41524.03 | 29.73 | skipped_fast |
| FLUIDUSDT | IDLE | 0.3 | 1.99 | 0.0 | 0.01 | 17205.48 | 20.79 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
