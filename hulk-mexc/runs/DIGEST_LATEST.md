# Hulk DIGEST — 2026-08-21T21:53:07Z

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
| PYTHUSDT | IDLE | 1.16 | 4.51 | 0.23 | 0.1 | 5674713.39 | 4.12 | skipped_fast |
| XRPUSDT | IDLE | 1.08 | 3.73 | 0.43 | 0.11 | 129976101.28 | 3.55 | skipped_fast |
| CHIPUSDT | IDLE | 1.87 | 5.61 | 3.4 | 0.05 | 527368.47 | 3.08 | skipped_fast |
| HBARUSDT | IDLE | 2.04 | 4.62 | 0.0 | 0.08 | 827378.45 | 1.26 | skipped_fast |
| ZBCNUSDT | IDLE | 1.92 | 8.19 | 2.75 | 0.11 | 491638.36 | 37.79 | skipped_fast |
| CCUSDT | IDLE | 1.31 | 3.89 | 0.28 | 0.1 | 635666.04 | 8.22 | skipped_fast |
| WUSDT | IDLE | 2.1 | 4.19 | 0.05 | 0.07 | 368794.73 | 19.71 | skipped_fast |
| BIOUSDT | IDLE | 2.38 | 5.2 | 1.32 | 0.03 | 187302.91 | 9.34 | skipped_fast |
| REDUSDT | IDLE | 1.34 | 11.01 | 8.79 | 0.18 | 154018.28 | 8.95 | skipped_fast |
| RWAINCUSDT | IDLE | 2.22 | 4.3 | 0.95 | 0.02 | 10222.59 | 10.66 | skipped_fast |
| RIZEUSDT | IDLE | 1.86 | 9.54 | 0.92 | 0.04 | 55825.62 | 47.31 | skipped_fast |
| EDELUSDT | IDLE | 1.89 | 4.12 | 0.44 | -0.03 | 83609.15 | 33.17 | skipped_fast |
| QAITUSDT | IDLE | 2.37 | 4.38 | 2.37 | -0.02 | 3827.91 | 59.7 | skipped_fast |
| KITEUSDT | IDLE | 1.26 | 4.0 | 1.03 | 0.11 | 61237.35 | 11.01 | skipped_fast |
| TELUSDT | IDLE | 2.06 | 5.25 | 0.73 | 0.03 | 185729.74 | 57.49 | skipped_fast |
| QNTUSDT | IDLE | 1.34 | 2.65 | 0.22 | 0.05 | 62607.57 | 13.87 | skipped_fast |
| RWAUSDT | IDLE | 0.6 | 1.17 | 0.16 | 0.04 | 54113.69 | 16.49 | skipped_fast |
| FLUIDUSDT | IDLE | 0.51 | 1.15 | 0.09 | 0.09 | 4171.26 | 21.87 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
