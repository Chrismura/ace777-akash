# Hulk DIGEST — 2026-09-17T14:16:29Z

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
| ETHUSDT | IDLE | 1.07 | 2.14 | 0.05 | 0.04 | 389576368.08 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.99 | 1.91 | 0.42 | 0.03 | 57204795.36 | 0.76 | skipped_fast |
| BTCUSDT | IDLE | 0.76 | 1.48 | 0.31 | 0.02 | 501210285.01 | 0.87 | skipped_fast |
| CCUSDT | IDLE | 1.05 | 3.81 | 1.81 | 0.11 | 663481.23 | 8.91 | skipped_fast |
| PYTHUSDT | IDLE | 1.57 | 3.19 | 0.25 | 0.06 | 556244.75 | 5.44 | skipped_fast |
| EDELUSDT | IDLE | 2.43 | 7.02 | 3.05 | -0.06 | 187944.01 | 16.13 | skipped_fast |
| REDUSDT | IDLE | 2.72 | 5.24 | 4.27 | 0.02 | 64278.53 | 18.43 | skipped_fast |
| CHIPUSDT | IDLE | 1.93 | 6.15 | 1.13 | 0.08 | 142497.38 | 20.36 | skipped_fast |
| RIZEUSDT | IDLE | 1.89 | 13.91 | 8.08 | -0.27 | 46994.33 | 115.65 | skipped_fast |
| ZBCNUSDT | IDLE | 1.37 | 2.73 | 0.08 | 0.04 | 184576.88 | 23.81 | skipped_fast |
| RWAINCUSDT | IDLE | 1.86 | 3.46 | 1.73 | -0.0 | 22509.53 | 5.91 | skipped_fast |
| HBARUSDT | IDLE | 0.91 | 1.8 | 0.17 | 0.03 | 536710.3 | 3.99 | skipped_fast |
| WUSDT | IDLE | 1.09 | 2.46 | 0.0 | 0.07 | 207089.55 | 14.84 | skipped_fast |
| KITEUSDT | IDLE | 0.85 | 2.77 | 2.43 | 0.07 | 67754.45 | 12.46 | skipped_fast |
| BIOUSDT | IDLE | 0.94 | 1.85 | 0.2 | 0.03 | 69725.88 | 11.84 | skipped_fast |
| TELUSDT | IDLE | 1.9 | 3.78 | 0.2 | 0.06 | 92878.05 | 54.09 | skipped_fast |
| QNTUSDT | IDLE | 1.1 | 2.09 | 0.74 | 0.04 | 37065.26 | 6.5 | skipped_fast |
| MNSRYUSDT | IDLE | 0.7 | 1.33 | 0.53 | 0.01 | 39307.89 | 4.21 | skipped_fast |
| RWAUSDT | IDLE | 0.53 | 0.98 | 0.52 | 0.01 | 58285.75 | 14.99 | skipped_fast |
| FLUIDUSDT | IDLE | 0.36 | 0.66 | 0.36 | 0.02 | 844.09 | 21.75 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
