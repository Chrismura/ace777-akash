# Hulk DIGEST — 2026-08-22T02:47:57Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.61 | 11.02 | 0.21 | 0.17 | 7253364.29 | 1.89 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.47 | 12.45 | 0.2 | 0.19 | 157376610.08 | 3.24 | skipped_fast |
| HBARUSDT | IDLE | 2.49 | 6.12 | 0.09 | 0.1 | 982635.81 | 2.45 | skipped_fast |
| CCUSDT | IDLE | 1.95 | 8.33 | 0.0 | 0.16 | 657682.01 | 7.68 | skipped_fast |
| ZBCNUSDT | IDLE | 2.47 | 9.63 | 2.24 | 0.1 | 539338.59 | 37.06 | skipped_fast |
| CHIPUSDT | IDLE | 2.34 | 5.39 | 0.15 | -0.02 | 454121.97 | 5.98 | skipped_fast |
| BIOUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.2 | 8.18 | 1.99 | 0.09 | 193189.9 | 5.97 | skipped_fast |
| WUSDT | IDLE | 1.98 | 5.85 | 0.13 | 0.11 | 415021.4 | 10.95 | skipped_fast |
| EDELUSDT | IDLE | 2.46 | 5.02 | 2.82 | -0.03 | 79887.94 | 55.71 | skipped_fast |
| RIZEUSDT | IDLE | 1.99 | 8.52 | 4.34 | 0.1 | 61352.04 | 44.22 | skipped_fast |
| REDUSDT | IDLE | 0.98 | 8.27 | 4.95 | 0.19 | 157953.72 | 19.17 | skipped_fast |
| RWAINCUSDT | IDLE | 1.83 | 3.27 | 2.58 | 0.02 | 9400.35 | 10.86 | skipped_fast |
| QNTUSDT | IDLE | 2.34 | 5.48 | 0.25 | 0.08 | 172543.72 | 5.96 | skipped_fast |
| KITEUSDT | IDLE | 1.33 | 4.09 | 0.22 | 0.12 | 62406.13 | 14.36 | skipped_fast |
| QAITUSDT | IDLE | 1.88 | 3.57 | 1.22 | 0.0 | 3930.15 | 63.67 | skipped_fast |
| TELUSDT | IDLE | 2.14 | 5.11 | 0.97 | 0.06 | 174243.88 | 56.8 | skipped_fast |
| RWAUSDT | IDLE | 1.44 | 2.83 | 0.32 | 0.05 | 55883.82 | 8.13 | skipped_fast |
| FLUIDUSDT | IDLE | 1.44 | 3.69 | 2.03 | 0.07 | 4710.05 | 19.7 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
