# Hulk DIGEST — 2026-08-28T09:07:24Z

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
| PYTHUSDT | IDLE | 1.43 | 2.57 | 1.9 | -0.02 | 7138132.54 | 2.06 | skipped_fast |
| QAITUSDT | WATCH_PULLBACK — tension haute + reflux | 4.35 | 55.46 | 32.26 | -0.18 | 46975.82 | 70.46 | skipped_fast |
| XRPUSDT | IDLE | 0.8 | 1.43 | 1.14 | -0.01 | 51962611.75 | 2.12 | skipped_fast |
| CHIPUSDT | IDLE | 1.45 | 7.33 | 0.29 | 0.12 | 677375.93 | 2.45 | skipped_fast |
| REDUSDT | IDLE | 3.18 | 5.62 | 4.99 | -0.04 | 81660.01 | 10.33 | skipped_fast |
| CCUSDT | IDLE | 1.51 | 2.69 | 2.14 | -0.05 | 475679.12 | 8.09 | skipped_fast |
| KITEUSDT | IDLE | 2.11 | 3.8 | 2.74 | -0.03 | 74307.51 | 9.41 | skipped_fast |
| WUSDT | IDLE | 1.06 | 1.91 | 1.37 | -0.02 | 197751.3 | 13.85 | skipped_fast |
| RIZEUSDT | IDLE | 0.91 | 10.92 | 5.04 | -0.17 | 113426.72 | 55.4 | skipped_fast |
| ZBCNUSDT | IDLE | 0.62 | 1.52 | 1.27 | 0.0 | 238391.7 | 14.98 | skipped_fast |
| BIOUSDT | IDLE | 0.73 | 1.34 | 0.77 | -0.01 | 92566.7 | 7.02 | skipped_fast |
| HBARUSDT | IDLE | 0.83 | 1.51 | 0.99 | -0.01 | 334391.29 | 1.29 | skipped_fast |
| TELUSDT | IDLE | 1.63 | 2.85 | 2.71 | -0.01 | 136563.18 | 32.8 | skipped_fast |
| EDELUSDT | IDLE | 0.42 | 2.61 | 1.61 | 0.07 | 49065.8 | 25.94 | skipped_fast |
| RWAINCUSDT | IDLE | 1.39 | 4.28 | 4.1 | -0.04 | 20583.26 | 165.56 | skipped_fast |
| FLUIDUSDT | IDLE | 1.43 | 2.68 | 1.16 | -0.02 | 3232.61 | 21.99 | skipped_fast |
| QNTUSDT | IDLE | 0.67 | 1.26 | 0.54 | -0.01 | 43336.36 | 3.21 | skipped_fast |
| RWAUSDT | IDLE | 0.37 | 0.66 | 0.5 | 0.01 | 53953.02 | 16.58 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
