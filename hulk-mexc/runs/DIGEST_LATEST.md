# Hulk DIGEST — 2026-10-01T01:51:33Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| QNTUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.08 | 10.17 | 0.99 | 0.05 | 10222745.94 | 5.69 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 3.54 | 6.25 | 5.52 | 0.01 | 1357363.76 | 11.55 | skipped_fast |
| ETHUSDT | IDLE | 0.48 | 0.94 | 0.09 | 0.01 | 372723275.73 | 0.07 | skipped_fast |
| XRPUSDT | IDLE | 0.43 | 0.81 | 0.36 | -0.01 | 52570094.22 | 2.01 | skipped_fast |
| BTCUSDT | IDLE | 0.26 | 0.48 | 0.32 | 0.0 | 618212980.69 | 0.0 | skipped_fast |
| CCUSDT | IDLE | 2.6 | 5.01 | 1.26 | 0.01 | 937116.55 | 6.3 | skipped_fast |
| WUSDT | IDLE | 1.81 | 3.33 | 1.9 | -0.02 | 807372.89 | 9.74 | skipped_fast |
| ZBCNUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.39 | 11.29 | 1.17 | 0.09 | 453810.47 | 32.51 | skipped_fast |
| PYTHUSDT | IDLE | 1.29 | 2.35 | 1.55 | -0.06 | 574497.51 | 6.54 | skipped_fast |
| KITEUSDT | IDLE | 1.99 | 4.85 | 0.23 | 0.08 | 78081.64 | 10.31 | skipped_fast |
| BIOUSDT | IDLE | 1.43 | 2.73 | 0.93 | -0.02 | 91524.39 | 6.47 | skipped_fast |
| RWAINCUSDT | IDLE | 1.78 | 3.62 | 3.08 | -0.04 | 10829.32 | 82.63 | skipped_fast |
| EDELUSDT | IDLE | 0.43 | 4.09 | 3.69 | 0.23 | 164384.24 | 32.14 | skipped_fast |
| CHIPUSDT | IDLE | 0.98 | 2.21 | 0.67 | -0.03 | 69865.01 | 13.86 | skipped_fast |
| TELUSDT | IDLE | 1.51 | 4.08 | 3.33 | 0.04 | 238669.4 | 30.18 | skipped_fast |
| REDUSDT | IDLE | 0.68 | 2.99 | 0.28 | 0.11 | 77172.32 | 12.26 | skipped_fast |
| RIZEUSDT | IDLE | 0.83 | 1.85 | 1.47 | 0.06 | 42885.49 | 29.27 | skipped_fast |
| FLUIDUSDT | IDLE | 0.92 | 1.7 | 0.89 | 0.02 | 1227.31 | 21.66 | skipped_fast |
| RWAUSDT | IDLE | 0.35 | 0.66 | 0.29 | -0.0 | 53399.39 | 36.56 | skipped_fast |
| MNSRYUSDT | IDLE | 0.3 | 0.56 | 0.3 | 0.0 | 38115.76 | 36.19 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
