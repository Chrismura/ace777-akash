# Hulk DIGEST — 2026-08-22T15:06:26Z

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
| PYTHUSDT | IDLE | 1.59 | 7.62 | 1.71 | 0.04 | 51471678.38 | 13.86 | skipped_fast |
| XRPUSDT | IDLE | 1.36 | 7.49 | 6.03 | 0.02 | 214056911.27 | 2.78 | skipped_fast |
| CCUSDT | IDLE | 1.31 | 5.65 | 2.41 | 0.11 | 801401.06 | 6.83 | skipped_fast |
| HBARUSDT | IDLE | 0.81 | 2.85 | 2.4 | -0.01 | 1172847.81 | 6.54 | skipped_fast |
| CHIPUSDT | IDLE | 0.63 | 3.51 | 2.56 | -0.11 | 614609.3 | 6.82 | skipped_fast |
| WUSDT | IDLE | 0.79 | 3.17 | 1.86 | -0.02 | 563029.92 | 13.9 | skipped_fast |
| KITEUSDT | IDLE | 2.75 | 6.37 | 1.83 | 0.03 | 83640.12 | 8.92 | skipped_fast |
| ZBCNUSDT | IDLE | 1.29 | 3.49 | 1.38 | -0.07 | 323751.0 | 27.62 | skipped_fast |
| BIOUSDT | IDLE | 0.98 | 6.58 | 4.92 | -0.06 | 225264.77 | 3.32 | skipped_fast |
| REDUSDT | IDLE | 0.48 | 5.1 | 4.51 | -0.03 | 150812.2 | 10.07 | skipped_fast |
| EDELUSDT | IDLE | 1.38 | 2.52 | 1.56 | -0.04 | 79030.51 | 34.11 | skipped_fast |
| QAITUSDT | IDLE | 1.99 | 3.76 | 1.48 | 0.01 | 2320.37 | 67.45 | skipped_fast |
| RIZEUSDT | IDLE | 0.79 | 3.28 | 0.45 | 0.04 | 46495.96 | 43.92 | skipped_fast |
| QNTUSDT | IDLE | 0.86 | 2.69 | 2.07 | -0.01 | 188414.04 | 4.72 | skipped_fast |
| RWAINCUSDT | IDLE | 0.77 | 1.53 | 0.0 | 0.01 | 9946.26 | 75.23 | skipped_fast |
| TELUSDT | IDLE | 1.07 | 2.75 | 0.89 | 0.02 | 141000.31 | 58.4 | skipped_fast |
| FLUIDUSDT | IDLE | 0.98 | 1.87 | 1.32 | -0.04 | 4682.03 | 22.39 | skipped_fast |
| RWAUSDT | IDLE | 0.65 | 1.23 | 0.48 | 0.02 | 57306.57 | 8.11 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
