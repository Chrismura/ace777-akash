# Hulk DIGEST — 2026-08-16T23:01:52Z

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
| XRPUSDT | IDLE | 0.66 | 1.2 | 0.83 | -0.01 | 6577203.49 | 1.01 | skipped_fast |
| RIZEUSDT | IDLE | 3.65 | 7.8 | 1.79 | 0.01 | 37378.03 | 59.59 | skipped_fast |
| CHIPUSDT | IDLE | 1.62 | 7.25 | 6.12 | 0.0 | 297034.62 | 14.41 | skipped_fast |
| PYTHUSDT | IDLE | 1.87 | 3.38 | 2.35 | -0.02 | 147758.03 | 5.19 | skipped_fast |
| CCUSDT | IDLE | 0.56 | 1.19 | 0.21 | -0.04 | 333175.51 | 6.27 | skipped_fast |
| BIOUSDT | IDLE | 1.51 | 2.75 | 1.79 | -0.02 | 67906.32 | 4.13 | skipped_fast |
| WUSDT | IDLE | 1.09 | 2.14 | 0.28 | 0.01 | 182280.56 | 15.2 | skipped_fast |
| ZBCNUSDT | IDLE | 0.85 | 1.57 | 0.83 | -0.02 | 191228.95 | 21.7 | skipped_fast |
| KITEUSDT | IDLE | 0.76 | 1.34 | 1.19 | -0.03 | 55685.58 | 12.85 | skipped_fast |
| REDUSDT | IDLE | 0.7 | 1.25 | 0.95 | -0.08 | 65727.61 | 13.86 | skipped_fast |
| QAITUSDT | IDLE | 1.25 | 3.83 | 0.0 | -0.01 | 2289.9 | 61.3 | skipped_fast |
| EDELUSDT | IDLE | 1.6 | 2.94 | 1.69 | 0.03 | 60611.06 | 131.06 | skipped_fast |
| RWAINCUSDT | IDLE | 0.78 | 1.37 | 1.29 | 0.06 | 9962.59 | 45.27 | skipped_fast |
| HBARUSDT | IDLE | 0.65 | 1.21 | 0.63 | -0.01 | 104058.86 | 1.54 | skipped_fast |
| TELUSDT | IDLE | 0.95 | 1.74 | 1.03 | -0.03 | 95286.68 | 41.61 | skipped_fast |
| QNTUSDT | IDLE | 0.86 | 1.61 | 0.77 | -0.02 | 33964.69 | 7.04 | skipped_fast |
| FLUIDUSDT | IDLE | 0.67 | 1.16 | 1.15 | 0.01 | 220.62 | 21.16 | skipped_fast |
| RWAUSDT | IDLE | 0.4 | 0.7 | 0.61 | -0.0 | 50700.01 | 17.5 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
