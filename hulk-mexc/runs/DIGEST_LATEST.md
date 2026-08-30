# Hulk DIGEST — 2026-08-30T15:13:59Z

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
| XRPUSDT | IDLE | 1.0 | 1.87 | 0.83 | 0.0 | 17906446.69 | 2.14 | skipped_fast |
| BTCUSDT | IDLE | 0.66 | 1.27 | 0.33 | 0.01 | 252178891.51 | 0.0 | skipped_fast |
| ETHUSDT | IDLE | 0.6 | 1.16 | 0.26 | 0.01 | 161723804.84 | 0.04 | skipped_fast |
| CHIPUSDT | IDLE | 4.25 | 8.32 | 4.29 | -0.0 | 560020.14 | 4.92 | skipped_fast |
| PYTHUSDT | IDLE | 3.78 | 7.17 | 2.65 | 0.02 | 400865.82 | 2.04 | skipped_fast |
| ZBCNUSDT | IDLE | 2.58 | 4.6 | 3.76 | -0.03 | 150660.52 | 9.49 | skipped_fast |
| EDELUSDT | IDLE | 1.91 | 5.99 | 4.52 | 0.11 | 111110.71 | 33.81 | skipped_fast |
| WUSDT | IDLE | 1.4 | 2.77 | 0.22 | 0.04 | 215886.26 | 13.63 | skipped_fast |
| CCUSDT | IDLE | 0.89 | 1.62 | 1.12 | 0.02 | 270633.05 | 10.13 | skipped_fast |
| REDUSDT | IDLE | 1.12 | 2.14 | 0.72 | 0.02 | 60330.8 | 13.6 | skipped_fast |
| BIOUSDT | IDLE | 0.75 | 1.36 | 0.91 | -0.01 | 74061.43 | 3.66 | skipped_fast |
| KITEUSDT | IDLE | 0.62 | 1.21 | 0.22 | -0.04 | 61099.86 | 11.66 | skipped_fast |
| RIZEUSDT | IDLE | 0.79 | 2.75 | 1.12 | -0.06 | 45955.84 | 61.0 | skipped_fast |
| RWAINCUSDT | IDLE | 1.5 | 3.01 | 0.0 | 0.0 | 1671.88 | 127.74 | skipped_fast |
| TELUSDT | IDLE | 1.35 | 2.59 | 0.7 | -0.02 | 78674.69 | 41.38 | skipped_fast |
| HBARUSDT | IDLE | 0.66 | 1.2 | 0.75 | -0.0 | 133325.69 | 1.33 | skipped_fast |
| QNTUSDT | IDLE | 0.51 | 0.96 | 0.45 | 0.01 | 37844.95 | 1.62 | skipped_fast |
| MNSRYUSDT | IDLE | 0.75 | 1.41 | 0.58 | 0.02 | 33144.43 | 30.66 | skipped_fast |
| RWAUSDT | IDLE | 0.46 | 0.9 | 0.08 | 0.02 | 53067.68 | 24.38 | skipped_fast |
| FLUIDUSDT | IDLE | 0.41 | 0.83 | 0.0 | 0.03 | 3154.32 | 21.73 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
