# Hulk DIGEST — 2026-10-07T13:07:58Z

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
| QNTUSDT | IDLE | 2.32 | 6.49 | 4.22 | -0.03 | 2626783.55 | 6.12 | skipped_fast |
| ETHUSDT | IDLE | 1.41 | 2.53 | 1.99 | -0.05 | 556557978.61 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 1.23 | 2.16 | 1.94 | -0.04 | 43130424.48 | 3.46 | skipped_fast |
| BTCUSDT | IDLE | 0.53 | 0.94 | 0.76 | -0.03 | 802296581.6 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.05 | 3.09 | 2.48 | -0.11 | 1058862.24 | 1.4 | skipped_fast |
| WUSDT | IDLE | 2.44 | 4.52 | 3.31 | -0.07 | 469467.8 | 14.43 | skipped_fast |
| ZBCNUSDT | IDLE | 3.3 | 8.67 | 3.74 | -0.03 | 237177.91 | 28.14 | skipped_fast |
| EDELUSDT | IDLE | 1.64 | 8.82 | 6.71 | -0.18 | 567546.73 | 54.31 | skipped_fast |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.41 | 6.14 | 5.49 | -0.06 | 65259.41 | 9.76 | skipped_fast |
| HBARUSDT | IDLE | 1.45 | 2.7 | 2.03 | -0.07 | 688324.75 | 3.19 | skipped_fast |
| CCUSDT | IDLE | 1.09 | 2.53 | 2.11 | -0.07 | 459242.24 | 8.47 | skipped_fast |
| CHIPUSDT | IDLE | 1.7 | 5.35 | 4.23 | -0.05 | 186681.39 | 14.38 | skipped_fast |
| RWAINCUSDT | IDLE | 2.23 | 6.31 | 2.25 | -0.04 | 56189.24 | 13.37 | skipped_fast |
| BIOUSDT | IDLE | 0.96 | 3.6 | 2.96 | -0.1 | 86762.12 | 7.02 | skipped_fast |
| RIZEUSDT | IDLE | 1.08 | 4.32 | 0.06 | 0.03 | 55315.58 | 52.35 | skipped_fast |
| REDUSDT | IDLE | 0.71 | 2.01 | 0.13 | -0.08 | 60500.58 | 8.56 | skipped_fast |
| TELUSDT | IDLE | 1.29 | 4.9 | 4.43 | 0.04 | 197936.79 | 34.92 | skipped_fast |
| RWAUSDT | IDLE | 0.86 | 1.51 | 1.34 | -0.03 | 52809.8 | 22.62 | skipped_fast |
| FLUIDUSDT | IDLE | 0.6 | 1.74 | 1.09 | -0.08 | 31306.69 | 21.79 | skipped_fast |
| MNSRYUSDT | IDLE | 0.37 | 0.65 | 0.56 | -0.01 | 39066.76 | 36.5 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
