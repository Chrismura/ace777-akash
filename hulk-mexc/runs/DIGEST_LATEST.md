# Hulk DIGEST — 2026-08-22T12:22:35Z

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
| PYTHUSDT | IDLE | 1.67 | 7.83 | 2.97 | 0.04 | 51609453.53 | 4.0 | skipped_fast |
| XRPUSDT | IDLE | 2.46 | 14.26 | 6.07 | 0.12 | 215802340.54 | 3.93 | skipped_fast |
| HBARUSDT | IDLE | 1.24 | 4.63 | 1.85 | 0.03 | 1260542.41 | 7.68 | skipped_fast |
| CCUSDT | IDLE | 1.6 | 8.38 | 3.36 | 0.14 | 774360.29 | 10.11 | skipped_fast |
| WUSDT | IDLE | 1.53 | 6.27 | 3.09 | 0.02 | 579058.28 | 14.73 | skipped_fast |
| ZBCNUSDT | IDLE | 2.2 | 5.77 | 3.55 | -0.02 | 371025.14 | 12.79 | skipped_fast |
| CHIPUSDT | IDLE | 0.7 | 4.16 | 1.09 | -0.09 | 608424.6 | 3.34 | skipped_fast |
| KITEUSDT | IDLE | 2.6 | 6.24 | 0.32 | 0.04 | 83362.23 | 4.41 | skipped_fast |
| BIOUSDT | IDLE | 0.78 | 5.65 | 1.16 | -0.02 | 240831.34 | 3.18 | skipped_fast |
| EDELUSDT | IDLE | 2.1 | 3.89 | 2.09 | -0.02 | 78079.04 | 56.47 | skipped_fast |
| QAITUSDT | IDLE | 2.2 | 4.16 | 1.63 | -0.0 | 2384.15 | 63.29 | skipped_fast |
| REDUSDT | IDLE | 0.46 | 6.02 | 2.06 | 0.03 | 153163.44 | 7.89 | skipped_fast |
| TELUSDT | IDLE | 2.17 | 5.61 | 3.93 | -0.03 | 164399.37 | 63.9 | skipped_fast |
| RWAINCUSDT | IDLE | 1.38 | 2.4 | 2.34 | -0.01 | 10094.52 | 76.09 | skipped_fast |
| QNTUSDT | IDLE | 1.03 | 3.47 | 0.75 | 0.01 | 187882.39 | 4.63 | skipped_fast |
| RIZEUSDT | IDLE | 0.46 | 1.91 | 0.29 | -0.04 | 48016.71 | 22.24 | skipped_fast |
| RWAUSDT | IDLE | 1.0 | 1.8 | 1.29 | 0.02 | 57686.96 | 16.27 | skipped_fast |
| FLUIDUSDT | IDLE | 1.01 | 1.93 | 1.38 | -0.01 | 5711.25 | 21.43 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
