# Hulk DIGEST — 2026-08-22T02:46:34Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.6 | 11.02 | 0.04 | 0.17 | 7231537.43 | 3.78 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.45 | 12.13 | 0.0 | 0.19 | 157120208.94 | 1.3 | skipped_fast |
| HBARUSDT | IDLE | 2.47 | 6.0 | 0.04 | 0.09 | 983547.19 | 1.23 | skipped_fast |
| CCUSDT | IDLE | 1.95 | 8.3 | 0.09 | 0.16 | 655509.98 | 7.68 | skipped_fast |
| ZBCNUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.45 | 9.63 | 1.84 | 0.11 | 540083.32 | 28.28 | skipped_fast |
| CHIPUSDT | IDLE | 2.28 | 5.26 | 0.06 | -0.02 | 454934.04 | 2.99 | skipped_fast |
| BIOUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.2 | 8.18 | 1.96 | 0.09 | 192918.15 | 3.0 | skipped_fast |
| WUSDT | IDLE | 1.98 | 5.85 | 0.09 | 0.11 | 413607.16 | 12.93 | skipped_fast |
| EDELUSDT | IDLE | 2.46 | 5.02 | 2.82 | -0.03 | 79887.94 | 44.59 | skipped_fast |
| RIZEUSDT | IDLE | 2.0 | 8.52 | 4.6 | 0.1 | 61337.86 | 44.22 | skipped_fast |
| REDUSDT | IDLE | 0.97 | 8.27 | 4.79 | 0.19 | 158030.83 | 10.39 | skipped_fast |
| QNTUSDT | IDLE | 2.34 | 5.48 | 0.22 | 0.08 | 172505.48 | 4.47 | skipped_fast |
| KITEUSDT | IDLE | 1.33 | 4.09 | 0.22 | 0.12 | 62460.0 | 11.66 | skipped_fast |
| RWAINCUSDT | IDLE | 1.83 | 3.27 | 2.58 | 0.02 | 9400.35 | 43.36 | skipped_fast |
| QAITUSDT | IDLE | 1.88 | 3.57 | 1.22 | 0.0 | 3930.15 | 63.67 | skipped_fast |
| TELUSDT | IDLE | 2.14 | 5.11 | 1.02 | 0.06 | 174198.55 | 67.1 | skipped_fast |
| RWAUSDT | IDLE | 1.44 | 2.83 | 0.32 | 0.04 | 55854.89 | 24.36 | skipped_fast |
| FLUIDUSDT | IDLE | 1.44 | 3.69 | 2.03 | 0.07 | 4710.05 | 21.07 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
