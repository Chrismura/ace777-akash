# Hulk DIGEST — 2026-08-21T22:43:32Z

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
| PYTHUSDT | IDLE | 1.36 | 5.17 | 0.22 | 0.11 | 5853099.9 | 2.04 | skipped_fast |
| XRPUSDT | IDLE | 1.65 | 6.38 | 0.05 | 0.15 | 135440548.06 | 4.83 | skipped_fast |
| CCUSDT | IDLE | 1.9 | 7.44 | 0.49 | 0.15 | 659604.29 | 9.72 | skipped_fast |
| HBARUSDT | IDLE | 2.19 | 4.71 | 0.4 | 0.08 | 872646.08 | 1.26 | skipped_fast |
| WUSDT | IDLE | 2.54 | 5.92 | 0.03 | 0.09 | 371157.52 | 12.24 | skipped_fast |
| ZBCNUSDT | IDLE | 1.78 | 7.69 | 0.0 | 0.12 | 507218.73 | 33.6 | skipped_fast |
| CHIPUSDT | IDLE | 1.5 | 4.54 | 1.54 | 0.05 | 533620.2 | 3.06 | skipped_fast |
| BIOUSDT | IDLE | 2.29 | 5.04 | 1.11 | 0.03 | 188116.05 | 3.11 | skipped_fast |
| REDUSDT | IDLE | 1.33 | 11.01 | 8.32 | 0.18 | 156276.14 | 16.22 | skipped_fast |
| EDELUSDT | IDLE | 2.28 | 5.04 | 0.0 | -0.03 | 82605.32 | 32.77 | skipped_fast |
| RWAINCUSDT | IDLE | 2.18 | 4.07 | 1.96 | 0.02 | 10244.46 | 16.16 | skipped_fast |
| TELUSDT | IDLE | 2.53 | 6.45 | 0.77 | 0.05 | 186895.47 | 20.68 | skipped_fast |
| QAITUSDT | IDLE | 2.34 | 4.38 | 1.94 | -0.02 | 3835.98 | 67.45 | skipped_fast |
| KITEUSDT | IDLE | 1.22 | 3.58 | 1.19 | 0.11 | 61443.95 | 12.92 | skipped_fast |
| RIZEUSDT | IDLE | 0.96 | 4.7 | 2.11 | 0.06 | 56399.15 | 36.52 | skipped_fast |
| QNTUSDT | IDLE | 2.13 | 4.26 | 0.0 | 0.06 | 80837.84 | 3.03 | skipped_fast |
| RWAUSDT | IDLE | 0.88 | 1.75 | 0.0 | 0.04 | 54181.55 | 16.39 | skipped_fast |
| FLUIDUSDT | IDLE | 0.51 | 1.15 | 0.08 | 0.09 | 4171.26 | 23.22 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
