# Hulk DIGEST — 2026-10-26T19:49:15Z

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
| ETHUSDT | IDLE | 1.09 | 2.02 | 1.07 | -0.01 | 144088089.6 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.98 | 1.83 | 0.9 | -0.0 | 24454950.28 | 2.32 | skipped_fast |
| BTCUSDT | IDLE | 0.84 | 1.53 | 0.97 | -0.01 | 355069689.44 | 0.0 | skipped_fast |
| QNTUSDT | IDLE | 1.9 | 7.97 | 6.54 | 0.05 | 1427668.11 | 4.91 | skipped_fast |
| PYTHUSDT | IDLE | 2.36 | 4.2 | 3.5 | -0.01 | 868996.48 | 5.39 | skipped_fast |
| WUSDT | IDLE | 3.08 | 6.36 | 1.27 | 0.03 | 653842.19 | 44.12 | skipped_fast |
| CHIPUSDT | IDLE | 2.31 | 18.66 | 5.44 | 0.19 | 313516.1 | 14.85 | skipped_fast |
| RWAINCUSDT | IDLE | 3.12 | 13.37 | 3.74 | -0.07 | 57523.16 | 5.98 | skipped_fast |
| EDELUSDT | IDLE | 2.48 | 4.44 | 3.52 | 0.02 | 92816.54 | 34.32 | skipped_fast |
| CCUSDT | IDLE | 1.27 | 2.25 | 1.96 | -0.03 | 204309.21 | 6.02 | skipped_fast |
| ZBCNUSDT | IDLE | 1.4 | 2.79 | 2.03 | -0.06 | 205447.76 | 28.91 | skipped_fast |
| BIOUSDT | IDLE | 1.77 | 3.18 | 2.43 | -0.01 | 59453.12 | 9.04 | skipped_fast |
| RIZEUSDT | IDLE | 2.32 | 4.4 | 1.6 | -0.0 | 45588.52 | 62.58 | skipped_fast |
| REDUSDT | IDLE | 1.62 | 2.9 | 2.28 | 0.0 | 62957.1 | 16.46 | skipped_fast |
| KITEUSDT | IDLE | 1.17 | 2.22 | 0.8 | 0.02 | 54037.68 | 9.64 | skipped_fast |
| WAXLUSDT | IDLE | 2.26 | 4.01 | 3.45 | -0.03 | 53384.36 | 35.72 | skipped_fast |
| HBARUSDT | IDLE | 1.14 | 2.07 | 1.43 | -0.01 | 256577.28 | 13.0 | skipped_fast |
| LAUSDT | IDLE | 1.74 | 3.41 | 2.49 | 0.01 | 64218.35 | 20.71 | skipped_fast |
| IOTAUSDT | IDLE | 1.58 | 2.83 | 2.22 | -0.02 | 84315.98 | 35.47 | skipped_fast |
| FLUIDUSDT | IDLE | 1.18 | 2.35 | 0.08 | -0.05 | 722.74 | 21.44 | skipped_fast |
| RWAUSDT | IDLE | 0.69 | 1.28 | 0.71 | -0.0 | 54291.33 | 15.92 | skipped_fast |
| MNSRYUSDT | IDLE | 0.39 | 0.74 | 0.23 | -0.01 | 41999.96 | 76.46 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
