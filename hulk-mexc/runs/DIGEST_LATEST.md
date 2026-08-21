# Hulk DIGEST — 2026-08-21T23:06:37Z

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
| PYTHUSDT | IDLE | 1.68 | 6.26 | 0.16 | 0.12 | 5970640.38 | 2.02 | skipped_fast |
| XRPUSDT | IDLE | 1.71 | 6.54 | 0.09 | 0.15 | 138152049.96 | 2.76 | skipped_fast |
| CCUSDT | IDLE | 1.89 | 7.42 | 0.62 | 0.14 | 665431.84 | 8.86 | skipped_fast |
| HBARUSDT | IDLE | 2.36 | 5.1 | 0.0 | 0.09 | 888728.04 | 3.76 | skipped_fast |
| ZBCNUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.51 | 10.07 | 0.51 | 0.14 | 510101.28 | 22.94 | skipped_fast |
| WUSDT | IDLE | 2.74 | 6.91 | 1.21 | 0.08 | 376458.35 | 10.24 | skipped_fast |
| CHIPUSDT | IDLE | 1.16 | 3.56 | 1.03 | 0.05 | 544884.64 | 3.07 | skipped_fast |
| BIOUSDT | IDLE | 2.29 | 5.04 | 0.98 | 0.02 | 187364.09 | 6.21 | skipped_fast |
| EDELUSDT | IDLE | 2.53 | 5.5 | 0.54 | -0.03 | 82518.01 | 21.81 | skipped_fast |
| RWAINCUSDT | IDLE | 2.18 | 4.07 | 1.96 | 0.02 | 10205.68 | 16.16 | skipped_fast |
| QAITUSDT | IDLE | 2.27 | 4.22 | 2.14 | -0.02 | 3921.68 | 43.69 | skipped_fast |
| REDUSDT | IDLE | 0.87 | 7.3 | 5.01 | 0.18 | 157242.09 | 18.63 | skipped_fast |
| TELUSDT | IDLE | 2.67 | 6.51 | 0.31 | 0.07 | 185107.21 | 41.19 | skipped_fast |
| QNTUSDT | IDLE | 2.49 | 5.13 | 0.0 | 0.07 | 96657.23 | 1.5 | skipped_fast |
| KITEUSDT | IDLE | 1.11 | 3.12 | 1.15 | 0.1 | 61452.52 | 12.04 | skipped_fast |
| RWAUSDT | IDLE | 1.01 | 2.0 | 0.16 | 0.04 | 54364.67 | 16.39 | skipped_fast |
| FLUIDUSDT | IDLE | 0.51 | 1.15 | 0.08 | 0.09 | 4171.26 | 21.83 | skipped_fast |
| RIZEUSDT | IDLE | 1.04 | 4.7 | 1.86 | 0.05 | 56647.57 | 289.51 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
