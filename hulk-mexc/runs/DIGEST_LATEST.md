# Hulk DIGEST — 2026-09-26T06:53:44Z

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
| XRPUSDT | IDLE | 1.29 | 2.29 | 1.99 | 0.01 | 109790420.23 | 2.58 | skipped_fast |
| ETHUSDT | IDLE | 0.26 | 0.46 | 0.35 | 0.0 | 294769712.74 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.18 | 0.32 | 0.23 | -0.0 | 638210465.21 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.32 | 3.33 | 2.03 | 0.08 | 1188787.74 | 1.36 | skipped_fast |
| CCUSDT | IDLE | 1.28 | 5.69 | 0.28 | 0.17 | 974505.95 | 7.3 | skipped_fast |
| HBARUSDT | IDLE | 1.2 | 2.15 | 1.62 | 0.02 | 863372.52 | 1.07 | skipped_fast |
| QNTUSDT | IDLE | 2.16 | 6.76 | 2.92 | 0.01 | 513395.43 | 6.87 | skipped_fast |
| WUSDT | IDLE | 1.01 | 2.01 | 0.4 | 0.06 | 475893.99 | 7.27 | skipped_fast |
| ZBCNUSDT | IDLE | 1.44 | 3.27 | 2.27 | 0.03 | 230995.05 | 5.69 | skipped_fast |
| REDUSDT | IDLE | 1.82 | 3.35 | 2.09 | 0.06 | 59492.05 | 6.41 | skipped_fast |
| KITEUSDT | IDLE | 1.58 | 4.12 | 3.07 | 0.08 | 76294.94 | 9.59 | skipped_fast |
| CHIPUSDT | IDLE | 1.19 | 2.91 | 2.12 | 0.06 | 147775.54 | 14.45 | skipped_fast |
| EDELUSDT | IDLE | 1.02 | 1.81 | 1.51 | -0.0 | 173454.28 | 37.24 | skipped_fast |
| RWAINCUSDT | IDLE | 1.84 | 4.42 | 0.54 | -0.04 | 11007.79 | 73.37 | skipped_fast |
| BIOUSDT | IDLE | 0.65 | 1.76 | 0.94 | 0.06 | 110571.48 | 6.13 | skipped_fast |
| RIZEUSDT | IDLE | 0.18 | 2.42 | 0.54 | -0.17 | 75332.73 | 51.53 | skipped_fast |
| TELUSDT | IDLE | 0.87 | 1.54 | 1.39 | 0.01 | 118791.33 | 36.92 | skipped_fast |
| FLUIDUSDT | IDLE | 0.96 | 1.83 | 0.62 | 0.01 | 3441.0 | 21.66 | skipped_fast |
| RWAUSDT | IDLE | 0.58 | 1.04 | 0.74 | -0.02 | 53455.89 | 7.41 | skipped_fast |
| MNSRYUSDT | IDLE | 0.46 | 0.89 | 0.17 | 0.01 | 40881.94 | 8.92 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
