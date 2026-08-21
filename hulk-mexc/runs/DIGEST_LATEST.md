# Hulk DIGEST — 2026-08-21T23:20:44Z

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
| PYTHUSDT | IDLE | 1.72 | 6.39 | 0.44 | 0.12 | 6040890.13 | 2.03 | skipped_fast |
| XRPUSDT | IDLE | 1.79 | 7.09 | 0.14 | 0.15 | 139027871.39 | 2.75 | skipped_fast |
| ZBCNUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.8 | 11.25 | 0.38 | 0.16 | 512511.31 | 18.89 | skipped_fast |
| HBARUSDT | IDLE | 2.53 | 6.15 | 0.01 | 0.1 | 895649.34 | 1.24 | skipped_fast |
| CCUSDT | IDLE | 1.92 | 7.42 | 1.25 | 0.13 | 644644.77 | 8.02 | skipped_fast |
| WUSDT | IDLE | 2.74 | 6.91 | 1.29 | 0.08 | 377604.89 | 9.22 | skipped_fast |
| CHIPUSDT | IDLE | 1.18 | 3.56 | 1.46 | 0.04 | 547988.74 | 3.09 | skipped_fast |
| BIOUSDT | IDLE | 2.3 | 5.04 | 1.14 | 0.03 | 187893.23 | 3.11 | skipped_fast |
| EDELUSDT | IDLE | 2.53 | 5.5 | 0.65 | -0.03 | 82500.72 | 21.83 | skipped_fast |
| RIZEUSDT | IDLE | 2.14 | 9.82 | 2.44 | 0.11 | 59593.95 | 21.64 | skipped_fast |
| RWAINCUSDT | IDLE | 2.2 | 4.07 | 2.22 | 0.02 | 10178.81 | 32.38 | skipped_fast |
| TELUSDT | IDLE | 2.7 | 6.62 | 0.15 | 0.07 | 185030.42 | 35.96 | skipped_fast |
| REDUSDT | IDLE | 0.87 | 7.3 | 4.53 | 0.19 | 157442.87 | 17.73 | skipped_fast |
| QAITUSDT | IDLE | 2.27 | 4.22 | 2.14 | -0.02 | 3921.68 | 67.45 | skipped_fast |
| QNTUSDT | IDLE | 2.51 | 5.27 | 0.04 | 0.07 | 118715.62 | 1.5 | skipped_fast |
| KITEUSDT | IDLE | 1.12 | 3.12 | 1.38 | 0.09 | 61563.96 | 9.29 | skipped_fast |
| RWAUSDT | IDLE | 1.07 | 2.08 | 0.41 | 0.04 | 54476.24 | 8.2 | skipped_fast |
| FLUIDUSDT | IDLE | 0.92 | 2.35 | 0.18 | 0.1 | 4226.13 | 21.13 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
