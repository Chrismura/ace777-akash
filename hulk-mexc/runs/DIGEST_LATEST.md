# Hulk DIGEST — 2026-10-27T02:36:48Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| XRPUSDT | IDLE | 1.17 | 2.19 | 0.95 | 0.01 | 24667918.63 | 1.54 | skipped_fast |
| ETHUSDT | IDLE | 0.72 | 1.35 | 0.66 | 0.01 | 127170400.33 | 0.3 | skipped_fast |
| BTCUSDT | IDLE | 0.46 | 0.83 | 0.56 | 0.0 | 356345158.83 | 0.02 | skipped_fast |
| QNTUSDT | IDLE | 0.51 | 2.21 | 1.26 | 0.07 | 1412231.49 | 4.44 | skipped_fast |
| PYTHUSDT | IDLE | 1.82 | 3.2 | 2.88 | -0.01 | 668497.65 | 1.37 | skipped_fast |
| WUSDT | IDLE | 1.55 | 2.99 | 2.13 | 0.05 | 641776.27 | 30.11 | skipped_fast |
| CCUSDT | IDLE | 1.18 | 2.1 | 1.72 | -0.02 | 191382.26 | 6.1 | skipped_fast |
| REDUSDT | IDLE | 1.75 | 3.09 | 2.75 | 0.01 | 61328.01 | 16.53 | skipped_fast |
| CHIPUSDT | IDLE | 0.44 | 3.36 | 1.96 | 0.19 | 329490.92 | 17.61 | skipped_fast |
| EDELUSDT | IDLE | 1.17 | 2.16 | 1.2 | 0.01 | 184699.23 | 6.21 | skipped_fast |
| ZBCNUSDT | IDLE | 1.01 | 1.83 | 1.21 | -0.04 | 224754.91 | 19.52 | skipped_fast |
| BIOUSDT | IDLE | 1.18 | 2.19 | 1.12 | 0.0 | 56861.85 | 4.52 | skipped_fast |
| RWAINCUSDT | IDLE | 0.83 | 2.65 | 1.64 | -0.11 | 57483.82 | 12.82 | skipped_fast |
| KITEUSDT | IDLE | 0.82 | 1.44 | 1.33 | 0.02 | 53915.74 | 11.47 | skipped_fast |
| LAUSDT | IDLE | 1.79 | 3.17 | 2.7 | 0.05 | 67529.87 | 24.2 | skipped_fast |
| RIZEUSDT | IDLE | 0.88 | 1.66 | 0.6 | -0.01 | 43201.89 | 64.89 | skipped_fast |
| HBARUSDT | IDLE | 0.92 | 1.66 | 1.15 | -0.0 | 211534.45 | 6.52 | skipped_fast |
| IOTAUSDT | IDLE | 1.51 | 2.75 | 1.86 | 0.0 | 91276.18 | 18.95 | skipped_fast |
| WAXLUSDT | IDLE | 1.75 | 3.11 | 2.56 | -0.02 | 53309.79 | 49.01 | skipped_fast |
| FLUIDUSDT | IDLE | 1.21 | 2.28 | 0.89 | 0.04 | 2190.24 | 21.69 | skipped_fast |
| RWAUSDT | IDLE | 0.65 | 1.21 | 0.56 | -0.0 | 53807.58 | 23.95 | skipped_fast |
| MNSRYUSDT | IDLE | 0.4 | 0.74 | 0.41 | 0.0 | 41693.67 | 76.46 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
