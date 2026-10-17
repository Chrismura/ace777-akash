# Hulk DIGEST — 2026-10-17T19:20:38Z

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
| XRPUSDT | IDLE | 0.68 | 1.3 | 0.43 | 0.0 | 14461262.92 | 1.54 | skipped_fast |
| ETHUSDT | IDLE | 0.65 | 1.23 | 0.5 | 0.0 | 81761736.98 | 0.04 | skipped_fast |
| PYTHUSDT | IDLE | 2.84 | 7.06 | 3.56 | -0.02 | 1064663.25 | 1.21 | skipped_fast |
| BTCUSDT | IDLE | 0.26 | 0.51 | 0.09 | 0.0 | 171750898.62 | 0.04 | skipped_fast |
| WUSDT | IDLE | 1.82 | 5.39 | 1.97 | -0.01 | 1133112.29 | 16.44 | skipped_fast |
| QNTUSDT | IDLE | 2.1 | 3.92 | 1.9 | -0.01 | 542845.45 | 1.0 | skipped_fast |
| CCUSDT | IDLE | 1.22 | 2.28 | 1.13 | 0.02 | 249226.92 | 9.57 | skipped_fast |
| ZBCNUSDT | IDLE | 1.22 | 2.34 | 0.67 | -0.01 | 194418.14 | 14.0 | skipped_fast |
| EDELUSDT | IDLE | 1.29 | 2.37 | 1.35 | -0.05 | 155524.12 | 17.52 | skipped_fast |
| CHIPUSDT | IDLE | 1.55 | 2.89 | 1.43 | -0.03 | 86273.66 | 15.84 | skipped_fast |
| BIOUSDT | IDLE | 1.33 | 2.62 | 0.32 | -0.02 | 68682.99 | 4.07 | skipped_fast |
| RWAINCUSDT | IDLE | 1.14 | 4.99 | 0.36 | 0.12 | 23039.82 | 5.19 | skipped_fast |
| KITEUSDT | IDLE | 1.11 | 2.13 | 1.08 | -0.02 | 63913.06 | 11.02 | skipped_fast |
| REDUSDT | IDLE | 0.95 | 1.78 | 0.79 | -0.02 | 59846.07 | 17.12 | skipped_fast |
| RIZEUSDT | IDLE | 0.95 | 1.8 | 0.92 | -0.04 | 49608.67 | 33.88 | skipped_fast |
| HBARUSDT | IDLE | 1.05 | 2.08 | 0.1 | 0.02 | 159143.23 | 7.17 | skipped_fast |
| TELUSDT | IDLE | 1.35 | 2.36 | 2.3 | -0.07 | 86125.38 | 18.13 | skipped_fast |
| FLUIDUSDT | IDLE | 1.46 | 2.74 | 1.17 | 0.02 | 2406.75 | 21.46 | skipped_fast |
| RWAUSDT | IDLE | 0.53 | 0.96 | 0.63 | 0.0 | 50848.64 | 15.87 | skipped_fast |
| MNSRYUSDT | IDLE | 0.53 | 1.05 | 0.03 | 0.01 | 29396.05 | 7.04 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
