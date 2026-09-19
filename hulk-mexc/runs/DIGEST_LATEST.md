# Hulk DIGEST — 2026-09-19T16:58:50Z

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
| XRPUSDT | IDLE | 1.34 | 2.5 | 1.17 | 0.04 | 60652850.37 | 0.7 | skipped_fast |
| BTCUSDT | IDLE | 0.46 | 0.91 | 0.09 | 0.01 | 511907422.23 | 0.0 | skipped_fast |
| ETHUSDT | IDLE | 0.46 | 0.9 | 0.07 | 0.02 | 367778970.75 | 0.04 | skipped_fast |
| WUSDT | IDLE | 2.62 | 4.86 | 2.56 | 0.02 | 665945.81 | 2.7 | skipped_fast |
| ZBCNUSDT | IDLE | 3.73 | 15.2 | 2.52 | 0.13 | 223912.58 | 44.01 | skipped_fast |
| PYTHUSDT | IDLE | 1.13 | 2.14 | 0.79 | 0.01 | 676414.95 | 1.65 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 4.39 | 9.89 | 6.28 | -0.03 | 5773.78 | 84.44 | skipped_fast |
| BIOUSDT | IDLE | 2.86 | 5.34 | 2.53 | 0.04 | 84669.45 | 10.68 | skipped_fast |
| CCUSDT | IDLE | 1.61 | 3.14 | 0.59 | 0.04 | 355388.27 | 7.96 | skipped_fast |
| CHIPUSDT | IDLE | 2.34 | 5.65 | 4.43 | 0.0 | 127416.91 | 18.23 | skipped_fast |
| HBARUSDT | IDLE | 1.19 | 2.37 | 0.07 | 0.05 | 528474.39 | 1.22 | skipped_fast |
| EDELUSDT | IDLE | 1.17 | 6.78 | 3.57 | -0.15 | 171862.4 | 33.5 | skipped_fast |
| KITEUSDT | IDLE | 1.09 | 2.05 | 0.82 | 0.06 | 70913.83 | 13.76 | skipped_fast |
| RIZEUSDT | IDLE | 1.51 | 6.49 | 5.52 | 0.05 | 38374.95 | 99.13 | skipped_fast |
| REDUSDT | IDLE | 0.63 | 2.7 | 2.05 | 0.01 | 133536.63 | 14.92 | skipped_fast |
| TELUSDT | IDLE | 1.36 | 4.13 | 2.43 | -0.01 | 128461.36 | 32.56 | skipped_fast |
| QNTUSDT | IDLE | 1.12 | 2.1 | 0.92 | 0.03 | 47205.41 | 4.59 | skipped_fast |
| RWAUSDT | IDLE | 0.82 | 1.55 | 0.66 | 0.0 | 54122.83 | 7.32 | skipped_fast |
| FLUIDUSDT | IDLE | 1.04 | 3.11 | 0.0 | 0.12 | 9838.49 | 23.65 | skipped_fast |
| MNSRYUSDT | IDLE | 0.83 | 1.52 | 0.94 | 0.0 | 36465.12 | 62.32 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
