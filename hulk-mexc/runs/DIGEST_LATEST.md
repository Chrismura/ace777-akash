# Hulk DIGEST — 2026-08-22T04:58:05Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.0 | 15.45 | 1.67 | 0.19 | 12992941.49 | 49.23 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.43 | 17.46 | 0.77 | 0.26 | 180295440.6 | 5.43 | skipped_fast |
| HBARUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.53 | 9.87 | 0.13 | 0.15 | 1089463.31 | 2.31 | skipped_fast |
| CCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.13 | 11.56 | 1.15 | 0.2 | 741619.0 | 7.37 | skipped_fast |
| CHIPUSDT | IDLE | 2.8 | 5.36 | 1.62 | 0.02 | 453845.01 | 2.99 | skipped_fast |
| WUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.14 | 8.62 | 0.87 | 0.15 | 448293.12 | 8.66 | skipped_fast |
| BIOUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.98 | 8.28 | 0.26 | 0.08 | 201771.24 | 2.91 | skipped_fast |
| ZBCNUSDT | IDLE | 1.42 | 4.29 | 0.93 | 0.11 | 538015.97 | 32.3 | skipped_fast |
| RWAINCUSDT | IDLE | 2.48 | 4.48 | 3.24 | 0.01 | 10345.47 | 21.57 | skipped_fast |
| QNTUSDT | IDLE | 2.58 | 9.16 | 4.02 | 0.1 | 186807.95 | 14.71 | skipped_fast |
| EDELUSDT | IDLE | 1.98 | 4.07 | 2.06 | -0.03 | 80245.04 | 22.2 | skipped_fast |
| RIZEUSDT | IDLE | 1.84 | 7.71 | 4.68 | 0.09 | 58618.63 | 46.02 | skipped_fast |
| KITEUSDT | IDLE | 1.75 | 6.71 | 0.02 | 0.15 | 68346.0 | 13.96 | skipped_fast |
| REDUSDT | IDLE | 0.94 | 7.96 | 4.71 | 0.21 | 157920.34 | 11.96 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3417.27 | 35.86 | skipped_fast |
| TELUSDT | IDLE | 1.95 | 5.52 | 0.44 | 0.1 | 183440.29 | 24.8 | skipped_fast |
| RWAUSDT | IDLE | 1.56 | 3.13 | 0.0 | 0.07 | 56587.82 | 15.99 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.08 | 3692.42 | 20.74 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
