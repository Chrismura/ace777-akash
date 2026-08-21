# Hulk DIGEST — 2026-08-21T23:46:47Z

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
| PYTHUSDT | IDLE | 1.77 | 6.39 | 1.57 | 0.1 | 6176749.36 | 4.1 | skipped_fast |
| XRPUSDT | IDLE | 1.95 | 8.23 | 1.01 | 0.15 | 141772383.28 | 3.43 | skipped_fast |
| ZBCNUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.85 | 11.25 | 1.88 | 0.13 | 514138.84 | 17.74 | skipped_fast |
| HBARUSDT | IDLE | 2.6 | 6.36 | 0.72 | 0.09 | 906716.95 | 2.5 | skipped_fast |
| CCUSDT | IDLE | 1.9 | 7.42 | 0.94 | 0.13 | 643743.24 | 9.77 | skipped_fast |
| WUSDT | IDLE | 2.77 | 6.91 | 1.74 | 0.08 | 378239.07 | 11.31 | skipped_fast |
| CHIPUSDT | IDLE | 1.18 | 3.56 | 1.43 | 0.03 | 546914.34 | 6.17 | skipped_fast |
| BIOUSDT | IDLE | 2.28 | 5.04 | 0.95 | 0.02 | 186562.35 | 3.11 | skipped_fast |
| EDELUSDT | IDLE | 2.59 | 5.5 | 1.52 | -0.02 | 80773.19 | 22.0 | skipped_fast |
| RIZEUSDT | IDLE | 2.21 | 9.82 | 4.81 | 0.12 | 58829.47 | 46.13 | skipped_fast |
| TELUSDT | IDLE | 2.82 | 6.89 | 0.36 | 0.07 | 190302.02 | 25.66 | skipped_fast |
| REDUSDT | IDLE | 0.87 | 7.3 | 4.82 | 0.18 | 157832.09 | 10.49 | skipped_fast |
| RWAINCUSDT | IDLE | 2.13 | 4.07 | 1.27 | 0.02 | 10299.86 | 21.39 | skipped_fast |
| QNTUSDT | IDLE | 2.58 | 5.68 | 0.04 | 0.08 | 147560.89 | 1.49 | skipped_fast |
| QAITUSDT | IDLE | 2.27 | 4.22 | 2.14 | -0.02 | 3921.68 | 67.45 | skipped_fast |
| KITEUSDT | IDLE | 1.1 | 3.12 | 1.0 | 0.1 | 61376.4 | 9.25 | skipped_fast |
| RWAUSDT | IDLE | 1.06 | 2.08 | 0.24 | 0.04 | 54519.53 | 8.18 | skipped_fast |
| FLUIDUSDT | IDLE | 1.09 | 2.87 | 0.66 | 0.1 | 4934.79 | 21.24 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
