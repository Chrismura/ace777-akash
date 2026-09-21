# Hulk DIGEST — 2026-09-21T11:04:14Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| BTCUSDT | IDLE | 2.45 | 4.77 | 0.92 | 0.05 | 659855254.27 | 0.0 | skipped_fast |
| XRPUSDT | IDLE | 2.22 | 4.87 | 0.11 | 0.08 | 63852609.06 | 2.68 | skipped_fast |
| ETHUSDT | IDLE | 2.03 | 3.89 | 1.16 | 0.06 | 489685272.65 | 0.37 | skipped_fast |
| HBARUSDT | IDLE | 1.39 | 3.73 | 0.09 | 0.12 | 1411250.32 | 1.12 | skipped_fast |
| PYTHUSDT | IDLE | 2.28 | 6.81 | 1.37 | 0.11 | 587793.08 | 7.81 | skipped_fast |
| CCUSDT | IDLE | 1.83 | 6.13 | 1.96 | 0.13 | 478048.3 | 11.14 | skipped_fast |
| CHIPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.66 | 15.42 | 0.58 | 0.2 | 113396.64 | 18.08 | skipped_fast |
| WUSDT | IDLE | 0.77 | 2.95 | 0.17 | 0.12 | 592310.13 | 7.47 | skipped_fast |
| ZBCNUSDT | IDLE | 2.3 | 4.81 | 1.54 | 0.07 | 195507.56 | 22.84 | skipped_fast |
| BIOUSDT | IDLE | 2.02 | 5.27 | 0.17 | 0.1 | 79450.91 | 13.68 | skipped_fast |
| TELUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.18 | 8.48 | 0.92 | 0.1 | 92807.91 | 18.56 | skipped_fast |
| KITEUSDT | IDLE | 1.99 | 3.9 | 0.57 | 0.06 | 64828.32 | 11.71 | skipped_fast |
| REDUSDT | IDLE | 1.82 | 3.4 | 1.65 | 0.02 | 80215.22 | 15.75 | skipped_fast |
| EDELUSDT | IDLE | 0.59 | 6.73 | 1.76 | 0.46 | 234988.88 | 24.18 | skipped_fast |
| RIZEUSDT | IDLE | 1.21 | 9.44 | 0.94 | -0.09 | 43761.61 | 47.58 | skipped_fast |
| FLUIDUSDT | IDLE | 2.41 | 5.08 | 1.75 | 0.06 | 9629.62 | 21.26 | skipped_fast |
| RWAINCUSDT | IDLE | 1.09 | 2.03 | 1.05 | 0.01 | 6242.28 | 29.52 | skipped_fast |
| QNTUSDT | IDLE | 1.37 | 2.74 | 0.0 | 0.06 | 119568.97 | 2.98 | skipped_fast |
| MNSRYUSDT | IDLE | 1.07 | 2.09 | 0.28 | 0.03 | 42258.86 | 12.98 | skipped_fast |
| RWAUSDT | IDLE | 0.86 | 1.55 | 1.16 | 0.01 | 56258.49 | 29.37 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
