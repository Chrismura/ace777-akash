# Hulk DIGEST — 2026-09-25T11:43:50Z

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
| XRPUSDT | IDLE | 2.23 | 4.63 | 0.45 | 0.08 | 79166116.1 | 3.16 | skipped_fast |
| ETHUSDT | IDLE | 1.47 | 2.83 | 0.71 | 0.03 | 367922587.38 | 0.07 | skipped_fast |
| BTCUSDT | IDLE | 0.94 | 1.79 | 0.59 | 0.02 | 711884381.03 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.84 | 6.74 | 0.54 | 0.13 | 1126244.15 | 5.56 | skipped_fast |
| HBARUSDT | IDLE | 2.58 | 5.01 | 1.01 | 0.06 | 934046.53 | 1.05 | skipped_fast |
| CCUSDT | IDLE | 1.91 | 7.32 | 0.4 | 0.14 | 658664.61 | 9.76 | skipped_fast |
| ZBCNUSDT | IDLE | 3.32 | 9.65 | 2.8 | 0.07 | 218279.21 | 27.69 | skipped_fast |
| RIZEUSDT | IDLE | 1.25 | 29.69 | 12.68 | 0.75 | 122364.71 | 43.32 | skipped_fast |
| WUSDT | IDLE | 2.18 | 4.36 | 0.0 | 0.06 | 331152.23 | 9.12 | skipped_fast |
| KITEUSDT | IDLE | 2.86 | 5.6 | 0.82 | -0.0 | 73801.37 | 9.93 | skipped_fast |
| QNTUSDT | IDLE | 0.92 | 9.34 | 6.09 | 0.35 | 622800.51 | 8.15 | skipped_fast |
| CHIPUSDT | IDLE | 1.83 | 9.9 | 1.64 | 0.19 | 108256.89 | 16.22 | skipped_fast |
| REDUSDT | IDLE | 2.04 | 5.87 | 0.0 | 0.11 | 135854.18 | 12.83 | skipped_fast |
| RWAINCUSDT | IDLE | 1.97 | 8.91 | 7.76 | 0.06 | 23532.88 | 81.34 | skipped_fast |
| BIOUSDT | IDLE | 1.46 | 4.04 | 0.32 | 0.1 | 93240.04 | 9.49 | skipped_fast |
| TELUSDT | IDLE | 2.62 | 5.12 | 0.83 | -0.01 | 112236.53 | 41.83 | skipped_fast |
| EDELUSDT | IDLE | 0.39 | 4.31 | 2.11 | 0.09 | 199229.82 | 71.42 | skipped_fast |
| FLUIDUSDT | IDLE | 1.5 | 3.44 | 0.47 | 0.09 | 435.65 | 22.12 | skipped_fast |
| MNSRYUSDT | IDLE | 1.27 | 2.42 | 0.82 | 0.03 | 44221.51 | 20.39 | skipped_fast |
| RWAUSDT | IDLE | 0.36 | 0.66 | 0.44 | 0.02 | 58906.65 | 21.89 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
