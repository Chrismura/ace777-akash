# Hulk DIGEST — 2026-08-28T15:08:20Z

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
| XRPUSDT | IDLE | 1.95 | 3.74 | 1.04 | -0.02 | 52002842.01 | 2.11 | skipped_fast |
| CHIPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.62 | 17.46 | 1.67 | 0.11 | 966391.24 | 15.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.71 | 3.77 | 1.59 | -0.03 | 1149596.62 | 2.1 | skipped_fast |
| QAITUSDT | IDLE | 2.44 | 32.58 | 21.1 | -0.19 | 72097.63 | 72.39 | skipped_fast |
| CCUSDT | IDLE | 1.36 | 2.53 | 1.22 | -0.04 | 400948.81 | 6.24 | skipped_fast |
| ZBCNUSDT | IDLE | 1.9 | 4.16 | 1.19 | -0.02 | 235324.09 | 15.04 | skipped_fast |
| WUSDT | IDLE | 1.7 | 3.16 | 1.65 | -0.03 | 205231.79 | 2.13 | skipped_fast |
| BIOUSDT | IDLE | 1.56 | 2.96 | 1.04 | -0.03 | 95088.31 | 3.5 | skipped_fast |
| REDUSDT | IDLE | 1.54 | 2.74 | 2.32 | -0.04 | 73502.06 | 10.41 | skipped_fast |
| RWAUSDT | IDLE | 3.05 | 5.99 | 0.72 | 0.04 | 54805.9 | 24.05 | skipped_fast |
| KITEUSDT | IDLE | 1.46 | 2.81 | 0.72 | -0.0 | 73105.52 | 11.84 | skipped_fast |
| RIZEUSDT | IDLE | 1.39 | 7.12 | 0.23 | -0.03 | 85303.37 | 54.17 | skipped_fast |
| HBARUSDT | IDLE | 1.32 | 2.45 | 1.21 | -0.03 | 311204.27 | 1.3 | skipped_fast |
| RWAINCUSDT | IDLE | 1.34 | 4.22 | 3.25 | -0.02 | 19066.46 | 104.14 | skipped_fast |
| EDELUSDT | IDLE | 0.65 | 2.88 | 2.38 | -0.12 | 58684.45 | 43.57 | skipped_fast |
| FLUIDUSDT | IDLE | 2.03 | 3.81 | 1.62 | -0.03 | 4276.02 | 21.7 | skipped_fast |
| TELUSDT | IDLE | 1.3 | 2.96 | 2.12 | -0.04 | 134813.86 | 11.09 | skipped_fast |
| QNTUSDT | IDLE | 1.62 | 2.97 | 1.83 | -0.0 | 48910.19 | 4.81 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
