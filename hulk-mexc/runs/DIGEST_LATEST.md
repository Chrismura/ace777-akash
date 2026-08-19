# Hulk DIGEST — 2026-08-19T07:52:51Z

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
| XRPUSDT | IDLE | 0.43 | 0.84 | 0.13 | 0.01 | 9988761.72 | 1.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.62 | 3.01 | 1.57 | 0.02 | 166683.9 | 2.58 | skipped_fast |
| CHIPUSDT | IDLE | 1.28 | 4.52 | 3.65 | -0.12 | 172503.51 | 7.81 | skipped_fast |
| CCUSDT | IDLE | 0.85 | 1.53 | 1.09 | -0.02 | 213222.52 | 7.8 | skipped_fast |
| REDUSDT | IDLE | 0.94 | 4.43 | 2.38 | -0.1 | 151337.31 | 27.21 | skipped_fast |
| ZBCNUSDT | IDLE | 0.95 | 1.86 | 0.27 | 0.01 | 156283.7 | 12.67 | skipped_fast |
| BIOUSDT | IDLE | 1.23 | 2.44 | 0.12 | 0.04 | 62177.33 | 3.97 | skipped_fast |
| EDELUSDT | IDLE | 1.47 | 2.58 | 2.38 | -0.04 | 59282.18 | 40.57 | skipped_fast |
| RIZEUSDT | IDLE | 1.51 | 4.17 | 3.07 | -0.05 | 27378.28 | 52.06 | skipped_fast |
| KITEUSDT | IDLE | 1.16 | 2.19 | 0.81 | -0.01 | 65478.24 | 14.26 | skipped_fast |
| WUSDT | IDLE | 0.89 | 1.73 | 0.37 | -0.0 | 115407.93 | 13.59 | skipped_fast |
| QAITUSDT | IDLE | 0.86 | 5.53 | 2.39 | -0.15 | 10123.09 | 63.67 | skipped_fast |
| RWAINCUSDT | IDLE | 0.76 | 1.49 | 1.29 | 0.01 | 10542.9 | 41.58 | skipped_fast |
| QNTUSDT | IDLE | 1.03 | 1.97 | 0.58 | 0.01 | 37566.37 | 3.53 | skipped_fast |
| HBARUSDT | IDLE | 0.62 | 1.15 | 0.66 | 0.03 | 119665.13 | 1.48 | skipped_fast |
| TELUSDT | IDLE | 0.69 | 1.25 | 0.89 | 0.04 | 87626.33 | 13.85 | skipped_fast |
| RWAUSDT | IDLE | 0.83 | 1.5 | 1.04 | -0.01 | 51595.25 | 17.57 | skipped_fast |
| FLUIDUSDT | IDLE | 0.88 | 1.68 | 0.58 | -0.01 | 187.92 | 23.06 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
