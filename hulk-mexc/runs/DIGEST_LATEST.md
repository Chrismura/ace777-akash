# Hulk DIGEST — 2026-09-14T10:41:56Z

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
| XRPUSDT | IDLE | 1.36 | 2.57 | 0.95 | 0.04 | 33527791.63 | 2.15 | skipped_fast |
| BTCUSDT | IDLE | 0.68 | 1.28 | 0.55 | 0.02 | 400070694.11 | 0.0 | skipped_fast |
| ETHUSDT | IDLE | 0.59 | 1.08 | 0.72 | 0.01 | 328456039.45 | 0.95 | skipped_fast |
| PYTHUSDT | IDLE | 2.64 | 5.67 | 4.43 | 0.04 | 517354.03 | 1.79 | skipped_fast |
| REDUSDT | IDLE | 2.54 | 6.16 | 1.21 | 0.05 | 163307.17 | 18.14 | skipped_fast |
| CHIPUSDT | IDLE | 2.26 | 6.88 | 4.62 | -0.1 | 106364.29 | 16.88 | skipped_fast |
| RIZEUSDT | IDLE | 1.62 | 19.05 | 6.97 | 0.21 | 72203.01 | 81.63 | skipped_fast |
| EDELUSDT | IDLE | 1.22 | 6.15 | 1.24 | 0.19 | 231673.65 | 20.94 | skipped_fast |
| CCUSDT | IDLE | 1.14 | 2.12 | 1.1 | 0.01 | 249335.99 | 8.36 | skipped_fast |
| WUSDT | IDLE | 1.18 | 2.25 | 0.71 | 0.03 | 217130.87 | 12.78 | skipped_fast |
| ZBCNUSDT | IDLE | 0.99 | 1.85 | 0.85 | -0.0 | 206934.13 | 2.26 | skipped_fast |
| BIOUSDT | IDLE | 0.98 | 1.89 | 0.43 | 0.01 | 74760.09 | 3.88 | skipped_fast |
| KITEUSDT | IDLE | 1.02 | 1.81 | 1.5 | -0.02 | 60204.32 | 12.2 | skipped_fast |
| RWAINCUSDT | IDLE | 1.41 | 2.61 | 1.4 | 0.02 | 9387.11 | 32.86 | skipped_fast |
| HBARUSDT | IDLE | 0.62 | 1.14 | 0.69 | 0.02 | 275797.89 | 1.31 | skipped_fast |
| TELUSDT | IDLE | 1.54 | 2.93 | 0.99 | 0.0 | 91706.13 | 56.23 | skipped_fast |
| FLUIDUSDT | IDLE | 1.12 | 2.06 | 1.17 | 0.01 | 797.35 | 21.75 | skipped_fast |
| QNTUSDT | IDLE | 0.58 | 1.1 | 0.39 | 0.0 | 38371.25 | 7.82 | skipped_fast |
| MNSRYUSDT | IDLE | 0.25 | 0.48 | 0.14 | -0.0 | 29334.62 | 6.97 | skipped_fast |
| RWAUSDT | IDLE | 0.2 | 0.37 | 0.22 | 0.01 | 53238.07 | 14.8 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
