# Hulk DIGEST — 2026-08-21T20:13:34Z

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
| PYTHUSDT | IDLE | 1.34 | 4.78 | 3.26 | 0.08 | 5479955.9 | 2.12 | skipped_fast |
| XRPUSDT | IDLE | 1.25 | 4.21 | 3.37 | 0.11 | 129047796.71 | 2.19 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.01 | 25.8 | 13.15 | 0.17 | 153968.19 | 27.77 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 2.5 | 10.86 | 6.48 | 0.11 | 477818.43 | 16.16 | skipped_fast |
| CCUSDT | IDLE | 1.49 | 3.91 | 1.75 | 0.07 | 632513.6 | 6.54 | skipped_fast |
| HBARUSDT | IDLE | 1.75 | 3.23 | 2.26 | 0.05 | 795812.53 | 1.31 | skipped_fast |
| CHIPUSDT | IDLE | 1.34 | 4.81 | 3.61 | 0.08 | 512511.44 | 3.1 | skipped_fast |
| WUSDT | IDLE | 2.13 | 3.92 | 2.3 | 0.05 | 367303.72 | 11.7 | skipped_fast |
| BIOUSDT | IDLE | 2.58 | 5.33 | 3.47 | 0.01 | 189954.4 | 6.35 | skipped_fast |
| EDELUSDT | IDLE | 2.52 | 4.41 | 4.23 | -0.05 | 80185.13 | 11.31 | skipped_fast |
| RIZEUSDT | IDLE | 1.91 | 9.71 | 1.65 | 0.02 | 56226.34 | 29.91 | skipped_fast |
| RWAINCUSDT | IDLE | 2.29 | 4.3 | 1.8 | 0.04 | 11178.26 | 37.5 | skipped_fast |
| KITEUSDT | IDLE | 1.26 | 4.0 | 2.7 | 0.1 | 61317.22 | 11.2 | skipped_fast |
| QAITUSDT | IDLE | 1.53 | 3.0 | 0.35 | -0.01 | 2806.14 | 67.05 | skipped_fast |
| TELUSDT | IDLE | 1.43 | 3.39 | 2.22 | 0.01 | 183545.83 | 43.27 | skipped_fast |
| QNTUSDT | IDLE | 1.44 | 2.65 | 1.52 | 0.04 | 59912.75 | 4.68 | skipped_fast |
| RWAUSDT | IDLE | 0.65 | 1.16 | 0.99 | 0.03 | 54399.79 | 8.3 | skipped_fast |
| FLUIDUSDT | IDLE | 0.58 | 1.15 | 1.1 | 0.07 | 4286.4 | 22.28 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
