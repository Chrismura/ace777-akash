# Hulk DIGEST — 2026-08-21T21:22:48Z

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
| PYTHUSDT | IDLE | 1.19 | 4.51 | 1.11 | 0.09 | 5617927.24 | 4.15 | skipped_fast |
| XRPUSDT | IDLE | 1.15 | 3.73 | 1.94 | 0.11 | 128769267.13 | 2.16 | skipped_fast |
| ZBCNUSDT | IDLE | 1.97 | 8.19 | 4.11 | 0.1 | 484713.62 | 9.58 | skipped_fast |
| CHIPUSDT | IDLE | 1.93 | 5.61 | 4.8 | 0.05 | 515691.88 | 6.27 | skipped_fast |
| CCUSDT | IDLE | 1.14 | 3.14 | 0.31 | 0.1 | 644364.36 | 9.21 | skipped_fast |
| HBARUSDT | IDLE | 1.59 | 3.04 | 0.87 | 0.07 | 809509.16 | 1.29 | skipped_fast |
| WUSDT | IDLE | 1.96 | 3.83 | 0.59 | 0.06 | 366654.07 | 12.56 | skipped_fast |
| BIOUSDT | IDLE | 2.45 | 5.2 | 2.4 | 0.01 | 186798.75 | 6.29 | skipped_fast |
| REDUSDT | IDLE | 1.35 | 11.01 | 9.56 | 0.17 | 153593.99 | 19.77 | skipped_fast |
| RWAINCUSDT | IDLE | 2.27 | 4.3 | 1.64 | 0.03 | 10270.17 | 5.38 | skipped_fast |
| RIZEUSDT | IDLE | 1.87 | 9.54 | 1.41 | 0.01 | 56198.17 | 45.77 | skipped_fast |
| EDELUSDT | IDLE | 2.04 | 4.12 | 2.53 | -0.05 | 82616.54 | 44.99 | skipped_fast |
| KITEUSDT | IDLE | 1.31 | 4.0 | 2.03 | 0.11 | 61049.96 | 12.98 | skipped_fast |
| QAITUSDT | IDLE | 2.5 | 4.38 | 4.2 | -0.04 | 3753.25 | 186.99 | skipped_fast |
| TELUSDT | IDLE | 1.35 | 3.39 | 0.74 | 0.02 | 178969.53 | 37.28 | skipped_fast |
| QNTUSDT | IDLE | 1.45 | 2.65 | 1.66 | 0.04 | 60554.04 | 1.56 | skipped_fast |
| RWAUSDT | IDLE | 0.62 | 1.17 | 0.49 | 0.03 | 53855.32 | 33.17 | skipped_fast |
| FLUIDUSDT | IDLE | 0.58 | 1.15 | 1.1 | 0.08 | 4161.15 | 22.12 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
