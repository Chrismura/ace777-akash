# Hulk DIGEST — 2026-08-21T23:51:18Z

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
| PYTHUSDT | IDLE | 1.78 | 6.39 | 1.88 | 0.1 | 6197878.03 | 4.11 | skipped_fast |
| XRPUSDT | IDLE | 1.98 | 8.23 | 1.66 | 0.14 | 141985812.99 | 3.45 | skipped_fast |
| ZBCNUSDT | IDLE | 2.91 | 11.25 | 3.33 | 0.11 | 514383.73 | 0.97 | skipped_fast |
| HBARUSDT | IDLE | 2.64 | 6.36 | 1.47 | 0.08 | 909252.72 | 2.51 | skipped_fast |
| CCUSDT | IDLE | 1.91 | 7.42 | 1.2 | 0.13 | 644854.52 | 9.8 | skipped_fast |
| WUSDT | IDLE | 2.8 | 6.91 | 2.27 | 0.07 | 378957.32 | 18.62 | skipped_fast |
| CHIPUSDT | IDLE | 1.2 | 3.56 | 1.86 | 0.03 | 545816.9 | 9.27 | skipped_fast |
| BIOUSDT | IDLE | 2.3 | 5.04 | 1.26 | 0.02 | 187232.85 | 3.12 | skipped_fast |
| EDELUSDT | IDLE | 2.57 | 5.5 | 1.19 | 0.0 | 80173.06 | 22.0 | skipped_fast |
| RIZEUSDT | IDLE | 2.21 | 9.82 | 4.8 | 0.12 | 58847.27 | 46.13 | skipped_fast |
| TELUSDT | IDLE | 2.83 | 6.89 | 0.46 | 0.07 | 190379.85 | 15.4 | skipped_fast |
| REDUSDT | IDLE | 0.87 | 7.3 | 4.97 | 0.18 | 157847.7 | 10.52 | skipped_fast |
| QNTUSDT | IDLE | 2.58 | 5.68 | 0.04 | 0.08 | 152313.03 | 1.49 | skipped_fast |
| QAITUSDT | IDLE | 2.27 | 4.22 | 2.14 | -0.01 | 3725.4 | 67.45 | skipped_fast |
| RWAINCUSDT | IDLE | 2.13 | 4.07 | 1.27 | 0.02 | 10306.4 | 53.56 | skipped_fast |
| KITEUSDT | IDLE | 1.13 | 3.12 | 1.54 | 0.09 | 61327.29 | 9.29 | skipped_fast |
| RWAUSDT | IDLE | 1.06 | 2.08 | 0.33 | 0.04 | 54605.15 | 24.56 | skipped_fast |
| FLUIDUSDT | IDLE | 1.09 | 2.87 | 0.66 | 0.1 | 4934.79 | 22.09 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
