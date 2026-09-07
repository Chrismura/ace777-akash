# Hulk DIGEST — 2026-09-07T14:35:58Z

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
| XRPUSDT | IDLE | 0.8 | 1.41 | 1.28 | -0.01 | 33970118.07 | 2.15 | skipped_fast |
| ETHUSDT | IDLE | 0.71 | 1.24 | 1.15 | 0.0 | 322386401.8 | 0.12 | skipped_fast |
| BTCUSDT | IDLE | 0.45 | 0.79 | 0.72 | -0.01 | 418454303.2 | 0.3 | skipped_fast |
| PYTHUSDT | IDLE | 1.82 | 3.26 | 2.47 | 0.02 | 562010.18 | 1.81 | skipped_fast |
| CCUSDT | IDLE | 1.53 | 2.79 | 1.79 | -0.02 | 422435.89 | 9.32 | skipped_fast |
| REDUSDT | IDLE | 3.01 | 5.6 | 2.78 | 0.04 | 63938.18 | 10.65 | skipped_fast |
| CHIPUSDT | IDLE | 1.55 | 4.12 | 3.17 | -0.07 | 329291.95 | 9.3 | skipped_fast |
| WUSDT | IDLE | 1.17 | 2.07 | 1.81 | 0.01 | 407321.18 | 10.69 | skipped_fast |
| HBARUSDT | IDLE | 1.82 | 3.44 | 1.37 | 0.02 | 460395.05 | 1.22 | skipped_fast |
| ZBCNUSDT | IDLE | 1.6 | 2.81 | 2.66 | -0.01 | 195783.22 | 25.91 | skipped_fast |
| RIZEUSDT | IDLE | 1.83 | 8.34 | 6.38 | -0.11 | 61299.91 | 65.21 | skipped_fast |
| EDELUSDT | IDLE | 1.51 | 4.12 | 2.42 | -0.04 | 81913.45 | 20.0 | skipped_fast |
| KITEUSDT | IDLE | 1.22 | 2.19 | 1.71 | -0.05 | 58837.02 | 2.48 | skipped_fast |
| BIOUSDT | IDLE | 1.15 | 2.14 | 1.08 | 0.01 | 68989.31 | 7.29 | skipped_fast |
| MNSRYUSDT | IDLE | 2.81 | 5.37 | 1.73 | -0.02 | 38871.69 | 51.84 | skipped_fast |
| RWAINCUSDT | IDLE | 1.21 | 3.8 | 2.19 | 0.06 | 5765.37 | 53.31 | skipped_fast |
| TELUSDT | IDLE | 1.87 | 3.29 | 3.01 | 0.0 | 108996.13 | 41.07 | skipped_fast |
| QNTUSDT | IDLE | 1.15 | 2.12 | 1.14 | 0.01 | 46960.25 | 4.56 | skipped_fast |
| RWAUSDT | IDLE | 0.4 | 0.73 | 0.43 | -0.01 | 53116.26 | 21.68 | skipped_fast |
| FLUIDUSDT | IDLE | 0.0 | 0.0 | 0.0 | -0.01 | 1152.45 | 21.79 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
