# Hulk DIGEST — 2026-10-23T22:23:16Z

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
| XRPUSDT | IDLE | 0.59 | 1.08 | 0.63 | -0.0 | 23063233.63 | 1.53 | skipped_fast |
| ETHUSDT | IDLE | 0.47 | 0.83 | 0.69 | 0.0 | 139943217.57 | 0.25 | skipped_fast |
| BTCUSDT | IDLE | 0.41 | 0.73 | 0.62 | -0.0 | 285669761.95 | 0.0 | skipped_fast |
| WUSDT | IDLE | 2.32 | 4.1 | 3.62 | -0.02 | 845204.07 | 14.62 | skipped_fast |
| PYTHUSDT | IDLE | 2.63 | 4.77 | 3.28 | -0.01 | 749445.74 | 2.81 | skipped_fast |
| QNTUSDT | IDLE | 1.83 | 3.52 | 0.95 | -0.02 | 1202985.59 | 1.09 | skipped_fast |
| EDELUSDT | IDLE | 2.04 | 3.74 | 2.32 | 0.0 | 525445.38 | 25.02 | skipped_fast |
| CHIPUSDT | IDLE | 3.17 | 5.76 | 3.83 | -0.01 | 83903.51 | 15.93 | skipped_fast |
| ZBCNUSDT | IDLE | 2.45 | 4.4 | 4.12 | 0.0 | 204774.98 | 25.49 | skipped_fast |
| REDUSDT | IDLE | 2.03 | 3.65 | 2.79 | 0.0 | 57644.77 | 9.25 | skipped_fast |
| RIZEUSDT | IDLE | 1.8 | 7.15 | 4.66 | -0.01 | 69717.88 | 45.49 | skipped_fast |
| BIOUSDT | IDLE | 1.67 | 2.93 | 2.68 | 0.01 | 75622.07 | 4.25 | skipped_fast |
| CCUSDT | IDLE | 1.09 | 1.96 | 1.45 | 0.0 | 177566.23 | 4.87 | skipped_fast |
| RWAINCUSDT | IDLE | 1.73 | 3.42 | 0.27 | 0.06 | 48889.99 | 10.7 | skipped_fast |
| KITEUSDT | IDLE | 1.36 | 2.47 | 1.67 | -0.01 | 57263.02 | 10.95 | skipped_fast |
| LAUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.07 | 8.69 | 0.71 | 0.16 | 64150.62 | 23.94 | skipped_fast |
| HBARUSDT | IDLE | 0.89 | 1.62 | 1.12 | -0.02 | 257884.8 | 10.22 | skipped_fast |
| WAXLUSDT | IDLE | 1.73 | 3.22 | 1.54 | -0.0 | 58994.23 | 12.49 | skipped_fast |
| FLUIDUSDT | IDLE | 1.85 | 3.34 | 2.34 | 0.02 | 4513.36 | 21.39 | skipped_fast |
| IOTAUSDT | IDLE | 1.35 | 2.48 | 1.48 | 0.01 | 70566.58 | 13.42 | skipped_fast |
| RWAUSDT | IDLE | 0.3 | 0.55 | 0.39 | 0.01 | 51079.46 | 15.75 | skipped_fast |
| MNSRYUSDT | IDLE | 0.39 | 0.72 | 0.44 | -0.0 | 36713.95 | 74.39 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
