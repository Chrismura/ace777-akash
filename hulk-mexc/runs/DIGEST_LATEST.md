# Hulk DIGEST — 2026-09-26T01:50:49Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| XRPUSDT | IDLE | 1.06 | 2.08 | 0.31 | 0.02 | 112535733.22 | 1.9 | skipped_fast |
| ETHUSDT | IDLE | 0.36 | 0.7 | 0.12 | 0.0 | 319176998.85 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.34 | 0.65 | 0.18 | -0.01 | 674929869.1 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.84 | 4.78 | 2.66 | 0.07 | 1255986.26 | 2.73 | skipped_fast |
| CCUSDT | IDLE | 1.52 | 6.93 | 1.14 | 0.16 | 897966.15 | 8.2 | skipped_fast |
| WUSDT | IDLE | 1.93 | 3.62 | 2.06 | 0.04 | 457873.69 | 5.71 | skipped_fast |
| HBARUSDT | IDLE | 1.31 | 2.43 | 1.32 | 0.02 | 859546.54 | 1.05 | skipped_fast |
| CHIPUSDT | IDLE | 1.87 | 4.72 | 4.45 | 0.04 | 154451.77 | 12.36 | skipped_fast |
| ZBCNUSDT | IDLE | 1.3 | 2.91 | 2.2 | 0.05 | 248229.39 | 15.78 | skipped_fast |
| QNTUSDT | IDLE | 0.97 | 4.29 | 0.57 | 0.11 | 564881.04 | 11.95 | skipped_fast |
| KITEUSDT | IDLE | 1.6 | 3.56 | 0.01 | 0.07 | 78902.77 | 8.08 | skipped_fast |
| BIOUSDT | IDLE | 1.16 | 3.32 | 2.04 | 0.07 | 113370.82 | 6.13 | skipped_fast |
| EDELUSDT | IDLE | 0.77 | 1.5 | 0.3 | -0.0 | 182930.73 | 16.89 | skipped_fast |
| REDUSDT | IDLE | 0.85 | 1.83 | 0.91 | 0.07 | 111763.33 | 20.11 | skipped_fast |
| RIZEUSDT | IDLE | 0.25 | 3.9 | 0.26 | 0.02 | 93421.39 | 33.67 | skipped_fast |
| TELUSDT | IDLE | 1.12 | 1.96 | 1.87 | -0.0 | 111658.82 | 6.13 | skipped_fast |
| RWAINCUSDT | IDLE | 0.42 | 1.27 | 0.75 | -0.08 | 13283.08 | 65.94 | skipped_fast |
| RWAUSDT | IDLE | 0.68 | 1.26 | 0.66 | -0.01 | 53433.28 | 29.56 | skipped_fast |
| MNSRYUSDT | IDLE | 0.56 | 1.02 | 0.73 | 0.02 | 41561.45 | 10.18 | skipped_fast |
| FLUIDUSDT | IDLE | 0.21 | 0.36 | 0.36 | 0.02 | 3296.62 | 19.34 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
