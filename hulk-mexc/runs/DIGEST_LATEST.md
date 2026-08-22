# Hulk DIGEST — 2026-08-22T03:39:37Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.4 | 11.15 | 0.32 | 0.18 | 7991217.07 | 1.87 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.48 | 14.16 | 1.64 | 0.2 | 164540147.86 | 9.54 | skipped_fast |
| HBARUSDT | IDLE | 2.42 | 6.93 | 0.68 | 0.11 | 1033194.7 | 1.21 | skipped_fast |
| CCUSDT | IDLE | 1.94 | 8.96 | 0.37 | 0.18 | 687527.47 | 8.39 | skipped_fast |
| CHIPUSDT | IDLE | 2.5 | 5.36 | 1.65 | -0.02 | 452371.13 | 2.99 | skipped_fast |
| BIOUSDT | IDLE | 3.0 | 7.36 | 2.14 | 0.08 | 198719.68 | 5.99 | skipped_fast |
| ZBCNUSDT | IDLE | 1.41 | 5.16 | 1.38 | 0.12 | 536939.73 | 21.92 | skipped_fast |
| WUSDT | IDLE | 1.81 | 5.83 | 0.29 | 0.12 | 423891.64 | 7.88 | skipped_fast |
| RIZEUSDT | IDLE | 1.82 | 7.71 | 4.36 | 0.1 | 59544.0 | 44.22 | skipped_fast |
| REDUSDT | IDLE | 0.94 | 7.96 | 4.63 | 0.2 | 157885.31 | 12.75 | skipped_fast |
| RWAINCUSDT | IDLE | 2.06 | 3.6 | 3.48 | 0.0 | 9369.97 | 32.72 | skipped_fast |
| EDELUSDT | IDLE | 1.99 | 3.95 | 2.93 | -0.03 | 80379.13 | 77.91 | skipped_fast |
| KITEUSDT | IDLE | 1.41 | 4.59 | 0.04 | 0.12 | 67745.18 | 9.78 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | 0.0 | 3808.79 | 63.67 | skipped_fast |
| QNTUSDT | IDLE | 1.85 | 4.68 | 0.19 | 0.1 | 174985.12 | 23.72 | skipped_fast |
| RWAUSDT | IDLE | 1.49 | 2.97 | 0.0 | 0.06 | 56324.26 | 8.02 | skipped_fast |
| TELUSDT | IDLE | 1.02 | 2.45 | 0.46 | 0.07 | 173585.92 | 35.8 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.07 | 4710.05 | 21.58 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
