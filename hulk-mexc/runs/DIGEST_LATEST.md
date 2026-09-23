# Hulk DIGEST — 2026-09-23T07:18:02Z

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
| XRPUSDT | IDLE | 2.37 | 5.31 | 1.98 | 0.07 | 116775587.71 | 1.23 | skipped_fast |
| PYTHUSDT | IDLE | 0.76 | 3.67 | 0.77 | 0.06 | 1765977.09 | 2.98 | skipped_fast |
| ETHUSDT | IDLE | 0.86 | 1.51 | 1.4 | 0.01 | 411217786.41 | 0.11 | skipped_fast |
| BTCUSDT | IDLE | 0.66 | 1.18 | 1.0 | 0.01 | 878213839.44 | 0.0 | skipped_fast |
| HBARUSDT | IDLE | 1.38 | 2.82 | 1.95 | 0.06 | 1826288.61 | 2.02 | skipped_fast |
| ZBCNUSDT | IDLE | 2.86 | 7.05 | 2.58 | 0.05 | 222796.86 | 25.23 | skipped_fast |
| CCUSDT | IDLE | 1.5 | 2.77 | 1.6 | -0.04 | 408336.61 | 6.97 | skipped_fast |
| WUSDT | IDLE | 1.89 | 3.68 | 0.7 | 0.05 | 313321.9 | 8.07 | skipped_fast |
| KITEUSDT | IDLE | 2.01 | 5.56 | 5.04 | 0.07 | 142621.86 | 11.92 | skipped_fast |
| BIOUSDT | IDLE | 1.81 | 3.51 | 0.69 | 0.06 | 110986.16 | 13.14 | skipped_fast |
| CHIPUSDT | IDLE | 1.38 | 2.65 | 1.73 | -0.03 | 196676.84 | 12.91 | skipped_fast |
| EDELUSDT | IDLE | 0.66 | 3.1 | 1.78 | -0.05 | 264921.57 | 6.57 | skipped_fast |
| REDUSDT | IDLE | 1.71 | 3.41 | 0.04 | 0.02 | 59765.07 | 17.88 | skipped_fast |
| RWAINCUSDT | IDLE | 0.77 | 1.84 | 1.65 | 0.02 | 21549.25 | 16.26 | skipped_fast |
| QNTUSDT | IDLE | 0.77 | 2.57 | 0.94 | 0.11 | 243232.99 | 1.33 | skipped_fast |
| RIZEUSDT | IDLE | 0.72 | 15.71 | 0.0 | 0.5 | 61670.96 | 151.85 | skipped_fast |
| TELUSDT | IDLE | 0.72 | 3.08 | 1.07 | 0.16 | 110758.3 | 59.06 | skipped_fast |
| FLUIDUSDT | IDLE | 0.75 | 1.32 | 1.17 | 0.02 | 2932.72 | 21.62 | skipped_fast |
| RWAUSDT | IDLE | 0.44 | 0.8 | 0.57 | 0.01 | 53237.38 | 14.43 | skipped_fast |
| MNSRYUSDT | IDLE | 0.29 | 0.54 | 0.22 | 0.01 | 39647.95 | 11.52 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
