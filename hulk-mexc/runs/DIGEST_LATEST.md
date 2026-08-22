# Hulk DIGEST — 2026-08-22T03:36:54Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.41 | 11.15 | 0.45 | 0.18 | 7947354.94 | 1.87 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.47 | 14.16 | 1.0 | 0.21 | 164353943.29 | 5.69 | skipped_fast |
| HBARUSDT | IDLE | 2.39 | 6.93 | 0.13 | 0.11 | 1030633.52 | 2.4 | skipped_fast |
| CCUSDT | IDLE | 1.94 | 8.96 | 0.41 | 0.18 | 687845.14 | 7.56 | skipped_fast |
| CHIPUSDT | IDLE | 2.41 | 5.36 | 0.21 | -0.0 | 452535.58 | 2.95 | skipped_fast |
| BIOUSDT | IDLE | 2.99 | 7.36 | 2.02 | 0.08 | 198675.92 | 2.99 | skipped_fast |
| ZBCNUSDT | IDLE | 1.39 | 5.16 | 1.03 | 0.12 | 537474.57 | 7.13 | skipped_fast |
| WUSDT | IDLE | 1.8 | 5.83 | 0.09 | 0.12 | 423506.53 | 7.86 | skipped_fast |
| RIZEUSDT | IDLE | 1.82 | 7.71 | 4.42 | 0.1 | 59535.54 | 18.73 | skipped_fast |
| REDUSDT | IDLE | 0.94 | 7.96 | 4.61 | 0.2 | 157909.35 | 17.5 | skipped_fast |
| EDELUSDT | IDLE | 1.93 | 3.95 | 2.17 | -0.02 | 80429.17 | 66.74 | skipped_fast |
| RWAINCUSDT | IDLE | 1.89 | 3.44 | 2.27 | 0.02 | 9342.5 | 27.11 | skipped_fast |
| KITEUSDT | IDLE | 1.41 | 4.59 | 0.0 | 0.12 | 67776.31 | 9.78 | skipped_fast |
| QNTUSDT | IDLE | 1.85 | 4.68 | 0.18 | 0.1 | 174250.14 | 5.91 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | 0.0 | 3808.79 | 63.67 | skipped_fast |
| RWAUSDT | IDLE | 1.49 | 2.97 | 0.08 | 0.06 | 56320.63 | 16.04 | skipped_fast |
| TELUSDT | IDLE | 1.03 | 2.45 | 0.56 | 0.07 | 173559.49 | 35.8 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.07 | 4710.05 | 15.99 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
