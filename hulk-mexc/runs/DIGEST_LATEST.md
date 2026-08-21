# Hulk DIGEST — 2026-08-21T23:11:18Z

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
| PYTHUSDT | IDLE | 1.72 | 6.39 | 0.46 | 0.12 | 5994221.71 | 2.03 | skipped_fast |
| XRPUSDT | IDLE | 1.75 | 6.77 | 0.34 | 0.15 | 138508114.1 | 2.07 | skipped_fast |
| CCUSDT | IDLE | 1.9 | 7.42 | 0.91 | 0.13 | 666483.54 | 8.9 | skipped_fast |
| HBARUSDT | IDLE | 2.39 | 5.24 | 0.19 | 0.09 | 890369.39 | 1.25 | skipped_fast |
| ZBCNUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.52 | 10.14 | 0.3 | 0.15 | 511376.15 | 23.82 | skipped_fast |
| WUSDT | IDLE | 2.75 | 6.91 | 1.38 | 0.08 | 374885.12 | 17.42 | skipped_fast |
| CHIPUSDT | IDLE | 1.16 | 3.56 | 1.03 | 0.05 | 544780.26 | 3.07 | skipped_fast |
| BIOUSDT | IDLE | 2.31 | 5.04 | 1.41 | 0.02 | 187465.16 | 6.24 | skipped_fast |
| EDELUSDT | IDLE | 2.53 | 5.5 | 0.54 | -0.03 | 82514.69 | 21.81 | skipped_fast |
| RWAINCUSDT | IDLE | 2.18 | 4.07 | 1.96 | 0.02 | 10220.57 | 16.16 | skipped_fast |
| REDUSDT | IDLE | 0.88 | 7.3 | 5.29 | 0.18 | 157411.96 | 10.56 | skipped_fast |
| QAITUSDT | IDLE | 2.27 | 4.22 | 2.14 | -0.02 | 3921.68 | 43.69 | skipped_fast |
| TELUSDT | IDLE | 2.66 | 6.51 | 0.26 | 0.07 | 185005.69 | 46.36 | skipped_fast |
| QNTUSDT | IDLE | 2.51 | 5.22 | 0.06 | 0.07 | 105778.29 | 1.5 | skipped_fast |
| KITEUSDT | IDLE | 1.11 | 3.12 | 1.15 | 0.09 | 61576.24 | 11.12 | skipped_fast |
| RWAUSDT | IDLE | 1.02 | 2.0 | 0.33 | 0.04 | 54423.15 | 8.19 | skipped_fast |
| FLUIDUSDT | IDLE | 0.92 | 2.35 | 0.18 | 0.1 | 4226.13 | 21.19 | skipped_fast |
| RIZEUSDT | IDLE | 1.51 | 7.18 | 0.0 | 0.11 | 58705.47 | 370.09 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
