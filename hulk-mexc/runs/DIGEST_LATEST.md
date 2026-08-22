# Hulk DIGEST — 2026-08-22T00:42:04Z

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
| PYTHUSDT | IDLE | 1.91 | 7.1 | 0.32 | 0.13 | 6448716.04 | 2.01 | skipped_fast |
| XRPUSDT | IDLE | 2.1 | 8.72 | 2.09 | 0.15 | 146812741.34 | 2.76 | skipped_fast |
| HBARUSDT | IDLE | 2.8 | 6.36 | 1.63 | 0.08 | 939718.04 | 2.52 | skipped_fast |
| ZBCNUSDT | IDLE | 2.89 | 11.25 | 2.78 | 0.12 | 544318.29 | 8.24 | skipped_fast |
| CCUSDT | IDLE | 1.95 | 7.42 | 1.14 | 0.15 | 640209.86 | 7.13 | skipped_fast |
| WUSDT | IDLE | 2.71 | 6.91 | 0.48 | 0.09 | 388096.43 | 10.16 | skipped_fast |
| CHIPUSDT | IDLE | 1.57 | 3.56 | 0.49 | 0.03 | 553007.47 | 6.11 | skipped_fast |
| BIOUSDT | IDLE | 2.48 | 5.62 | 0.0 | 0.04 | 186240.75 | 12.27 | skipped_fast |
| RIZEUSDT | IDLE | 2.24 | 9.82 | 3.28 | 0.12 | 59995.73 | 21.89 | skipped_fast |
| EDELUSDT | IDLE | 2.56 | 5.5 | 0.98 | -0.01 | 79922.68 | 21.93 | skipped_fast |
| QAITUSDT | IDLE | 2.27 | 4.22 | 2.14 | -0.01 | 3715.41 | 19.88 | skipped_fast |
| TELUSDT | IDLE | 2.84 | 6.89 | 0.61 | 0.06 | 186355.76 | 30.9 | skipped_fast |
| QNTUSDT | IDLE | 2.56 | 5.42 | 1.46 | 0.06 | 170544.18 | 4.55 | skipped_fast |
| REDUSDT | IDLE | 0.73 | 6.54 | 1.22 | 0.24 | 158088.24 | 18.04 | skipped_fast |
| RWAINCUSDT | IDLE | 1.7 | 2.99 | 2.7 | 0.04 | 9787.93 | 32.35 | skipped_fast |
| KITEUSDT | IDLE | 1.06 | 3.12 | 0.09 | 0.1 | 61152.41 | 11.93 | skipped_fast |
| RWAUSDT | IDLE | 1.08 | 2.08 | 0.49 | 0.03 | 54757.4 | 16.43 | skipped_fast |
| FLUIDUSDT | IDLE | 1.17 | 2.87 | 0.66 | 0.09 | 4845.77 | 21.06 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
