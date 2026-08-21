# Hulk DIGEST — 2026-08-21T22:39:28Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : XRPUSDT, HBARUSDT, QAITUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT
- Watch only : QNTUSDT, FLUIDUSDT, RWAUSDT

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| PYTHUSDT | IDLE | 1.36 | 5.17 | 0.35 | 0.11 | 5834952.77 | 2.05 | skipped_fast |
| XRPUSDT | IDLE | 1.58 | 5.94 | 0.1 | 0.14 | 134898042.61 | 2.77 | skipped_fast |
| CCUSDT | IDLE | 1.81 | 6.86 | 0.0 | 0.14 | 660423.0 | 8.85 | skipped_fast |
| HBARUSDT | IDLE | 2.21 | 4.71 | 0.68 | 0.08 | 873065.0 | 1.27 | skipped_fast |
| WUSDT | IDLE | 2.47 | 5.48 | 0.02 | 0.09 | 371778.64 | 11.26 | skipped_fast |
| ZBCNUSDT | IDLE | 1.57 | 6.77 | 0.08 | 0.11 | 504740.4 | 0.98 | skipped_fast |
| CHIPUSDT | IDLE | 1.5 | 4.54 | 1.6 | 0.05 | 533671.89 | 3.06 | skipped_fast |
| BIOUSDT | IDLE | 2.29 | 5.04 | 1.02 | 0.03 | 188311.77 | 3.11 | skipped_fast |
| REDUSDT | IDLE | 1.33 | 11.01 | 8.29 | 0.18 | 156048.83 | 12.15 | skipped_fast |
| EDELUSDT | IDLE | 2.3 | 5.04 | 0.22 | -0.03 | 82630.38 | 21.83 | skipped_fast |
| RWAINCUSDT | IDLE | 2.18 | 4.07 | 1.96 | 0.02 | 10279.27 | 16.16 | skipped_fast |
| TELUSDT | IDLE | 2.53 | 6.45 | 0.87 | 0.05 | 186944.01 | 15.54 | skipped_fast |
| QAITUSDT | IDLE | 2.37 | 4.38 | 2.37 | -0.02 | 3825.97 | 63.67 | skipped_fast |
| KITEUSDT | IDLE | 1.21 | 3.58 | 0.95 | 0.11 | 61515.15 | 12.89 | skipped_fast |
| QNTUSDT | IDLE | 2.09 | 4.18 | 0.0 | 0.06 | 78855.0 | 1.52 | skipped_fast |
| RIZEUSDT | IDLE | 0.95 | 4.7 | 1.79 | 0.06 | 56365.99 | 45.14 | skipped_fast |
| RWAUSDT | IDLE | 0.88 | 1.75 | 0.08 | 0.04 | 54146.88 | 16.41 | skipped_fast |
| FLUIDUSDT | IDLE | 0.51 | 1.15 | 0.08 | 0.09 | 4171.26 | 11.93 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
