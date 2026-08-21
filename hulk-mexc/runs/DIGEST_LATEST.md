# Hulk DIGEST — 2026-08-21T20:37:42Z

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
| PYTHUSDT | IDLE | 1.31 | 4.78 | 2.54 | 0.08 | 5538314.39 | 4.2 | skipped_fast |
| XRPUSDT | IDLE | 1.24 | 4.21 | 3.13 | 0.11 | 128952708.39 | 2.91 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.01 | 25.8 | 12.71 | 0.17 | 154006.61 | 8.92 | skipped_fast |
| ZBCNUSDT | IDLE | 2.46 | 10.86 | 5.18 | 0.12 | 478514.84 | 19.92 | skipped_fast |
| CCUSDT | IDLE | 1.41 | 3.91 | 0.33 | 0.09 | 637841.68 | 10.12 | skipped_fast |
| HBARUSDT | IDLE | 1.72 | 3.23 | 1.86 | 0.05 | 809516.34 | 1.3 | skipped_fast |
| CHIPUSDT | IDLE | 1.33 | 4.81 | 3.19 | 0.08 | 514837.53 | 3.09 | skipped_fast |
| WUSDT | IDLE | 2.08 | 3.92 | 1.63 | 0.06 | 368345.8 | 13.75 | skipped_fast |
| BIOUSDT | IDLE | 2.55 | 5.33 | 3.01 | 0.02 | 189206.49 | 3.16 | skipped_fast |
| EDELUSDT | IDLE | 2.79 | 5.01 | 4.23 | -0.05 | 81443.99 | 22.65 | skipped_fast |
| RWAINCUSDT | IDLE | 2.29 | 4.3 | 1.8 | 0.02 | 10919.36 | 26.77 | skipped_fast |
| RIZEUSDT | IDLE | 1.88 | 9.71 | 0.62 | 0.02 | 56288.46 | 47.09 | skipped_fast |
| KITEUSDT | IDLE | 1.25 | 4.0 | 2.59 | 0.1 | 60748.89 | 9.32 | skipped_fast |
| QAITUSDT | IDLE | 1.53 | 3.0 | 0.35 | -0.01 | 2793.19 | 67.05 | skipped_fast |
| TELUSDT | IDLE | 1.38 | 3.39 | 1.37 | 0.01 | 183198.77 | 21.46 | skipped_fast |
| QNTUSDT | IDLE | 1.45 | 2.65 | 1.69 | 0.04 | 59929.4 | 14.07 | skipped_fast |
| RWAUSDT | IDLE | 0.71 | 1.25 | 1.15 | 0.03 | 53873.94 | 8.32 | skipped_fast |
| FLUIDUSDT | IDLE | 0.58 | 1.15 | 1.1 | 0.07 | 4286.4 | 21.55 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
