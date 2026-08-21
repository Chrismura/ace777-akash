# Hulk DIGEST — 2026-08-21T19:59:57Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : XRPUSDT, HBARUSDT, QAITUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT
- Watch only : QNTUSDT, FLUIDUSDT, RWAUSDT

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| PYTHUSDT | IDLE | 1.38 | 4.99 | 4.67 | 0.06 | 5448077.07 | 2.14 | skipped_fast |
| XRPUSDT | IDLE | 1.17 | 4.21 | 3.59 | 0.11 | 128814212.05 | 2.19 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.15 | 26.97 | 13.79 | 0.16 | 153880.16 | 15.62 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 2.55 | 11.37 | 9.18 | 0.07 | 481638.75 | 23.8 | skipped_fast |
| CCUSDT | IDLE | 2.03 | 5.44 | 1.56 | 0.07 | 634454.84 | 5.59 | skipped_fast |
| HBARUSDT | IDLE | 1.61 | 3.1 | 2.88 | 0.05 | 793700.45 | 1.31 | skipped_fast |
| CHIPUSDT | IDLE | 1.24 | 4.81 | 4.18 | 0.09 | 513844.01 | 3.11 | skipped_fast |
| WUSDT | IDLE | 2.17 | 3.92 | 3.04 | 0.05 | 363542.41 | 11.8 | skipped_fast |
| BIOUSDT | IDLE | 2.64 | 5.33 | 4.42 | -0.0 | 190090.75 | 3.21 | skipped_fast |
| EDELUSDT | IDLE | 2.44 | 4.29 | 3.9 | -0.05 | 79684.76 | 22.52 | skipped_fast |
| RIZEUSDT | IDLE | 2.25 | 11.27 | 2.99 | 0.02 | 56425.72 | 45.77 | skipped_fast |
| KITEUSDT | IDLE | 1.29 | 4.0 | 3.42 | 0.1 | 61382.87 | 11.29 | skipped_fast |
| RWAINCUSDT | IDLE | 2.23 | 4.3 | 1.11 | 0.04 | 11032.33 | 91.28 | skipped_fast |
| TELUSDT | IDLE | 1.89 | 4.46 | 3.0 | 0.01 | 183671.83 | 32.56 | skipped_fast |
| QAITUSDT | IDLE | 1.65 | 3.0 | 1.98 | -0.01 | 2868.1 | 63.29 | skipped_fast |
| QNTUSDT | IDLE | 1.66 | 3.01 | 2.03 | 0.04 | 59926.75 | 6.28 | skipped_fast |
| RWAUSDT | IDLE | 0.66 | 1.16 | 1.07 | 0.03 | 54278.65 | 8.31 | skipped_fast |
| FLUIDUSDT | IDLE | 0.73 | 1.48 | 1.14 | 0.07 | 4276.39 | 23.87 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
