# Hulk DIGEST — 2026-08-22T15:29:11Z

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
| PYTHUSDT | IDLE | 1.58 | 7.62 | 1.21 | 0.04 | 51495137.22 | 1.97 | skipped_fast |
| XRPUSDT | IDLE | 1.35 | 7.49 | 5.45 | 0.02 | 214872597.71 | 3.45 | skipped_fast |
| CCUSDT | IDLE | 1.34 | 5.65 | 3.51 | 0.09 | 796070.28 | 6.05 | skipped_fast |
| HBARUSDT | IDLE | 0.87 | 3.03 | 2.73 | -0.02 | 1164011.88 | 3.94 | skipped_fast |
| CHIPUSDT | IDLE | 0.64 | 3.51 | 2.66 | -0.09 | 606306.49 | 6.81 | skipped_fast |
| WUSDT | IDLE | 0.79 | 3.17 | 2.01 | -0.03 | 554391.33 | 10.71 | skipped_fast |
| KITEUSDT | IDLE | 2.79 | 6.37 | 2.54 | 0.02 | 85141.52 | 8.99 | skipped_fast |
| ZBCNUSDT | IDLE | 1.33 | 3.49 | 2.19 | -0.06 | 324675.32 | 33.02 | skipped_fast |
| BIOUSDT | IDLE | 0.97 | 6.58 | 4.79 | -0.07 | 221349.8 | 6.62 | skipped_fast |
| EDELUSDT | IDLE | 1.41 | 2.52 | 2.01 | -0.05 | 79179.87 | 11.41 | skipped_fast |
| REDUSDT | IDLE | 0.53 | 5.67 | 5.08 | -0.06 | 147861.05 | 9.22 | skipped_fast |
| QAITUSDT | IDLE | 1.99 | 3.76 | 1.48 | 0.01 | 2320.37 | 67.45 | skipped_fast |
| RIZEUSDT | IDLE | 0.79 | 3.28 | 0.3 | 0.03 | 56470.36 | 33.69 | skipped_fast |
| QNTUSDT | IDLE | 0.87 | 2.69 | 2.36 | -0.02 | 188310.81 | 9.47 | skipped_fast |
| RWAINCUSDT | IDLE | 0.77 | 1.53 | 0.0 | 0.01 | 9801.28 | 75.23 | skipped_fast |
| TELUSDT | IDLE | 1.11 | 2.75 | 1.58 | -0.01 | 140506.66 | 42.71 | skipped_fast |
| FLUIDUSDT | IDLE | 0.98 | 1.87 | 1.32 | -0.04 | 4625.53 | 21.72 | skipped_fast |
| RWAUSDT | IDLE | 0.66 | 1.23 | 0.65 | 0.02 | 57318.37 | 16.25 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
