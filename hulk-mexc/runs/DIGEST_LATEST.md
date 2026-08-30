# Hulk DIGEST — 2026-08-30T08:07:58Z

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
| XRPUSDT | IDLE | 0.66 | 1.21 | 0.77 | 0.01 | 16090544.4 | 0.72 | skipped_fast |
| CHIPUSDT | IDLE | 2.7 | 4.83 | 3.74 | -0.03 | 701395.66 | 2.52 | skipped_fast |
| CCUSDT | IDLE | 1.22 | 2.21 | 1.79 | 0.07 | 303576.06 | 9.28 | skipped_fast |
| PYTHUSDT | IDLE | 0.57 | 1.01 | 0.84 | 0.02 | 299669.62 | 2.11 | skipped_fast |
| REDUSDT | IDLE | 1.57 | 2.8 | 2.3 | -0.0 | 76336.3 | 11.89 | skipped_fast |
| BIOUSDT | IDLE | 1.39 | 2.59 | 1.3 | -0.01 | 71275.53 | 3.66 | skipped_fast |
| WUSDT | IDLE | 0.8 | 1.43 | 1.18 | 0.0 | 200256.92 | 10.92 | skipped_fast |
| ZBCNUSDT | IDLE | 0.78 | 1.55 | 0.05 | -0.02 | 170978.49 | 11.42 | skipped_fast |
| KITEUSDT | IDLE | 0.79 | 1.87 | 1.4 | 0.01 | 70147.38 | 19.47 | skipped_fast |
| EDELUSDT | IDLE | 0.3 | 5.46 | 3.09 | 0.13 | 122447.22 | 42.86 | skipped_fast |
| RIZEUSDT | IDLE | 0.9 | 3.72 | 1.07 | -0.04 | 43673.5 | 58.56 | skipped_fast |
| RWAINCUSDT | IDLE | 0.91 | 1.59 | 1.57 | -0.03 | 1551.94 | 79.32 | skipped_fast |
| HBARUSDT | IDLE | 0.63 | 1.18 | 0.52 | 0.0 | 142017.5 | 1.34 | skipped_fast |
| QNTUSDT | IDLE | 0.56 | 1.01 | 0.73 | 0.01 | 33690.99 | 3.25 | skipped_fast |
| RWAUSDT | IDLE | 0.68 | 1.32 | 0.24 | 0.01 | 53128.51 | 24.5 | skipped_fast |
| TELUSDT | IDLE | 0.66 | 1.19 | 0.82 | -0.03 | 74306.05 | 35.61 | skipped_fast |
| FLUIDUSDT | IDLE | 0.01 | 0.02 | 0.02 | 0.01 | 1354.07 | 21.49 | skipped_fast |
| QAITUSDT | ERR | — | — | — | — | — | — | HTTP Error 400: Bad Request |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
