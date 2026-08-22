# Hulk DIGEST — 2026-08-22T03:21:31Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.4 | 10.96 | 0.78 | 0.17 | 7702498.77 | 1.88 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.37 | 12.88 | 0.13 | 0.22 | 162151026.68 | 6.97 | skipped_fast |
| HBARUSDT | IDLE | 2.26 | 6.02 | 0.04 | 0.11 | 1007144.17 | 1.21 | skipped_fast |
| CCUSDT | IDLE | 1.97 | 8.96 | 1.49 | 0.17 | 680872.32 | 6.79 | skipped_fast |
| BIOUSDT | IDLE | 3.02 | 7.36 | 2.43 | 0.07 | 197615.25 | 3.01 | skipped_fast |
| CHIPUSDT | IDLE | 1.93 | 4.28 | 0.3 | -0.01 | 450761.33 | 2.98 | skipped_fast |
| ZBCNUSDT | IDLE | 1.43 | 5.16 | 1.85 | 0.12 | 538984.92 | 17.25 | skipped_fast |
| WUSDT | IDLE | 1.77 | 5.61 | 0.2 | 0.13 | 416755.96 | 10.86 | skipped_fast |
| EDELUSDT | IDLE | 1.96 | 3.83 | 3.37 | -0.03 | 79996.06 | 22.45 | skipped_fast |
| RIZEUSDT | IDLE | 1.82 | 7.71 | 4.33 | 0.1 | 59527.1 | 44.22 | skipped_fast |
| REDUSDT | IDLE | 0.92 | 7.96 | 3.55 | 0.2 | 157916.87 | 10.24 | skipped_fast |
| RWAINCUSDT | IDLE | 1.94 | 3.44 | 3.0 | 0.01 | 9365.24 | 21.62 | skipped_fast |
| KITEUSDT | IDLE | 1.39 | 4.4 | 0.42 | 0.12 | 68211.58 | 11.66 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | 0.0 | 3808.79 | 63.67 | skipped_fast |
| QNTUSDT | IDLE | 1.69 | 4.0 | 0.0 | 0.09 | 174171.15 | 5.94 | skipped_fast |
| TELUSDT | IDLE | 0.94 | 2.19 | 0.82 | 0.06 | 173353.69 | 10.28 | skipped_fast |
| RWAUSDT | IDLE | 1.29 | 2.56 | 0.16 | 0.05 | 56254.41 | 16.13 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.07 | 4710.05 | 19.51 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
