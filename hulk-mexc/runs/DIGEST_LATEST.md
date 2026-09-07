# Hulk DIGEST — 2026-09-07T05:47:14Z

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
| XRPUSDT | IDLE | 1.15 | 2.12 | 1.21 | -0.01 | 29462380.91 | 1.42 | skipped_fast |
| ETHUSDT | IDLE | 0.93 | 1.71 | 0.96 | -0.0 | 290358735.53 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.6 | 1.09 | 0.71 | -0.0 | 393742072.61 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.76 | 4.96 | 3.67 | -0.01 | 585397.98 | 1.8 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.06 | 7.19 | 6.14 | -0.05 | 440199.64 | 5.36 | skipped_fast |
| EDELUSDT | IDLE | 3.95 | 7.34 | 3.69 | 0.0 | 68354.89 | 56.18 | skipped_fast |
| WUSDT | IDLE | 1.57 | 2.87 | 1.8 | 0.03 | 414186.85 | 13.43 | skipped_fast |
| CCUSDT | IDLE | 1.52 | 2.82 | 1.43 | 0.01 | 381450.84 | 9.95 | skipped_fast |
| BIOUSDT | IDLE | 1.52 | 2.8 | 1.62 | -0.02 | 76507.98 | 3.65 | skipped_fast |
| RWAINCUSDT | IDLE | 1.6 | 6.24 | 3.22 | 0.12 | 6380.15 | 14.48 | skipped_fast |
| HBARUSDT | IDLE | 1.14 | 2.08 | 1.37 | -0.01 | 402342.47 | 1.23 | skipped_fast |
| RIZEUSDT | IDLE | 1.15 | 8.69 | 1.6 | -0.17 | 71238.07 | 57.33 | skipped_fast |
| KITEUSDT | IDLE | 1.23 | 2.24 | 1.4 | -0.02 | 56277.25 | 10.34 | skipped_fast |
| ZBCNUSDT | IDLE | 0.9 | 1.67 | 0.89 | -0.01 | 134912.09 | 11.31 | skipped_fast |
| REDUSDT | IDLE | 1.1 | 2.06 | 0.89 | 0.01 | 66708.42 | 12.55 | skipped_fast |
| TELUSDT | IDLE | 1.18 | 2.21 | 1.02 | 0.01 | 97943.45 | 23.0 | skipped_fast |
| FLUIDUSDT | IDLE | 1.01 | 1.76 | 1.73 | -0.01 | 1096.83 | 19.61 | skipped_fast |
| QNTUSDT | IDLE | 0.67 | 1.22 | 0.83 | -0.0 | 37477.38 | 7.51 | skipped_fast |
| RWAUSDT | IDLE | 0.53 | 0.94 | 0.86 | -0.02 | 53593.35 | 36.06 | skipped_fast |
| MNSRYUSDT | IDLE | 0.1 | 0.19 | 0.04 | -0.0 | 39344.23 | 8.06 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
