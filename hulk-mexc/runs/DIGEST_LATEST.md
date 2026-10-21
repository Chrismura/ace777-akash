# Hulk DIGEST — 2026-10-21T06:05:58Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| ETHUSDT | IDLE | 0.63 | 1.11 | 1.01 | 0.02 | 182435535.94 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.48 | 0.86 | 0.73 | 0.02 | 24046698.88 | 0.75 | skipped_fast |
| BTCUSDT | IDLE | 0.4 | 0.71 | 0.65 | 0.01 | 312047827.03 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.17 | 3.64 | 2.5 | 0.11 | 985266.69 | 3.76 | skipped_fast |
| ZBCNUSDT | IDLE | 2.99 | 13.11 | 4.94 | 0.11 | 245615.53 | 0.43 | skipped_fast |
| CHIPUSDT | IDLE | 2.46 | 6.15 | 0.15 | 0.06 | 457360.39 | 13.02 | skipped_fast |
| WUSDT | IDLE | 1.64 | 3.1 | 1.21 | 0.05 | 643665.74 | 18.48 | skipped_fast |
| EDELUSDT | IDLE | 1.37 | 6.48 | 5.62 | 0.16 | 325759.83 | 11.61 | skipped_fast |
| QNTUSDT | IDLE | 0.97 | 1.82 | 0.86 | 0.03 | 778917.87 | 0.51 | skipped_fast |
| CCUSDT | IDLE | 0.87 | 1.53 | 1.46 | 0.01 | 282092.19 | 7.66 | skipped_fast |
| RWAINCUSDT | IDLE | 1.35 | 6.7 | 1.29 | -0.05 | 78283.8 | 5.43 | skipped_fast |
| REDUSDT | IDLE | 1.52 | 2.8 | 1.55 | 0.04 | 59634.87 | 17.48 | skipped_fast |
| KITEUSDT | IDLE | 1.0 | 2.0 | 0.02 | 0.01 | 71241.68 | 10.52 | skipped_fast |
| HBARUSDT | IDLE | 1.0 | 1.77 | 1.58 | 0.0 | 334581.85 | 9.63 | skipped_fast |
| BIOUSDT | IDLE | 0.68 | 1.23 | 0.89 | 0.05 | 60697.26 | 8.15 | skipped_fast |
| RIZEUSDT | IDLE | 0.47 | 2.04 | 0.22 | 0.06 | 61068.38 | 28.66 | skipped_fast |
| WAXLUSDT | IDLE | 1.64 | 2.95 | 2.22 | -0.03 | 57656.35 | 39.65 | skipped_fast |
| LAUSDT | IDLE | 1.46 | 3.73 | 0.21 | 0.08 | 56214.4 | 24.71 | skipped_fast |
| IOTAUSDT | IDLE | 1.17 | 2.09 | 1.73 | 0.01 | 76776.03 | 23.88 | skipped_fast |
| FLUIDUSDT | IDLE | 0.44 | 1.6 | 1.53 | 0.02 | 14691.99 | 17.57 | skipped_fast |
| RWAUSDT | IDLE | 0.33 | 0.63 | 0.23 | 0.0 | 52507.09 | 31.35 | skipped_fast |
| MNSRYUSDT | IDLE | 0.17 | 0.33 | 0.07 | -0.0 | 40030.87 | 9.98 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
