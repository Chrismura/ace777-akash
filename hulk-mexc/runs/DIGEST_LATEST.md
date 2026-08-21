# Hulk DIGEST — 2026-08-21T21:58:08Z

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
| PYTHUSDT | IDLE | 1.22 | 4.74 | 0.29 | 0.1 | 5687141.92 | 2.05 | skipped_fast |
| XRPUSDT | IDLE | 1.09 | 3.73 | 0.62 | 0.12 | 129708137.42 | 1.42 | skipped_fast |
| HBARUSDT | IDLE | 2.11 | 4.71 | 0.68 | 0.08 | 834158.0 | 1.27 | skipped_fast |
| CHIPUSDT | IDLE | 1.87 | 5.61 | 3.49 | 0.04 | 526899.58 | 6.18 | skipped_fast |
| ZBCNUSDT | IDLE | 1.91 | 8.19 | 2.5 | 0.11 | 492872.82 | 32.23 | skipped_fast |
| CCUSDT | IDLE | 1.3 | 3.92 | 0.0 | 0.11 | 636561.77 | 9.1 | skipped_fast |
| WUSDT | IDLE | 2.1 | 4.19 | 0.1 | 0.07 | 367632.47 | 18.68 | skipped_fast |
| BIOUSDT | IDLE | 2.36 | 5.2 | 1.11 | 0.04 | 186104.21 | 3.11 | skipped_fast |
| REDUSDT | IDLE | 1.33 | 11.01 | 8.38 | 0.19 | 153784.95 | 8.92 | skipped_fast |
| TELUSDT | IDLE | 2.55 | 6.45 | 1.28 | 0.05 | 191798.77 | 20.8 | skipped_fast |
| QAITUSDT | IDLE | 2.37 | 4.38 | 2.37 | -0.02 | 3827.91 | 59.7 | skipped_fast |
| EDELUSDT | IDLE | 1.99 | 4.12 | 1.87 | -0.05 | 83450.0 | 66.74 | skipped_fast |
| RWAINCUSDT | IDLE | 2.22 | 4.3 | 0.9 | 0.03 | 10238.87 | 53.39 | skipped_fast |
| KITEUSDT | IDLE | 1.26 | 4.0 | 1.04 | 0.11 | 61287.48 | 11.01 | skipped_fast |
| RIZEUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.25 | 11.42 | 1.96 | 0.05 | 56173.82 | 189.49 | skipped_fast |
| QNTUSDT | IDLE | 1.34 | 2.65 | 0.17 | 0.05 | 62404.75 | 3.08 | skipped_fast |
| RWAUSDT | IDLE | 0.67 | 1.33 | 0.08 | 0.04 | 54149.84 | 8.23 | skipped_fast |
| FLUIDUSDT | IDLE | 0.51 | 1.15 | 0.09 | 0.09 | 4171.26 | 21.78 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
