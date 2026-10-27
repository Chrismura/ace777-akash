# Hulk DIGEST — 2026-10-27T21:17:18Z

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
| XRPUSDT | IDLE | 0.44 | 0.81 | 0.5 | 0.02 | 19562215.82 | 1.51 | skipped_fast |
| ETHUSDT | IDLE | 0.41 | 0.74 | 0.53 | 0.02 | 228524085.75 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.24 | 0.46 | 0.1 | 0.01 | 322027528.65 | 0.0 | skipped_fast |
| WUSDT | IDLE | 1.64 | 3.55 | 2.88 | 0.05 | 667929.57 | 16.4 | skipped_fast |
| ZBCNUSDT | IDLE | 2.11 | 6.63 | 3.65 | 0.0 | 236994.5 | 25.93 | skipped_fast |
| EDELUSDT | IDLE | 1.1 | 1.96 | 1.55 | 0.0 | 474112.97 | 21.63 | skipped_fast |
| PYTHUSDT | IDLE | 1.4 | 2.75 | 0.29 | 0.0 | 373209.66 | 2.73 | skipped_fast |
| QNTUSDT | IDLE | 1.06 | 1.93 | 1.22 | -0.01 | 721040.07 | 5.02 | skipped_fast |
| CCUSDT | IDLE | 1.25 | 2.22 | 1.92 | -0.0 | 215998.24 | 9.17 | skipped_fast |
| CHIPUSDT | IDLE | 1.46 | 3.61 | 1.03 | 0.06 | 132029.34 | 16.51 | skipped_fast |
| RWAINCUSDT | IDLE | 1.89 | 4.2 | 2.02 | -0.04 | 64052.56 | 73.31 | skipped_fast |
| RIZEUSDT | IDLE | 1.78 | 3.53 | 0.14 | 0.01 | 33058.39 | 46.24 | skipped_fast |
| REDUSDT | IDLE | 1.23 | 2.52 | 1.54 | 0.07 | 59664.88 | 14.88 | skipped_fast |
| BIOUSDT | IDLE | 1.03 | 1.92 | 0.97 | 0.03 | 58751.34 | 8.87 | skipped_fast |
| KITEUSDT | IDLE | 0.65 | 1.3 | 0.18 | 0.04 | 57411.79 | 9.25 | skipped_fast |
| LAUSDT | IDLE | 1.85 | 3.7 | 2.03 | 0.03 | 59282.46 | 21.55 | skipped_fast |
| HBARUSDT | IDLE | 0.64 | 1.18 | 0.63 | -0.0 | 270547.36 | 10.51 | skipped_fast |
| IOTAUSDT | IDLE | 0.79 | 1.46 | 0.78 | 0.0 | 79072.92 | 23.84 | skipped_fast |
| WAXLUSDT | IDLE | 0.61 | 1.17 | 0.39 | 0.05 | 56481.24 | 57.19 | skipped_fast |
| RWAUSDT | IDLE | 0.22 | 0.4 | 0.32 | -0.0 | 57728.51 | 15.97 | skipped_fast |
| FLUIDUSDT | IDLE | 0.32 | 0.63 | 0.12 | 0.02 | 2559.81 | 21.43 | skipped_fast |
| MNSRYUSDT | IDLE | 0.42 | 0.81 | 0.26 | 0.0 | 37852.68 | 79.41 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
