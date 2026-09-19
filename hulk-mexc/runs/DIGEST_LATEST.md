# Hulk DIGEST — 2026-09-19T18:58:54Z

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
| XRPUSDT | IDLE | 1.25 | 2.27 | 1.59 | 0.03 | 60571805.09 | 2.8 | skipped_fast |
| ETHUSDT | IDLE | 0.85 | 1.53 | 1.14 | 0.01 | 326402619.44 | 1.06 | skipped_fast |
| BTCUSDT | IDLE | 0.5 | 0.91 | 0.59 | 0.01 | 480801854.03 | 0.0 | skipped_fast |
| WUSDT | IDLE | 2.4 | 4.33 | 3.09 | 0.01 | 599406.07 | 9.02 | skipped_fast |
| ZBCNUSDT | IDLE | 3.38 | 13.64 | 3.18 | 0.11 | 228774.62 | 36.95 | skipped_fast |
| PYTHUSDT | IDLE | 1.4 | 2.54 | 1.74 | 0.01 | 684466.3 | 6.64 | skipped_fast |
| CCUSDT | IDLE | 1.5 | 2.69 | 2.13 | 0.01 | 341975.14 | 9.89 | skipped_fast |
| HBARUSDT | IDLE | 1.19 | 2.31 | 0.49 | 0.04 | 579163.13 | 2.44 | skipped_fast |
| BIOUSDT | IDLE | 1.87 | 3.35 | 2.54 | 0.02 | 82947.52 | 14.31 | skipped_fast |
| EDELUSDT | IDLE | 1.29 | 7.36 | 4.31 | -0.14 | 168353.57 | 43.83 | skipped_fast |
| RIZEUSDT | IDLE | 2.05 | 8.93 | 6.2 | 0.04 | 37858.42 | 103.09 | skipped_fast |
| CHIPUSDT | IDLE | 1.32 | 3.04 | 2.63 | 0.0 | 126225.54 | 20.82 | skipped_fast |
| RWAINCUSDT | IDLE | 2.34 | 5.78 | 0.0 | -0.01 | 5952.13 | 94.51 | skipped_fast |
| KITEUSDT | IDLE | 1.13 | 2.05 | 1.38 | 0.05 | 71355.74 | 12.99 | skipped_fast |
| REDUSDT | IDLE | 0.63 | 2.7 | 2.07 | 0.01 | 135175.49 | 8.14 | skipped_fast |
| TELUSDT | IDLE | 1.24 | 3.66 | 2.89 | -0.01 | 126589.43 | 33.01 | skipped_fast |
| FLUIDUSDT | IDLE | 1.24 | 2.42 | 1.9 | 0.07 | 9472.77 | 23.16 | skipped_fast |
| QNTUSDT | IDLE | 0.8 | 1.46 | 0.99 | 0.03 | 51129.77 | 4.59 | skipped_fast |
| RWAUSDT | IDLE | 0.57 | 1.03 | 0.8 | 0.01 | 54364.39 | 29.37 | skipped_fast |
| MNSRYUSDT | IDLE | 0.84 | 1.5 | 1.25 | -0.01 | 36324.16 | 62.32 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
