# Hulk DIGEST — 2026-08-22T12:40:04Z

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
| XRPUSDT | IDLE | 2.49 | 14.26 | 7.29 | 0.1 | 216365631.96 | 2.65 | skipped_fast |
| PYTHUSDT | IDLE | 1.63 | 7.83 | 1.63 | 0.05 | 51600164.31 | 9.87 | skipped_fast |
| HBARUSDT | IDLE | 1.26 | 4.63 | 2.21 | 0.02 | 1259727.41 | 5.14 | skipped_fast |
| CCUSDT | IDLE | 1.58 | 8.38 | 2.52 | 0.15 | 776224.81 | 10.84 | skipped_fast |
| WUSDT | IDLE | 1.56 | 6.27 | 3.82 | 0.0 | 576663.2 | 9.54 | skipped_fast |
| ZBCNUSDT | IDLE | 2.22 | 5.77 | 4.09 | -0.01 | 335470.55 | 23.63 | skipped_fast |
| CHIPUSDT | IDLE | 0.72 | 4.16 | 1.65 | -0.1 | 603602.59 | 3.35 | skipped_fast |
| KITEUSDT | IDLE | 2.69 | 6.37 | 0.88 | 0.03 | 84476.68 | 13.33 | skipped_fast |
| EDELUSDT | IDLE | 2.13 | 3.89 | 2.43 | -0.02 | 78179.72 | 22.57 | skipped_fast |
| BIOUSDT | IDLE | 0.81 | 5.65 | 2.83 | -0.04 | 238925.6 | 3.24 | skipped_fast |
| QAITUSDT | IDLE | 2.22 | 4.16 | 1.9 | -0.01 | 2408.77 | 67.45 | skipped_fast |
| TELUSDT | IDLE | 2.16 | 5.61 | 3.83 | -0.03 | 163521.62 | 42.49 | skipped_fast |
| REDUSDT | IDLE | 0.47 | 6.02 | 3.72 | -0.0 | 153312.82 | 21.45 | skipped_fast |
| RWAINCUSDT | IDLE | 1.38 | 2.4 | 2.34 | -0.01 | 10007.28 | 70.63 | skipped_fast |
| QNTUSDT | IDLE | 1.07 | 3.47 | 1.7 | -0.0 | 187751.27 | 1.56 | skipped_fast |
| RIZEUSDT | IDLE | 0.46 | 1.91 | 0.19 | -0.0 | 46780.16 | 46.13 | skipped_fast |
| RWAUSDT | IDLE | 0.98 | 1.8 | 1.04 | 0.02 | 57792.32 | 32.52 | skipped_fast |
| FLUIDUSDT | IDLE | 1.01 | 1.93 | 1.38 | -0.02 | 5705.21 | 21.52 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
