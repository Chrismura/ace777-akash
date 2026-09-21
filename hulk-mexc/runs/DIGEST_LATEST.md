# Hulk DIGEST — 2026-09-21T20:04:27Z

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
| XRPUSDT | IDLE | 1.08 | 2.32 | 0.51 | 0.07 | 89287874.03 | 1.99 | skipped_fast |
| ETHUSDT | IDLE | 0.89 | 1.75 | 0.25 | 0.05 | 703801473.68 | 1.05 | skipped_fast |
| BTCUSDT | IDLE | 0.75 | 1.46 | 0.22 | 0.07 | 995832212.01 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.36 | 5.49 | 4.39 | 0.04 | 673275.4 | 6.29 | skipped_fast |
| HBARUSDT | IDLE | 1.46 | 3.42 | 2.02 | 0.07 | 1141629.56 | 1.09 | skipped_fast |
| WUSDT | IDLE | 1.54 | 3.46 | 1.85 | 0.02 | 596288.44 | 5.96 | skipped_fast |
| CCUSDT | IDLE | 1.06 | 2.76 | 1.23 | 0.07 | 575973.34 | 6.88 | skipped_fast |
| ZBCNUSDT | IDLE | 2.24 | 6.77 | 3.4 | 0.07 | 249705.26 | 16.98 | skipped_fast |
| REDUSDT | IDLE | 1.59 | 2.87 | 2.01 | -0.0 | 104781.79 | 8.6 | skipped_fast |
| BIOUSDT | IDLE | 1.55 | 2.88 | 1.44 | 0.04 | 100666.86 | 13.87 | skipped_fast |
| CHIPUSDT | IDLE | 1.13 | 5.87 | 1.21 | 0.12 | 141859.38 | 16.95 | skipped_fast |
| EDELUSDT | IDLE | 0.72 | 4.58 | 2.35 | 0.24 | 236821.4 | 22.73 | skipped_fast |
| KITEUSDT | IDLE | 1.38 | 2.49 | 1.84 | 0.03 | 76785.79 | 11.0 | skipped_fast |
| RWAINCUSDT | IDLE | 0.9 | 1.56 | 1.54 | 0.03 | 12110.31 | 5.78 | skipped_fast |
| TELUSDT | IDLE | 1.86 | 5.24 | 0.84 | 0.09 | 99646.65 | 36.14 | skipped_fast |
| QNTUSDT | IDLE | 1.36 | 2.53 | 1.26 | 0.03 | 107869.39 | 5.99 | skipped_fast |
| RIZEUSDT | IDLE | 0.77 | 6.2 | 0.39 | -0.1 | 48422.07 | 94.94 | skipped_fast |
| FLUIDUSDT | IDLE | 0.87 | 1.81 | 0.8 | 0.08 | 9952.77 | 21.54 | skipped_fast |
| RWAUSDT | IDLE | 0.67 | 1.24 | 0.72 | 0.01 | 56383.61 | 21.73 | skipped_fast |
| MNSRYUSDT | IDLE | 0.17 | 0.32 | 0.17 | 0.03 | 42688.04 | 12.87 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
