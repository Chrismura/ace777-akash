# Hulk DIGEST — 2026-08-22T15:03:14Z

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
| PYTHUSDT | IDLE | 1.58 | 7.62 | 1.36 | 0.05 | 51466013.63 | 1.97 | skipped_fast |
| XRPUSDT | IDLE | 1.35 | 7.49 | 5.47 | 0.03 | 213963692.66 | 3.46 | skipped_fast |
| CCUSDT | IDLE | 1.31 | 5.65 | 2.47 | 0.11 | 801119.23 | 4.27 | skipped_fast |
| HBARUSDT | IDLE | 0.81 | 2.85 | 2.34 | -0.01 | 1174864.86 | 2.62 | skipped_fast |
| CHIPUSDT | IDLE | 0.63 | 3.51 | 2.36 | -0.11 | 614322.29 | 3.4 | skipped_fast |
| WUSDT | IDLE | 0.78 | 3.17 | 1.68 | -0.02 | 562999.75 | 11.75 | skipped_fast |
| KITEUSDT | IDLE | 2.73 | 6.37 | 1.61 | 0.03 | 83598.92 | 11.59 | skipped_fast |
| ZBCNUSDT | IDLE | 1.25 | 3.49 | 0.68 | -0.06 | 323124.85 | 21.33 | skipped_fast |
| BIOUSDT | IDLE | 0.97 | 6.58 | 4.7 | -0.06 | 224069.0 | 3.31 | skipped_fast |
| EDELUSDT | IDLE | 1.39 | 2.52 | 1.68 | -0.04 | 79019.19 | 22.73 | skipped_fast |
| QAITUSDT | IDLE | 2.01 | 3.76 | 1.79 | -0.01 | 2374.33 | 67.45 | skipped_fast |
| REDUSDT | IDLE | 0.47 | 5.1 | 4.25 | -0.04 | 150733.71 | 21.94 | skipped_fast |
| RIZEUSDT | IDLE | 0.79 | 3.28 | 0.47 | 0.04 | 46485.3 | 43.92 | skipped_fast |
| QNTUSDT | IDLE | 0.86 | 2.69 | 2.0 | -0.01 | 188403.75 | 9.44 | skipped_fast |
| TELUSDT | IDLE | 1.09 | 2.75 | 1.16 | 0.02 | 140805.47 | 37.16 | skipped_fast |
| RWAINCUSDT | IDLE | 0.77 | 1.53 | 0.0 | 0.01 | 9946.26 | 75.23 | skipped_fast |
| FLUIDUSDT | IDLE | 0.98 | 1.87 | 1.32 | -0.04 | 4682.03 | 21.65 | skipped_fast |
| RWAUSDT | IDLE | 0.63 | 1.23 | 0.24 | 0.02 | 57320.71 | 16.21 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
