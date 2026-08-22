# Hulk DIGEST — 2026-08-22T02:12:09Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.42 | 8.42 | 1.04 | 0.14 | 6910683.44 | 1.95 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.28 | 10.03 | 0.13 | 0.17 | 154217613.4 | 1.99 | skipped_fast |
| HBARUSDT | IDLE | 2.3 | 4.9 | 0.36 | 0.08 | 954768.66 | 1.24 | skipped_fast |
| ZBCNUSDT | IDLE | 2.49 | 9.63 | 2.95 | 0.08 | 545855.04 | 25.69 | skipped_fast |
| CCUSDT | IDLE | 1.68 | 6.1 | 0.3 | 0.14 | 654208.97 | 7.86 | skipped_fast |
| CHIPUSDT | IDLE | 1.8 | 4.16 | 0.03 | 0.01 | 514189.95 | 6.05 | skipped_fast |
| BIOUSDT | IDLE | 2.98 | 6.88 | 0.27 | 0.09 | 190538.14 | 2.97 | skipped_fast |
| WUSDT | IDLE | 1.74 | 4.41 | 0.5 | 0.08 | 399994.48 | 4.04 | skipped_fast |
| EDELUSDT | IDLE | 2.37 | 5.02 | 1.41 | -0.01 | 79571.3 | 22.0 | skipped_fast |
| RIZEUSDT | IDLE | 1.97 | 8.52 | 3.77 | 0.11 | 61164.98 | 45.71 | skipped_fast |
| REDUSDT | IDLE | 1.0 | 8.27 | 6.14 | 0.17 | 156764.42 | 9.71 | skipped_fast |
| QNTUSDT | IDLE | 2.3 | 4.89 | 1.16 | 0.07 | 171291.6 | 9.05 | skipped_fast |
| KITEUSDT | IDLE | 1.34 | 4.09 | 0.49 | 0.12 | 61399.08 | 10.79 | skipped_fast |
| QAITUSDT | IDLE | 1.78 | 3.57 | 0.0 | 0.01 | 3870.41 | 31.31 | skipped_fast |
| RWAINCUSDT | IDLE | 1.82 | 3.27 | 2.48 | 0.01 | 9604.71 | 59.6 | skipped_fast |
| TELUSDT | IDLE | 2.15 | 5.11 | 1.23 | 0.04 | 179079.2 | 77.82 | skipped_fast |
| FLUIDUSDT | IDLE | 1.44 | 3.69 | 2.03 | 0.07 | 4710.05 | 20.47 | skipped_fast |
| RWAUSDT | IDLE | 1.07 | 2.08 | 0.41 | 0.04 | 54771.02 | 16.39 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
