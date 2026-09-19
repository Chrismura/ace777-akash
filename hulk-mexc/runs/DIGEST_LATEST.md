# Hulk DIGEST — 2026-09-19T17:02:01Z

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
| XRPUSDT | IDLE | 1.08 | 1.97 | 1.26 | 0.04 | 60578058.42 | 2.09 | skipped_fast |
| BTCUSDT | IDLE | 0.47 | 0.91 | 0.16 | 0.01 | 511707837.65 | 0.0 | skipped_fast |
| ETHUSDT | IDLE | 0.46 | 0.9 | 0.13 | 0.02 | 366768961.97 | 0.08 | skipped_fast |
| WUSDT | IDLE | 2.4 | 4.42 | 2.56 | 0.02 | 660182.36 | 6.29 | skipped_fast |
| ZBCNUSDT | IDLE | 3.6 | 14.49 | 3.66 | 0.12 | 224835.74 | 35.21 | skipped_fast |
| PYTHUSDT | IDLE | 1.09 | 2.09 | 0.62 | 0.01 | 675765.94 | 4.94 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 4.39 | 9.89 | 6.28 | -0.03 | 5773.78 | 90.5 | skipped_fast |
| CCUSDT | IDLE | 1.38 | 2.69 | 0.41 | 0.04 | 355425.92 | 11.48 | skipped_fast |
| CHIPUSDT | IDLE | 1.9 | 4.45 | 3.04 | 0.01 | 127605.93 | 20.52 | skipped_fast |
| BIOUSDT | IDLE | 1.7 | 3.09 | 2.09 | 0.04 | 84865.45 | 7.12 | skipped_fast |
| HBARUSDT | IDLE | 1.04 | 2.05 | 0.24 | 0.05 | 530741.87 | 1.22 | skipped_fast |
| RIZEUSDT | IDLE | 1.87 | 8.17 | 6.13 | 0.03 | 38361.67 | 101.24 | skipped_fast |
| EDELUSDT | IDLE | 0.85 | 4.81 | 3.38 | -0.15 | 171262.96 | 28.72 | skipped_fast |
| REDUSDT | IDLE | 0.64 | 2.7 | 2.19 | 0.02 | 133506.58 | 8.15 | skipped_fast |
| KITEUSDT | IDLE | 1.08 | 2.05 | 0.79 | 0.06 | 70952.23 | 11.19 | skipped_fast |
| TELUSDT | IDLE | 1.19 | 3.73 | 1.41 | -0.01 | 128441.06 | 39.09 | skipped_fast |
| FLUIDUSDT | IDLE | 1.26 | 3.11 | 0.0 | 0.12 | 9838.49 | 21.43 | skipped_fast |
| RWAUSDT | IDLE | 0.79 | 1.48 | 0.66 | 0.0 | 54040.53 | 14.65 | skipped_fast |
| QNTUSDT | IDLE | 0.66 | 1.18 | 0.94 | 0.03 | 47107.44 | 3.06 | skipped_fast |
| MNSRYUSDT | IDLE | 0.83 | 1.52 | 0.98 | 0.0 | 36561.19 | 62.32 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
