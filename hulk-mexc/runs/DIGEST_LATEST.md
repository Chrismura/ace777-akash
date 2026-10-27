# Hulk DIGEST — 2026-10-27T14:11:41Z

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
| XRPUSDT | IDLE | 1.24 | 2.38 | 0.62 | 0.02 | 21411709.98 | 2.28 | skipped_fast |
| ETHUSDT | IDLE | 1.0 | 1.88 | 0.74 | 0.0 | 153781187.4 | 0.69 | skipped_fast |
| BTCUSDT | IDLE | 0.64 | 1.21 | 0.5 | 0.0 | 328561571.12 | 0.01 | skipped_fast |
| WUSDT | IDLE | 3.46 | 6.82 | 2.09 | 0.08 | 618370.08 | 22.56 | skipped_fast |
| QNTUSDT | IDLE | 2.86 | 5.67 | 4.85 | -0.07 | 890948.61 | 4.55 | skipped_fast |
| CHIPUSDT | IDLE | 2.44 | 8.15 | 3.2 | 0.06 | 286778.28 | 15.33 | skipped_fast |
| REDUSDT | IDLE | 3.6 | 6.97 | 1.56 | 0.04 | 61036.96 | 14.5 | skipped_fast |
| KITEUSDT | IDLE | 3.28 | 6.39 | 1.16 | 0.04 | 55885.06 | 4.24 | skipped_fast |
| PYTHUSDT | IDLE | 0.99 | 1.8 | 1.23 | -0.04 | 463399.55 | 2.76 | skipped_fast |
| EDELUSDT | IDLE | 1.29 | 2.41 | 1.07 | 0.01 | 394469.31 | 15.44 | skipped_fast |
| CCUSDT | IDLE | 1.69 | 3.38 | 0.06 | -0.01 | 226192.42 | 6.06 | skipped_fast |
| RWAINCUSDT | IDLE | 1.61 | 6.31 | 5.94 | -0.14 | 57308.19 | 13.58 | skipped_fast |
| ZBCNUSDT | IDLE | 1.18 | 3.23 | 2.23 | 0.02 | 249500.65 | 56.65 | skipped_fast |
| BIOUSDT | IDLE | 1.39 | 2.62 | 1.12 | -0.01 | 56014.25 | 9.06 | skipped_fast |
| WAXLUSDT | IDLE | 2.12 | 4.04 | 1.39 | 0.03 | 54512.52 | 53.08 | skipped_fast |
| LAUSDT | IDLE | 1.63 | 3.23 | 0.15 | 0.01 | 60699.18 | 23.87 | skipped_fast |
| HBARUSDT | IDLE | 0.82 | 1.5 | 0.94 | -0.02 | 191347.23 | 1.32 | skipped_fast |
| RIZEUSDT | IDLE | 0.58 | 1.1 | 0.39 | 0.0 | 41715.55 | 65.33 | skipped_fast |
| IOTAUSDT | IDLE | 1.04 | 2.0 | 0.59 | -0.01 | 95582.32 | 21.4 | skipped_fast |
| RWAUSDT | IDLE | 1.21 | 2.29 | 0.8 | -0.01 | 56954.58 | 40.31 | skipped_fast |
| FLUIDUSDT | IDLE | 1.24 | 2.23 | 1.65 | 0.03 | 3345.88 | 21.69 | skipped_fast |
| MNSRYUSDT | IDLE | 0.39 | 0.77 | 0.13 | 0.0 | 37069.38 | 79.41 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
