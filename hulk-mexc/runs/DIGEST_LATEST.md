# Hulk DIGEST — 2026-08-21T23:52:34Z

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
| PYTHUSDT | IDLE | 1.77 | 6.39 | 1.77 | 0.1 | 6202487.7 | 2.05 | skipped_fast |
| XRPUSDT | IDLE | 1.98 | 8.23 | 1.69 | 0.14 | 142012730.07 | 2.76 | skipped_fast |
| ZBCNUSDT | IDLE | 2.93 | 11.25 | 3.82 | 0.11 | 514434.22 | 23.46 | skipped_fast |
| HBARUSDT | IDLE | 2.65 | 6.36 | 1.51 | 0.08 | 909425.45 | 1.26 | skipped_fast |
| CCUSDT | IDLE | 1.91 | 7.42 | 1.19 | 0.13 | 643868.46 | 9.8 | skipped_fast |
| WUSDT | IDLE | 2.8 | 6.91 | 2.26 | 0.07 | 378899.34 | 13.42 | skipped_fast |
| CHIPUSDT | IDLE | 1.19 | 3.56 | 1.58 | 0.03 | 545816.39 | 3.09 | skipped_fast |
| BIOUSDT | IDLE | 2.3 | 5.04 | 1.2 | 0.02 | 187215.63 | 3.11 | skipped_fast |
| EDELUSDT | IDLE | 2.58 | 5.5 | 1.41 | 0.0 | 80197.96 | 22.0 | skipped_fast |
| RIZEUSDT | IDLE | 2.21 | 9.82 | 4.89 | 0.12 | 58853.15 | 46.13 | skipped_fast |
| TELUSDT | IDLE | 2.83 | 6.89 | 0.46 | 0.07 | 191324.97 | 25.66 | skipped_fast |
| REDUSDT | IDLE | 0.87 | 7.3 | 5.09 | 0.18 | 157793.99 | 17.84 | skipped_fast |
| QNTUSDT | IDLE | 2.58 | 5.68 | 0.03 | 0.08 | 154022.24 | 1.49 | skipped_fast |
| RWAINCUSDT | IDLE | 2.13 | 4.07 | 1.27 | 0.02 | 10306.4 | 42.83 | skipped_fast |
| QAITUSDT | IDLE | 2.27 | 4.22 | 2.14 | -0.01 | 3715.41 | 67.45 | skipped_fast |
| KITEUSDT | IDLE | 1.12 | 3.12 | 1.38 | 0.09 | 61329.33 | 11.12 | skipped_fast |
| RWAUSDT | IDLE | 1.06 | 2.08 | 0.33 | 0.04 | 54538.83 | 24.56 | skipped_fast |
| FLUIDUSDT | IDLE | 1.09 | 2.87 | 0.66 | 0.1 | 4934.79 | 22.03 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
