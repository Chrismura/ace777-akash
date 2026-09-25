# Hulk DIGEST — 2026-09-25T22:48:35Z

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
| XRPUSDT | IDLE | 1.01 | 1.94 | 0.53 | 0.02 | 115827903.84 | 1.91 | skipped_fast |
| ETHUSDT | IDLE | 0.42 | 0.81 | 0.23 | 0.0 | 324605877.29 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.33 | 0.65 | 0.13 | -0.0 | 684699329.35 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.02 | 5.87 | 0.32 | 0.11 | 1237871.51 | 2.67 | skipped_fast |
| CCUSDT | IDLE | 1.61 | 6.68 | 2.28 | 0.15 | 848026.53 | 9.25 | skipped_fast |
| HBARUSDT | IDLE | 1.78 | 3.46 | 0.62 | 0.03 | 902370.01 | 1.05 | skipped_fast |
| EDELUSDT | IDLE | 2.61 | 4.68 | 3.66 | 0.0 | 180513.19 | 6.78 | skipped_fast |
| WUSDT | IDLE | 1.72 | 3.35 | 0.64 | 0.05 | 409966.26 | 8.14 | skipped_fast |
| RIZEUSDT | IDLE | 1.28 | 18.86 | 14.04 | -0.01 | 111036.31 | 34.17 | skipped_fast |
| ZBCNUSDT | IDLE | 1.87 | 4.18 | 3.42 | 0.06 | 253159.8 | 43.0 | skipped_fast |
| CHIPUSDT | IDLE | 2.0 | 5.09 | 0.54 | 0.04 | 160607.55 | 16.08 | skipped_fast |
| KITEUSDT | IDLE | 1.8 | 3.49 | 0.69 | 0.02 | 80308.24 | 9.79 | skipped_fast |
| QNTUSDT | IDLE | 0.58 | 2.42 | 1.26 | 0.1 | 557410.4 | 5.11 | skipped_fast |
| BIOUSDT | IDLE | 1.11 | 3.35 | 0.72 | 0.08 | 113335.55 | 3.02 | skipped_fast |
| REDUSDT | IDLE | 0.78 | 1.87 | 1.13 | 0.09 | 137381.76 | 14.38 | skipped_fast |
| RWAINCUSDT | IDLE | 0.83 | 2.63 | 0.75 | -0.09 | 14313.6 | 20.11 | skipped_fast |
| TELUSDT | IDLE | 1.2 | 2.15 | 1.62 | 0.0 | 116233.56 | 54.86 | skipped_fast |
| MNSRYUSDT | IDLE | 0.69 | 1.26 | 0.85 | 0.02 | 41073.05 | 5.09 | skipped_fast |
| FLUIDUSDT | IDLE | 0.58 | 1.08 | 0.52 | 0.02 | 3356.58 | 22.13 | skipped_fast |
| RWAUSDT | IDLE | 0.59 | 1.04 | 0.88 | -0.01 | 54395.63 | 51.64 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
