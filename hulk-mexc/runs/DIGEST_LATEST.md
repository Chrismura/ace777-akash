# Hulk DIGEST — 2026-08-21T21:26:20Z

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
| PYTHUSDT | IDLE | 1.18 | 4.51 | 0.96 | 0.09 | 5626279.71 | 2.07 | skipped_fast |
| XRPUSDT | IDLE | 1.13 | 3.73 | 1.63 | 0.11 | 129015772.01 | 2.88 | skipped_fast |
| ZBCNUSDT | IDLE | 1.96 | 8.19 | 4.03 | 0.1 | 484574.47 | 1.01 | skipped_fast |
| CHIPUSDT | IDLE | 1.89 | 5.61 | 3.91 | 0.06 | 517688.36 | 12.39 | skipped_fast |
| CCUSDT | IDLE | 1.12 | 3.14 | 0.04 | 0.1 | 645192.25 | 5.51 | skipped_fast |
| HBARUSDT | IDLE | 1.56 | 3.04 | 0.51 | 0.07 | 812925.12 | 2.56 | skipped_fast |
| WUSDT | IDLE | 1.95 | 3.83 | 0.44 | 0.07 | 367527.04 | 10.45 | skipped_fast |
| BIOUSDT | IDLE | 2.43 | 5.2 | 2.06 | 0.02 | 186878.9 | 3.14 | skipped_fast |
| REDUSDT | IDLE | 1.34 | 11.01 | 9.2 | 0.17 | 153809.95 | 26.18 | skipped_fast |
| EDELUSDT | IDLE | 2.01 | 4.12 | 2.09 | -0.05 | 82811.73 | 22.47 | skipped_fast |
| RIZEUSDT | IDLE | 1.87 | 9.54 | 1.34 | 0.02 | 56005.96 | 45.77 | skipped_fast |
| RWAINCUSDT | IDLE | 2.27 | 4.3 | 1.64 | 0.03 | 10270.17 | 26.86 | skipped_fast |
| KITEUSDT | IDLE | 1.31 | 4.0 | 1.99 | 0.11 | 61062.07 | 10.18 | skipped_fast |
| QAITUSDT | IDLE | 2.33 | 4.38 | 1.83 | -0.01 | 3754.88 | 151.45 | skipped_fast |
| TELUSDT | IDLE | 1.34 | 3.39 | 0.58 | 0.02 | 178849.22 | 37.24 | skipped_fast |
| QNTUSDT | IDLE | 1.4 | 2.65 | 1.03 | 0.04 | 62227.75 | 1.55 | skipped_fast |
| RWAUSDT | IDLE | 0.63 | 1.17 | 0.58 | 0.03 | 53895.05 | 24.82 | skipped_fast |
| FLUIDUSDT | IDLE | 0.51 | 1.15 | 0.09 | 0.09 | 4171.26 | 18.47 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
