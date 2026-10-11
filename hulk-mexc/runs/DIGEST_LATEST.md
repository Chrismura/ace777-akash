# Hulk DIGEST — 2026-10-11T19:26:32Z

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
| WUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.6 | 23.42 | 0.73 | 0.2 | 2169914.04 | 15.51 | skipped_fast |
| XRPUSDT | IDLE | 1.27 | 2.36 | 1.2 | 0.0 | 14829137.42 | 1.42 | skipped_fast |
| ETHUSDT | IDLE | 1.13 | 2.14 | 0.75 | 0.01 | 212523676.7 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.73 | 1.38 | 0.58 | 0.01 | 154234426.05 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.53 | 2.97 | 0.6 | -0.01 | 826657.56 | 2.57 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.61 | 22.33 | 11.8 | 0.01 | 40603.4 | 33.59 | skipped_fast |
| EDELUSDT | IDLE | 2.76 | 4.96 | 3.79 | -0.02 | 408545.72 | 10.56 | skipped_fast |
| ZBCNUSDT | IDLE | 2.97 | 5.42 | 3.41 | 0.01 | 204342.05 | 31.34 | skipped_fast |
| CHIPUSDT | IDLE | 1.63 | 6.53 | 3.26 | 0.08 | 352616.79 | 11.71 | skipped_fast |
| CCUSDT | IDLE | 1.95 | 4.18 | 0.48 | 0.07 | 327387.61 | 9.43 | skipped_fast |
| QNTUSDT | IDLE | 1.04 | 2.0 | 0.47 | 0.01 | 822003.76 | 1.63 | skipped_fast |
| TELUSDT | IDLE | 3.96 | 7.35 | 4.31 | -0.03 | 161443.11 | 28.88 | skipped_fast |
| REDUSDT | IDLE | 1.86 | 3.58 | 0.98 | 0.01 | 57490.21 | 14.46 | skipped_fast |
| RWAINCUSDT | IDLE | 1.74 | 4.86 | 2.1 | 0.01 | 28430.75 | 4.88 | skipped_fast |
| BIOUSDT | IDLE | 1.21 | 2.26 | 1.09 | 0.02 | 87978.03 | 6.68 | skipped_fast |
| HBARUSDT | IDLE | 1.42 | 2.69 | 0.99 | 0.01 | 286300.0 | 6.44 | skipped_fast |
| KITEUSDT | IDLE | 1.08 | 2.13 | 0.26 | -0.01 | 73443.49 | 8.59 | skipped_fast |
| RWAUSDT | IDLE | 1.74 | 3.21 | 1.75 | 0.02 | 52291.53 | 23.19 | skipped_fast |
| FLUIDUSDT | IDLE | 0.74 | 5.76 | 0.37 | 0.06 | 57755.44 | 22.47 | skipped_fast |
| MNSRYUSDT | IDLE | 0.92 | 1.75 | 0.54 | -0.01 | 30731.58 | 12.27 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
