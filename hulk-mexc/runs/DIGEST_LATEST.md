# Hulk DIGEST — 2026-09-16T13:13:09Z

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
| ETHUSDT | IDLE | 1.1 | 2.0 | 1.35 | -0.03 | 494466562.96 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.84 | 2.21 | 2.07 | -0.12 | 89934183.84 | 2.36 | skipped_fast |
| BTCUSDT | IDLE | 0.68 | 1.24 | 0.76 | -0.02 | 594911308.1 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.32 | 2.4 | 1.61 | -0.03 | 687226.55 | 1.9 | skipped_fast |
| CHIPUSDT | IDLE | 2.44 | 5.63 | 2.94 | -0.04 | 98334.2 | 13.37 | skipped_fast |
| EDELUSDT | IDLE | 0.58 | 8.49 | 5.17 | 0.37 | 449165.39 | 40.98 | skipped_fast |
| RIZEUSDT | IDLE | 1.42 | 20.93 | 1.3 | 0.47 | 49655.24 | 36.04 | skipped_fast |
| REDUSDT | IDLE | 2.21 | 3.87 | 3.73 | -0.07 | 67667.69 | 20.24 | skipped_fast |
| CCUSDT | IDLE | 0.52 | 0.95 | 0.66 | -0.05 | 384018.74 | 9.89 | skipped_fast |
| WUSDT | IDLE | 1.1 | 2.33 | 2.21 | -0.1 | 223898.91 | 18.26 | skipped_fast |
| ZBCNUSDT | IDLE | 1.13 | 2.99 | 1.45 | -0.06 | 202711.66 | 64.26 | skipped_fast |
| BIOUSDT | IDLE | 1.12 | 2.0 | 1.56 | -0.02 | 80867.36 | 4.06 | skipped_fast |
| HBARUSDT | IDLE | 0.68 | 1.19 | 1.18 | -0.07 | 408457.6 | 1.36 | skipped_fast |
| TELUSDT | IDLE | 1.92 | 4.72 | 4.1 | -0.08 | 122876.0 | 63.18 | skipped_fast |
| RWAINCUSDT | IDLE | 0.87 | 1.52 | 1.5 | -0.04 | 13600.57 | 17.5 | skipped_fast |
| KITEUSDT | IDLE | 0.55 | 0.97 | 0.83 | -0.07 | 60639.28 | 12.08 | skipped_fast |
| FLUIDUSDT | IDLE | 1.42 | 2.48 | 2.42 | -0.08 | 1926.8 | 20.65 | skipped_fast |
| QNTUSDT | IDLE | 0.77 | 1.35 | 1.25 | -0.06 | 45911.19 | 8.45 | skipped_fast |
| RWAUSDT | IDLE | 0.66 | 1.23 | 0.61 | -0.02 | 52421.71 | 45.77 | skipped_fast |
| MNSRYUSDT | IDLE | 0.23 | 0.45 | 0.0 | -0.02 | 33858.95 | 7.07 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
