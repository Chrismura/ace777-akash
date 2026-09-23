# Hulk DIGEST — 2026-09-23T07:17:22Z

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
| XRPUSDT | IDLE | 2.36 | 5.31 | 1.95 | 0.07 | 116795387.39 | 1.23 | skipped_fast |
| PYTHUSDT | IDLE | 0.75 | 3.67 | 0.69 | 0.06 | 1765925.21 | 1.49 | skipped_fast |
| ETHUSDT | IDLE | 0.86 | 1.51 | 1.36 | 0.01 | 411228568.12 | 0.04 | skipped_fast |
| HBARUSDT | IDLE | 1.38 | 2.82 | 1.95 | 0.06 | 1826432.34 | 1.01 | skipped_fast |
| BTCUSDT | IDLE | 0.66 | 1.18 | 0.97 | 0.01 | 878304115.2 | 0.0 | skipped_fast |
| ZBCNUSDT | IDLE | 2.86 | 7.05 | 2.61 | 0.05 | 223199.76 | 26.17 | skipped_fast |
| CCUSDT | IDLE | 1.51 | 2.77 | 1.67 | -0.04 | 408390.52 | 11.32 | skipped_fast |
| WUSDT | IDLE | 1.89 | 3.68 | 0.71 | 0.05 | 313326.48 | 10.49 | skipped_fast |
| KITEUSDT | IDLE | 2.01 | 5.56 | 5.15 | 0.07 | 142716.06 | 9.69 | skipped_fast |
| BIOUSDT | IDLE | 1.8 | 3.51 | 0.55 | 0.06 | 110979.6 | 9.85 | skipped_fast |
| CHIPUSDT | IDLE | 1.38 | 2.65 | 1.75 | -0.03 | 196691.43 | 12.89 | skipped_fast |
| EDELUSDT | IDLE | 0.65 | 3.1 | 1.68 | -0.04 | 264923.07 | 16.44 | skipped_fast |
| REDUSDT | IDLE | 1.71 | 3.41 | 0.0 | 0.02 | 59813.37 | 17.23 | skipped_fast |
| RIZEUSDT | IDLE | 0.66 | 14.04 | 0.0 | 0.5 | 61329.2 | 9.56 | skipped_fast |
| RWAINCUSDT | IDLE | 0.77 | 1.84 | 1.65 | 0.02 | 21524.39 | 21.68 | skipped_fast |
| QNTUSDT | IDLE | 0.77 | 2.57 | 0.99 | 0.11 | 243229.99 | 1.33 | skipped_fast |
| TELUSDT | IDLE | 0.74 | 3.08 | 1.7 | 0.15 | 110321.11 | 80.8 | skipped_fast |
| FLUIDUSDT | IDLE | 0.75 | 1.32 | 1.17 | 0.02 | 2932.72 | 21.63 | skipped_fast |
| RWAUSDT | IDLE | 0.44 | 0.8 | 0.5 | 0.01 | 53237.38 | 14.43 | skipped_fast |
| MNSRYUSDT | IDLE | 0.29 | 0.54 | 0.26 | 0.01 | 39635.16 | 11.52 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
