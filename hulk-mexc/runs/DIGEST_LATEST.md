# Hulk DIGEST — 2026-09-25T23:27:51Z

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
| XRPUSDT | IDLE | 1.03 | 1.94 | 0.75 | 0.02 | 115440179.6 | 2.55 | skipped_fast |
| ETHUSDT | IDLE | 0.42 | 0.81 | 0.24 | 0.0 | 323450426.05 | 0.07 | skipped_fast |
| BTCUSDT | IDLE | 0.33 | 0.65 | 0.13 | -0.0 | 688304671.54 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.09 | 5.67 | 1.46 | 0.1 | 1244757.08 | 2.7 | skipped_fast |
| CCUSDT | IDLE | 1.22 | 4.89 | 1.85 | 0.15 | 854719.82 | 6.91 | skipped_fast |
| HBARUSDT | IDLE | 1.57 | 3.05 | 0.57 | 0.02 | 928383.72 | 1.05 | skipped_fast |
| WUSDT | IDLE | 1.97 | 3.88 | 0.44 | 0.05 | 427365.7 | 10.5 | skipped_fast |
| EDELUSDT | IDLE | 2.66 | 4.72 | 3.95 | 0.0 | 181634.09 | 23.77 | skipped_fast |
| ZBCNUSDT | IDLE | 1.98 | 4.36 | 4.14 | 0.05 | 248141.56 | 14.94 | skipped_fast |
| RIZEUSDT | IDLE | 1.25 | 18.48 | 13.56 | 0.02 | 107698.99 | 34.14 | skipped_fast |
| CHIPUSDT | IDLE | 2.08 | 5.74 | 0.34 | 0.06 | 161469.81 | 11.9 | skipped_fast |
| QNTUSDT | IDLE | 0.71 | 3.19 | 0.21 | 0.1 | 568299.85 | 5.03 | skipped_fast |
| BIOUSDT | IDLE | 1.12 | 3.35 | 1.05 | 0.07 | 114404.75 | 3.03 | skipped_fast |
| REDUSDT | IDLE | 0.79 | 1.87 | 1.26 | 0.08 | 137030.23 | 12.1 | skipped_fast |
| KITEUSDT | IDLE | 0.93 | 1.85 | 0.07 | 0.02 | 79928.48 | 11.24 | skipped_fast |
| RWAINCUSDT | IDLE | 0.68 | 2.15 | 0.75 | -0.08 | 13630.7 | 15.09 | skipped_fast |
| TELUSDT | IDLE | 1.21 | 2.15 | 1.74 | -0.01 | 115864.75 | 48.9 | skipped_fast |
| MNSRYUSDT | IDLE | 0.69 | 1.25 | 0.82 | 0.02 | 41313.43 | 6.36 | skipped_fast |
| RWAUSDT | IDLE | 0.52 | 0.96 | 0.59 | -0.01 | 54416.04 | 22.15 | skipped_fast |
| FLUIDUSDT | IDLE | 0.38 | 0.68 | 0.52 | 0.03 | 3326.58 | 22.1 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
