# Hulk DIGEST — 2026-09-20T01:00:28Z

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
| XRPUSDT | IDLE | 1.48 | 2.66 | 2.02 | -0.0 | 56725045.22 | 2.84 | skipped_fast |
| ETHUSDT | IDLE | 0.46 | 0.85 | 0.5 | 0.0 | 223576385.46 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.36 | 0.68 | 0.21 | -0.0 | 438008402.24 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.65 | 3.21 | 0.55 | 0.03 | 651710.36 | 4.88 | skipped_fast |
| WUSDT | IDLE | 1.69 | 3.35 | 0.19 | 0.02 | 510368.37 | 6.28 | skipped_fast |
| CCUSDT | IDLE | 2.07 | 3.68 | 3.01 | -0.03 | 324388.14 | 10.15 | skipped_fast |
| HBARUSDT | IDLE | 1.49 | 2.95 | 0.23 | 0.04 | 580245.42 | 1.22 | skipped_fast |
| EDELUSDT | IDLE | 1.82 | 6.53 | 4.26 | -0.1 | 117995.15 | 29.94 | skipped_fast |
| ZBCNUSDT | IDLE | 1.14 | 4.2 | 3.81 | 0.08 | 215845.46 | 43.26 | skipped_fast |
| RWAINCUSDT | IDLE | 1.91 | 4.19 | 3.56 | -0.04 | 7501.07 | 17.85 | skipped_fast |
| CHIPUSDT | IDLE | 1.36 | 3.98 | 1.22 | -0.02 | 119166.47 | 16.06 | skipped_fast |
| REDUSDT | IDLE | 1.13 | 2.12 | 1.15 | 0.03 | 126221.8 | 7.41 | skipped_fast |
| BIOUSDT | IDLE | 1.09 | 2.13 | 0.39 | 0.03 | 90293.36 | 7.11 | skipped_fast |
| KITEUSDT | IDLE | 0.97 | 1.86 | 0.53 | 0.02 | 78888.31 | 21.81 | skipped_fast |
| TELUSDT | IDLE | 1.62 | 3.34 | 2.64 | -0.08 | 99721.19 | 54.35 | skipped_fast |
| QNTUSDT | IDLE | 1.33 | 2.53 | 0.86 | 0.04 | 56451.75 | 4.55 | skipped_fast |
| RIZEUSDT | IDLE | 1.19 | 4.68 | 2.74 | 0.01 | 39834.71 | 237.18 | skipped_fast |
| RWAUSDT | IDLE | 0.89 | 1.55 | 1.53 | 0.0 | 52364.57 | 36.89 | skipped_fast |
| FLUIDUSDT | IDLE | 0.6 | 1.14 | 0.41 | 0.03 | 8313.18 | 19.65 | skipped_fast |
| MNSRYUSDT | IDLE | 0.32 | 0.63 | 0.03 | -0.01 | 34709.14 | 13.23 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
