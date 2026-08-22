# Hulk DIGEST — 2026-08-22T02:21:52Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.38 | 8.42 | 0.19 | 0.14 | 6950114.4 | 3.87 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.31 | 10.26 | 0.39 | 0.17 | 154368776.5 | 3.32 | skipped_fast |
| HBARUSDT | IDLE | 2.28 | 4.9 | 0.02 | 0.08 | 961808.99 | 1.24 | skipped_fast |
| ZBCNUSDT | IDLE | 2.49 | 9.63 | 2.8 | 0.09 | 544224.12 | 17.91 | skipped_fast |
| CCUSDT | IDLE | 1.69 | 6.26 | 0.13 | 0.14 | 656271.52 | 2.61 | skipped_fast |
| CHIPUSDT | IDLE | 2.22 | 5.07 | 0.45 | -0.01 | 505374.62 | 3.02 | skipped_fast |
| BIOUSDT | IDLE | 3.09 | 7.64 | 0.74 | 0.09 | 192670.71 | 14.83 | skipped_fast |
| WUSDT | IDLE | 1.82 | 4.92 | 0.0 | 0.1 | 401224.25 | 12.03 | skipped_fast |
| EDELUSDT | IDLE | 2.43 | 5.02 | 2.39 | -0.03 | 79693.92 | 33.43 | skipped_fast |
| RIZEUSDT | IDLE | 1.98 | 8.52 | 3.93 | 0.11 | 61288.73 | 15.21 | skipped_fast |
| REDUSDT | IDLE | 1.01 | 8.27 | 6.93 | 0.17 | 157080.67 | 9.78 | skipped_fast |
| QNTUSDT | IDLE | 2.24 | 4.89 | 0.3 | 0.07 | 171119.24 | 4.49 | skipped_fast |
| RWAINCUSDT | IDLE | 1.82 | 3.27 | 2.48 | 0.0 | 9379.52 | 32.54 | skipped_fast |
| KITEUSDT | IDLE | 1.35 | 4.09 | 0.79 | 0.12 | 61686.82 | 10.82 | skipped_fast |
| QAITUSDT | IDLE | 1.86 | 3.57 | 0.94 | 0.0 | 3916.13 | 39.49 | skipped_fast |
| TELUSDT | IDLE | 2.15 | 5.11 | 1.13 | 0.04 | 179452.9 | 25.86 | skipped_fast |
| FLUIDUSDT | IDLE | 1.44 | 3.69 | 2.03 | 0.07 | 4710.05 | 18.99 | skipped_fast |
| RWAUSDT | IDLE | 1.06 | 2.08 | 0.24 | 0.04 | 54795.17 | 16.37 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
