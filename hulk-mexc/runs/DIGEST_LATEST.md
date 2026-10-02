# Hulk DIGEST — 2026-10-02T21:45:14Z

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
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 3.19 | 11.86 | 10.36 | -0.09 | 4904288.56 | 7.53 | skipped_fast |
| XRPUSDT | IDLE | 2.32 | 4.28 | 2.44 | -0.01 | 66716005.9 | 2.71 | skipped_fast |
| ETHUSDT | IDLE | 1.1 | 1.97 | 1.56 | -0.01 | 545383851.04 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 1.04 | 1.91 | 1.16 | 0.0 | 911054481.74 | 0.0 | skipped_fast |
| EDELUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.42 | 31.13 | 1.12 | 0.28 | 707780.93 | 26.45 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.49 | 10.9 | 9.06 | -0.01 | 490467.55 | 9.97 | skipped_fast |
| HBARUSDT | IDLE | 3.14 | 7.85 | 3.85 | -0.02 | 993559.93 | 6.98 | skipped_fast |
| PYTHUSDT | IDLE | 3.29 | 7.23 | 3.27 | 0.04 | 557974.52 | 7.77 | skipped_fast |
| CCUSDT | IDLE | 3.03 | 6.56 | 4.07 | -0.01 | 532793.13 | 6.75 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.09 | 7.45 | 6.23 | 0.01 | 90349.22 | 18.74 | skipped_fast |
| RIZEUSDT | IDLE | 4.07 | 20.43 | 2.53 | 0.01 | 47178.59 | 90.6 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 3.36 | 7.81 | 5.8 | 0.0 | 100730.65 | 6.69 | skipped_fast |
| KITEUSDT | IDLE | 3.15 | 5.71 | 3.97 | -0.02 | 79618.09 | 5.48 | skipped_fast |
| REDUSDT | IDLE | 1.89 | 8.56 | 6.93 | -0.08 | 117030.36 | 7.99 | skipped_fast |
| ZBCNUSDT | IDLE | 1.67 | 4.65 | 3.95 | -0.02 | 238269.38 | 31.7 | skipped_fast |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.14 | 8.99 | 7.4 | -0.09 | 149068.7 | 35.71 | skipped_fast |
| RWAINCUSDT | IDLE | 2.18 | 6.29 | 2.51 | -0.02 | 6351.15 | 59.17 | skipped_fast |
| FLUIDUSDT | IDLE | 1.5 | 3.74 | 2.3 | 0.06 | 6215.75 | 21.61 | skipped_fast |
| RWAUSDT | IDLE | 0.87 | 1.54 | 1.3 | -0.01 | 54824.36 | 7.31 | skipped_fast |
| MNSRYUSDT | IDLE | 0.55 | 1.04 | 0.38 | 0.01 | 40420.92 | 34.85 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
