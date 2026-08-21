# Hulk DIGEST — 2026-08-21T19:59:20Z

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
| PYTHUSDT | IDLE | 1.37 | 4.99 | 4.35 | 0.06 | 5446482.6 | 2.13 | skipped_fast |
| XRPUSDT | IDLE | 1.18 | 4.21 | 3.85 | 0.12 | 128903473.72 | 2.93 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.15 | 26.97 | 13.78 | 0.16 | 153954.24 | 25.51 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 2.55 | 11.37 | 9.19 | 0.07 | 481676.78 | 31.06 | skipped_fast |
| CCUSDT | IDLE | 2.04 | 5.44 | 1.83 | 0.07 | 634395.86 | 6.54 | skipped_fast |
| HBARUSDT | IDLE | 1.62 | 3.1 | 2.95 | 0.05 | 793745.56 | 1.31 | skipped_fast |
| CHIPUSDT | IDLE | 1.24 | 4.81 | 4.18 | 0.09 | 513965.77 | 3.11 | skipped_fast |
| WUSDT | IDLE | 2.16 | 3.92 | 2.95 | 0.05 | 363525.78 | 10.72 | skipped_fast |
| BIOUSDT | IDLE | 2.65 | 5.33 | 4.51 | -0.0 | 190573.01 | 9.64 | skipped_fast |
| EDELUSDT | IDLE | 2.44 | 4.29 | 3.9 | -0.04 | 79659.76 | 22.52 | skipped_fast |
| RIZEUSDT | IDLE | 2.25 | 11.27 | 2.99 | 0.02 | 56425.13 | 45.77 | skipped_fast |
| RWAINCUSDT | IDLE | 2.23 | 4.3 | 1.11 | 0.04 | 11032.33 | 69.72 | skipped_fast |
| TELUSDT | IDLE | 1.89 | 4.46 | 3.11 | 0.0 | 183654.99 | 37.97 | skipped_fast |
| QAITUSDT | IDLE | 1.65 | 3.0 | 1.98 | -0.01 | 2868.1 | 63.29 | skipped_fast |
| KITEUSDT | IDLE | 1.29 | 4.0 | 3.44 | 0.1 | 61378.42 | 123.17 | skipped_fast |
| QNTUSDT | IDLE | 1.66 | 3.01 | 2.03 | 0.04 | 59935.96 | 4.71 | skipped_fast |
| RWAUSDT | IDLE | 0.66 | 1.16 | 1.07 | 0.03 | 54283.0 | 8.31 | skipped_fast |
| FLUIDUSDT | IDLE | 0.73 | 1.48 | 1.14 | 0.07 | 4276.39 | 22.42 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
