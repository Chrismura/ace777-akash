# Hulk DIGEST — 2026-10-10T23:05:17Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| ETHUSDT | IDLE | 0.3 | 0.56 | 0.33 | 0.01 | 115016258.49 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.31 | 0.58 | 0.31 | 0.01 | 12950209.83 | 0.71 | skipped_fast |
| BTCUSDT | IDLE | 0.12 | 0.23 | 0.06 | 0.01 | 169103545.65 | 0.0 | skipped_fast |
| WUSDT | IDLE | 1.07 | 3.34 | 2.58 | 0.02 | 1263707.94 | 7.38 | skipped_fast |
| QNTUSDT | IDLE | 1.14 | 2.11 | 1.19 | -0.04 | 1242467.75 | 3.33 | skipped_fast |
| PYTHUSDT | IDLE | 0.89 | 1.64 | 0.97 | -0.02 | 770026.96 | 2.54 | skipped_fast |
| CHIPUSDT | IDLE | 2.22 | 19.7 | 2.04 | 0.32 | 248492.36 | 15.98 | skipped_fast |
| EDELUSDT | IDLE | 2.39 | 4.71 | 3.31 | -0.05 | 253420.34 | 10.44 | skipped_fast |
| BIOUSDT | IDLE | 1.52 | 2.76 | 1.82 | 0.03 | 87786.66 | 3.42 | skipped_fast |
| CCUSDT | IDLE | 0.68 | 1.3 | 0.38 | -0.03 | 275845.46 | 8.4 | skipped_fast |
| ZBCNUSDT | IDLE | 0.66 | 1.31 | 0.11 | 0.03 | 199932.25 | 18.16 | skipped_fast |
| KITEUSDT | IDLE | 1.02 | 2.18 | 1.9 | 0.07 | 61708.68 | 11.73 | skipped_fast |
| TELUSDT | IDLE | 1.9 | 3.46 | 2.25 | -0.03 | 138369.39 | 28.07 | skipped_fast |
| REDUSDT | IDLE | 0.59 | 1.05 | 0.87 | 0.02 | 55616.76 | 14.64 | skipped_fast |
| RIZEUSDT | IDLE | 1.01 | 1.82 | 1.35 | -0.05 | 33107.22 | 58.33 | skipped_fast |
| HBARUSDT | IDLE | 0.44 | 0.79 | 0.56 | 0.01 | 309520.22 | 4.33 | skipped_fast |
| RWAINCUSDT | IDLE | 0.52 | 1.04 | 0.0 | -0.02 | 9523.81 | 44.24 | skipped_fast |
| FLUIDUSDT | IDLE | 1.29 | 2.45 | 0.87 | 0.01 | 8391.47 | 21.8 | skipped_fast |
| MNSRYUSDT | IDLE | 1.04 | 1.82 | 1.68 | -0.01 | 36920.86 | 52.18 | skipped_fast |
| RWAUSDT | IDLE | 0.44 | 0.79 | 0.63 | 0.0 | 53129.11 | 7.87 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
