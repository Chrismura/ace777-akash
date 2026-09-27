# Hulk DIGEST — 2026-09-27T15:09:41Z

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
| WUSDT | IDLE | 1.65 | 10.01 | 5.99 | 0.15 | 3675851.82 | 8.88 | skipped_fast |
| PYTHUSDT | IDLE | 1.85 | 6.98 | 5.17 | 0.08 | 2131450.9 | 4.78 | skipped_fast |
| QNTUSDT | IDLE | 0.77 | 13.0 | 3.03 | 0.53 | 5698192.97 | 15.73 | skipped_fast |
| XRPUSDT | IDLE | 1.37 | 2.43 | 2.06 | -0.02 | 44250919.74 | 0.66 | skipped_fast |
| ETHUSDT | IDLE | 0.77 | 1.37 | 1.16 | -0.0 | 185524959.16 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.52 | 0.92 | 0.78 | 0.01 | 452835473.93 | 0.0 | skipped_fast |
| CCUSDT | IDLE | 2.58 | 4.61 | 3.68 | -0.03 | 537321.06 | 9.74 | skipped_fast |
| HBARUSDT | IDLE | 1.73 | 3.07 | 2.65 | -0.01 | 686271.88 | 1.07 | skipped_fast |
| CHIPUSDT | IDLE | 2.17 | 5.15 | 4.52 | -0.05 | 121347.73 | 19.02 | skipped_fast |
| BIOUSDT | IDLE | 1.62 | 2.88 | 2.4 | -0.03 | 100304.93 | 6.37 | skipped_fast |
| ZBCNUSDT | IDLE | 1.23 | 2.21 | 1.7 | -0.03 | 219446.34 | 19.47 | skipped_fast |
| KITEUSDT | IDLE | 1.05 | 3.18 | 2.31 | 0.07 | 177817.14 | 8.09 | skipped_fast |
| RWAINCUSDT | IDLE | 2.11 | 17.2 | 2.19 | 0.28 | 17508.29 | 138.49 | skipped_fast |
| EDELUSDT | IDLE | 1.27 | 2.9 | 2.61 | -0.07 | 135812.8 | 28.25 | skipped_fast |
| REDUSDT | IDLE | 1.43 | 2.55 | 2.08 | -0.0 | 64485.83 | 6.51 | skipped_fast |
| TELUSDT | IDLE | 1.55 | 6.69 | 0.11 | 0.17 | 138574.2 | 16.09 | skipped_fast |
| RIZEUSDT | IDLE | 0.29 | 1.11 | 0.51 | -0.04 | 46009.55 | 59.3 | skipped_fast |
| RWAUSDT | IDLE | 0.64 | 1.21 | 0.49 | 0.01 | 55884.1 | 7.07 | skipped_fast |
| FLUIDUSDT | IDLE | 0.72 | 1.31 | 0.8 | 0.02 | 1527.84 | 20.93 | skipped_fast |
| MNSRYUSDT | IDLE | 0.38 | 0.7 | 0.37 | 0.01 | 39580.2 | 15.17 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
