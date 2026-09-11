# Hulk DIGEST — 2026-09-11T03:15:20Z

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
| XRPUSDT | IDLE | 1.04 | 1.93 | 0.97 | -0.04 | 40933528.04 | 1.49 | skipped_fast |
| ETHUSDT | IDLE | 0.63 | 1.16 | 0.62 | -0.01 | 426877295.99 | 0.9 | skipped_fast |
| BTCUSDT | IDLE | 0.5 | 0.93 | 0.43 | -0.02 | 536480634.12 | 0.0 | skipped_fast |
| RIZEUSDT | IDLE | 0.97 | 51.94 | 24.51 | -0.46 | 146810.46 | 89.37 | skipped_fast |
| CHIPUSDT | IDLE | 3.29 | 7.69 | 3.51 | -0.03 | 99582.39 | 14.71 | skipped_fast |
| PYTHUSDT | IDLE | 1.65 | 2.97 | 2.26 | -0.02 | 415861.13 | 1.96 | skipped_fast |
| CCUSDT | IDLE | 1.22 | 2.31 | 1.54 | -0.06 | 451444.01 | 7.15 | skipped_fast |
| EDELUSDT | IDLE | 1.49 | 6.03 | 4.18 | -0.04 | 207045.77 | 18.57 | skipped_fast |
| ZBCNUSDT | IDLE | 0.96 | 1.81 | 0.72 | -0.02 | 206693.67 | 25.09 | skipped_fast |
| WUSDT | IDLE | 1.02 | 1.89 | 0.97 | -0.03 | 163789.02 | 17.81 | skipped_fast |
| BIOUSDT | IDLE | 0.98 | 1.87 | 0.64 | -0.03 | 76929.09 | 4.01 | skipped_fast |
| KITEUSDT | IDLE | 0.9 | 1.72 | 0.55 | -0.03 | 57882.35 | 13.75 | skipped_fast |
| REDUSDT | IDLE | 0.84 | 1.51 | 1.08 | -0.05 | 59903.9 | 19.04 | skipped_fast |
| RWAINCUSDT | IDLE | 0.59 | 1.18 | 0.0 | 0.03 | 4182.63 | 5.54 | skipped_fast |
| TELUSDT | IDLE | 1.74 | 3.03 | 2.94 | -0.03 | 88264.27 | 51.27 | skipped_fast |
| HBARUSDT | IDLE | 0.79 | 1.45 | 0.88 | -0.03 | 179668.22 | 1.33 | skipped_fast |
| FLUIDUSDT | IDLE | 1.69 | 3.38 | 0.0 | -0.02 | 1894.98 | 21.78 | skipped_fast |
| QNTUSDT | IDLE | 0.93 | 1.69 | 1.18 | -0.04 | 35595.63 | 7.76 | skipped_fast |
| RWAUSDT | IDLE | 0.57 | 1.07 | 0.45 | -0.02 | 50424.49 | 22.86 | skipped_fast |
| MNSRYUSDT | IDLE | 0.31 | 0.56 | 0.4 | -0.01 | 35396.24 | 18.19 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
