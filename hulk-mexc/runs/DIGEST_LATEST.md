# Hulk DIGEST — 2026-10-15T00:30:32Z

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
| PYTHUSDT | IDLE | 2.7 | 7.05 | 2.55 | 0.08 | 2121461.78 | 12.94 | skipped_fast |
| WUSDT | IDLE | 1.34 | 4.52 | 2.23 | -0.08 | 2388046.75 | 3.24 | skipped_fast |
| ETHUSDT | IDLE | 0.71 | 1.35 | 0.41 | -0.03 | 244561255.07 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.66 | 1.28 | 0.29 | -0.03 | 47065685.06 | 2.25 | skipped_fast |
| BTCUSDT | IDLE | 0.34 | 0.64 | 0.27 | -0.02 | 457582291.79 | 0.0 | skipped_fast |
| QNTUSDT | IDLE | 1.94 | 3.6 | 1.88 | -0.03 | 1038748.88 | 1.47 | skipped_fast |
| EDELUSDT | IDLE | 2.35 | 4.26 | 2.99 | -0.04 | 185944.23 | 12.2 | skipped_fast |
| RWAINCUSDT | IDLE | 2.58 | 5.72 | 2.09 | -0.03 | 25320.81 | 5.07 | skipped_fast |
| CCUSDT | IDLE | 1.01 | 2.07 | 1.82 | -0.08 | 394350.56 | 6.08 | skipped_fast |
| CHIPUSDT | IDLE | 1.39 | 4.97 | 4.53 | -0.12 | 103229.05 | 11.81 | skipped_fast |
| HBARUSDT | IDLE | 1.01 | 1.96 | 0.35 | -0.03 | 521987.45 | 5.9 | skipped_fast |
| ZBCNUSDT | IDLE | 1.23 | 2.25 | 1.63 | -0.05 | 194244.43 | 33.66 | skipped_fast |
| REDUSDT | IDLE | 1.6 | 3.03 | 1.17 | 0.0 | 63065.43 | 15.8 | skipped_fast |
| BIOUSDT | IDLE | 0.85 | 1.56 | 0.94 | -0.05 | 66706.15 | 7.58 | skipped_fast |
| TELUSDT | IDLE | 2.05 | 3.66 | 2.87 | -0.02 | 94686.98 | 22.75 | skipped_fast |
| KITEUSDT | IDLE | 0.55 | 1.66 | 0.99 | -0.03 | 87286.19 | 8.7 | skipped_fast |
| RIZEUSDT | IDLE | 0.64 | 3.53 | 3.05 | -0.03 | 53120.93 | 54.33 | skipped_fast |
| FLUIDUSDT | IDLE | 1.03 | 3.22 | 1.05 | 0.04 | 20476.06 | 21.35 | skipped_fast |
| RWAUSDT | IDLE | 0.5 | 0.88 | 0.79 | -0.03 | 56705.42 | 8.0 | skipped_fast |
| MNSRYUSDT | IDLE | 0.31 | 0.59 | 0.17 | -0.01 | 33933.14 | 37.99 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
