# Hulk DIGEST — 2026-08-21T21:35:15Z

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
| PYTHUSDT | IDLE | 1.17 | 4.51 | 0.49 | 0.1 | 5642641.57 | 2.06 | skipped_fast |
| XRPUSDT | IDLE | 1.09 | 3.73 | 0.7 | 0.11 | 129388145.69 | 4.99 | skipped_fast |
| CHIPUSDT | IDLE | 1.88 | 5.61 | 3.61 | 0.06 | 517201.12 | 6.19 | skipped_fast |
| ZBCNUSDT | IDLE | 1.97 | 8.19 | 4.26 | 0.1 | 488319.45 | 40.92 | skipped_fast |
| CCUSDT | IDLE | 1.18 | 3.37 | 0.0 | 0.1 | 646644.13 | 7.32 | skipped_fast |
| HBARUSDT | IDLE | 1.54 | 3.08 | 0.0 | 0.07 | 817879.47 | 1.28 | skipped_fast |
| WUSDT | IDLE | 1.93 | 3.83 | 0.15 | 0.07 | 368100.51 | 11.47 | skipped_fast |
| BIOUSDT | IDLE | 2.43 | 5.2 | 2.09 | 0.02 | 187983.63 | 6.27 | skipped_fast |
| REDUSDT | IDLE | 1.34 | 11.01 | 8.73 | 0.18 | 154196.71 | 18.75 | skipped_fast |
| EDELUSDT | IDLE | 1.99 | 4.12 | 1.87 | -0.05 | 83681.63 | 22.4 | skipped_fast |
| RIZEUSDT | IDLE | 1.87 | 9.54 | 1.49 | 0.02 | 56026.48 | 45.77 | skipped_fast |
| RWAINCUSDT | IDLE | 2.24 | 4.3 | 1.22 | 0.03 | 10157.2 | 43.22 | skipped_fast |
| KITEUSDT | IDLE | 1.28 | 4.0 | 1.33 | 0.11 | 61032.43 | 12.89 | skipped_fast |
| TELUSDT | IDLE | 1.92 | 4.81 | 1.15 | 0.03 | 182969.05 | 63.29 | skipped_fast |
| QAITUSDT | IDLE | 2.33 | 4.38 | 1.83 | -0.01 | 3809.29 | 186.99 | skipped_fast |
| QNTUSDT | IDLE | 1.37 | 2.65 | 0.57 | 0.04 | 62895.36 | 7.73 | skipped_fast |
| RWAUSDT | IDLE | 0.62 | 1.17 | 0.41 | 0.03 | 53945.51 | 16.56 | skipped_fast |
| FLUIDUSDT | IDLE | 0.51 | 1.15 | 0.09 | 0.09 | 4171.26 | 21.19 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
