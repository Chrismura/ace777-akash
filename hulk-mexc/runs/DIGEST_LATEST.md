# Hulk DIGEST — 2026-10-27T19:15:54Z

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
| ETHUSDT | IDLE | 0.94 | 1.8 | 0.58 | 0.01 | 224972637.49 | 0.34 | skipped_fast |
| XRPUSDT | IDLE | 0.88 | 1.7 | 0.34 | 0.02 | 19382419.06 | 1.51 | skipped_fast |
| BTCUSDT | IDLE | 0.59 | 1.15 | 0.18 | 0.01 | 315793268.05 | 0.0 | skipped_fast |
| WUSDT | IDLE | 2.26 | 5.0 | 3.34 | 0.04 | 677057.8 | 19.35 | skipped_fast |
| QNTUSDT | IDLE | 1.33 | 2.55 | 0.79 | -0.02 | 749574.51 | 4.0 | skipped_fast |
| EDELUSDT | IDLE | 1.26 | 2.23 | 1.94 | 0.01 | 477466.26 | 24.71 | skipped_fast |
| PYTHUSDT | IDLE | 1.41 | 2.75 | 0.44 | -0.02 | 399393.46 | 2.73 | skipped_fast |
| CHIPUSDT | IDLE | 2.5 | 5.97 | 1.13 | -0.01 | 141069.73 | 18.42 | skipped_fast |
| ZBCNUSDT | IDLE | 1.08 | 3.1 | 1.24 | 0.03 | 256796.25 | 21.16 | skipped_fast |
| BIOUSDT | IDLE | 1.87 | 3.69 | 0.31 | 0.02 | 58641.23 | 8.81 | skipped_fast |
| REDUSDT | IDLE | 1.86 | 3.72 | 0.69 | 0.06 | 59957.21 | 14.2 | skipped_fast |
| CCUSDT | IDLE | 1.03 | 1.9 | 1.08 | -0.01 | 224229.57 | 8.08 | skipped_fast |
| KITEUSDT | IDLE | 1.59 | 2.85 | 2.74 | 0.03 | 56985.36 | 9.35 | skipped_fast |
| LAUSDT | IDLE | 2.91 | 6.04 | 1.88 | 0.04 | 58701.92 | 16.54 | skipped_fast |
| RWAINCUSDT | IDLE | 1.65 | 4.65 | 0.26 | -0.08 | 63329.99 | 45.86 | skipped_fast |
| RIZEUSDT | IDLE | 1.7 | 3.34 | 0.46 | -0.0 | 46025.37 | 55.84 | skipped_fast |
| HBARUSDT | IDLE | 0.92 | 1.75 | 0.54 | -0.01 | 239377.41 | 9.18 | skipped_fast |
| IOTAUSDT | IDLE | 1.08 | 2.01 | 0.96 | -0.01 | 77236.84 | 26.09 | skipped_fast |
| WAXLUSDT | IDLE | 0.78 | 1.5 | 0.38 | 0.03 | 55268.14 | 38.65 | skipped_fast |
| RWAUSDT | IDLE | 0.7 | 1.37 | 0.24 | -0.0 | 57340.58 | 39.89 | skipped_fast |
| FLUIDUSDT | IDLE | 0.73 | 1.47 | 0.0 | 0.05 | 3238.71 | 21.25 | skipped_fast |
| MNSRYUSDT | IDLE | 0.43 | 0.78 | 0.59 | -0.0 | 37371.64 | 79.41 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
