# Hulk DIGEST — 2026-10-07T16:09:29Z

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
| QNTUSDT | IDLE | 1.11 | 4.01 | 0.08 | -0.07 | 2928804.72 | 4.9 | skipped_fast |
| XRPUSDT | IDLE | 1.08 | 2.04 | 0.86 | -0.04 | 44695818.02 | 2.08 | skipped_fast |
| BTCUSDT | IDLE | 0.65 | 1.26 | 0.3 | -0.03 | 802503506.36 | 0.0 | skipped_fast |
| ETHUSDT | IDLE | 0.65 | 1.26 | 0.24 | -0.05 | 595923155.54 | 0.04 | skipped_fast |
| PYTHUSDT | IDLE | 0.96 | 2.57 | 0.4 | -0.08 | 1051934.3 | 1.39 | skipped_fast |
| EDELUSDT | IDLE | 1.82 | 9.92 | 8.16 | -0.16 | 594396.74 | 12.5 | skipped_fast |
| WUSDT | IDLE | 2.85 | 6.25 | 0.01 | -0.02 | 484299.77 | 13.11 | skipped_fast |
| ZBCNUSDT | IDLE | 2.58 | 6.63 | 3.94 | -0.05 | 275544.07 | 16.16 | skipped_fast |
| HBARUSDT | IDLE | 1.17 | 2.64 | 1.12 | -0.07 | 714682.06 | 6.4 | skipped_fast |
| CCUSDT | IDLE | 1.04 | 2.67 | 0.68 | -0.08 | 433901.2 | 7.52 | skipped_fast |
| CHIPUSDT | IDLE | 1.49 | 5.22 | 0.0 | -0.02 | 179763.13 | 7.87 | skipped_fast |
| RWAINCUSDT | IDLE | 2.24 | 5.29 | 2.45 | -0.04 | 55505.23 | 80.72 | skipped_fast |
| KITEUSDT | IDLE | 1.26 | 2.51 | 0.01 | -0.05 | 64178.57 | 11.07 | skipped_fast |
| RIZEUSDT | IDLE | 1.16 | 4.32 | 0.29 | 0.01 | 57555.54 | 29.05 | skipped_fast |
| REDUSDT | IDLE | 1.02 | 2.68 | 0.71 | -0.08 | 59605.91 | 8.61 | skipped_fast |
| BIOUSDT | IDLE | 0.83 | 3.37 | 0.0 | -0.09 | 84715.5 | 3.43 | skipped_fast |
| TELUSDT | IDLE | 0.81 | 3.17 | 2.1 | 0.05 | 193019.73 | 14.94 | skipped_fast |
| FLUIDUSDT | IDLE | 1.38 | 2.75 | 0.01 | -0.01 | 20183.64 | 18.24 | skipped_fast |
| RWAUSDT | IDLE | 0.42 | 0.76 | 0.53 | -0.03 | 52518.72 | 7.54 | skipped_fast |
| MNSRYUSDT | IDLE | 0.66 | 1.2 | 0.83 | -0.02 | 39935.12 | 44.5 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
