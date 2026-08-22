# Hulk DIGEST — 2026-08-22T16:28:45Z

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
| PYTHUSDT | IDLE | 1.47 | 7.24 | 0.25 | 0.07 | 51439034.09 | 3.9 | skipped_fast |
| XRPUSDT | IDLE | 1.34 | 7.64 | 3.95 | 0.05 | 215638883.23 | 4.08 | skipped_fast |
| HBARUSDT | IDLE | 0.81 | 3.03 | 1.11 | -0.0 | 1130626.1 | 1.29 | skipped_fast |
| CCUSDT | IDLE | 0.98 | 4.14 | 2.36 | 0.09 | 764389.28 | 10.25 | skipped_fast |
| CHIPUSDT | IDLE | 0.57 | 3.36 | 1.03 | -0.1 | 627573.6 | 3.36 | skipped_fast |
| WUSDT | IDLE | 0.62 | 2.58 | 1.05 | -0.01 | 544198.91 | 12.72 | skipped_fast |
| ZBCNUSDT | IDLE | 1.29 | 3.49 | 1.33 | -0.04 | 316205.62 | 25.54 | skipped_fast |
| BIOUSDT | IDLE | 0.96 | 6.58 | 4.32 | -0.06 | 219804.92 | 3.29 | skipped_fast |
| KITEUSDT | IDLE | 1.89 | 4.35 | 1.51 | 0.03 | 85279.81 | 10.68 | skipped_fast |
| EDELUSDT | IDLE | 1.4 | 2.52 | 1.9 | -0.03 | 74806.16 | 22.83 | skipped_fast |
| REDUSDT | IDLE | 0.52 | 5.67 | 4.17 | -0.13 | 132976.37 | 14.62 | skipped_fast |
| RIZEUSDT | IDLE | 1.32 | 3.23 | 0.15 | 0.03 | 56591.4 | 45.5 | skipped_fast |
| QAITUSDT | IDLE | 1.67 | 3.19 | 0.94 | 0.01 | 2320.37 | 67.45 | skipped_fast |
| QNTUSDT | IDLE | 0.86 | 2.69 | 2.08 | -0.02 | 183798.77 | 6.3 | skipped_fast |
| RWAINCUSDT | IDLE | 0.77 | 1.53 | 0.0 | 0.03 | 8171.79 | 64.45 | skipped_fast |
| TELUSDT | IDLE | 0.95 | 2.37 | 1.16 | 0.01 | 137774.84 | 53.13 | skipped_fast |
| RWAUSDT | IDLE | 0.55 | 1.06 | 0.32 | 0.02 | 56365.65 | 24.32 | skipped_fast |
| FLUIDUSDT | IDLE | 0.0 | 0.0 | 0.0 | -0.03 | 4618.58 | 21.63 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
