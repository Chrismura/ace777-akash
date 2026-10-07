# Hulk DIGEST — 2026-10-07T19:09:58Z

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
| QNTUSDT | IDLE | 2.02 | 7.17 | 0.86 | -0.01 | 3409227.22 | 7.91 | skipped_fast |
| XRPUSDT | IDLE | 1.04 | 1.94 | 0.94 | -0.05 | 46802163.45 | 2.1 | skipped_fast |
| ETHUSDT | IDLE | 0.82 | 1.55 | 0.62 | -0.05 | 536181432.82 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.53 | 1.02 | 0.29 | -0.02 | 804568546.65 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.06 | 2.91 | 0.06 | -0.07 | 1039701.72 | 2.76 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 3.65 | 17.62 | 12.75 | -0.15 | 56267.11 | 5.0 | skipped_fast |
| WUSDT | IDLE | 2.72 | 5.75 | 1.39 | -0.01 | 478908.84 | 9.77 | skipped_fast |
| EDELUSDT | IDLE | 1.47 | 7.94 | 5.78 | -0.18 | 523045.22 | 27.38 | skipped_fast |
| CCUSDT | IDLE | 1.37 | 3.04 | 0.85 | -0.07 | 452564.34 | 8.35 | skipped_fast |
| CHIPUSDT | IDLE | 2.28 | 7.66 | 2.17 | -0.02 | 167188.67 | 5.89 | skipped_fast |
| ZBCNUSDT | IDLE | 1.86 | 4.79 | 3.49 | -0.09 | 277599.83 | 23.24 | skipped_fast |
| HBARUSDT | IDLE | 0.98 | 2.16 | 1.4 | -0.08 | 720969.88 | 5.41 | skipped_fast |
| FLUIDUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.61 | 10.61 | 1.94 | 0.06 | 15532.37 | 21.76 | skipped_fast |
| KITEUSDT | IDLE | 1.46 | 2.73 | 1.33 | -0.05 | 64045.56 | 9.71 | skipped_fast |
| BIOUSDT | IDLE | 1.19 | 4.4 | 1.22 | -0.09 | 83008.83 | 6.88 | skipped_fast |
| REDUSDT | IDLE | 1.18 | 2.76 | 1.4 | -0.08 | 56916.77 | 16.0 | skipped_fast |
| RIZEUSDT | IDLE | 1.06 | 2.62 | 1.95 | -0.09 | 57443.5 | 53.4 | skipped_fast |
| TELUSDT | IDLE | 1.16 | 4.78 | 1.3 | 0.09 | 211551.03 | 29.23 | skipped_fast |
| RWAUSDT | IDLE | 0.48 | 0.91 | 0.3 | -0.02 | 52883.02 | 7.51 | skipped_fast |
| MNSRYUSDT | IDLE | 0.68 | 1.29 | 0.51 | -0.02 | 40664.48 | 24.83 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
