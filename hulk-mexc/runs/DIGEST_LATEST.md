# Hulk DIGEST — 2026-08-22T04:29:21Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.89 | 13.61 | 0.82 | 0.2 | 11056583.59 | 5.5 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.14 | 12.41 | 0.61 | 0.22 | 170071480.03 | 2.52 | skipped_fast |
| CCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.15 | 11.56 | 1.81 | 0.2 | 732250.37 | 9.89 | skipped_fast |
| HBARUSDT | IDLE | 2.28 | 7.14 | 0.87 | 0.11 | 1033405.38 | 1.19 | skipped_fast |
| CHIPUSDT | IDLE | 2.76 | 5.36 | 1.03 | 0.01 | 442635.66 | 5.94 | skipped_fast |
| BIOUSDT | IDLE | 2.99 | 7.36 | 1.91 | 0.07 | 199987.4 | 2.99 | skipped_fast |
| WUSDT | IDLE | 1.96 | 7.18 | 0.41 | 0.14 | 434155.87 | 12.6 | skipped_fast |
| ZBCNUSDT | IDLE | 1.41 | 4.29 | 0.92 | 0.14 | 535395.71 | 22.26 | skipped_fast |
| EDELUSDT | IDLE | 2.06 | 4.07 | 3.26 | -0.04 | 80073.25 | 22.45 | skipped_fast |
| RIZEUSDT | IDLE | 1.85 | 7.71 | 4.96 | 0.1 | 59195.54 | 44.52 | skipped_fast |
| REDUSDT | IDLE | 0.93 | 7.96 | 4.4 | 0.21 | 158461.9 | 10.34 | skipped_fast |
| KITEUSDT | IDLE | 1.61 | 5.55 | 0.69 | 0.13 | 67812.83 | 8.86 | skipped_fast |
| RWAINCUSDT | IDLE | 2.05 | 3.6 | 3.27 | -0.0 | 9290.79 | 81.46 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3389.73 | 63.67 | skipped_fast |
| QNTUSDT | IDLE | 1.53 | 3.8 | 0.38 | 0.09 | 179097.08 | 1.48 | skipped_fast |
| TELUSDT | IDLE | 1.31 | 3.12 | 0.45 | 0.08 | 176602.41 | 40.57 | skipped_fast |
| RWAUSDT | IDLE | 1.55 | 3.05 | 0.32 | 0.06 | 56271.08 | 16.05 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.08 | 3702.43 | 22.35 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
