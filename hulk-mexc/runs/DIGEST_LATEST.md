# Hulk DIGEST — 2026-08-21T19:49:10Z

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
| PYTHUSDT | IDLE | 1.36 | 4.99 | 4.04 | 0.07 | 5427106.67 | 2.13 | skipped_fast |
| XRPUSDT | IDLE | 1.16 | 4.21 | 3.45 | 0.11 | 129031500.42 | 2.19 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.15 | 26.97 | 13.61 | 0.16 | 152974.46 | 9.01 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 2.56 | 11.37 | 9.45 | 0.06 | 482366.95 | 27.51 | skipped_fast |
| CCUSDT | IDLE | 2.04 | 5.44 | 1.8 | 0.07 | 631119.36 | 5.61 | skipped_fast |
| HBARUSDT | IDLE | 1.61 | 3.08 | 2.92 | 0.05 | 791593.58 | 1.31 | skipped_fast |
| CHIPUSDT | IDLE | 1.24 | 4.81 | 4.09 | 0.09 | 514496.7 | 3.11 | skipped_fast |
| WUSDT | IDLE | 2.15 | 3.92 | 2.85 | 0.05 | 360758.47 | 14.97 | skipped_fast |
| BIOUSDT | IDLE | 2.65 | 5.33 | 4.57 | -0.0 | 190294.62 | 3.21 | skipped_fast |
| EDELUSDT | IDLE | 2.43 | 4.29 | 3.79 | -0.04 | 79576.3 | 22.52 | skipped_fast |
| RIZEUSDT | IDLE | 2.25 | 11.27 | 2.94 | 0.01 | 56477.45 | 45.77 | skipped_fast |
| RWAINCUSDT | IDLE | 2.23 | 4.3 | 1.11 | 0.04 | 11032.33 | 64.34 | skipped_fast |
| KITEUSDT | IDLE | 1.29 | 4.0 | 3.41 | 0.09 | 61051.07 | 11.29 | skipped_fast |
| QAITUSDT | IDLE | 1.65 | 3.0 | 1.98 | -0.01 | 2917.53 | 63.29 | skipped_fast |
| TELUSDT | IDLE | 1.84 | 4.46 | 2.11 | 0.02 | 183333.75 | 37.69 | skipped_fast |
| QNTUSDT | IDLE | 1.66 | 3.01 | 2.04 | 0.04 | 59858.76 | 7.85 | skipped_fast |
| RWAUSDT | IDLE | 0.64 | 1.16 | 0.82 | 0.04 | 54417.91 | 24.89 | skipped_fast |
| FLUIDUSDT | IDLE | 0.73 | 1.48 | 1.14 | 0.07 | 4331.26 | 22.43 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
