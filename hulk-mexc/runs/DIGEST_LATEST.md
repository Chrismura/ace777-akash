# Hulk DIGEST — 2026-08-19T10:55:40Z

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
| XRPUSDT | IDLE | 0.53 | 1.01 | 0.39 | 0.01 | 10430248.94 | 0.99 | skipped_fast |
| CHIPUSDT | IDLE | 1.44 | 4.68 | 0.0 | -0.07 | 165386.64 | 3.76 | skipped_fast |
| PYTHUSDT | IDLE | 1.39 | 2.5 | 1.8 | 0.01 | 176956.31 | 2.61 | skipped_fast |
| BIOUSDT | IDLE | 1.32 | 2.42 | 1.46 | 0.03 | 64818.09 | 4.0 | skipped_fast |
| CCUSDT | IDLE | 0.72 | 1.44 | 0.02 | -0.0 | 214123.68 | 8.8 | skipped_fast |
| REDUSDT | IDLE | 0.85 | 3.42 | 2.29 | -0.13 | 143765.55 | 13.71 | skipped_fast |
| ZBCNUSDT | IDLE | 0.84 | 1.66 | 0.14 | 0.01 | 156840.04 | 14.47 | skipped_fast |
| KITEUSDT | IDLE | 1.18 | 2.19 | 1.19 | -0.0 | 57378.94 | 16.55 | skipped_fast |
| WUSDT | IDLE | 0.89 | 1.78 | 0.06 | 0.0 | 100859.2 | 8.61 | skipped_fast |
| RIZEUSDT | IDLE | 1.32 | 3.86 | 1.14 | -0.04 | 29309.49 | 51.27 | skipped_fast |
| EDELUSDT | IDLE | 1.27 | 2.31 | 1.59 | -0.03 | 59245.11 | 67.25 | skipped_fast |
| QAITUSDT | IDLE | 1.05 | 6.87 | 1.79 | -0.14 | 12413.68 | 65.65 | skipped_fast |
| RWAINCUSDT | IDLE | 0.79 | 1.49 | 0.59 | -0.0 | 10123.01 | 59.38 | skipped_fast |
| HBARUSDT | IDLE | 0.51 | 0.91 | 0.75 | 0.02 | 138827.36 | 1.48 | skipped_fast |
| TELUSDT | IDLE | 0.89 | 1.74 | 0.2 | 0.03 | 86932.49 | 27.36 | skipped_fast |
| QNTUSDT | IDLE | 0.79 | 1.42 | 1.02 | 0.01 | 37781.44 | 1.77 | skipped_fast |
| RWAUSDT | IDLE | 0.54 | 1.06 | 0.09 | -0.01 | 52367.75 | 8.76 | skipped_fast |
| FLUIDUSDT | IDLE | 0.84 | 1.66 | 0.15 | -0.01 | 1273.66 | 21.23 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
