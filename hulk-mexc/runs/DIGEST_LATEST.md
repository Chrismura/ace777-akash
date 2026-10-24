# Hulk DIGEST — 2026-10-24T22:32:54Z

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
| XRPUSDT | IDLE | 0.9 | 1.76 | 0.29 | -0.0 | 29756448.57 | 1.55 | skipped_fast |
| ETHUSDT | IDLE | 0.79 | 1.54 | 0.26 | -0.02 | 135617653.66 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.33 | 0.64 | 0.16 | -0.01 | 275708425.96 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.68 | 3.27 | 0.57 | -0.0 | 621145.58 | 1.43 | skipped_fast |
| WUSDT | IDLE | 1.2 | 2.69 | 1.32 | -0.05 | 828167.24 | 64.12 | skipped_fast |
| EDELUSDT | IDLE | 1.57 | 3.78 | 2.18 | -0.06 | 594849.19 | 9.98 | skipped_fast |
| ZBCNUSDT | IDLE | 3.04 | 6.85 | 4.44 | -0.02 | 231747.69 | 15.8 | skipped_fast |
| RIZEUSDT | IDLE | 3.55 | 9.96 | 3.17 | -0.02 | 41580.87 | 60.47 | skipped_fast |
| CHIPUSDT | IDLE | 2.65 | 5.74 | 0.61 | 0.02 | 80568.31 | 18.04 | skipped_fast |
| CCUSDT | IDLE | 1.07 | 2.06 | 0.52 | -0.01 | 233839.82 | 11.86 | skipped_fast |
| RWAINCUSDT | IDLE | 1.56 | 2.75 | 2.46 | -0.02 | 53116.89 | 5.49 | skipped_fast |
| REDUSDT | IDLE | 1.15 | 4.25 | 1.44 | 0.07 | 100962.65 | 14.72 | skipped_fast |
| QNTUSDT | IDLE | 1.08 | 1.96 | 1.29 | -0.02 | 385333.44 | 0.56 | skipped_fast |
| BIOUSDT | IDLE | 1.14 | 2.24 | 0.22 | -0.02 | 68693.85 | 8.78 | skipped_fast |
| KITEUSDT | IDLE | 0.98 | 1.94 | 0.15 | -0.03 | 61989.51 | 9.61 | skipped_fast |
| LAUSDT | IDLE | 1.36 | 6.6 | 5.54 | 0.01 | 102680.92 | 17.73 | skipped_fast |
| HBARUSDT | IDLE | 1.09 | 2.08 | 0.68 | -0.0 | 202997.74 | 5.17 | skipped_fast |
| WAXLUSDT | IDLE | 0.99 | 2.91 | 0.83 | 0.05 | 57870.97 | 30.53 | skipped_fast |
| IOTAUSDT | IDLE | 1.03 | 1.98 | 0.57 | -0.02 | 71939.82 | 48.28 | skipped_fast |
| FLUIDUSDT | IDLE | 0.78 | 1.68 | 0.25 | -0.07 | 15056.09 | 17.19 | skipped_fast |
| RWAUSDT | IDLE | 0.58 | 1.12 | 0.24 | -0.01 | 53739.08 | 15.91 | skipped_fast |
| MNSRYUSDT | IDLE | 0.39 | 0.74 | 0.26 | -0.01 | 38002.58 | 77.07 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
