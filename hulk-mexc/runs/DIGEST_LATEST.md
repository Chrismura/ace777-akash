# Hulk DIGEST — 2026-10-20T08:59:46Z

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
| ETHUSDT | IDLE | 0.89 | 1.57 | 1.39 | -0.02 | 131841948.14 | 0.29 | skipped_fast |
| XRPUSDT | IDLE | 0.69 | 1.21 | 1.11 | -0.02 | 20543504.26 | 0.77 | skipped_fast |
| BTCUSDT | IDLE | 0.62 | 1.09 | 0.94 | -0.02 | 304939094.55 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.68 | 3.09 | 1.81 | -0.03 | 1003822.91 | 1.38 | skipped_fast |
| WUSDT | IDLE | 2.11 | 3.83 | 2.59 | 0.01 | 727215.83 | 15.41 | skipped_fast |
| EDELUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.86 | 15.54 | 0.66 | 0.17 | 297851.8 | 21.95 | skipped_fast |
| CCUSDT | IDLE | 2.47 | 4.36 | 3.92 | 0.01 | 462845.79 | 5.79 | skipped_fast |
| QNTUSDT | IDLE | 2.62 | 4.71 | 3.52 | -0.04 | 624156.2 | 0.52 | skipped_fast |
| CHIPUSDT | IDLE | 2.57 | 6.6 | 2.72 | 0.03 | 92754.49 | 13.71 | skipped_fast |
| KITEUSDT | IDLE | 1.76 | 3.15 | 2.52 | 0.05 | 78780.26 | 12.31 | skipped_fast |
| ZBCNUSDT | IDLE | 1.32 | 2.41 | 1.53 | -0.02 | 170655.89 | 24.48 | skipped_fast |
| HBARUSDT | IDLE | 1.16 | 2.05 | 1.81 | -0.02 | 396465.93 | 6.05 | skipped_fast |
| RWAINCUSDT | IDLE | 1.02 | 1.82 | 1.43 | 0.02 | 74801.75 | 5.19 | skipped_fast |
| BIOUSDT | IDLE | 1.02 | 1.84 | 1.38 | -0.01 | 65948.73 | 4.25 | skipped_fast |
| REDUSDT | IDLE | 1.07 | 1.9 | 1.63 | -0.0 | 58350.21 | 8.78 | skipped_fast |
| RIZEUSDT | IDLE | 0.66 | 2.43 | 2.1 | -0.08 | 67213.01 | 23.76 | skipped_fast |
| LAUSDT | IDLE | 1.4 | 2.49 | 2.07 | -0.02 | 55763.98 | 17.29 | skipped_fast |
| IOTAUSDT | IDLE | 1.22 | 2.17 | 1.86 | 0.0 | 90943.18 | 28.74 | skipped_fast |
| WAXLUSDT | IDLE | 1.44 | 2.98 | 1.94 | -0.06 | 56959.8 | 51.08 | skipped_fast |
| FLUIDUSDT | IDLE | 1.29 | 2.38 | 1.4 | -0.01 | 4449.41 | 21.56 | skipped_fast |
| RWAUSDT | IDLE | 0.21 | 0.39 | 0.16 | 0.01 | 51735.15 | 15.7 | skipped_fast |
| MNSRYUSDT | IDLE | 0.14 | 0.26 | 0.07 | -0.0 | 40020.43 | 5.7 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
