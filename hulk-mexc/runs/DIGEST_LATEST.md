# Hulk DIGEST — 2026-10-11T18:25:39Z

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
| WUSDT | IDLE | 3.72 | 16.04 | 4.03 | 0.09 | 1353969.48 | 18.74 | skipped_fast |
| XRPUSDT | IDLE | 1.25 | 2.38 | 0.76 | 0.01 | 14195500.15 | 2.12 | skipped_fast |
| ETHUSDT | IDLE | 1.11 | 2.14 | 0.54 | 0.01 | 212488733.4 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.72 | 1.38 | 0.37 | 0.01 | 151902828.93 | 0.0 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.62 | 23.17 | 6.33 | 0.07 | 38674.95 | 31.61 | skipped_fast |
| PYTHUSDT | IDLE | 1.31 | 2.51 | 0.77 | -0.02 | 792693.63 | 1.29 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 4.33 | 11.9 | 6.7 | 0.01 | 28075.2 | 53.41 | skipped_fast |
| CHIPUSDT | IDLE | 2.25 | 9.0 | 4.36 | 0.11 | 382189.57 | 16.26 | skipped_fast |
| ZBCNUSDT | IDLE | 2.82 | 5.42 | 1.43 | 0.03 | 197980.63 | 2.55 | skipped_fast |
| EDELUSDT | IDLE | 1.97 | 3.5 | 2.95 | -0.01 | 408709.45 | 18.32 | skipped_fast |
| QNTUSDT | IDLE | 1.08 | 2.06 | 0.62 | 0.02 | 828289.06 | 1.23 | skipped_fast |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 4.03 | 7.23 | 5.47 | -0.04 | 154351.6 | 35.09 | skipped_fast |
| CCUSDT | IDLE | 1.82 | 3.67 | 0.37 | 0.07 | 314811.33 | 8.68 | skipped_fast |
| REDUSDT | IDLE | 1.83 | 3.58 | 0.56 | 0.01 | 58043.46 | 15.06 | skipped_fast |
| BIOUSDT | IDLE | 1.17 | 2.3 | 0.23 | 0.04 | 86321.73 | 3.32 | skipped_fast |
| KITEUSDT | IDLE | 1.09 | 2.17 | 0.1 | -0.02 | 72637.65 | 7.8 | skipped_fast |
| HBARUSDT | IDLE | 1.43 | 2.7 | 1.01 | 0.01 | 252259.33 | 5.37 | skipped_fast |
| RWAUSDT | IDLE | 1.09 | 2.13 | 0.39 | 0.01 | 50916.82 | 15.53 | skipped_fast |
| FLUIDUSDT | IDLE | 0.75 | 5.76 | 0.99 | 0.08 | 55740.94 | 21.67 | skipped_fast |
| MNSRYUSDT | IDLE | 0.91 | 1.75 | 0.47 | -0.01 | 30800.93 | 8.17 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
