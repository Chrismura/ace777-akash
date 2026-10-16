# Hulk DIGEST — 2026-10-16T05:23:22Z

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
| WUSDT | IDLE | 2.92 | 7.46 | 3.34 | -0.0 | 2378090.67 | 14.66 | skipped_fast |
| PYTHUSDT | IDLE | 0.59 | 3.38 | 2.09 | 0.08 | 4080817.17 | 3.22 | skipped_fast |
| ETHUSDT | IDLE | 0.7 | 1.35 | 0.34 | 0.04 | 236278397.38 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.72 | 1.41 | 0.23 | 0.03 | 36345918.06 | 2.24 | skipped_fast |
| BTCUSDT | IDLE | 0.53 | 1.01 | 0.33 | 0.01 | 432536830.0 | 0.0 | skipped_fast |
| QNTUSDT | IDLE | 1.33 | 3.9 | 1.44 | 0.07 | 1171119.15 | 2.41 | skipped_fast |
| CCUSDT | IDLE | 1.75 | 3.28 | 1.46 | -0.02 | 420753.14 | 4.68 | skipped_fast |
| CHIPUSDT | IDLE | 1.88 | 9.97 | 4.96 | 0.09 | 181439.69 | 10.09 | skipped_fast |
| ZBCNUSDT | IDLE | 1.66 | 3.2 | 0.93 | 0.06 | 184783.77 | 2.67 | skipped_fast |
| REDUSDT | IDLE | 1.76 | 5.33 | 3.23 | -0.05 | 92199.79 | 14.65 | skipped_fast |
| KITEUSDT | IDLE | 1.91 | 3.44 | 2.48 | 0.01 | 68402.06 | 10.68 | skipped_fast |
| RWAINCUSDT | IDLE | 1.53 | 3.05 | 1.73 | 0.02 | 28653.06 | 10.05 | skipped_fast |
| BIOUSDT | IDLE | 1.23 | 2.36 | 0.65 | 0.04 | 73458.07 | 3.87 | skipped_fast |
| EDELUSDT | IDLE | 0.72 | 2.07 | 1.32 | -0.08 | 209877.66 | 34.2 | skipped_fast |
| RIZEUSDT | IDLE | 0.65 | 1.73 | 1.01 | -0.0 | 67407.72 | 40.9 | skipped_fast |
| HBARUSDT | IDLE | 1.19 | 2.26 | 0.78 | 0.05 | 169352.31 | 2.34 | skipped_fast |
| TELUSDT | IDLE | 0.64 | 1.25 | 0.17 | 0.04 | 82648.93 | 16.81 | skipped_fast |
| FLUIDUSDT | IDLE | 0.85 | 1.71 | 0.0 | 0.01 | 8533.83 | 21.45 | skipped_fast |
| RWAUSDT | IDLE | 0.46 | 0.88 | 0.32 | 0.02 | 52447.07 | 39.57 | skipped_fast |
| MNSRYUSDT | IDLE | 0.24 | 0.45 | 0.23 | 0.01 | 38669.48 | 25.42 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
