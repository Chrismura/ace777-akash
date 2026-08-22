# Hulk DIGEST — 2026-08-22T16:33:27Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : XRPUSDT, HBARUSDT, QAITUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT
- Watch only : QNTUSDT, FLUIDUSDT, RWAUSDT

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| PYTHUSDT | IDLE | 1.54 | 7.64 | 0.0 | 0.07 | 51432718.25 | 1.94 | skipped_fast |
| XRPUSDT | IDLE | 1.34 | 7.64 | 3.97 | 0.05 | 215186126.02 | 3.4 | skipped_fast |
| HBARUSDT | IDLE | 0.81 | 3.03 | 1.19 | -0.01 | 1126988.53 | 5.17 | skipped_fast |
| CCUSDT | IDLE | 0.98 | 4.14 | 2.33 | 0.08 | 764392.62 | 10.26 | skipped_fast |
| CHIPUSDT | IDLE | 0.57 | 3.36 | 0.83 | -0.1 | 627421.04 | 6.7 | skipped_fast |
| WUSDT | IDLE | 0.62 | 2.58 | 0.93 | -0.01 | 544076.96 | 12.72 | skipped_fast |
| ZBCNUSDT | IDLE | 1.28 | 3.49 | 1.13 | -0.03 | 315514.44 | 16.35 | skipped_fast |
| BIOUSDT | IDLE | 0.96 | 6.58 | 4.13 | -0.06 | 219835.34 | 3.29 | skipped_fast |
| KITEUSDT | IDLE | 1.92 | 4.35 | 2.04 | 0.02 | 85162.98 | 8.96 | skipped_fast |
| EDELUSDT | IDLE | 1.41 | 2.52 | 2.01 | -0.03 | 74856.14 | 22.83 | skipped_fast |
| REDUSDT | IDLE | 0.52 | 5.67 | 4.03 | -0.15 | 133272.99 | 13.68 | skipped_fast |
| RIZEUSDT | IDLE | 1.32 | 3.23 | 0.15 | 0.1 | 50959.31 | 45.5 | skipped_fast |
| QAITUSDT | IDLE | 1.67 | 3.19 | 0.94 | -0.01 | 2319.29 | 67.45 | skipped_fast |
| QNTUSDT | IDLE | 0.87 | 2.69 | 2.24 | -0.02 | 183309.54 | 4.74 | skipped_fast |
| RWAINCUSDT | IDLE | 0.77 | 1.53 | 0.0 | 0.03 | 8171.79 | 59.06 | skipped_fast |
| TELUSDT | IDLE | 0.95 | 2.37 | 1.21 | 0.0 | 137204.02 | 10.63 | skipped_fast |
| RWAUSDT | IDLE | 0.54 | 1.06 | 0.08 | 0.03 | 56422.69 | 24.32 | skipped_fast |
| FLUIDUSDT | IDLE | 0.0 | 0.0 | 0.0 | -0.03 | 4618.58 | 21.63 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
