# Hulk DIGEST — 2026-09-05T16:29:30Z

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
| XRPUSDT | IDLE | 0.68 | 1.28 | 0.56 | 0.01 | 21472648.96 | 1.42 | skipped_fast |
| ETHUSDT | IDLE | 0.29 | 0.56 | 0.09 | 0.0 | 171824878.58 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.22 | 0.43 | 0.06 | 0.0 | 341295991.01 | 0.0 | skipped_fast |
| CHIPUSDT | IDLE | 2.2 | 7.88 | 0.0 | 0.1 | 425771.11 | 5.02 | skipped_fast |
| KITEUSDT | IDLE | 2.68 | 6.21 | 4.89 | -0.03 | 60863.22 | 12.67 | skipped_fast |
| PYTHUSDT | IDLE | 1.61 | 2.99 | 1.51 | 0.02 | 329669.31 | 1.83 | skipped_fast |
| CCUSDT | IDLE | 1.37 | 2.71 | 0.19 | 0.03 | 282673.78 | 7.2 | skipped_fast |
| RIZEUSDT | IDLE | 1.23 | 11.89 | 3.5 | 0.13 | 153624.68 | 16.49 | skipped_fast |
| WUSDT | IDLE | 1.44 | 2.58 | 2.02 | 0.03 | 158044.71 | 12.13 | skipped_fast |
| ZBCNUSDT | IDLE | 1.22 | 2.18 | 1.77 | -0.0 | 183388.11 | 10.07 | skipped_fast |
| BIOUSDT | IDLE | 1.47 | 2.86 | 0.5 | 0.04 | 78566.52 | 7.17 | skipped_fast |
| REDUSDT | IDLE | 1.39 | 2.48 | 1.99 | 0.02 | 62135.41 | 8.81 | skipped_fast |
| RWAINCUSDT | IDLE | 1.78 | 3.17 | 2.6 | -0.02 | 7443.22 | 32.41 | skipped_fast |
| EDELUSDT | IDLE | 0.27 | 4.89 | 2.24 | -0.01 | 183312.79 | 28.61 | skipped_fast |
| HBARUSDT | IDLE | 1.02 | 1.81 | 1.5 | 0.04 | 309499.72 | 1.25 | skipped_fast |
| RWAUSDT | IDLE | 1.23 | 2.37 | 0.56 | 0.03 | 51719.75 | 28.21 | skipped_fast |
| TELUSDT | IDLE | 1.11 | 2.14 | 0.52 | -0.01 | 69872.86 | 46.76 | skipped_fast |
| QNTUSDT | IDLE | 0.6 | 1.15 | 0.4 | -0.0 | 39834.04 | 4.68 | skipped_fast |
| FLUIDUSDT | IDLE | 0.81 | 1.43 | 1.31 | 0.01 | 867.92 | 21.82 | skipped_fast |
| MNSRYUSDT | IDLE | 0.16 | 0.3 | 0.07 | 0.0 | 38240.9 | 27.3 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
