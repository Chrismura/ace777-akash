# Hulk DIGEST — 2026-08-22T16:32:13Z

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
| PYTHUSDT | IDLE | 1.55 | 7.64 | 0.1 | 0.07 | 51434075.49 | 13.59 | skipped_fast |
| XRPUSDT | IDLE | 1.34 | 7.64 | 3.96 | 0.04 | 215188258.71 | 2.72 | skipped_fast |
| HBARUSDT | IDLE | 0.82 | 3.03 | 1.3 | -0.01 | 1127301.63 | 5.18 | skipped_fast |
| CCUSDT | IDLE | 0.98 | 4.14 | 2.32 | 0.08 | 764174.29 | 8.54 | skipped_fast |
| CHIPUSDT | IDLE | 0.57 | 3.36 | 0.8 | -0.1 | 627467.87 | 3.35 | skipped_fast |
| WUSDT | IDLE | 0.62 | 2.58 | 0.88 | -0.01 | 544078.22 | 8.47 | skipped_fast |
| ZBCNUSDT | IDLE | 1.28 | 3.49 | 1.21 | -0.03 | 315395.06 | 9.7 | skipped_fast |
| BIOUSDT | IDLE | 0.96 | 6.58 | 4.13 | -0.06 | 219819.82 | 3.29 | skipped_fast |
| KITEUSDT | IDLE | 1.92 | 4.35 | 2.05 | 0.02 | 85159.7 | 14.33 | skipped_fast |
| EDELUSDT | IDLE | 1.42 | 2.52 | 2.13 | -0.03 | 74856.14 | 22.83 | skipped_fast |
| REDUSDT | IDLE | 0.52 | 5.67 | 4.13 | -0.15 | 132898.26 | 10.03 | skipped_fast |
| RIZEUSDT | IDLE | 1.32 | 3.23 | 0.15 | 0.1 | 50952.77 | 45.5 | skipped_fast |
| QAITUSDT | IDLE | 1.67 | 3.19 | 0.94 | -0.01 | 2319.29 | 67.45 | skipped_fast |
| QNTUSDT | IDLE | 0.86 | 2.69 | 2.13 | -0.02 | 183315.78 | 4.73 | skipped_fast |
| RWAINCUSDT | IDLE | 0.77 | 1.53 | 0.0 | 0.03 | 8171.79 | 69.84 | skipped_fast |
| TELUSDT | IDLE | 0.93 | 2.37 | 0.84 | 0.01 | 138274.61 | 15.94 | skipped_fast |
| RWAUSDT | IDLE | 0.55 | 1.06 | 0.24 | 0.02 | 56417.29 | 16.22 | skipped_fast |
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
