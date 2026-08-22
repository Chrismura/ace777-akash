# Hulk DIGEST — 2026-08-22T16:27:35Z

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
| PYTHUSDT | IDLE | 1.47 | 7.24 | 0.16 | 0.07 | 51439814.33 | 1.95 | skipped_fast |
| XRPUSDT | IDLE | 1.33 | 7.64 | 3.82 | 0.05 | 215620663.24 | 4.08 | skipped_fast |
| HBARUSDT | IDLE | 0.81 | 3.03 | 1.11 | -0.0 | 1130632.25 | 3.88 | skipped_fast |
| CCUSDT | IDLE | 0.99 | 4.14 | 2.67 | 0.08 | 763520.22 | 8.56 | skipped_fast |
| CHIPUSDT | IDLE | 0.57 | 3.36 | 1.03 | -0.1 | 627592.42 | 6.71 | skipped_fast |
| WUSDT | IDLE | 0.62 | 2.58 | 1.03 | -0.01 | 544193.53 | 19.09 | skipped_fast |
| ZBCNUSDT | IDLE | 1.29 | 3.49 | 1.34 | -0.03 | 316168.96 | 22.49 | skipped_fast |
| BIOUSDT | IDLE | 0.96 | 6.58 | 4.22 | -0.06 | 219776.32 | 3.29 | skipped_fast |
| KITEUSDT | IDLE | 1.88 | 4.35 | 1.36 | 0.04 | 85368.93 | 8.92 | skipped_fast |
| EDELUSDT | IDLE | 1.42 | 2.52 | 2.13 | -0.03 | 74831.17 | 22.86 | skipped_fast |
| REDUSDT | IDLE | 0.52 | 5.67 | 4.17 | -0.13 | 132970.19 | 14.62 | skipped_fast |
| RIZEUSDT | IDLE | 1.32 | 3.23 | 0.15 | 0.03 | 56591.38 | 45.5 | skipped_fast |
| QAITUSDT | IDLE | 1.67 | 3.19 | 0.94 | 0.01 | 2320.37 | 67.45 | skipped_fast |
| QNTUSDT | IDLE | 0.86 | 2.69 | 2.08 | -0.02 | 183928.43 | 6.3 | skipped_fast |
| RWAINCUSDT | IDLE | 0.77 | 1.53 | 0.0 | 0.02 | 8619.61 | 48.3 | skipped_fast |
| TELUSDT | IDLE | 0.95 | 2.37 | 1.21 | 0.01 | 137810.86 | 53.16 | skipped_fast |
| RWAUSDT | IDLE | 0.55 | 1.06 | 0.32 | 0.02 | 56316.11 | 40.57 | skipped_fast |
| FLUIDUSDT | IDLE | 0.0 | 0.0 | 0.0 | -0.03 | 4618.58 | 22.4 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
