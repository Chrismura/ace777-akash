# Hulk DIGEST — 2026-10-06T04:40:16Z

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
| QNTUSDT | IDLE | 2.42 | 4.52 | 3.43 | 0.05 | 2823953.7 | 3.46 | skipped_fast |
| BTCUSDT | IDLE | 0.85 | 1.62 | 0.59 | 0.0 | 577847825.35 | 0.0 | skipped_fast |
| XRPUSDT | IDLE | 0.77 | 1.41 | 0.92 | 0.0 | 29597884.93 | 0.67 | skipped_fast |
| ETHUSDT | IDLE | 0.59 | 1.08 | 0.68 | 0.0 | 327603520.09 | 0.41 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.94 | 35.82 | 18.92 | 0.17 | 102968.79 | 48.16 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.75 | 8.26 | 5.51 | 0.01 | 340899.75 | 10.02 | skipped_fast |
| PYTHUSDT | IDLE | 2.4 | 4.34 | 3.04 | 0.01 | 592311.88 | 1.29 | skipped_fast |
| WUSDT | IDLE | 3.22 | 5.78 | 4.36 | -0.02 | 385984.44 | 9.95 | skipped_fast |
| ZBCNUSDT | IDLE | 2.46 | 4.34 | 3.81 | 0.0 | 294401.72 | 11.82 | skipped_fast |
| CCUSDT | IDLE | 1.04 | 1.89 | 1.3 | -0.0 | 463161.07 | 7.92 | skipped_fast |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 2.66 | 16.47 | 12.31 | 0.1 | 95401.09 | 19.24 | skipped_fast |
| BIOUSDT | IDLE | 1.89 | 5.0 | 3.77 | 0.03 | 113231.38 | 3.21 | skipped_fast |
| CHIPUSDT | IDLE | 1.93 | 6.94 | 2.0 | 0.12 | 121339.35 | 18.42 | skipped_fast |
| REDUSDT | IDLE | 2.23 | 3.92 | 3.65 | -0.04 | 65392.6 | 7.83 | skipped_fast |
| HBARUSDT | IDLE | 1.01 | 1.78 | 1.58 | -0.02 | 425502.01 | 5.95 | skipped_fast |
| KITEUSDT | IDLE | 1.11 | 2.0 | 1.45 | -0.02 | 67987.17 | 10.76 | skipped_fast |
| RWAINCUSDT | IDLE | 1.48 | 3.28 | 2.97 | -0.03 | 18357.49 | 59.22 | skipped_fast |
| TELUSDT | IDLE | 1.99 | 3.53 | 3.05 | -0.05 | 131610.97 | 31.98 | skipped_fast |
| MNSRYUSDT | IDLE | 0.39 | 0.68 | 0.64 | 0.0 | 45336.34 | 5.15 | skipped_fast |
| RWAUSDT | IDLE | 0.27 | 0.52 | 0.15 | -0.01 | 51250.78 | 14.7 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
