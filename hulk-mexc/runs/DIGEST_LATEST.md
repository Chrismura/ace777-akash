# Hulk DIGEST — 2026-10-17T04:12:08Z

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
| PYTHUSDT | IDLE | 1.14 | 3.7 | 3.04 | -0.1 | 1790776.25 | 3.53 | skipped_fast |
| XRPUSDT | IDLE | 0.38 | 0.71 | 0.3 | -0.02 | 26146463.61 | 1.53 | skipped_fast |
| ETHUSDT | IDLE | 0.29 | 0.56 | 0.18 | -0.0 | 197508803.25 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.27 | 0.49 | 0.3 | -0.01 | 307761975.31 | 0.0 | skipped_fast |
| WUSDT | IDLE | 1.2 | 3.01 | 1.84 | -0.06 | 1349381.22 | 18.99 | skipped_fast |
| QNTUSDT | IDLE | 1.09 | 2.11 | 0.46 | -0.01 | 733382.63 | 4.45 | skipped_fast |
| ZBCNUSDT | IDLE | 1.75 | 3.14 | 2.43 | -0.02 | 202431.4 | 17.88 | skipped_fast |
| RIZEUSDT | IDLE | 2.63 | 6.09 | 1.38 | -0.02 | 50491.52 | 60.6 | skipped_fast |
| CCUSDT | IDLE | 0.77 | 1.41 | 0.85 | -0.03 | 356147.33 | 4.85 | skipped_fast |
| REDUSDT | IDLE | 1.94 | 3.73 | 2.6 | -0.02 | 73865.89 | 7.66 | skipped_fast |
| EDELUSDT | IDLE | 0.91 | 1.64 | 1.18 | 0.01 | 191739.87 | 23.77 | skipped_fast |
| RWAINCUSDT | IDLE | 1.12 | 5.25 | 3.6 | -0.09 | 24988.49 | 5.57 | skipped_fast |
| CHIPUSDT | IDLE | 0.77 | 2.42 | 1.19 | -0.08 | 120793.0 | 12.94 | skipped_fast |
| BIOUSDT | IDLE | 0.76 | 1.4 | 0.79 | -0.02 | 65860.62 | 3.98 | skipped_fast |
| KITEUSDT | IDLE | 0.86 | 1.68 | 0.29 | 0.01 | 56955.72 | 10.62 | skipped_fast |
| HBARUSDT | IDLE | 0.81 | 1.54 | 0.47 | -0.01 | 316251.91 | 5.95 | skipped_fast |
| TELUSDT | IDLE | 0.96 | 1.69 | 1.49 | -0.03 | 95326.62 | 23.32 | skipped_fast |
| FLUIDUSDT | IDLE | 0.76 | 1.39 | 0.93 | 0.01 | 4292.23 | 21.4 | skipped_fast |
| MNSRYUSDT | IDLE | 0.33 | 0.57 | 0.55 | -0.0 | 32294.85 | 4.24 | skipped_fast |
| RWAUSDT | IDLE | 0.14 | 0.24 | 0.24 | -0.0 | 52847.77 | 7.96 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
