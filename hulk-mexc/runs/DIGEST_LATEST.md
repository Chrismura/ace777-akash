# Hulk DIGEST — 2026-08-22T16:03:00Z

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
| PYTHUSDT | IDLE | 1.51 | 7.24 | 1.42 | 0.04 | 51469191.55 | 1.97 | skipped_fast |
| XRPUSDT | IDLE | 1.38 | 7.64 | 5.7 | 0.03 | 215664573.04 | 2.08 | skipped_fast |
| HBARUSDT | IDLE | 0.86 | 3.03 | 2.52 | -0.02 | 1149695.36 | 3.93 | skipped_fast |
| CCUSDT | IDLE | 0.95 | 4.14 | 1.61 | 0.1 | 762839.31 | 10.17 | skipped_fast |
| CHIPUSDT | IDLE | 0.59 | 3.36 | 1.56 | -0.09 | 624838.2 | 6.75 | skipped_fast |
| WUSDT | IDLE | 0.66 | 2.58 | 2.11 | -0.02 | 553408.05 | 9.65 | skipped_fast |
| ZBCNUSDT | IDLE | 1.31 | 3.49 | 1.72 | -0.06 | 319785.66 | 15.91 | skipped_fast |
| BIOUSDT | IDLE | 0.98 | 6.58 | 5.01 | -0.07 | 218593.04 | 3.32 | skipped_fast |
| KITEUSDT | IDLE | 1.89 | 4.35 | 1.56 | 0.03 | 85501.44 | 21.39 | skipped_fast |
| EDELUSDT | IDLE | 1.35 | 2.41 | 1.9 | -0.03 | 75060.95 | 11.4 | skipped_fast |
| REDUSDT | IDLE | 0.53 | 5.67 | 4.5 | -0.16 | 133757.24 | 13.75 | skipped_fast |
| RIZEUSDT | IDLE | 1.32 | 3.21 | 0.25 | 0.03 | 56509.73 | 28.63 | skipped_fast |
| QAITUSDT | IDLE | 1.67 | 3.19 | 0.94 | 0.01 | 2320.37 | 67.45 | skipped_fast |
| QNTUSDT | IDLE | 0.87 | 2.69 | 2.33 | -0.03 | 184286.81 | 4.73 | skipped_fast |
| RWAINCUSDT | IDLE | 0.77 | 1.53 | 0.0 | 0.02 | 8954.22 | 75.23 | skipped_fast |
| TELUSDT | IDLE | 0.97 | 2.37 | 1.52 | -0.0 | 138505.31 | 48.01 | skipped_fast |
| RWAUSDT | IDLE | 0.55 | 1.06 | 0.24 | 0.02 | 56572.28 | 24.36 | skipped_fast |
| FLUIDUSDT | IDLE | 0.0 | 0.0 | 0.0 | -0.04 | 4625.53 | 22.48 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
