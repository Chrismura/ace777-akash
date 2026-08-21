# Hulk DIGEST — 2026-08-21T21:41:05Z

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
| PYTHUSDT | IDLE | 1.17 | 4.51 | 0.64 | 0.1 | 5652458.05 | 2.07 | skipped_fast |
| XRPUSDT | IDLE | 1.1 | 3.73 | 0.81 | 0.11 | 129250302.9 | 1.43 | skipped_fast |
| CHIPUSDT | IDLE | 1.89 | 5.61 | 3.88 | 0.05 | 516840.35 | 6.2 | skipped_fast |
| ZBCNUSDT | IDLE | 1.95 | 8.19 | 3.77 | 0.1 | 489894.6 | 37.7 | skipped_fast |
| CCUSDT | IDLE | 1.29 | 3.75 | 0.43 | 0.1 | 651816.12 | 8.23 | skipped_fast |
| HBARUSDT | IDLE | 1.64 | 3.24 | 0.2 | 0.07 | 818111.39 | 1.28 | skipped_fast |
| WUSDT | IDLE | 1.96 | 3.83 | 0.58 | 0.06 | 369024.63 | 11.5 | skipped_fast |
| BIOUSDT | IDLE | 2.42 | 5.2 | 1.93 | 0.02 | 187845.01 | 3.13 | skipped_fast |
| REDUSDT | IDLE | 1.35 | 11.01 | 9.47 | 0.17 | 154232.27 | 10.68 | skipped_fast |
| RIZEUSDT | IDLE | 1.86 | 9.54 | 1.13 | 0.03 | 55836.45 | 14.03 | skipped_fast |
| EDELUSDT | IDLE | 1.91 | 4.12 | 0.66 | -0.04 | 83583.79 | 44.44 | skipped_fast |
| RWAINCUSDT | IDLE | 2.22 | 4.3 | 0.95 | 0.03 | 10249.04 | 42.69 | skipped_fast |
| KITEUSDT | IDLE | 1.28 | 4.0 | 1.48 | 0.11 | 61097.24 | 11.05 | skipped_fast |
| QAITUSDT | IDLE | 2.33 | 4.38 | 1.83 | -0.01 | 3809.29 | 115.79 | skipped_fast |
| TELUSDT | IDLE | 1.89 | 4.81 | 0.78 | 0.03 | 182980.16 | 36.76 | skipped_fast |
| QNTUSDT | IDLE | 1.38 | 2.65 | 0.74 | 0.04 | 62627.26 | 3.1 | skipped_fast |
| RWAUSDT | IDLE | 0.6 | 1.17 | 0.25 | 0.03 | 53979.53 | 24.78 | skipped_fast |
| FLUIDUSDT | IDLE | 0.51 | 1.15 | 0.09 | 0.09 | 4171.26 | 21.93 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
