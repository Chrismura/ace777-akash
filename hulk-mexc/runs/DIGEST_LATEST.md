# Hulk DIGEST — 2026-08-21T22:44:22Z

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
| PYTHUSDT | IDLE | 1.36 | 5.17 | 0.2 | 0.11 | 5857960.98 | 6.13 | skipped_fast |
| XRPUSDT | IDLE | 1.67 | 6.41 | 0.46 | 0.15 | 135560518.82 | 2.77 | skipped_fast |
| CCUSDT | IDLE | 1.88 | 7.44 | 0.14 | 0.14 | 659981.12 | 6.17 | skipped_fast |
| HBARUSDT | IDLE | 2.18 | 4.71 | 0.31 | 0.08 | 872724.43 | 1.26 | skipped_fast |
| WUSDT | IDLE | 2.55 | 5.94 | 0.13 | 0.09 | 371174.06 | 8.17 | skipped_fast |
| ZBCNUSDT | IDLE | 1.89 | 8.12 | 0.18 | 0.13 | 507492.68 | 36.39 | skipped_fast |
| CHIPUSDT | IDLE | 1.52 | 4.54 | 2.05 | 0.06 | 533588.57 | 12.31 | skipped_fast |
| BIOUSDT | IDLE | 2.3 | 5.04 | 1.26 | 0.03 | 188091.11 | 3.11 | skipped_fast |
| REDUSDT | IDLE | 1.33 | 11.01 | 8.32 | 0.18 | 156292.31 | 7.3 | skipped_fast |
| EDELUSDT | IDLE | 2.3 | 5.04 | 0.22 | -0.03 | 82630.34 | 21.83 | skipped_fast |
| RWAINCUSDT | IDLE | 2.18 | 4.07 | 1.96 | 0.02 | 10244.46 | 16.16 | skipped_fast |
| TELUSDT | IDLE | 2.52 | 6.45 | 0.72 | 0.06 | 186912.57 | 5.17 | skipped_fast |
| QAITUSDT | IDLE | 2.34 | 4.38 | 1.94 | -0.02 | 3835.98 | 67.45 | skipped_fast |
| KITEUSDT | IDLE | 1.22 | 3.58 | 1.16 | 0.11 | 61473.08 | 12.92 | skipped_fast |
| QNTUSDT | IDLE | 2.15 | 4.29 | 0.02 | 0.06 | 81551.91 | 1.51 | skipped_fast |
| RIZEUSDT | IDLE | 0.96 | 4.7 | 1.96 | 0.06 | 56410.67 | 46.99 | skipped_fast |
| RWAUSDT | IDLE | 0.88 | 1.75 | 0.08 | 0.04 | 54148.86 | 16.39 | skipped_fast |
| FLUIDUSDT | IDLE | 0.51 | 1.15 | 0.08 | 0.09 | 4171.26 | 21.83 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
