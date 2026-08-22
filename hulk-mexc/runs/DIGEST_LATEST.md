# Hulk DIGEST — 2026-08-22T03:55:53Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.48 | 11.77 | 1.11 | 0.17 | 8953112.26 | 7.48 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.49 | 14.16 | 1.78 | 0.19 | 166169118.52 | 3.19 | skipped_fast |
| HBARUSDT | IDLE | 2.41 | 6.93 | 0.47 | 0.1 | 1034399.56 | 1.2 | skipped_fast |
| CCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.07 | 10.39 | 0.44 | 0.19 | 701695.25 | 7.46 | skipped_fast |
| CHIPUSDT | IDLE | 2.46 | 5.36 | 0.94 | -0.03 | 459560.32 | 5.94 | skipped_fast |
| BIOUSDT | IDLE | 3.0 | 7.36 | 2.2 | 0.07 | 199214.6 | 6.01 | skipped_fast |
| WUSDT | IDLE | 1.86 | 6.23 | 0.01 | 0.13 | 425119.27 | 13.69 | skipped_fast |
| ZBCNUSDT | IDLE | 1.44 | 5.37 | 1.18 | 0.13 | 537803.67 | 33.73 | skipped_fast |
| EDELUSDT | IDLE | 2.0 | 3.95 | 3.15 | -0.04 | 80658.63 | 33.73 | skipped_fast |
| RIZEUSDT | IDLE | 1.83 | 7.71 | 4.67 | 0.11 | 59280.39 | 68.11 | skipped_fast |
| REDUSDT | IDLE | 0.9 | 7.96 | 2.14 | 0.23 | 157659.06 | 16.41 | skipped_fast |
| KITEUSDT | IDLE | 1.55 | 5.3 | 0.32 | 0.13 | 67624.56 | 12.42 | skipped_fast |
| RWAINCUSDT | IDLE | 2.02 | 3.6 | 2.95 | 0.01 | 9351.15 | 54.47 | skipped_fast |
| QNTUSDT | IDLE | 1.87 | 4.68 | 0.47 | 0.1 | 178512.42 | 5.93 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3389.73 | 63.67 | skipped_fast |
| RWAUSDT | IDLE | 1.61 | 3.22 | 0.0 | 0.06 | 56272.74 | 8.01 | skipped_fast |
| TELUSDT | IDLE | 1.01 | 2.45 | 0.25 | 0.07 | 174005.84 | 40.84 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.07 | 4710.05 | 21.56 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
