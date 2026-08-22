# Hulk DIGEST — 2026-08-22T00:00:45Z

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
| PYTHUSDT | IDLE | 1.77 | 6.39 | 1.49 | 0.1 | 6236125.5 | 2.05 | skipped_fast |
| XRPUSDT | IDLE | 1.97 | 8.23 | 1.35 | 0.15 | 142156954.86 | 2.06 | skipped_fast |
| HBARUSDT | IDLE | 2.63 | 6.36 | 1.25 | 0.09 | 909553.2 | 1.25 | skipped_fast |
| ZBCNUSDT | IDLE | 2.89 | 11.25 | 2.78 | 0.12 | 515207.06 | 24.67 | skipped_fast |
| CCUSDT | IDLE | 1.93 | 7.42 | 0.69 | 0.13 | 645311.69 | 5.32 | skipped_fast |
| WUSDT | IDLE | 2.79 | 6.91 | 1.9 | 0.08 | 379038.83 | 14.42 | skipped_fast |
| CHIPUSDT | IDLE | 1.62 | 3.56 | 1.19 | 0.05 | 541244.94 | 3.08 | skipped_fast |
| BIOUSDT | IDLE | 2.29 | 5.04 | 1.08 | 0.03 | 187182.1 | 3.11 | skipped_fast |
| EDELUSDT | IDLE | 2.58 | 5.5 | 1.3 | -0.01 | 80067.22 | 21.98 | skipped_fast |
| RIZEUSDT | IDLE | 2.19 | 9.82 | 4.13 | 0.13 | 58938.18 | 22.08 | skipped_fast |
| TELUSDT | IDLE | 2.83 | 6.89 | 0.41 | 0.06 | 189780.94 | 15.4 | skipped_fast |
| QNTUSDT | IDLE | 2.48 | 5.42 | 0.31 | 0.07 | 166696.77 | 1.5 | skipped_fast |
| QAITUSDT | IDLE | 2.27 | 4.22 | 2.14 | -0.01 | 3715.41 | 67.45 | skipped_fast |
| KITEUSDT | IDLE | 1.09 | 3.12 | 0.87 | 0.09 | 61500.55 | 12.93 | skipped_fast |
| REDUSDT | IDLE | 0.56 | 4.91 | 1.51 | 0.18 | 157698.01 | 45.8 | skipped_fast |
| RWAINCUSDT | IDLE | 1.6 | 2.99 | 1.43 | 0.02 | 10296.2 | 91.37 | skipped_fast |
| RWAUSDT | IDLE | 1.06 | 2.08 | 0.24 | 0.04 | 54446.81 | 16.35 | skipped_fast |
| FLUIDUSDT | IDLE | 1.17 | 2.87 | 0.66 | 0.1 | 4934.79 | 41.89 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
