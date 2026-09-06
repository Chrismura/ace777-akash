# Hulk DIGEST — 2026-09-06T10:31:15Z

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
| ETHUSDT | IDLE | 0.88 | 1.61 | 1.0 | 0.02 | 230049041.62 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.76 | 1.41 | 0.7 | 0.01 | 25459888.04 | 0.71 | skipped_fast |
| BTCUSDT | IDLE | 0.34 | 0.65 | 0.16 | 0.0 | 404118659.66 | 0.0 | skipped_fast |
| CHIPUSDT | IDLE | 2.69 | 7.32 | 1.4 | 0.07 | 401133.37 | 1.65 | skipped_fast |
| PYTHUSDT | IDLE | 1.48 | 2.7 | 1.77 | 0.02 | 431815.13 | 1.82 | skipped_fast |
| RIZEUSDT | IDLE | 2.2 | 12.15 | 9.7 | 0.02 | 90033.23 | 63.12 | skipped_fast |
| CCUSDT | IDLE | 1.02 | 1.93 | 0.67 | 0.02 | 304826.22 | 7.25 | skipped_fast |
| ZBCNUSDT | IDLE | 1.44 | 2.76 | 0.74 | 0.02 | 224503.5 | 24.12 | skipped_fast |
| RWAINCUSDT | IDLE | 2.33 | 4.65 | 0.05 | 0.05 | 9400.36 | 46.94 | skipped_fast |
| WUSDT | IDLE | 1.14 | 2.13 | 1.05 | 0.01 | 174333.16 | 9.91 | skipped_fast |
| BIOUSDT | IDLE | 1.26 | 2.29 | 1.56 | 0.01 | 93992.05 | 3.61 | skipped_fast |
| EDELUSDT | IDLE | 1.6 | 2.83 | 2.47 | -0.0 | 68759.58 | 37.52 | skipped_fast |
| REDUSDT | IDLE | 1.39 | 2.75 | 0.24 | 0.01 | 61782.48 | 12.48 | skipped_fast |
| HBARUSDT | IDLE | 0.86 | 1.61 | 0.76 | 0.01 | 422441.87 | 1.23 | skipped_fast |
| KITEUSDT | IDLE | 1.13 | 1.99 | 1.78 | -0.03 | 65361.87 | 8.64 | skipped_fast |
| QNTUSDT | IDLE | 1.55 | 2.79 | 2.05 | 0.03 | 39935.74 | 6.08 | skipped_fast |
| TELUSDT | IDLE | 0.83 | 1.47 | 1.22 | 0.0 | 71185.17 | 35.17 | skipped_fast |
| RWAUSDT | IDLE | 0.6 | 1.07 | 0.92 | 0.0 | 53040.88 | 14.3 | skipped_fast |
| MNSRYUSDT | IDLE | 0.6 | 1.15 | 0.32 | 0.02 | 42620.46 | 18.76 | skipped_fast |
| FLUIDUSDT | IDLE | 0.47 | 0.91 | 0.14 | 0.02 | 353.17 | 22.09 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
