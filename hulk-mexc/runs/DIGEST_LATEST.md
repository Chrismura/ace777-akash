# Hulk DIGEST — 2026-09-15T00:44:03Z

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
| ETHUSDT | IDLE | 2.42 | 4.25 | 3.92 | 0.01 | 444060376.31 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 2.12 | 5.34 | 5.01 | 0.05 | 74961611.44 | 2.82 | skipped_fast |
| BTCUSDT | IDLE | 1.2 | 2.09 | 2.05 | 0.01 | 558859236.9 | 0.0 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.72 | 30.63 | 5.48 | 0.33 | 363381.9 | 11.15 | skipped_fast |
| CCUSDT | IDLE | 2.55 | 4.46 | 4.24 | 0.0 | 315000.04 | 7.34 | skipped_fast |
| PYTHUSDT | IDLE | 0.92 | 1.69 | 1.04 | -0.0 | 391035.39 | 3.57 | skipped_fast |
| ZBCNUSDT | IDLE | 1.84 | 3.42 | 1.7 | 0.03 | 199177.73 | 20.18 | skipped_fast |
| WUSDT | IDLE | 1.61 | 2.92 | 2.03 | 0.02 | 208770.89 | 10.95 | skipped_fast |
| KITEUSDT | IDLE | 2.21 | 4.01 | 2.72 | -0.0 | 65339.49 | 12.23 | skipped_fast |
| BIOUSDT | IDLE | 1.48 | 2.6 | 2.46 | 0.02 | 97797.07 | 11.65 | skipped_fast |
| REDUSDT | IDLE | 0.95 | 3.09 | 1.04 | 0.09 | 189216.37 | 16.97 | skipped_fast |
| HBARUSDT | IDLE | 1.35 | 2.48 | 1.51 | 0.04 | 354992.52 | 1.28 | skipped_fast |
| CHIPUSDT | IDLE | 1.16 | 2.25 | 1.09 | 0.01 | 75482.62 | 19.13 | skipped_fast |
| TELUSDT | IDLE | 2.27 | 5.57 | 4.12 | 0.05 | 104775.34 | 54.36 | skipped_fast |
| RWAINCUSDT | IDLE | 0.73 | 1.44 | 0.11 | 0.0 | 5557.17 | 5.48 | skipped_fast |
| RIZEUSDT | IDLE | 0.41 | 4.73 | 2.4 | 0.03 | 55767.03 | 54.07 | skipped_fast |
| FLUIDUSDT | IDLE | 1.36 | 2.37 | 2.31 | 0.02 | 1523.93 | 21.14 | skipped_fast |
| QNTUSDT | IDLE | 0.82 | 1.54 | 0.68 | 0.03 | 43560.24 | 4.66 | skipped_fast |
| RWAUSDT | IDLE | 0.59 | 1.05 | 0.89 | -0.0 | 55163.38 | 14.91 | skipped_fast |
| MNSRYUSDT | IDLE | 0.76 | 1.34 | 1.19 | 0.01 | 31629.21 | 44.22 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
