# Hulk DIGEST — 2026-09-18T18:55:38Z

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
| XRPUSDT | IDLE | 2.9 | 6.26 | 1.12 | 0.07 | 57821581.64 | 3.6 | skipped_fast |
| ETHUSDT | IDLE | 2.64 | 5.22 | 0.36 | 0.07 | 544763222.37 | 0.5 | skipped_fast |
| BTCUSDT | IDLE | 2.13 | 4.21 | 0.31 | 0.06 | 694068071.79 | 0.0 | skipped_fast |
| WUSDT | IDLE | 2.87 | 11.64 | 4.3 | 0.12 | 895855.81 | 9.16 | skipped_fast |
| PYTHUSDT | IDLE | 1.54 | 3.61 | 1.58 | 0.06 | 681300.4 | 5.01 | skipped_fast |
| RIZEUSDT | IDLE | 1.96 | 32.25 | 13.22 | -0.11 | 57663.0 | 78.74 | skipped_fast |
| CCUSDT | IDLE | 0.89 | 3.0 | 0.5 | 0.1 | 661772.7 | 4.53 | skipped_fast |
| HBARUSDT | IDLE | 1.63 | 3.13 | 0.93 | 0.04 | 594065.79 | 1.27 | skipped_fast |
| ZBCNUSDT | IDLE | 1.88 | 3.53 | 1.58 | 0.04 | 234056.68 | 24.12 | skipped_fast |
| EDELUSDT | IDLE | 0.91 | 8.23 | 4.0 | 0.18 | 231260.48 | 29.22 | skipped_fast |
| CHIPUSDT | IDLE | 0.99 | 4.57 | 2.82 | 0.15 | 186803.89 | 18.54 | skipped_fast |
| FLUIDUSDT | IDLE | 2.88 | 11.14 | 2.74 | 0.12 | 2376.06 | 20.86 | skipped_fast |
| BIOUSDT | IDLE | 1.2 | 3.28 | 0.44 | 0.08 | 86687.71 | 3.66 | skipped_fast |
| REDUSDT | IDLE | 1.23 | 4.01 | 0.82 | 0.12 | 64398.09 | 10.31 | skipped_fast |
| KITEUSDT | IDLE | 1.21 | 2.15 | 1.77 | 0.05 | 78036.29 | 14.57 | skipped_fast |
| RWAINCUSDT | IDLE | 1.23 | 2.45 | 0.0 | 0.01 | 7045.35 | 5.83 | skipped_fast |
| QNTUSDT | IDLE | 1.56 | 2.92 | 1.36 | 0.04 | 72771.44 | 4.71 | skipped_fast |
| TELUSDT | IDLE | 1.6 | 4.45 | 2.86 | 0.05 | 97166.03 | 45.83 | skipped_fast |
| MNSRYUSDT | IDLE | 1.66 | 3.27 | 0.29 | 0.06 | 42670.54 | 55.57 | skipped_fast |
| RWAUSDT | IDLE | 1.09 | 2.01 | 1.17 | 0.01 | 58713.65 | 66.59 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
