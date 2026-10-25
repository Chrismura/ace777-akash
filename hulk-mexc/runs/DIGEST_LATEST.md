# Hulk DIGEST — 2026-10-25T11:02:17Z

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
| ETHUSDT | IDLE | 0.83 | 1.53 | 0.86 | -0.02 | 127815037.0 | 0.56 | skipped_fast |
| XRPUSDT | IDLE | 0.67 | 1.23 | 0.68 | 0.01 | 22703855.61 | 2.31 | skipped_fast |
| BTCUSDT | IDLE | 0.41 | 0.76 | 0.38 | -0.0 | 202239092.72 | 0.0 | skipped_fast |
| WUSDT | IDLE | 2.09 | 3.71 | 3.08 | -0.05 | 806459.89 | 15.98 | skipped_fast |
| EDELUSDT | IDLE | 1.49 | 3.92 | 3.48 | -0.09 | 536667.51 | 27.39 | skipped_fast |
| PYTHUSDT | IDLE | 1.42 | 2.72 | 0.86 | 0.01 | 491489.35 | 1.41 | skipped_fast |
| QNTUSDT | IDLE | 2.17 | 4.04 | 1.95 | 0.02 | 410364.51 | 1.65 | skipped_fast |
| REDUSDT | IDLE | 2.26 | 4.01 | 3.37 | -0.06 | 72006.13 | 17.38 | skipped_fast |
| BIOUSDT | IDLE | 1.59 | 2.91 | 1.81 | -0.04 | 66094.22 | 9.0 | skipped_fast |
| RWAINCUSDT | IDLE | 1.62 | 3.11 | 0.92 | -0.01 | 56498.97 | 5.45 | skipped_fast |
| CCUSDT | IDLE | 0.85 | 1.58 | 0.85 | -0.02 | 198031.79 | 3.0 | skipped_fast |
| ZBCNUSDT | IDLE | 0.78 | 1.73 | 1.25 | 0.01 | 224982.4 | 23.28 | skipped_fast |
| KITEUSDT | IDLE | 1.19 | 2.18 | 1.28 | -0.05 | 59018.1 | 11.7 | skipped_fast |
| CHIPUSDT | IDLE | 1.0 | 3.16 | 0.27 | 0.03 | 91731.63 | 17.95 | skipped_fast |
| LAUSDT | IDLE | 1.68 | 7.45 | 5.14 | -0.2 | 91776.39 | 24.51 | skipped_fast |
| HBARUSDT | IDLE | 1.0 | 1.79 | 1.36 | -0.0 | 201497.77 | 11.74 | skipped_fast |
| IOTAUSDT | IDLE | 1.55 | 2.75 | 2.29 | -0.03 | 65652.97 | 32.82 | skipped_fast |
| RIZEUSDT | IDLE | 0.46 | 1.14 | 0.76 | -0.04 | 41564.27 | 62.58 | skipped_fast |
| WAXLUSDT | IDLE | 1.62 | 2.98 | 1.77 | -0.05 | 54064.25 | 60.64 | skipped_fast |
| RWAUSDT | IDLE | 0.87 | 1.59 | 0.94 | -0.0 | 52084.81 | 23.78 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 2.12 | 0.0 | -0.03 | 7213.49 | 21.6 | skipped_fast |
| MNSRYUSDT | IDLE | 0.38 | 0.76 | 0.01 | -0.01 | 37568.61 | 77.07 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
