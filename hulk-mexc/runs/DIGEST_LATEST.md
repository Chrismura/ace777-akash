# Hulk DIGEST — 2026-09-14T21:35:22Z

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
| XRPUSDT | IDLE | 2.33 | 6.41 | 3.1 | 0.06 | 72933016.09 | 2.08 | skipped_fast |
| ETHUSDT | IDLE | 2.35 | 4.36 | 2.29 | 0.02 | 444334838.2 | 0.31 | skipped_fast |
| BTCUSDT | IDLE | 0.8 | 1.48 | 0.86 | 0.02 | 569438231.7 | 0.0 | skipped_fast |
| EDELUSDT | IDLE | 2.31 | 13.42 | 4.83 | 0.14 | 285397.53 | 19.55 | skipped_fast |
| PYTHUSDT | IDLE | 1.69 | 3.25 | 0.93 | -0.01 | 420735.31 | 3.55 | skipped_fast |
| CCUSDT | IDLE | 2.01 | 3.82 | 1.27 | 0.02 | 316032.62 | 7.12 | skipped_fast |
| ZBCNUSDT | IDLE | 2.43 | 4.6 | 1.79 | 0.02 | 194969.27 | 14.22 | skipped_fast |
| WUSDT | IDLE | 1.94 | 3.63 | 1.69 | -0.0 | 214805.64 | 10.92 | skipped_fast |
| KITEUSDT | IDLE | 2.29 | 4.38 | 1.3 | 0.0 | 64864.41 | 12.04 | skipped_fast |
| BIOUSDT | IDLE | 1.97 | 3.69 | 1.67 | 0.01 | 96804.88 | 3.85 | skipped_fast |
| REDUSDT | IDLE | 1.34 | 4.94 | 1.13 | 0.08 | 188429.57 | 7.79 | skipped_fast |
| TELUSDT | IDLE | 3.24 | 8.53 | 3.7 | 0.05 | 104686.59 | 54.14 | skipped_fast |
| HBARUSDT | IDLE | 1.83 | 3.5 | 1.01 | 0.03 | 365631.05 | 1.27 | skipped_fast |
| CHIPUSDT | IDLE | 1.71 | 3.17 | 2.58 | -0.04 | 90611.58 | 16.88 | skipped_fast |
| RWAINCUSDT | IDLE | 1.35 | 2.44 | 1.79 | -0.0 | 4969.88 | 5.51 | skipped_fast |
| RIZEUSDT | IDLE | 0.62 | 7.09 | 4.03 | -0.01 | 56095.31 | 62.46 | skipped_fast |
| FLUIDUSDT | IDLE | 1.6 | 3.03 | 1.12 | 0.01 | 1624.56 | 22.51 | skipped_fast |
| QNTUSDT | IDLE | 1.03 | 1.89 | 1.08 | -0.0 | 43621.63 | 6.24 | skipped_fast |
| MNSRYUSDT | IDLE | 1.01 | 1.97 | 0.33 | 0.01 | 31214.45 | 41.23 | skipped_fast |
| RWAUSDT | IDLE | 0.41 | 0.74 | 0.59 | -0.01 | 56392.61 | 22.3 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
