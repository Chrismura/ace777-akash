# Hulk DIGEST — 2026-10-10T12:56:00Z

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
| WUSDT | IDLE | 3.74 | 7.31 | 1.6 | 0.01 | 1071697.02 | 5.13 | skipped_fast |
| XRPUSDT | IDLE | 0.36 | 0.65 | 0.47 | 0.01 | 18814054.2 | 0.71 | skipped_fast |
| BTCUSDT | IDLE | 0.2 | 0.37 | 0.15 | -0.0 | 212660892.18 | 0.0 | skipped_fast |
| ETHUSDT | IDLE | 0.13 | 0.25 | 0.08 | 0.0 | 84839130.39 | 0.04 | skipped_fast |
| PYTHUSDT | IDLE | 0.97 | 2.72 | 1.75 | -0.07 | 1258811.67 | 5.09 | skipped_fast |
| QNTUSDT | IDLE | 1.82 | 3.57 | 0.49 | 0.02 | 1182009.18 | 2.38 | skipped_fast |
| EDELUSDT | IDLE | 3.21 | 7.46 | 4.6 | 0.03 | 237500.44 | 2.59 | skipped_fast |
| KITEUSDT | IDLE | 2.74 | 6.5 | 0.29 | 0.05 | 75515.93 | 10.05 | skipped_fast |
| CCUSDT | IDLE | 1.1 | 1.96 | 1.6 | -0.03 | 404013.63 | 5.01 | skipped_fast |
| ZBCNUSDT | IDLE | 0.62 | 1.19 | 0.36 | -0.02 | 237316.31 | 0.87 | skipped_fast |
| CHIPUSDT | IDLE | 1.09 | 3.48 | 2.84 | 0.07 | 96422.81 | 13.39 | skipped_fast |
| REDUSDT | IDLE | 1.39 | 2.64 | 0.97 | 0.03 | 54901.96 | 14.64 | skipped_fast |
| BIOUSDT | IDLE | 1.09 | 2.0 | 1.17 | 0.03 | 76033.79 | 3.49 | skipped_fast |
| RWAINCUSDT | IDLE | 1.99 | 3.6 | 2.57 | -0.03 | 9430.91 | 103.02 | skipped_fast |
| HBARUSDT | IDLE | 0.78 | 1.47 | 0.61 | 0.01 | 342217.13 | 4.31 | skipped_fast |
| TELUSDT | IDLE | 1.83 | 3.23 | 2.86 | -0.01 | 105436.28 | 32.77 | skipped_fast |
| RIZEUSDT | IDLE | 0.47 | 1.56 | 0.81 | 0.04 | 50217.54 | 53.54 | skipped_fast |
| RWAUSDT | IDLE | 0.34 | 0.63 | 0.39 | -0.01 | 53585.24 | 15.72 | skipped_fast |
| FLUIDUSDT | IDLE | 0.5 | 1.46 | 0.89 | -0.0 | 10257.07 | 21.69 | skipped_fast |
| MNSRYUSDT | IDLE | 0.36 | 0.69 | 0.23 | 0.0 | 39606.12 | 20.3 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
