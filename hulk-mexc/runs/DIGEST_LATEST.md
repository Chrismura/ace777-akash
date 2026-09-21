# Hulk DIGEST — 2026-09-21T14:04:13Z

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
| BTCUSDT | IDLE | 1.31 | 2.55 | 0.45 | 0.06 | 817887761.25 | 0.0 | skipped_fast |
| ETHUSDT | IDLE | 1.12 | 2.15 | 0.66 | 0.06 | 574980988.54 | 0.99 | skipped_fast |
| XRPUSDT | IDLE | 0.99 | 2.03 | 0.75 | 0.08 | 74224986.12 | 2.02 | skipped_fast |
| HBARUSDT | IDLE | 2.43 | 5.58 | 2.03 | 0.05 | 1478899.11 | 1.1 | skipped_fast |
| CCUSDT | IDLE | 1.58 | 4.42 | 3.07 | 0.1 | 588875.03 | 0.87 | skipped_fast |
| PYTHUSDT | IDLE | 1.09 | 2.71 | 0.78 | 0.1 | 641318.2 | 4.65 | skipped_fast |
| WUSDT | IDLE | 0.86 | 2.88 | 1.61 | 0.1 | 630191.45 | 10.05 | skipped_fast |
| CHIPUSDT | IDLE | 2.22 | 11.98 | 6.51 | 0.15 | 122885.16 | 21.19 | skipped_fast |
| ZBCNUSDT | IDLE | 2.02 | 5.37 | 2.03 | 0.07 | 204171.32 | 16.06 | skipped_fast |
| RIZEUSDT | IDLE | 2.05 | 15.81 | 5.6 | -0.13 | 48141.44 | 94.59 | skipped_fast |
| EDELUSDT | IDLE | 0.66 | 8.0 | 2.6 | 0.46 | 241177.38 | 20.24 | skipped_fast |
| BIOUSDT | IDLE | 1.45 | 3.41 | 1.84 | 0.08 | 89205.01 | 10.38 | skipped_fast |
| REDUSDT | IDLE | 1.36 | 2.6 | 0.8 | 0.02 | 103923.13 | 16.92 | skipped_fast |
| RWAINCUSDT | IDLE | 1.58 | 3.33 | 0.0 | 0.02 | 5157.71 | 5.76 | skipped_fast |
| KITEUSDT | IDLE | 1.32 | 2.44 | 1.35 | 0.06 | 66283.34 | 12.56 | skipped_fast |
| QNTUSDT | IDLE | 1.33 | 2.58 | 0.57 | 0.06 | 127399.73 | 7.4 | skipped_fast |
| TELUSDT | IDLE | 1.84 | 5.1 | 1.52 | 0.1 | 94251.49 | 67.67 | skipped_fast |
| RWAUSDT | IDLE | 0.93 | 1.77 | 0.58 | 0.02 | 56085.89 | 21.84 | skipped_fast |
| FLUIDUSDT | IDLE | 1.23 | 2.71 | 0.15 | 0.08 | 10333.13 | 45.02 | skipped_fast |
| MNSRYUSDT | IDLE | 0.84 | 1.63 | 0.36 | 0.03 | 42259.9 | 20.66 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
