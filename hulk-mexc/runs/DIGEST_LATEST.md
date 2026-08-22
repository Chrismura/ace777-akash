# Hulk DIGEST — 2026-08-22T05:03:33Z

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
| PYTHUSDT | IDLE | 3.22 | 15.45 | 3.42 | 0.17 | 13613087.05 | 20.41 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.5 | 19.29 | 0.55 | 0.29 | 182403112.23 | 6.51 | skipped_fast |
| HBARUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.55 | 10.13 | 0.17 | 0.16 | 1117260.37 | 2.31 | skipped_fast |
| CCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.14 | 11.56 | 1.15 | 0.2 | 743868.5 | 4.91 | skipped_fast |
| CHIPUSDT | IDLE | 2.8 | 5.36 | 1.59 | 0.01 | 446759.3 | 2.99 | skipped_fast |
| WUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.13 | 8.22 | 0.68 | 0.15 | 449648.59 | 14.39 | skipped_fast |
| BIOUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.04 | 9.0 | 0.49 | 0.09 | 203530.26 | 2.9 | skipped_fast |
| ZBCNUSDT | IDLE | 1.5 | 4.29 | 0.64 | 0.11 | 537608.48 | 22.68 | skipped_fast |
| QNTUSDT | IDLE | 2.72 | 9.16 | 3.91 | 0.1 | 186987.41 | 7.33 | skipped_fast |
| RWAINCUSDT | IDLE | 2.48 | 4.48 | 3.24 | 0.01 | 10345.47 | 21.57 | skipped_fast |
| KITEUSDT | IDLE | 1.83 | 6.62 | 0.55 | 0.14 | 68374.42 | 14.0 | skipped_fast |
| REDUSDT | IDLE | 1.0 | 7.96 | 6.15 | 0.18 | 158120.6 | 46.97 | skipped_fast |
| EDELUSDT | IDLE | 1.58 | 3.28 | 1.42 | -0.02 | 80245.22 | 33.31 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3417.27 | 35.86 | skipped_fast |
| RIZEUSDT | IDLE | 1.08 | 4.41 | 3.58 | 0.09 | 58619.06 | 46.02 | skipped_fast |
| TELUSDT | IDLE | 1.95 | 5.52 | 0.39 | 0.1 | 184082.42 | 49.55 | skipped_fast |
| RWAUSDT | IDLE | 1.65 | 3.29 | 0.08 | 0.07 | 56783.13 | 23.93 | skipped_fast |
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
