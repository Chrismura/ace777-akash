# Hulk DIGEST — 2026-10-10T06:43:25Z

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
| WUSDT | IDLE | 2.4 | 6.03 | 5.03 | -0.02 | 1976256.04 | 19.5 | skipped_fast |
| PYTHUSDT | IDLE | 1.82 | 4.61 | 2.99 | -0.06 | 1491370.05 | 2.5 | skipped_fast |
| XRPUSDT | IDLE | 0.52 | 1.02 | 0.19 | 0.01 | 23952486.98 | 1.42 | skipped_fast |
| ETHUSDT | IDLE | 0.22 | 0.42 | 0.11 | -0.0 | 141372321.02 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.18 | 0.35 | 0.06 | 0.0 | 241011272.97 | 0.0 | skipped_fast |
| QNTUSDT | IDLE | 1.14 | 2.03 | 1.67 | 0.0 | 1226237.83 | 2.04 | skipped_fast |
| CCUSDT | IDLE | 1.14 | 2.33 | 1.77 | 0.02 | 571440.51 | 9.88 | skipped_fast |
| ZBCNUSDT | IDLE | 0.93 | 2.42 | 1.08 | -0.09 | 264426.38 | 12.79 | skipped_fast |
| RIZEUSDT | IDLE | 1.06 | 5.68 | 5.09 | 0.05 | 67308.58 | 17.96 | skipped_fast |
| BIOUSDT | IDLE | 1.38 | 2.59 | 1.09 | 0.01 | 61833.73 | 6.9 | skipped_fast |
| EDELUSDT | IDLE | 0.63 | 2.37 | 1.58 | 0.12 | 208156.49 | 15.0 | skipped_fast |
| REDUSDT | IDLE | 1.19 | 2.16 | 1.53 | 0.0 | 58015.63 | 8.69 | skipped_fast |
| CHIPUSDT | IDLE | 0.99 | 3.18 | 0.32 | 0.07 | 88434.75 | 13.13 | skipped_fast |
| KITEUSDT | IDLE | 1.07 | 2.04 | 0.62 | -0.03 | 75830.43 | 10.63 | skipped_fast |
| RWAINCUSDT | IDLE | 1.16 | 2.29 | 0.14 | 0.04 | 8509.11 | 52.37 | skipped_fast |
| HBARUSDT | IDLE | 0.73 | 1.43 | 0.25 | 0.0 | 298011.37 | 3.23 | skipped_fast |
| RWAUSDT | IDLE | 1.72 | 3.08 | 2.45 | -0.01 | 51972.38 | 23.58 | skipped_fast |
| TELUSDT | IDLE | 1.3 | 2.61 | 0.0 | 0.01 | 112086.02 | 31.86 | skipped_fast |
| MNSRYUSDT | IDLE | 0.75 | 1.42 | 0.48 | 0.01 | 42023.56 | 20.25 | skipped_fast |
| FLUIDUSDT | IDLE | 0.23 | 1.44 | 0.24 | 0.01 | 18653.96 | 20.76 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
