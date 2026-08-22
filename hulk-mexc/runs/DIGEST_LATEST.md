# Hulk DIGEST — 2026-08-22T03:16:55Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.39 | 10.96 | 0.41 | 0.18 | 7651699.14 | 3.74 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.28 | 11.43 | 0.56 | 0.2 | 161059382.27 | 5.16 | skipped_fast |
| HBARUSDT | IDLE | 2.24 | 5.87 | 0.18 | 0.11 | 1004534.76 | 1.21 | skipped_fast |
| CCUSDT | IDLE | 1.98 | 8.96 | 1.72 | 0.17 | 679641.0 | 10.21 | skipped_fast |
| BIOUSDT | IDLE | 3.04 | 7.36 | 2.78 | 0.06 | 197904.38 | 3.01 | skipped_fast |
| CHIPUSDT | IDLE | 1.96 | 4.28 | 0.77 | -0.02 | 448466.35 | 3.0 | skipped_fast |
| WUSDT | IDLE | 1.79 | 5.61 | 0.54 | 0.12 | 417876.8 | 12.85 | skipped_fast |
| ZBCNUSDT | IDLE | 1.44 | 5.16 | 2.23 | 0.12 | 540318.99 | 46.65 | skipped_fast |
| EDELUSDT | IDLE | 1.95 | 3.83 | 3.26 | -0.04 | 80045.99 | 22.42 | skipped_fast |
| RIZEUSDT | IDLE | 1.82 | 7.71 | 4.37 | 0.1 | 59519.73 | 44.22 | skipped_fast |
| REDUSDT | IDLE | 0.93 | 7.96 | 3.95 | 0.2 | 158000.38 | 8.7 | skipped_fast |
| RWAINCUSDT | IDLE | 1.94 | 3.44 | 3.0 | -0.0 | 9452.18 | 16.21 | skipped_fast |
| KITEUSDT | IDLE | 1.39 | 4.4 | 0.47 | 0.12 | 67588.87 | 8.96 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | 0.0 | 3808.79 | 63.67 | skipped_fast |
| QNTUSDT | IDLE | 1.69 | 3.97 | 0.15 | 0.09 | 174120.61 | 8.92 | skipped_fast |
| RWAUSDT | IDLE | 1.31 | 2.56 | 0.4 | 0.05 | 56174.9 | 16.14 | skipped_fast |
| TELUSDT | IDLE | 0.92 | 2.19 | 0.46 | 0.07 | 173404.99 | 51.2 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.07 | 4710.05 | 23.06 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
