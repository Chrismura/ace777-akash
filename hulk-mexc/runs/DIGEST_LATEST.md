# Hulk DIGEST — 2026-10-20T18:23:24Z

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
| XRPUSDT | IDLE | 2.09 | 3.93 | 1.69 | 0.02 | 23546987.98 | 1.51 | skipped_fast |
| ETHUSDT | IDLE | 2.06 | 3.91 | 1.34 | 0.02 | 148694565.16 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 1.35 | 2.55 | 0.94 | 0.01 | 323440669.15 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 3.25 | 7.6 | 1.06 | 0.07 | 1006650.68 | 1.29 | skipped_fast |
| WUSDT | IDLE | 3.18 | 6.16 | 1.36 | 0.02 | 691528.06 | 17.23 | skipped_fast |
| QNTUSDT | IDLE | 3.27 | 6.0 | 3.54 | 0.01 | 720393.64 | 0.51 | skipped_fast |
| ZBCNUSDT | IDLE | 4.08 | 7.65 | 3.34 | 0.02 | 190248.77 | 30.9 | skipped_fast |
| CHIPUSDT | IDLE | 2.79 | 9.87 | 4.77 | 0.08 | 175332.83 | 8.86 | skipped_fast |
| EDELUSDT | IDLE | 1.62 | 15.52 | 1.61 | 0.33 | 337141.0 | 16.7 | skipped_fast |
| CCUSDT | IDLE | 1.81 | 3.41 | 1.43 | 0.02 | 408008.02 | 6.64 | skipped_fast |
| REDUSDT | IDLE | 2.96 | 5.63 | 1.92 | 0.03 | 59546.82 | 9.32 | skipped_fast |
| BIOUSDT | IDLE | 2.94 | 5.72 | 1.12 | 0.06 | 63143.81 | 8.1 | skipped_fast |
| HBARUSDT | IDLE | 2.54 | 4.66 | 2.86 | 0.01 | 399748.63 | 3.6 | skipped_fast |
| KITEUSDT | IDLE | 1.89 | 3.46 | 2.16 | 0.01 | 84770.33 | 9.04 | skipped_fast |
| IOTAUSDT | IDLE | 3.17 | 5.95 | 3.39 | 0.05 | 92724.58 | 25.85 | skipped_fast |
| LAUSDT | IDLE | 3.15 | 6.0 | 1.98 | 0.03 | 56240.32 | 13.08 | skipped_fast |
| RWAINCUSDT | IDLE | 1.32 | 4.0 | 3.53 | -0.05 | 71239.66 | 5.38 | skipped_fast |
| WAXLUSDT | IDLE | 2.98 | 5.42 | 3.66 | -0.04 | 55949.99 | 48.44 | skipped_fast |
| RIZEUSDT | IDLE | 1.05 | 4.33 | 1.84 | 0.02 | 69662.72 | 38.34 | skipped_fast |
| FLUIDUSDT | IDLE | 2.12 | 4.1 | 1.0 | 0.05 | 4946.21 | 21.45 | skipped_fast |
| RWAUSDT | IDLE | 0.78 | 1.42 | 0.93 | 0.01 | 52065.72 | 7.84 | skipped_fast |
| MNSRYUSDT | IDLE | 0.82 | 1.52 | 0.85 | -0.0 | 40388.08 | 19.94 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
