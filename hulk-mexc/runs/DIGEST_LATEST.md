# Hulk DIGEST — 2026-08-30T16:05:52Z

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
| XRPUSDT | IDLE | 0.84 | 1.57 | 0.71 | 0.01 | 18086383.3 | 2.86 | skipped_fast |
| ETHUSDT | IDLE | 0.64 | 1.27 | 0.06 | 0.02 | 166108093.74 | 1.09 | skipped_fast |
| BTCUSDT | IDLE | 0.56 | 1.12 | 0.01 | 0.01 | 258484384.66 | 0.0 | skipped_fast |
| CHIPUSDT | IDLE | 4.13 | 8.01 | 4.69 | -0.01 | 552040.05 | 2.47 | skipped_fast |
| PYTHUSDT | IDLE | 3.15 | 5.93 | 2.51 | 0.02 | 406967.87 | 4.08 | skipped_fast |
| ZBCNUSDT | IDLE | 2.56 | 4.6 | 3.49 | -0.03 | 162444.52 | 12.58 | skipped_fast |
| EDELUSDT | IDLE | 2.15 | 5.99 | 5.01 | 0.06 | 72796.11 | 34.1 | skipped_fast |
| WUSDT | IDLE | 1.33 | 2.63 | 0.26 | 0.04 | 221069.93 | 14.67 | skipped_fast |
| CCUSDT | IDLE | 0.89 | 1.62 | 1.1 | 0.02 | 268679.8 | 6.75 | skipped_fast |
| REDUSDT | IDLE | 1.1 | 2.14 | 0.4 | 0.02 | 60225.13 | 9.92 | skipped_fast |
| BIOUSDT | IDLE | 0.73 | 1.36 | 0.62 | -0.01 | 73934.37 | 7.29 | skipped_fast |
| KITEUSDT | IDLE | 0.64 | 1.21 | 0.53 | -0.04 | 60919.34 | 12.47 | skipped_fast |
| RIZEUSDT | IDLE | 0.69 | 2.45 | 0.71 | -0.05 | 45927.0 | 47.32 | skipped_fast |
| TELUSDT | IDLE | 1.72 | 3.37 | 0.41 | -0.01 | 81931.62 | 35.05 | skipped_fast |
| RWAINCUSDT | IDLE | 1.5 | 3.01 | 0.0 | 0.0 | 1671.88 | 127.74 | skipped_fast |
| HBARUSDT | IDLE | 0.63 | 1.13 | 0.82 | -0.01 | 130271.74 | 1.33 | skipped_fast |
| QNTUSDT | IDLE | 0.5 | 0.96 | 0.31 | 0.01 | 38434.61 | 6.46 | skipped_fast |
| MNSRYUSDT | IDLE | 0.76 | 1.41 | 0.69 | 0.01 | 33068.89 | 40.01 | skipped_fast |
| RWAUSDT | IDLE | 0.42 | 0.82 | 0.16 | 0.01 | 53130.45 | 32.52 | skipped_fast |
| FLUIDUSDT | IDLE | 0.41 | 0.83 | 0.0 | 0.03 | 3154.32 | 21.65 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
