# Hulk DIGEST — 2026-09-11T05:17:10Z

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
| XRPUSDT | IDLE | 0.61 | 1.21 | 0.1 | -0.03 | 40499914.35 | 0.74 | skipped_fast |
| ETHUSDT | IDLE | 0.56 | 1.1 | 0.16 | -0.01 | 446608290.69 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.42 | 0.82 | 0.07 | -0.02 | 556402971.55 | 0.0 | skipped_fast |
| RIZEUSDT | IDLE | 0.9 | 47.43 | 27.67 | -0.49 | 165591.17 | 220.18 | skipped_fast |
| PYTHUSDT | IDLE | 1.12 | 2.15 | 0.66 | -0.02 | 393618.48 | 1.94 | skipped_fast |
| CHIPUSDT | IDLE | 2.3 | 5.11 | 4.28 | -0.05 | 99337.88 | 15.11 | skipped_fast |
| CCUSDT | IDLE | 0.82 | 1.68 | 0.21 | -0.05 | 460722.46 | 7.1 | skipped_fast |
| WUSDT | IDLE | 1.55 | 2.97 | 0.87 | -0.01 | 158531.43 | 13.45 | skipped_fast |
| ZBCNUSDT | IDLE | 1.28 | 2.51 | 0.4 | -0.03 | 202034.55 | 18.75 | skipped_fast |
| EDELUSDT | IDLE | 0.87 | 3.7 | 2.66 | -0.07 | 204662.38 | 28.24 | skipped_fast |
| BIOUSDT | IDLE | 1.09 | 2.11 | 0.52 | -0.02 | 74157.99 | 7.97 | skipped_fast |
| REDUSDT | IDLE | 1.05 | 2.04 | 0.45 | -0.03 | 60579.01 | 10.64 | skipped_fast |
| FLUIDUSDT | IDLE | 2.5 | 5.01 | 0.0 | -0.02 | 1895.67 | 12.86 | skipped_fast |
| KITEUSDT | IDLE | 0.81 | 1.5 | 0.86 | -0.03 | 57398.24 | 12.92 | skipped_fast |
| RWAINCUSDT | IDLE | 1.03 | 1.85 | 1.43 | 0.01 | 3855.6 | 27.97 | skipped_fast |
| TELUSDT | IDLE | 1.63 | 3.0 | 1.68 | -0.02 | 89486.31 | 34.21 | skipped_fast |
| HBARUSDT | IDLE | 0.61 | 1.22 | 0.03 | -0.02 | 177610.99 | 1.32 | skipped_fast |
| QNTUSDT | IDLE | 0.69 | 1.33 | 0.31 | -0.03 | 36182.99 | 6.18 | skipped_fast |
| RWAUSDT | IDLE | 0.4 | 0.77 | 0.23 | -0.02 | 50022.26 | 7.61 | skipped_fast |
| MNSRYUSDT | IDLE | 0.26 | 0.46 | 0.39 | -0.02 | 34883.54 | 5.6 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
