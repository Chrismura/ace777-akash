# Hulk DIGEST — 2026-08-22T12:06:16Z

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
| PYTHUSDT | IDLE | 1.74 | 7.83 | 5.15 | 0.01 | 51609315.63 | 2.05 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 2.51 | 14.26 | 7.96 | 0.11 | 215473879.7 | 4.01 | skipped_fast |
| HBARUSDT | IDLE | 1.28 | 4.63 | 2.74 | 0.02 | 1252998.31 | 6.46 | skipped_fast |
| CCUSDT | IDLE | 1.64 | 8.38 | 5.04 | 0.13 | 775457.72 | 5.99 | skipped_fast |
| WUSDT | IDLE | 1.56 | 6.27 | 3.72 | 0.02 | 579627.63 | 10.59 | skipped_fast |
| ZBCNUSDT | IDLE | 2.27 | 5.77 | 4.96 | -0.04 | 380890.04 | 30.64 | skipped_fast |
| CHIPUSDT | IDLE | 0.71 | 4.16 | 1.29 | -0.09 | 618755.88 | 3.35 | skipped_fast |
| KITEUSDT | IDLE | 2.59 | 6.24 | 0.16 | 0.05 | 82604.31 | 19.41 | skipped_fast |
| EDELUSDT | IDLE | 2.18 | 3.89 | 3.09 | -0.04 | 78185.86 | 22.78 | skipped_fast |
| BIOUSDT | IDLE | 0.79 | 5.65 | 1.86 | -0.02 | 240867.35 | 3.2 | skipped_fast |
| QAITUSDT | IDLE | 2.2 | 4.16 | 1.63 | -0.0 | 2385.65 | 63.29 | skipped_fast |
| REDUSDT | IDLE | 0.46 | 6.02 | 2.84 | 0.03 | 153545.65 | 11.57 | skipped_fast |
| TELUSDT | IDLE | 2.2 | 5.61 | 4.5 | -0.03 | 165007.56 | 48.01 | skipped_fast |
| RWAINCUSDT | IDLE | 1.38 | 2.4 | 2.34 | -0.0 | 10250.54 | 70.63 | skipped_fast |
| QNTUSDT | IDLE | 1.07 | 3.47 | 1.59 | 0.01 | 188362.53 | 7.78 | skipped_fast |
| RIZEUSDT | IDLE | 0.49 | 1.91 | 1.01 | -0.05 | 47921.01 | 46.44 | skipped_fast |
| RWAUSDT | IDLE | 1.0 | 1.8 | 1.37 | 0.01 | 57855.86 | 24.46 | skipped_fast |
| FLUIDUSDT | IDLE | 1.01 | 1.93 | 1.38 | -0.01 | 5711.25 | 14.85 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
