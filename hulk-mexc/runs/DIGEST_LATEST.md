# Hulk DIGEST — 2026-08-22T00:40:20Z

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
| PYTHUSDT | IDLE | 1.87 | 6.97 | 0.1 | 0.12 | 6441090.13 | 6.02 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.08 | 8.72 | 1.69 | 0.15 | 146498034.46 | 2.75 | skipped_fast |
| ZBCNUSDT | IDLE | 2.89 | 11.25 | 2.73 | 0.11 | 543746.68 | 3.39 | skipped_fast |
| HBARUSDT | IDLE | 2.78 | 6.36 | 1.37 | 0.08 | 939647.48 | 1.25 | skipped_fast |
| CCUSDT | IDLE | 1.93 | 7.42 | 0.82 | 0.15 | 640398.81 | 7.1 | skipped_fast |
| WUSDT | IDLE | 2.71 | 6.91 | 0.55 | 0.09 | 388073.79 | 11.16 | skipped_fast |
| CHIPUSDT | IDLE | 1.58 | 3.56 | 0.67 | 0.03 | 553281.92 | 3.06 | skipped_fast |
| BIOUSDT | IDLE | 2.37 | 5.36 | 0.18 | 0.03 | 186114.17 | 9.2 | skipped_fast |
| EDELUSDT | IDLE | 2.55 | 5.5 | 0.87 | -0.01 | 79867.72 | 21.93 | skipped_fast |
| RIZEUSDT | IDLE | 2.24 | 9.82 | 3.32 | 0.12 | 59985.64 | 45.4 | skipped_fast |
| QAITUSDT | IDLE | 2.27 | 4.22 | 2.14 | -0.01 | 3715.41 | 19.88 | skipped_fast |
| TELUSDT | IDLE | 2.83 | 6.89 | 0.56 | 0.06 | 186313.31 | 36.04 | skipped_fast |
| QNTUSDT | IDLE | 2.55 | 5.42 | 1.33 | 0.06 | 170527.02 | 3.03 | skipped_fast |
| REDUSDT | IDLE | 0.74 | 6.54 | 1.61 | 0.23 | 158116.45 | 19.62 | skipped_fast |
| RWAINCUSDT | IDLE | 1.7 | 2.99 | 2.7 | 0.04 | 9787.93 | 21.55 | skipped_fast |
| KITEUSDT | IDLE | 1.06 | 3.12 | 0.2 | 0.1 | 61155.86 | 11.93 | skipped_fast |
| RWAUSDT | IDLE | 1.08 | 2.08 | 0.57 | 0.03 | 54731.82 | 8.21 | skipped_fast |
| FLUIDUSDT | IDLE | 1.17 | 2.87 | 0.66 | 0.09 | 4845.77 | 21.7 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
