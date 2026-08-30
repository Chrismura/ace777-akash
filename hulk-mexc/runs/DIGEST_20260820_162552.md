# Hulk DIGEST — 2026-08-20T16:25:52Z

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
| XRPUSDT | IDLE | 1.89 | 9.66 | 0.48 | 0.18 | 76681499.71 | 2.38 | skipped_fast |
| PYTHUSDT | IDLE | 1.35 | 4.1 | 1.67 | 0.1 | 1124774.73 | 2.26 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.49 | 12.28 | 5.48 | 0.08 | 253137.7 | 4.99 | skipped_fast |
| CHIPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.82 | 8.61 | 1.96 | 0.1 | 283830.9 | 3.28 | skipped_fast |
| CCUSDT | IDLE | 1.25 | 3.17 | 2.98 | 0.09 | 484968.28 | 9.81 | skipped_fast |
| BIOUSDT | IDLE | 1.73 | 8.96 | 7.46 | 0.04 | 245122.91 | 6.58 | skipped_fast |
| WUSDT | IDLE | 1.68 | 3.21 | 0.96 | 0.05 | 317848.28 | 14.67 | skipped_fast |
| REDUSDT | IDLE | 1.23 | 8.34 | 6.67 | 0.09 | 200451.75 | 12.48 | skipped_fast |
| HBARUSDT | IDLE | 1.06 | 2.09 | 0.19 | 0.06 | 451395.63 | 1.36 | skipped_fast |
| TELUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.06 | 9.41 | 1.21 | 0.14 | 160627.44 | 22.3 | skipped_fast |
| KITEUSDT | IDLE | 1.45 | 2.83 | 0.48 | 0.03 | 58981.92 | 13.22 | skipped_fast |
| RIZEUSDT | IDLE | 1.06 | 7.23 | 3.34 | 0.07 | 62989.63 | 24.85 | skipped_fast |
| RWAINCUSDT | IDLE | 1.59 | 2.95 | 1.49 | -0.0 | 7213.6 | 44.52 | skipped_fast |
| EDELUSDT | IDLE | 0.57 | 2.94 | 0.44 | 0.08 | 94618.98 | 33.13 | skipped_fast |
| QAITUSDT | IDLE | 1.0 | 2.01 | 0.0 | 0.01 | 5336.18 | 46.39 | skipped_fast |
| QNTUSDT | IDLE | 1.0 | 2.09 | 1.42 | 0.06 | 62106.12 | 8.12 | skipped_fast |
| RWAUSDT | IDLE | 0.46 | 0.86 | 0.34 | 0.01 | 52155.7 | 17.17 | skipped_fast |
| FLUIDUSDT | IDLE | 0.75 | 1.49 | 0.01 | 0.06 | 3025.89 | 29.86 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
