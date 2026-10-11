# Hulk DIGEST — 2026-10-11T08:33:42Z

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
| XRPUSDT | IDLE | 0.52 | 0.96 | 0.52 | -0.01 | 10067512.12 | 2.15 | skipped_fast |
| ETHUSDT | IDLE | 0.29 | 0.51 | 0.46 | 0.0 | 167457069.36 | 0.2 | skipped_fast |
| BTCUSDT | IDLE | 0.27 | 0.51 | 0.23 | 0.0 | 135689376.05 | 0.0 | skipped_fast |
| WUSDT | IDLE | 1.54 | 4.74 | 2.06 | 0.03 | 1235503.18 | 6.89 | skipped_fast |
| PYTHUSDT | IDLE | 3.01 | 5.54 | 3.26 | -0.02 | 723948.94 | 2.58 | skipped_fast |
| QNTUSDT | IDLE | 0.86 | 1.64 | 0.87 | -0.05 | 1279660.09 | 0.84 | skipped_fast |
| EDELUSDT | IDLE | 2.45 | 4.54 | 2.39 | -0.04 | 363630.87 | 15.45 | skipped_fast |
| CHIPUSDT | IDLE | 1.29 | 11.69 | 7.23 | 0.22 | 313997.33 | 15.68 | skipped_fast |
| BIOUSDT | IDLE | 2.56 | 5.01 | 0.77 | 0.03 | 78355.0 | 10.09 | skipped_fast |
| CCUSDT | IDLE | 1.51 | 3.02 | 0.0 | -0.0 | 225984.79 | 14.05 | skipped_fast |
| RIZEUSDT | IDLE | 2.17 | 4.09 | 2.55 | -0.04 | 32533.72 | 58.15 | skipped_fast |
| ZBCNUSDT | IDLE | 1.11 | 1.97 | 1.64 | -0.01 | 149463.09 | 13.32 | skipped_fast |
| RWAINCUSDT | IDLE | 1.4 | 2.46 | 2.21 | -0.02 | 19496.27 | 5.02 | skipped_fast |
| REDUSDT | IDLE | 1.36 | 2.61 | 0.69 | 0.0 | 57723.3 | 14.68 | skipped_fast |
| KITEUSDT | IDLE | 0.94 | 1.74 | 0.88 | 0.0 | 75177.39 | 10.32 | skipped_fast |
| FLUIDUSDT | IDLE | 2.29 | 4.57 | 0.0 | 0.02 | 9481.28 | 21.38 | skipped_fast |
| TELUSDT | IDLE | 1.67 | 3.04 | 2.01 | -0.05 | 135969.13 | 34.11 | skipped_fast |
| HBARUSDT | IDLE | 0.78 | 1.48 | 0.49 | -0.01 | 277805.7 | 5.44 | skipped_fast |
| RWAUSDT | IDLE | 0.53 | 0.95 | 0.71 | -0.01 | 53124.09 | 7.93 | skipped_fast |
| MNSRYUSDT | IDLE | 0.58 | 1.03 | 0.93 | -0.02 | 34181.47 | 28.86 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
