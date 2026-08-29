# Hulk DIGEST — 2026-08-29T06:09:37Z

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
| CHIPUSDT | IDLE | 2.49 | 12.37 | 2.54 | 0.09 | 1179644.17 | 4.64 | skipped_fast |
| XRPUSDT | IDLE | 0.62 | 1.13 | 0.79 | -0.03 | 43908214.17 | 0.72 | skipped_fast |
| QAITUSDT | IDLE | 2.35 | 20.42 | 14.43 | -0.01 | 84590.7 | 20.35 | skipped_fast |
| PYTHUSDT | IDLE | 0.83 | 1.48 | 1.21 | -0.02 | 517431.79 | 4.22 | skipped_fast |
| RIZEUSDT | IDLE | 2.64 | 6.18 | 2.13 | -0.04 | 28972.32 | 56.03 | skipped_fast |
| WUSDT | IDLE | 1.16 | 2.18 | 0.99 | -0.03 | 208366.63 | 16.29 | skipped_fast |
| KITEUSDT | IDLE | 1.56 | 2.76 | 2.44 | -0.02 | 73273.77 | 12.67 | skipped_fast |
| REDUSDT | IDLE | 1.63 | 3.09 | 1.14 | -0.02 | 61076.13 | 13.81 | skipped_fast |
| CCUSDT | IDLE | 0.65 | 1.18 | 0.77 | -0.02 | 234413.55 | 5.42 | skipped_fast |
| EDELUSDT | IDLE | 1.14 | 4.37 | 2.51 | -0.09 | 89810.51 | 19.07 | skipped_fast |
| ZBCNUSDT | IDLE | 0.61 | 1.56 | 1.07 | -0.07 | 175373.13 | 14.36 | skipped_fast |
| HBARUSDT | IDLE | 0.54 | 0.95 | 0.87 | -0.04 | 462913.03 | 1.33 | skipped_fast |
| BIOUSDT | IDLE | 0.43 | 0.76 | 0.64 | -0.03 | 82187.31 | 3.6 | skipped_fast |
| TELUSDT | IDLE | 1.28 | 2.29 | 1.79 | -0.05 | 94356.36 | 62.88 | skipped_fast |
| RWAINCUSDT | IDLE | 0.0 | 0.0 | 0.0 | -0.01 | 3436.55 | 54.82 | skipped_fast |
| FLUIDUSDT | IDLE | 0.9 | 1.61 | 1.22 | -0.05 | 3721.3 | 21.65 | skipped_fast |
| QNTUSDT | IDLE | 0.58 | 1.12 | 0.21 | -0.02 | 40677.29 | 4.88 | skipped_fast |
| RWAUSDT | IDLE | 0.51 | 0.99 | 0.16 | 0.0 | 55517.71 | 16.43 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
