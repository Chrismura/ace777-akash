# Hulk DIGEST — 2026-08-22T03:57:58Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.48 | 11.77 | 1.37 | 0.17 | 9129090.93 | 3.75 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.49 | 14.16 | 1.87 | 0.19 | 166205690.06 | 2.55 | skipped_fast |
| HBARUSDT | IDLE | 2.41 | 6.93 | 0.6 | 0.1 | 1033635.5 | 2.41 | skipped_fast |
| CCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.07 | 10.39 | 0.43 | 0.19 | 702559.81 | 12.42 | skipped_fast |
| CHIPUSDT | IDLE | 2.47 | 5.36 | 1.15 | -0.02 | 458801.08 | 5.95 | skipped_fast |
| BIOUSDT | IDLE | 3.01 | 7.36 | 2.23 | 0.07 | 199161.78 | 3.0 | skipped_fast |
| ZBCNUSDT | IDLE | 1.45 | 5.37 | 1.22 | 0.13 | 537610.05 | 19.5 | skipped_fast |
| WUSDT | IDLE | 1.87 | 6.27 | 0.18 | 0.13 | 425004.75 | 13.69 | skipped_fast |
| EDELUSDT | IDLE | 2.0 | 3.95 | 3.15 | -0.04 | 80633.57 | 33.69 | skipped_fast |
| RIZEUSDT | IDLE | 1.82 | 7.71 | 4.55 | 0.11 | 59288.09 | 46.02 | skipped_fast |
| REDUSDT | IDLE | 0.91 | 7.96 | 2.77 | 0.23 | 157571.51 | 10.16 | skipped_fast |
| KITEUSDT | IDLE | 1.55 | 5.3 | 0.4 | 0.13 | 67520.08 | 7.05 | skipped_fast |
| RWAINCUSDT | IDLE | 2.02 | 3.6 | 2.95 | 0.01 | 9351.15 | 38.1 | skipped_fast |
| QNTUSDT | IDLE | 1.88 | 4.68 | 0.68 | 0.09 | 178485.25 | 8.88 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3389.73 | 63.67 | skipped_fast |
| RWAUSDT | IDLE | 1.62 | 3.22 | 0.16 | 0.06 | 56340.67 | 8.01 | skipped_fast |
| TELUSDT | IDLE | 1.02 | 2.45 | 0.41 | 0.07 | 174164.98 | 40.86 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.07 | 4710.05 | 21.59 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
