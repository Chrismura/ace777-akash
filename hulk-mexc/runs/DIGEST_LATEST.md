# Hulk DIGEST — 2026-08-22T00:54:46Z

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
| PYTHUSDT | IDLE | 2.0 | 7.38 | 0.66 | 0.12 | 6519817.62 | 2.01 | skipped_fast |
| XRPUSDT | IDLE | 2.11 | 8.72 | 2.4 | 0.14 | 147764194.36 | 4.84 | skipped_fast |
| HBARUSDT | IDLE | 2.81 | 6.36 | 1.81 | 0.07 | 942119.97 | 1.26 | skipped_fast |
| ZBCNUSDT | IDLE | 2.92 | 11.25 | 3.52 | 0.1 | 543268.46 | 15.1 | skipped_fast |
| CCUSDT | IDLE | 1.96 | 7.42 | 1.56 | 0.14 | 645343.47 | 5.36 | skipped_fast |
| WUSDT | IDLE | 2.72 | 6.91 | 0.76 | 0.09 | 391220.68 | 14.25 | skipped_fast |
| CHIPUSDT | IDLE | 1.57 | 3.56 | 0.43 | 0.02 | 544924.34 | 6.11 | skipped_fast |
| BIOUSDT | IDLE | 2.53 | 5.62 | 0.86 | 0.03 | 186651.98 | 3.08 | skipped_fast |
| EDELUSDT | IDLE | 2.64 | 5.5 | 2.17 | -0.02 | 79720.14 | 33.24 | skipped_fast |
| RIZEUSDT | IDLE | 2.25 | 9.82 | 3.53 | 0.12 | 60173.12 | 45.4 | skipped_fast |
| TELUSDT | IDLE | 2.84 | 6.89 | 0.61 | 0.06 | 183939.61 | 20.61 | skipped_fast |
| REDUSDT | IDLE | 0.99 | 8.58 | 3.37 | 0.2 | 159479.39 | 18.84 | skipped_fast |
| QNTUSDT | IDLE | 2.55 | 5.42 | 1.25 | 0.07 | 170534.13 | 3.02 | skipped_fast |
| QAITUSDT | IDLE | 2.2 | 4.22 | 1.21 | 0.0 | 3842.9 | 63.29 | skipped_fast |
| KITEUSDT | IDLE | 1.4 | 4.15 | 0.0 | 0.11 | 60888.61 | 31.71 | skipped_fast |
| RWAINCUSDT | IDLE | 1.7 | 2.99 | 2.7 | 0.02 | 9620.44 | 53.97 | skipped_fast |
| RWAUSDT | IDLE | 1.09 | 2.08 | 0.65 | 0.04 | 54970.44 | 16.43 | skipped_fast |
| FLUIDUSDT | IDLE | 1.17 | 2.87 | 0.66 | 0.09 | 4845.77 | 36.31 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
