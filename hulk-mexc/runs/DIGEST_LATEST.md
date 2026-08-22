# Hulk DIGEST — 2026-08-22T15:24:02Z

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
| PYTHUSDT | IDLE | 1.61 | 7.62 | 2.43 | 0.04 | 51496449.63 | 9.98 | skipped_fast |
| XRPUSDT | IDLE | 1.36 | 7.49 | 6.09 | 0.02 | 214916928.93 | 2.78 | skipped_fast |
| CCUSDT | IDLE | 1.32 | 5.65 | 2.91 | 0.1 | 799246.09 | 6.01 | skipped_fast |
| HBARUSDT | IDLE | 0.86 | 2.96 | 2.88 | -0.02 | 1167554.1 | 5.26 | skipped_fast |
| CHIPUSDT | IDLE | 0.64 | 3.51 | 2.92 | -0.1 | 613870.17 | 6.84 | skipped_fast |
| WUSDT | IDLE | 0.8 | 3.17 | 2.36 | -0.02 | 555295.57 | 9.68 | skipped_fast |
| KITEUSDT | IDLE | 2.81 | 6.37 | 2.89 | 0.02 | 85177.59 | 9.94 | skipped_fast |
| ZBCNUSDT | IDLE | 1.36 | 3.49 | 2.69 | -0.07 | 325205.69 | 19.7 | skipped_fast |
| BIOUSDT | IDLE | 0.99 | 6.58 | 5.48 | -0.07 | 221709.23 | 3.33 | skipped_fast |
| EDELUSDT | IDLE | 1.42 | 2.52 | 2.12 | -0.05 | 79102.41 | 22.83 | skipped_fast |
| REDUSDT | IDLE | 0.53 | 5.62 | 5.31 | -0.05 | 150087.88 | 21.3 | skipped_fast |
| QAITUSDT | IDLE | 1.99 | 3.76 | 1.48 | 0.01 | 2320.37 | 67.45 | skipped_fast |
| RIZEUSDT | IDLE | 0.79 | 3.28 | 0.44 | 0.03 | 56016.09 | 21.94 | skipped_fast |
| QNTUSDT | IDLE | 0.89 | 2.69 | 2.62 | -0.02 | 188363.36 | 1.58 | skipped_fast |
| RWAINCUSDT | IDLE | 0.77 | 1.53 | 0.0 | 0.01 | 9839.83 | 75.23 | skipped_fast |
| TELUSDT | IDLE | 1.11 | 2.75 | 1.58 | -0.01 | 140263.86 | 48.04 | skipped_fast |
| FLUIDUSDT | IDLE | 0.98 | 1.87 | 1.32 | -0.04 | 4625.53 | 24.0 | skipped_fast |
| RWAUSDT | IDLE | 0.66 | 1.23 | 0.65 | 0.02 | 57301.64 | 16.25 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
