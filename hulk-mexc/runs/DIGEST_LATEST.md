# Hulk DIGEST — 2026-08-22T03:46:26Z

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
| PYTHUSDT | IDLE | 2.51 | 11.77 | 2.24 | 0.17 | 8389211.02 | 13.25 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.49 | 14.16 | 1.88 | 0.2 | 165399832.31 | 4.47 | skipped_fast |
| HBARUSDT | IDLE | 2.44 | 6.93 | 1.09 | 0.11 | 1033272.14 | 1.21 | skipped_fast |
| CCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.0 | 9.7 | 0.11 | 0.19 | 694230.76 | 11.6 | skipped_fast |
| CHIPUSDT | IDLE | 2.53 | 5.36 | 2.0 | -0.03 | 454022.22 | 5.98 | skipped_fast |
| BIOUSDT | IDLE | 3.02 | 7.36 | 2.49 | 0.08 | 199083.68 | 3.0 | skipped_fast |
| WUSDT | IDLE | 1.83 | 5.83 | 0.59 | 0.12 | 424351.64 | 0.99 | skipped_fast |
| ZBCNUSDT | IDLE | 1.47 | 5.16 | 2.84 | 0.12 | 536980.24 | 39.51 | skipped_fast |
| RIZEUSDT | IDLE | 1.81 | 7.71 | 4.15 | 0.11 | 59465.42 | 45.81 | skipped_fast |
| EDELUSDT | IDLE | 1.95 | 3.95 | 2.39 | -0.02 | 80451.95 | 33.28 | skipped_fast |
| REDUSDT | IDLE | 0.92 | 7.96 | 3.38 | 0.22 | 158013.66 | 17.31 | skipped_fast |
| RWAINCUSDT | IDLE | 2.02 | 3.6 | 2.95 | 0.01 | 9351.15 | 38.1 | skipped_fast |
| KITEUSDT | IDLE | 1.47 | 4.86 | 0.13 | 0.12 | 67685.12 | 9.78 | skipped_fast |
| QNTUSDT | IDLE | 1.88 | 4.68 | 0.58 | 0.09 | 175011.84 | 11.86 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3389.73 | 63.67 | skipped_fast |
| RWAUSDT | IDLE | 1.49 | 2.97 | 0.08 | 0.06 | 56198.46 | 8.02 | skipped_fast |
| TELUSDT | IDLE | 1.03 | 2.45 | 0.51 | 0.07 | 173765.2 | 51.15 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.07 | 4710.05 | 21.61 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
