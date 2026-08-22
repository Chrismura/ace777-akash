# Hulk DIGEST — 2026-08-22T04:12:44Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.84 | 13.11 | 0.11 | 0.2 | 10241424.42 | 7.32 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.14 | 12.22 | 1.3 | 0.2 | 166980149.27 | 3.8 | skipped_fast |
| CCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.1 | 11.56 | 0.07 | 0.22 | 721525.63 | 19.45 | skipped_fast |
| HBARUSDT | IDLE | 2.1 | 6.18 | 0.0 | 0.11 | 1009107.64 | 1.2 | skipped_fast |
| CHIPUSDT | IDLE | 2.87 | 5.36 | 2.5 | 0.0 | 451653.59 | 6.03 | skipped_fast |
| BIOUSDT | IDLE | 3.02 | 7.36 | 2.52 | 0.06 | 199772.79 | 3.01 | skipped_fast |
| WUSDT | IDLE | 1.97 | 7.18 | 0.66 | 0.14 | 428964.35 | 11.67 | skipped_fast |
| ZBCNUSDT | IDLE | 1.44 | 4.29 | 1.38 | 0.12 | 535352.58 | 16.65 | skipped_fast |
| EDELUSDT | IDLE | 2.07 | 4.07 | 3.37 | -0.04 | 80357.19 | 22.47 | skipped_fast |
| RIZEUSDT | IDLE | 1.86 | 7.71 | 5.01 | 0.1 | 59143.7 | 44.52 | skipped_fast |
| REDUSDT | IDLE | 0.93 | 7.96 | 3.81 | 0.21 | 157875.18 | 23.72 | skipped_fast |
| KITEUSDT | IDLE | 1.59 | 5.55 | 0.34 | 0.13 | 67554.12 | 12.38 | skipped_fast |
| RWAINCUSDT | IDLE | 2.04 | 3.6 | 3.22 | 0.01 | 9433.64 | 70.25 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3389.73 | 63.67 | skipped_fast |
| QNTUSDT | IDLE | 1.54 | 3.8 | 0.59 | 0.09 | 178574.52 | 4.45 | skipped_fast |
| RWAUSDT | IDLE | 1.54 | 3.05 | 0.24 | 0.06 | 56296.3 | 8.03 | skipped_fast |
| TELUSDT | IDLE | 1.03 | 2.4 | 0.61 | 0.07 | 173831.79 | 40.92 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.08 | 3702.43 | 19.53 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
