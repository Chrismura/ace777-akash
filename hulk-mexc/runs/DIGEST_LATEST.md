# Hulk DIGEST — 2026-09-27T11:07:50Z

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
| WUSDT | IDLE | 1.88 | 11.19 | 8.38 | 0.13 | 3120640.25 | 17.88 | skipped_fast |
| PYTHUSDT | IDLE | 1.54 | 6.09 | 2.55 | 0.13 | 2051812.13 | 1.16 | skipped_fast |
| QNTUSDT | IDLE | 0.51 | 9.87 | 8.97 | 0.57 | 5220472.87 | 0.6 | skipped_fast |
| XRPUSDT | IDLE | 1.03 | 2.0 | 0.45 | -0.01 | 40973463.95 | 1.95 | skipped_fast |
| ETHUSDT | IDLE | 0.46 | 0.82 | 0.64 | 0.01 | 158848300.64 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.37 | 0.71 | 0.24 | 0.01 | 430049211.79 | 0.0 | skipped_fast |
| CCUSDT | IDLE | 1.44 | 2.86 | 0.09 | 0.02 | 618306.51 | 0.73 | skipped_fast |
| EDELUSDT | IDLE | 2.41 | 5.84 | 4.08 | -0.05 | 148326.43 | 38.39 | skipped_fast |
| REDUSDT | IDLE | 2.49 | 4.43 | 3.67 | 0.01 | 64514.97 | 12.83 | skipped_fast |
| HBARUSDT | IDLE | 1.23 | 2.26 | 1.28 | 0.0 | 620607.74 | 1.06 | skipped_fast |
| ZBCNUSDT | IDLE | 1.44 | 2.73 | 1.04 | -0.01 | 226912.67 | 10.38 | skipped_fast |
| KITEUSDT | IDLE | 1.34 | 5.21 | 4.83 | 0.09 | 170739.66 | 10.15 | skipped_fast |
| CHIPUSDT | IDLE | 1.16 | 2.7 | 2.01 | 0.0 | 120751.1 | 14.33 | skipped_fast |
| BIOUSDT | IDLE | 0.87 | 1.57 | 1.18 | -0.04 | 96576.71 | 6.27 | skipped_fast |
| RIZEUSDT | IDLE | 0.99 | 3.84 | 0.97 | -0.03 | 46693.1 | 61.87 | skipped_fast |
| RWAINCUSDT | IDLE | 0.88 | 3.68 | 0.0 | 0.07 | 7160.93 | 36.99 | skipped_fast |
| TELUSDT | IDLE | 0.93 | 3.19 | 1.18 | 0.1 | 131306.3 | 11.37 | skipped_fast |
| MNSRYUSDT | IDLE | 0.96 | 1.91 | 0.04 | 0.01 | 39248.39 | 25.2 | skipped_fast |
| FLUIDUSDT | IDLE | 1.03 | 1.9 | 1.11 | 0.02 | 1017.93 | 21.54 | skipped_fast |
| RWAUSDT | IDLE | 1.0 | 1.85 | 0.98 | 0.04 | 55899.91 | 49.56 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
