# Hulk DIGEST — 2026-08-22T05:03:06Z

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
| PYTHUSDT | IDLE | 3.2 | 15.45 | 2.69 | 0.17 | 13479506.46 | 16.57 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.45 | 18.29 | 0.11 | 0.28 | 181736717.52 | 3.57 | skipped_fast |
| HBARUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.55 | 10.13 | 0.15 | 0.15 | 1116979.35 | 1.15 | skipped_fast |
| CCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.15 | 11.56 | 1.22 | 0.2 | 742867.62 | 9.84 | skipped_fast |
| CHIPUSDT | IDLE | 2.78 | 5.36 | 1.29 | 0.02 | 446758.89 | 2.99 | skipped_fast |
| WUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.13 | 8.22 | 0.81 | 0.15 | 449343.22 | 13.44 | skipped_fast |
| BIOUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.03 | 9.0 | 0.23 | 0.1 | 203490.45 | 2.9 | skipped_fast |
| ZBCNUSDT | IDLE | 1.5 | 4.29 | 0.68 | 0.11 | 537444.77 | 13.7 | skipped_fast |
| QNTUSDT | IDLE | 2.72 | 9.16 | 3.91 | 0.1 | 187008.38 | 7.34 | skipped_fast |
| RWAINCUSDT | IDLE | 2.48 | 4.48 | 3.24 | 0.01 | 10345.47 | 21.57 | skipped_fast |
| KITEUSDT | IDLE | 1.83 | 6.62 | 0.55 | 0.14 | 68338.05 | 9.64 | skipped_fast |
| REDUSDT | IDLE | 0.99 | 7.96 | 5.48 | 0.19 | 157922.74 | 16.9 | skipped_fast |
| EDELUSDT | IDLE | 1.57 | 3.28 | 1.31 | -0.02 | 80245.14 | 44.4 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3417.27 | 35.86 | skipped_fast |
| RIZEUSDT | IDLE | 1.08 | 4.41 | 3.58 | 0.09 | 58617.29 | 46.02 | skipped_fast |
| TELUSDT | IDLE | 1.94 | 5.52 | 0.2 | 0.11 | 184090.71 | 44.61 | skipped_fast |
| RWAUSDT | IDLE | 1.65 | 3.29 | 0.08 | 0.07 | 56759.68 | 15.96 | skipped_fast |
| FLUIDUSDT | IDLE | 0.88 | 2.07 | 2.03 | 0.08 | 3692.42 | 22.04 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
