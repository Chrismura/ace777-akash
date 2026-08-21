# Hulk DIGEST — 2026-08-21T23:56:20Z

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
| PYTHUSDT | IDLE | 1.77 | 6.39 | 1.67 | 0.1 | 6219441.47 | 2.05 | skipped_fast |
| XRPUSDT | IDLE | 1.98 | 8.23 | 1.64 | 0.14 | 142028913.41 | 1.38 | skipped_fast |
| HBARUSDT | IDLE | 2.63 | 6.36 | 1.32 | 0.08 | 908337.31 | 1.26 | skipped_fast |
| ZBCNUSDT | IDLE | 2.9 | 11.25 | 3.2 | 0.11 | 515181.13 | 67.52 | skipped_fast |
| CCUSDT | IDLE | 1.91 | 7.42 | 1.14 | 0.13 | 644197.98 | 8.89 | skipped_fast |
| WUSDT | IDLE | 2.78 | 6.91 | 1.9 | 0.08 | 379072.85 | 14.42 | skipped_fast |
| CHIPUSDT | IDLE | 1.2 | 3.56 | 1.7 | 0.04 | 545155.25 | 3.09 | skipped_fast |
| BIOUSDT | IDLE | 2.29 | 5.04 | 1.05 | 0.02 | 187295.59 | 3.11 | skipped_fast |
| EDELUSDT | IDLE | 2.56 | 5.5 | 1.09 | 0.0 | 80138.56 | 21.95 | skipped_fast |
| RIZEUSDT | IDLE | 2.21 | 9.82 | 4.8 | 0.12 | 58872.79 | 32.44 | skipped_fast |
| TELUSDT | IDLE | 2.83 | 6.89 | 0.46 | 0.06 | 189417.95 | 10.27 | skipped_fast |
| QNTUSDT | IDLE | 2.59 | 5.68 | 0.06 | 0.07 | 155171.37 | 1.49 | skipped_fast |
| REDUSDT | IDLE | 0.87 | 7.3 | 4.97 | 0.18 | 157746.18 | 17.78 | skipped_fast |
| RWAINCUSDT | IDLE | 2.13 | 4.07 | 1.27 | 0.02 | 10291.37 | 37.46 | skipped_fast |
| QAITUSDT | IDLE | 2.27 | 4.22 | 2.14 | -0.01 | 3715.41 | 67.45 | skipped_fast |
| KITEUSDT | IDLE | 1.1 | 3.12 | 0.91 | 0.09 | 61512.66 | 11.1 | skipped_fast |
| RWAUSDT | IDLE | 1.06 | 2.08 | 0.33 | 0.03 | 54494.02 | 16.38 | skipped_fast |
| FLUIDUSDT | IDLE | 1.09 | 2.87 | 0.66 | 0.1 | 4934.79 | 22.01 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
