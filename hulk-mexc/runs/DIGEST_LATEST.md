# Hulk DIGEST — 2026-10-29T10:20:41Z

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
| XRPUSDT | IDLE | 0.75 | 1.31 | 1.24 | -0.03 | 23960284.69 | 1.55 | skipped_fast |
| ETHUSDT | IDLE | 0.69 | 1.27 | 0.73 | -0.02 | 234501805.54 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.47 | 0.86 | 0.51 | -0.02 | 342618997.37 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.67 | 2.97 | 2.45 | -0.04 | 446588.27 | 1.43 | skipped_fast |
| WUSDT | IDLE | 1.87 | 3.52 | 1.44 | -0.03 | 492958.61 | 57.1 | skipped_fast |
| CCUSDT | IDLE | 0.73 | 1.41 | 0.39 | -0.06 | 408795.97 | 13.44 | skipped_fast |
| EDELUSDT | IDLE | 1.38 | 2.45 | 2.04 | -0.04 | 195836.08 | 6.41 | skipped_fast |
| LAUSDT | IDLE | 3.2 | 5.7 | 4.66 | -0.04 | 57811.9 | 21.15 | skipped_fast |
| QNTUSDT | IDLE | 1.45 | 2.61 | 1.92 | -0.05 | 425713.39 | 1.04 | skipped_fast |
| HBARUSDT | IDLE | 0.84 | 1.54 | 0.95 | -0.04 | 567040.58 | 5.42 | skipped_fast |
| CHIPUSDT | IDLE | 0.69 | 3.55 | 1.94 | -0.12 | 242811.58 | 18.95 | skipped_fast |
| REDUSDT | IDLE | 1.59 | 2.85 | 2.17 | -0.04 | 64175.73 | 16.35 | skipped_fast |
| BIOUSDT | IDLE | 1.53 | 2.85 | 1.34 | -0.03 | 68115.89 | 9.06 | skipped_fast |
| ZBCNUSDT | IDLE | 0.77 | 1.43 | 0.79 | -0.01 | 253727.49 | 26.78 | skipped_fast |
| RWAINCUSDT | IDLE | 1.17 | 4.82 | 2.72 | -0.09 | 31563.35 | 7.16 | skipped_fast |
| KITEUSDT | IDLE | 0.84 | 1.51 | 1.1 | -0.04 | 59953.02 | 11.61 | skipped_fast |
| FLUIDUSDT | IDLE | 2.33 | 4.39 | 3.46 | -0.06 | 6151.7 | 21.25 | skipped_fast |
| RIZEUSDT | IDLE | 0.96 | 1.83 | 0.54 | -0.03 | 39412.6 | 49.3 | skipped_fast |
| WAXLUSDT | IDLE | 1.73 | 4.01 | 2.56 | -0.07 | 54068.32 | 54.64 | skipped_fast |
| IOTAUSDT | IDLE | 1.14 | 2.11 | 1.53 | -0.06 | 98904.24 | 15.01 | skipped_fast |
| RWAUSDT | IDLE | 1.15 | 2.01 | 1.9 | -0.01 | 56467.04 | 32.08 | skipped_fast |
| MNSRYUSDT | IDLE | 0.27 | 0.53 | 0.1 | -0.01 | 37381.74 | 16.2 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
