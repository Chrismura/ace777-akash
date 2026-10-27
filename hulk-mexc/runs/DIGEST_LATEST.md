# Hulk DIGEST — 2026-10-27T16:13:23Z

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
| XRPUSDT | IDLE | 1.11 | 2.14 | 0.58 | 0.02 | 20808987.95 | 0.76 | skipped_fast |
| ETHUSDT | IDLE | 0.95 | 1.83 | 0.43 | 0.01 | 163788696.21 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.55 | 1.07 | 0.26 | 0.0 | 313272739.06 | 0.0 | skipped_fast |
| WUSDT | IDLE | 3.65 | 8.51 | 2.33 | 0.06 | 686508.32 | 20.69 | skipped_fast |
| QNTUSDT | IDLE | 2.5 | 4.47 | 3.49 | -0.05 | 863983.21 | 4.03 | skipped_fast |
| KITEUSDT | IDLE | 3.26 | 6.38 | 2.01 | 0.04 | 57166.83 | 13.49 | skipped_fast |
| EDELUSDT | IDLE | 1.52 | 2.8 | 1.61 | 0.0 | 439881.49 | 3.08 | skipped_fast |
| REDUSDT | IDLE | 3.15 | 6.21 | 0.54 | 0.05 | 59651.54 | 14.28 | skipped_fast |
| PYTHUSDT | IDLE | 1.16 | 2.13 | 1.25 | -0.04 | 449971.34 | 5.52 | skipped_fast |
| CHIPUSDT | IDLE | 1.82 | 6.12 | 2.12 | 0.03 | 271661.92 | 16.77 | skipped_fast |
| CCUSDT | IDLE | 1.95 | 3.85 | 0.29 | -0.01 | 224018.76 | 6.01 | skipped_fast |
| ZBCNUSDT | IDLE | 0.67 | 1.87 | 1.09 | 0.01 | 256090.7 | 28.37 | skipped_fast |
| LAUSDT | IDLE | 2.69 | 5.36 | 0.17 | 0.02 | 59188.69 | 20.02 | skipped_fast |
| BIOUSDT | IDLE | 1.27 | 2.51 | 0.18 | 0.0 | 55798.4 | 8.92 | skipped_fast |
| RWAINCUSDT | IDLE | 0.64 | 2.26 | 0.94 | -0.11 | 62790.33 | 6.75 | skipped_fast |
| WAXLUSDT | IDLE | 1.9 | 3.63 | 1.09 | 0.0 | 53990.86 | 42.72 | skipped_fast |
| HBARUSDT | IDLE | 0.92 | 1.79 | 0.38 | -0.01 | 200542.69 | 10.48 | skipped_fast |
| RIZEUSDT | IDLE | 0.69 | 1.34 | 0.33 | -0.02 | 39804.9 | 67.89 | skipped_fast |
| RWAUSDT | IDLE | 1.44 | 2.87 | 0.08 | 0.0 | 57269.58 | 23.91 | skipped_fast |
| IOTAUSDT | IDLE | 1.07 | 2.01 | 0.82 | -0.01 | 88409.86 | 33.14 | skipped_fast |
| FLUIDUSDT | IDLE | 0.82 | 1.64 | 0.0 | 0.03 | 3237.2 | 21.35 | skipped_fast |
| MNSRYUSDT | IDLE | 0.41 | 0.77 | 0.31 | -0.0 | 37245.13 | 79.41 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
