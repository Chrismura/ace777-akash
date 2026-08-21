# Hulk DIGEST — 2026-08-21T21:17:31Z

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
| PYTHUSDT | IDLE | 1.19 | 4.51 | 1.11 | 0.09 | 5613048.95 | 2.08 | skipped_fast |
| XRPUSDT | IDLE | 1.15 | 3.73 | 2.04 | 0.1 | 128585574.0 | 1.44 | skipped_fast |
| CHIPUSDT | IDLE | 1.91 | 5.61 | 4.32 | 0.06 | 515513.27 | 6.24 | skipped_fast |
| ZBCNUSDT | IDLE | 1.99 | 8.19 | 4.81 | 0.09 | 483211.3 | 23.38 | skipped_fast |
| CCUSDT | IDLE | 1.15 | 3.14 | 0.47 | 0.1 | 643810.51 | 5.53 | skipped_fast |
| HBARUSDT | IDLE | 1.58 | 3.04 | 0.86 | 0.06 | 810720.17 | 1.29 | skipped_fast |
| WUSDT | IDLE | 1.97 | 3.83 | 0.67 | 0.06 | 366924.62 | 17.82 | skipped_fast |
| BIOUSDT | IDLE | 2.46 | 5.2 | 2.49 | 0.01 | 187211.78 | 9.44 | skipped_fast |
| REDUSDT | IDLE | 1.34 | 11.01 | 9.17 | 0.16 | 153551.65 | 23.77 | skipped_fast |
| EDELUSDT | IDLE | 2.07 | 4.12 | 2.97 | -0.06 | 82446.49 | 11.34 | skipped_fast |
| RWAINCUSDT | IDLE | 2.27 | 4.3 | 1.64 | 0.03 | 10271.93 | 10.75 | skipped_fast |
| RIZEUSDT | IDLE | 1.87 | 9.54 | 1.46 | 0.01 | 56206.04 | 45.77 | skipped_fast |
| QAITUSDT | IDLE | 2.5 | 4.38 | 4.2 | -0.04 | 3753.25 | 107.85 | skipped_fast |
| KITEUSDT | IDLE | 1.31 | 4.0 | 2.03 | 0.11 | 60975.98 | 11.12 | skipped_fast |
| TELUSDT | IDLE | 1.39 | 3.39 | 1.48 | 0.01 | 179197.48 | 42.9 | skipped_fast |
| QNTUSDT | IDLE | 1.45 | 2.65 | 1.66 | 0.03 | 61270.13 | 1.56 | skipped_fast |
| RWAUSDT | IDLE | 0.67 | 1.17 | 1.07 | 0.03 | 53765.77 | 41.55 | skipped_fast |
| FLUIDUSDT | IDLE | 0.58 | 1.15 | 1.1 | 0.08 | 4161.15 | 37.89 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
