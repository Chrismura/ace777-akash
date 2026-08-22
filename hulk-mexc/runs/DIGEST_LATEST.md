# Hulk DIGEST — 2026-08-22T00:51:30Z

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
| PYTHUSDT | IDLE | 2.0 | 7.38 | 0.68 | 0.12 | 6497793.08 | 8.05 | skipped_fast |
| XRPUSDT | IDLE | 2.1 | 8.72 | 2.09 | 0.15 | 147630063.9 | 2.07 | skipped_fast |
| HBARUSDT | IDLE | 2.81 | 6.36 | 1.77 | 0.07 | 941891.53 | 1.26 | skipped_fast |
| ZBCNUSDT | IDLE | 2.91 | 11.25 | 3.41 | 0.1 | 543715.12 | 25.82 | skipped_fast |
| CCUSDT | IDLE | 1.96 | 7.42 | 1.43 | 0.14 | 645108.66 | 5.35 | skipped_fast |
| WUSDT | IDLE | 2.73 | 6.91 | 0.93 | 0.09 | 389076.78 | 15.29 | skipped_fast |
| CHIPUSDT | IDLE | 1.57 | 3.56 | 0.4 | 0.03 | 548321.78 | 6.11 | skipped_fast |
| BIOUSDT | IDLE | 2.53 | 5.62 | 0.89 | 0.03 | 186505.99 | 15.43 | skipped_fast |
| EDELUSDT | IDLE | 2.6 | 5.5 | 1.63 | -0.02 | 79980.41 | 33.13 | skipped_fast |
| RIZEUSDT | IDLE | 2.22 | 9.82 | 2.65 | 0.13 | 60130.29 | 45.1 | skipped_fast |
| TELUSDT | IDLE | 2.84 | 6.89 | 0.66 | 0.06 | 184210.4 | 25.75 | skipped_fast |
| QAITUSDT | IDLE | 2.26 | 4.22 | 1.99 | -0.01 | 3786.48 | 15.91 | skipped_fast |
| QNTUSDT | IDLE | 2.57 | 5.42 | 1.61 | 0.06 | 170522.57 | 4.55 | skipped_fast |
| REDUSDT | IDLE | 0.97 | 8.58 | 2.28 | 0.24 | 159716.17 | 59.97 | skipped_fast |
| RWAINCUSDT | IDLE | 1.7 | 2.99 | 2.7 | 0.03 | 9754.98 | 53.97 | skipped_fast |
| KITEUSDT | IDLE | 1.05 | 3.12 | 0.03 | 0.1 | 60963.32 | 9.15 | skipped_fast |
| RWAUSDT | IDLE | 1.08 | 2.08 | 0.57 | 0.03 | 54946.42 | 8.21 | skipped_fast |
| FLUIDUSDT | IDLE | 1.17 | 2.87 | 0.66 | 0.09 | 4845.77 | 21.71 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
