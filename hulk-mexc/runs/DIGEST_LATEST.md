# Hulk DIGEST — 2026-08-22T12:49:51Z

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
| XRPUSDT | IDLE | 2.49 | 14.26 | 7.03 | 0.09 | 215994598.62 | 1.32 | skipped_fast |
| PYTHUSDT | IDLE | 1.63 | 7.83 | 1.59 | 0.05 | 51595865.33 | 13.82 | skipped_fast |
| HBARUSDT | IDLE | 1.26 | 4.63 | 2.24 | 0.01 | 1252448.22 | 5.14 | skipped_fast |
| CCUSDT | IDLE | 1.62 | 8.38 | 4.16 | 0.13 | 774868.99 | 10.17 | skipped_fast |
| WUSDT | IDLE | 1.56 | 6.27 | 3.78 | -0.0 | 575068.13 | 12.72 | skipped_fast |
| ZBCNUSDT | IDLE | 2.2 | 5.77 | 3.62 | -0.0 | 335332.44 | 18.43 | skipped_fast |
| CHIPUSDT | IDLE | 0.73 | 4.16 | 2.01 | -0.1 | 606410.98 | 3.37 | skipped_fast |
| KITEUSDT | IDLE | 2.68 | 6.37 | 0.85 | 0.04 | 84875.71 | 12.38 | skipped_fast |
| EDELUSDT | IDLE | 2.2 | 3.89 | 3.42 | -0.03 | 78229.57 | 33.92 | skipped_fast |
| BIOUSDT | IDLE | 0.81 | 5.65 | 2.74 | -0.05 | 238221.13 | 3.24 | skipped_fast |
| QAITUSDT | IDLE | 2.22 | 4.16 | 1.9 | -0.01 | 2384.58 | 67.45 | skipped_fast |
| REDUSDT | IDLE | 0.47 | 6.02 | 3.41 | 0.01 | 152793.45 | 11.57 | skipped_fast |
| TELUSDT | IDLE | 2.17 | 5.61 | 3.93 | -0.03 | 163188.69 | 58.46 | skipped_fast |
| RWAINCUSDT | IDLE | 1.38 | 2.4 | 2.34 | -0.01 | 10007.28 | 70.63 | skipped_fast |
| QNTUSDT | IDLE | 1.06 | 3.47 | 1.53 | -0.01 | 187592.12 | 6.22 | skipped_fast |
| RIZEUSDT | IDLE | 0.5 | 2.03 | 0.56 | -0.01 | 46794.99 | 46.13 | skipped_fast |
| RWAUSDT | IDLE | 0.98 | 1.8 | 1.12 | 0.02 | 57551.01 | 8.12 | skipped_fast |
| FLUIDUSDT | IDLE | 1.01 | 1.93 | 1.38 | -0.04 | 5072.55 | 22.26 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
