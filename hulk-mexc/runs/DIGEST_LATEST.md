# Hulk DIGEST — 2026-09-24T20:39:56Z

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
| XRPUSDT | IDLE | 1.77 | 3.4 | 0.91 | 0.03 | 68648519.84 | 1.96 | skipped_fast |
| ETHUSDT | IDLE | 1.04 | 1.98 | 0.65 | 0.0 | 348177971.51 | 0.04 | skipped_fast |
| PYTHUSDT | IDLE | 2.12 | 7.43 | 5.13 | 0.08 | 1324750.93 | 1.48 | skipped_fast |
| BTCUSDT | IDLE | 0.88 | 1.67 | 0.66 | -0.0 | 708805914.26 | 0.0 | skipped_fast |
| CCUSDT | IDLE | 2.89 | 5.72 | 0.41 | 0.05 | 476014.75 | 6.11 | skipped_fast |
| CHIPUSDT | IDLE | 3.17 | 15.49 | 2.94 | 0.14 | 85657.08 | 10.49 | skipped_fast |
| RIZEUSDT | IDLE | 2.96 | 31.49 | 4.71 | 0.36 | 61157.21 | 118.12 | skipped_fast |
| HBARUSDT | IDLE | 1.33 | 2.56 | 0.7 | 0.03 | 813710.56 | 1.08 | skipped_fast |
| RWAINCUSDT | IDLE | 3.39 | 14.23 | 2.31 | 0.14 | 10370.13 | 99.46 | skipped_fast |
| EDELUSDT | IDLE | 2.19 | 5.99 | 0.39 | 0.01 | 155030.62 | 10.57 | skipped_fast |
| WUSDT | IDLE | 1.44 | 2.69 | 1.2 | 0.05 | 239401.3 | 5.09 | skipped_fast |
| ZBCNUSDT | IDLE | 1.61 | 3.02 | 1.3 | 0.03 | 218437.25 | 18.36 | skipped_fast |
| BIOUSDT | IDLE | 1.79 | 5.64 | 1.71 | 0.11 | 85023.56 | 6.42 | skipped_fast |
| REDUSDT | IDLE | 1.34 | 3.67 | 1.11 | 0.07 | 100912.83 | 13.66 | skipped_fast |
| QNTUSDT | IDLE | 1.47 | 9.41 | 1.06 | 0.22 | 230053.6 | 11.57 | skipped_fast |
| KITEUSDT | IDLE | 1.29 | 2.44 | 0.94 | 0.02 | 65329.69 | 9.76 | skipped_fast |
| TELUSDT | IDLE | 2.59 | 4.77 | 2.78 | -0.04 | 109625.72 | 42.54 | skipped_fast |
| FLUIDUSDT | IDLE | 1.32 | 2.6 | 0.28 | 0.05 | 2468.58 | 20.66 | skipped_fast |
| RWAUSDT | IDLE | 0.78 | 1.47 | 0.65 | 0.02 | 56605.29 | 7.3 | skipped_fast |
| MNSRYUSDT | IDLE | 0.14 | 0.25 | 0.14 | 0.0 | 37475.0 | 7.77 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
