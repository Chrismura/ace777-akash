# Hulk DIGEST — 2026-10-14T23:27:55Z

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
| PYTHUSDT | IDLE | 2.72 | 7.97 | 2.34 | 0.09 | 2080354.81 | 1.17 | skipped_fast |
| WUSDT | IDLE | 1.28 | 4.66 | 2.47 | -0.1 | 2395984.56 | 7.15 | skipped_fast |
| ETHUSDT | IDLE | 0.73 | 1.35 | 0.77 | -0.03 | 238150655.25 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.67 | 1.28 | 0.37 | -0.02 | 46940815.82 | 1.5 | skipped_fast |
| BTCUSDT | IDLE | 0.36 | 0.64 | 0.54 | -0.02 | 446468937.19 | 0.0 | skipped_fast |
| QNTUSDT | IDLE | 1.95 | 3.6 | 2.04 | -0.04 | 1065123.77 | 0.98 | skipped_fast |
| CCUSDT | IDLE | 1.05 | 2.15 | 1.98 | -0.08 | 399727.75 | 3.47 | skipped_fast |
| RWAINCUSDT | IDLE | 2.45 | 5.89 | 2.19 | -0.03 | 25682.69 | 15.26 | skipped_fast |
| EDELUSDT | IDLE | 1.72 | 3.21 | 1.57 | -0.03 | 174068.33 | 15.04 | skipped_fast |
| ZBCNUSDT | IDLE | 1.43 | 2.62 | 1.9 | -0.04 | 202029.12 | 17.05 | skipped_fast |
| CHIPUSDT | IDLE | 1.4 | 4.82 | 4.06 | -0.1 | 101561.4 | 11.69 | skipped_fast |
| HBARUSDT | IDLE | 0.97 | 1.87 | 0.46 | -0.03 | 521498.28 | 4.74 | skipped_fast |
| TELUSDT | IDLE | 2.59 | 4.58 | 3.94 | -0.03 | 98366.96 | 17.09 | skipped_fast |
| REDUSDT | IDLE | 1.3 | 2.6 | 0.0 | 0.02 | 62871.25 | 18.28 | skipped_fast |
| KITEUSDT | IDLE | 0.72 | 2.09 | 1.48 | -0.02 | 86755.58 | 8.67 | skipped_fast |
| BIOUSDT | IDLE | 0.81 | 1.56 | 0.38 | -0.04 | 66942.32 | 3.77 | skipped_fast |
| RIZEUSDT | IDLE | 0.67 | 3.64 | 2.61 | -0.01 | 50880.86 | 17.16 | skipped_fast |
| FLUIDUSDT | IDLE | 1.28 | 4.0 | 1.36 | 0.05 | 19165.45 | 21.58 | skipped_fast |
| RWAUSDT | IDLE | 0.49 | 0.88 | 0.71 | -0.03 | 56507.57 | 8.0 | skipped_fast |
| MNSRYUSDT | IDLE | 0.39 | 0.72 | 0.34 | -0.01 | 35168.4 | 23.94 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
