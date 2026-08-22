# Hulk DIGEST — 2026-08-22T00:56:34Z

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
| PYTHUSDT | IDLE | 1.99 | 7.38 | 0.52 | 0.13 | 6526079.16 | 2.01 | skipped_fast |
| XRPUSDT | IDLE | 2.1 | 8.72 | 2.21 | 0.14 | 147763959.71 | 2.76 | skipped_fast |
| HBARUSDT | IDLE | 2.79 | 6.36 | 1.55 | 0.08 | 942600.72 | 2.52 | skipped_fast |
| ZBCNUSDT | IDLE | 2.91 | 11.25 | 3.27 | 0.1 | 543188.84 | 16.04 | skipped_fast |
| CCUSDT | IDLE | 1.94 | 7.42 | 0.89 | 0.14 | 651192.83 | 9.77 | skipped_fast |
| WUSDT | IDLE | 2.72 | 6.91 | 0.74 | 0.09 | 391272.83 | 13.22 | skipped_fast |
| CHIPUSDT | IDLE | 1.56 | 3.56 | 0.33 | 0.02 | 544876.42 | 3.05 | skipped_fast |
| BIOUSDT | IDLE | 2.48 | 5.62 | 0.09 | 0.04 | 186668.21 | 3.06 | skipped_fast |
| EDELUSDT | IDLE | 2.64 | 5.5 | 2.17 | -0.02 | 79729.11 | 33.24 | skipped_fast |
| RIZEUSDT | IDLE | 2.25 | 9.82 | 3.56 | 0.12 | 60186.0 | 43.92 | skipped_fast |
| TELUSDT | IDLE | 2.84 | 6.89 | 0.66 | 0.06 | 183883.92 | 15.46 | skipped_fast |
| REDUSDT | IDLE | 0.97 | 8.58 | 2.65 | 0.2 | 159451.31 | 17.17 | skipped_fast |
| QNTUSDT | IDLE | 2.54 | 5.42 | 1.15 | 0.07 | 170546.2 | 4.53 | skipped_fast |
| QAITUSDT | IDLE | 2.2 | 4.22 | 1.21 | 0.01 | 3850.39 | 67.05 | skipped_fast |
| RWAINCUSDT | IDLE | 1.7 | 2.99 | 2.7 | 0.02 | 9620.44 | 21.55 | skipped_fast |
| KITEUSDT | IDLE | 1.45 | 4.3 | 0.03 | 0.12 | 60957.34 | 22.68 | skipped_fast |
| RWAUSDT | IDLE | 1.09 | 2.08 | 0.65 | 0.04 | 54962.89 | 8.22 | skipped_fast |
| FLUIDUSDT | IDLE | 1.17 | 2.87 | 0.66 | 0.09 | 4845.77 | 9.07 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
