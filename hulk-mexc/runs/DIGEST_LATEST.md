# Hulk DIGEST — 2026-10-10T08:51:57Z

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
| WUSDT | IDLE | 1.35 | 3.63 | 3.19 | -0.05 | 1761676.04 | 14.96 | skipped_fast |
| XRPUSDT | IDLE | 0.47 | 0.89 | 0.4 | 0.0 | 23459820.51 | 1.42 | skipped_fast |
| BTCUSDT | IDLE | 0.2 | 0.39 | 0.07 | 0.0 | 237342073.34 | 0.0 | skipped_fast |
| ETHUSDT | IDLE | 0.19 | 0.37 | 0.13 | -0.0 | 118027485.96 | 0.04 | skipped_fast |
| PYTHUSDT | IDLE | 1.1 | 2.9 | 1.86 | -0.07 | 1441858.76 | 1.26 | skipped_fast |
| QNTUSDT | IDLE | 1.8 | 3.57 | 0.26 | 0.04 | 1174003.83 | 2.77 | skipped_fast |
| CCUSDT | IDLE | 0.81 | 1.7 | 0.98 | 0.03 | 576126.49 | 4.94 | skipped_fast |
| KITEUSDT | IDLE | 2.09 | 4.12 | 0.45 | 0.0 | 76562.02 | 9.57 | skipped_fast |
| CHIPUSDT | IDLE | 1.24 | 4.04 | 2.79 | 0.06 | 99820.36 | 13.3 | skipped_fast |
| ZBCNUSDT | IDLE | 0.67 | 1.75 | 0.67 | -0.07 | 263493.83 | 10.52 | skipped_fast |
| EDELUSDT | IDLE | 0.61 | 2.32 | 1.11 | 0.12 | 209171.55 | 7.46 | skipped_fast |
| REDUSDT | IDLE | 1.34 | 2.64 | 0.26 | 0.02 | 57015.66 | 10.56 | skipped_fast |
| BIOUSDT | IDLE | 1.13 | 2.06 | 1.37 | 0.01 | 72313.07 | 6.93 | skipped_fast |
| RWAINCUSDT | IDLE | 2.09 | 3.65 | 3.52 | -0.0 | 10193.52 | 98.23 | skipped_fast |
| HBARUSDT | IDLE | 0.99 | 1.9 | 0.5 | 0.01 | 300261.07 | 3.23 | skipped_fast |
| TELUSDT | IDLE | 1.62 | 2.95 | 1.96 | -0.01 | 119955.79 | 32.49 | skipped_fast |
| RWAUSDT | IDLE | 1.66 | 2.92 | 2.61 | -0.01 | 52043.58 | 23.59 | skipped_fast |
| RIZEUSDT | IDLE | 0.4 | 2.28 | 1.17 | 0.07 | 64876.41 | 53.39 | skipped_fast |
| MNSRYUSDT | IDLE | 0.4 | 0.77 | 0.15 | 0.01 | 41156.06 | 8.1 | skipped_fast |
| FLUIDUSDT | IDLE | 0.25 | 1.47 | 1.13 | -0.0 | 17283.43 | 19.47 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
