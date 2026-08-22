# Hulk DIGEST — 2026-08-22T03:37:37Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.41 | 11.15 | 0.6 | 0.17 | 7959830.51 | 1.87 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.47 | 14.16 | 1.08 | 0.21 | 164469741.7 | 5.7 | skipped_fast |
| HBARUSDT | IDLE | 2.4 | 6.93 | 0.36 | 0.11 | 1032164.77 | 8.41 | skipped_fast |
| CCUSDT | IDLE | 1.95 | 8.96 | 0.57 | 0.18 | 687855.14 | 18.52 | skipped_fast |
| CHIPUSDT | IDLE | 2.48 | 5.36 | 1.32 | -0.01 | 452593.98 | 8.94 | skipped_fast |
| BIOUSDT | IDLE | 3.0 | 7.36 | 2.05 | 0.08 | 198679.95 | 3.0 | skipped_fast |
| ZBCNUSDT | IDLE | 1.41 | 5.16 | 1.37 | 0.12 | 537450.76 | 22.38 | skipped_fast |
| WUSDT | IDLE | 1.81 | 5.83 | 0.32 | 0.12 | 423479.15 | 11.82 | skipped_fast |
| RIZEUSDT | IDLE | 1.82 | 7.71 | 4.41 | 0.1 | 59544.13 | 44.22 | skipped_fast |
| REDUSDT | IDLE | 0.94 | 7.96 | 4.51 | 0.2 | 157940.92 | 8.75 | skipped_fast |
| EDELUSDT | IDLE | 1.93 | 3.95 | 2.17 | -0.02 | 80379.14 | 55.59 | skipped_fast |
| KITEUSDT | IDLE | 1.41 | 4.59 | 0.08 | 0.12 | 67759.91 | 11.57 | skipped_fast |
| RWAINCUSDT | IDLE | 1.94 | 3.44 | 2.9 | 0.01 | 9343.86 | 76.13 | skipped_fast |
| QNTUSDT | IDLE | 1.85 | 4.68 | 0.1 | 0.1 | 174257.0 | 8.86 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | 0.0 | 3808.79 | 63.67 | skipped_fast |
| RWAUSDT | IDLE | 1.5 | 2.97 | 0.16 | 0.06 | 56293.6 | 8.02 | skipped_fast |
| TELUSDT | IDLE | 1.03 | 2.45 | 0.61 | 0.07 | 173556.19 | 40.92 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.07 | 4710.05 | 22.28 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
