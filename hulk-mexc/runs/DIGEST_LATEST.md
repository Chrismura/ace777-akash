# Hulk DIGEST — 2026-09-11T15:16:51Z

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
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.61 | 130.41 | 30.65 | 0.4 | 145735.42 | 86.52 | skipped_fast |
| XRPUSDT | IDLE | 4.21 | 8.82 | 3.17 | 0.02 | 50936291.42 | 2.88 | skipped_fast |
| ETHUSDT | IDLE | 4.07 | 9.44 | 2.13 | 0.07 | 568208653.46 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 2.58 | 4.93 | 1.51 | 0.02 | 527759008.96 | 0.0 | skipped_fast |
| CCUSDT | IDLE | 4.01 | 7.68 | 2.33 | -0.01 | 476954.16 | 7.02 | skipped_fast |
| PYTHUSDT | IDLE | 3.95 | 7.72 | 1.15 | 0.02 | 370925.09 | 3.76 | skipped_fast |
| EDELUSDT | IDLE | 4.06 | 7.66 | 3.11 | -0.01 | 195297.21 | 18.33 | skipped_fast |
| WUSDT | IMPULSE_WAIT — spike en cours, pas chase | 4.02 | 8.01 | 0.25 | 0.04 | 170569.89 | 22.05 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 4.08 | 8.51 | 6.13 | 0.02 | 10075.6 | 38.73 | skipped_fast |
| REDUSDT | IDLE | 3.83 | 7.46 | 1.4 | 0.02 | 61229.25 | 19.11 | skipped_fast |
| BIOUSDT | IDLE | 3.32 | 6.49 | 1.0 | 0.02 | 81117.57 | 3.9 | skipped_fast |
| ZBCNUSDT | IDLE | 2.88 | 5.61 | 1.0 | 0.02 | 175529.89 | 10.1 | skipped_fast |
| CHIPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.85 | 9.31 | 0.04 | 0.03 | 138180.59 | 14.35 | skipped_fast |
| TELUSDT | IDLE | 4.19 | 8.79 | 2.86 | 0.01 | 103612.62 | 38.86 | skipped_fast |
| KITEUSDT | IDLE | 2.08 | 4.0 | 1.01 | 0.01 | 59534.05 | 12.76 | skipped_fast |
| HBARUSDT | IDLE | 2.61 | 5.04 | 1.14 | 0.01 | 207235.81 | 1.31 | skipped_fast |
| QNTUSDT | IDLE | 2.78 | 5.19 | 2.46 | -0.0 | 40923.88 | 6.12 | skipped_fast |
| FLUIDUSDT | IDLE | 2.47 | 4.94 | 0.0 | 0.03 | 1301.56 | 23.77 | skipped_fast |
| RWAUSDT | IDLE | 1.63 | 3.2 | 0.44 | 0.02 | 51141.65 | 14.85 | skipped_fast |
| MNSRYUSDT | IDLE | 1.63 | 3.1 | 1.04 | 0.02 | 38353.01 | 60.64 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
