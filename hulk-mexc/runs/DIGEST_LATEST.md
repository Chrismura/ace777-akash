# Hulk DIGEST — 2026-08-22T11:55:22Z

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
| PYTHUSDT | IDLE | 2.16 | 9.66 | 6.86 | 0.01 | 51609512.34 | 6.15 | skipped_fast |
| XRPUSDT | IDLE | 2.34 | 14.26 | 8.68 | 0.09 | 216254425.92 | 2.69 | skipped_fast |
| CCUSDT | IDLE | 2.03 | 10.24 | 6.84 | 0.12 | 780836.24 | 7.72 | skipped_fast |
| HBARUSDT | IDLE | 1.46 | 5.26 | 3.33 | 0.02 | 1255187.34 | 10.35 | skipped_fast |
| WUSDT | IDLE | 1.56 | 6.27 | 3.73 | 0.01 | 581731.04 | 13.78 | skipped_fast |
| ZBCNUSDT | IDLE | 2.29 | 5.93 | 4.22 | -0.03 | 382700.44 | 16.99 | skipped_fast |
| CHIPUSDT | IDLE | 0.71 | 4.16 | 1.29 | -0.1 | 617931.57 | 3.34 | skipped_fast |
| KITEUSDT | IDLE | 2.6 | 6.24 | 0.29 | 0.04 | 81713.91 | 12.34 | skipped_fast |
| EDELUSDT | IDLE | 2.75 | 4.93 | 3.82 | -0.04 | 79308.74 | 45.51 | skipped_fast |
| BIOUSDT | IDLE | 0.93 | 6.64 | 2.42 | -0.04 | 241335.76 | 6.45 | skipped_fast |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.65 | 6.75 | 5.46 | -0.03 | 167382.09 | 16.03 | skipped_fast |
| QAITUSDT | IDLE | 2.2 | 4.16 | 1.63 | 0.0 | 2446.18 | 63.29 | skipped_fast |
| REDUSDT | IDLE | 0.47 | 6.02 | 3.77 | 0.03 | 154696.24 | 20.56 | skipped_fast |
| RWAINCUSDT | IDLE | 1.38 | 2.4 | 2.34 | -0.02 | 10327.23 | 76.09 | skipped_fast |
| QNTUSDT | IDLE | 1.07 | 3.47 | 1.68 | 0.0 | 188360.49 | 9.34 | skipped_fast |
| RIZEUSDT | IDLE | 0.66 | 2.89 | 0.84 | -0.03 | 48642.22 | 46.44 | skipped_fast |
| FLUIDUSDT | IDLE | 1.87 | 3.68 | 1.96 | -0.01 | 5711.25 | 22.29 | skipped_fast |
| RWAUSDT | IDLE | 1.0 | 1.8 | 1.37 | 0.01 | 57824.19 | 16.31 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
