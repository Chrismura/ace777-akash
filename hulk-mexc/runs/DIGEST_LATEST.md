# Hulk DIGEST — 2026-09-01T22:27:22Z

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
| XRPUSDT | IDLE | 1.47 | 2.62 | 2.08 | -0.03 | 34781636.53 | 1.49 | skipped_fast |
| ETHUSDT | IDLE | 1.26 | 2.34 | 1.18 | -0.02 | 335478828.1 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.9 | 1.7 | 0.73 | -0.02 | 530286312.42 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.92 | 5.74 | 0.63 | 0.06 | 676578.01 | 1.93 | skipped_fast |
| CHIPUSDT | IDLE | 2.24 | 11.2 | 3.26 | 0.15 | 680026.37 | 2.25 | skipped_fast |
| WUSDT | IDLE | 2.21 | 4.18 | 3.67 | 0.05 | 407251.8 | 11.48 | skipped_fast |
| ZBCNUSDT | IDLE | 2.8 | 4.94 | 4.44 | -0.01 | 203191.81 | 34.01 | skipped_fast |
| REDUSDT | IDLE | 1.87 | 5.85 | 2.89 | 0.09 | 115768.23 | 9.58 | skipped_fast |
| CCUSDT | IDLE | 0.97 | 2.16 | 1.58 | -0.08 | 332985.71 | 7.04 | skipped_fast |
| RIZEUSDT | IDLE | 2.03 | 4.22 | 2.74 | -0.05 | 40575.66 | 57.25 | skipped_fast |
| EDELUSDT | IDLE | 0.8 | 6.02 | 5.07 | -0.08 | 138247.61 | 18.42 | skipped_fast |
| KITEUSDT | IDLE | 1.46 | 2.78 | 0.97 | 0.04 | 68308.66 | 12.23 | skipped_fast |
| BIOUSDT | IDLE | 1.28 | 2.29 | 1.82 | -0.04 | 70032.36 | 7.87 | skipped_fast |
| TELUSDT | IDLE | 2.65 | 4.83 | 3.15 | -0.04 | 94593.72 | 36.17 | skipped_fast |
| RWAINCUSDT | IDLE | 1.52 | 2.8 | 1.56 | -0.02 | 6196.92 | 5.88 | skipped_fast |
| FLUIDUSDT | IDLE | 2.56 | 4.47 | 4.28 | -0.03 | 229.45 | 18.13 | skipped_fast |
| HBARUSDT | IDLE | 0.9 | 1.66 | 0.91 | 0.0 | 249262.74 | 1.35 | skipped_fast |
| QNTUSDT | IDLE | 1.52 | 2.91 | 0.88 | 0.05 | 46794.75 | 4.7 | skipped_fast |
| MNSRYUSDT | IDLE | 0.9 | 1.64 | 1.13 | -0.02 | 34517.91 | 8.24 | skipped_fast |
| RWAUSDT | IDLE | 0.41 | 0.93 | 0.69 | -0.02 | 59241.13 | 7.71 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
