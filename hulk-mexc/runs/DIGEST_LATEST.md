# Hulk DIGEST — 2026-10-26T22:33:25Z

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
| ETHUSDT | IDLE | 0.78 | 1.38 | 1.15 | -0.02 | 145551554.54 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.7 | 1.25 | 1.05 | -0.01 | 24094405.45 | 1.55 | skipped_fast |
| BTCUSDT | IDLE | 0.5 | 0.89 | 0.75 | -0.01 | 360348026.18 | 0.04 | skipped_fast |
| QNTUSDT | IDLE | 1.31 | 5.55 | 4.22 | 0.06 | 1440200.56 | 9.36 | skipped_fast |
| PYTHUSDT | IDLE | 2.1 | 3.75 | 2.98 | -0.03 | 785578.1 | 4.07 | skipped_fast |
| WUSDT | IDLE | 1.78 | 3.36 | 2.89 | 0.03 | 646541.1 | 17.95 | skipped_fast |
| CHIPUSDT | IDLE | 1.62 | 12.1 | 10.42 | 0.15 | 325197.54 | 19.63 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 2.59 | 9.21 | 7.72 | -0.14 | 57168.51 | 25.71 | skipped_fast |
| EDELUSDT | IDLE | 2.25 | 3.98 | 3.49 | 0.01 | 117045.93 | 31.16 | skipped_fast |
| RIZEUSDT | IDLE | 2.28 | 4.28 | 1.92 | -0.0 | 44734.28 | 27.89 | skipped_fast |
| CCUSDT | IDLE | 1.44 | 2.58 | 2.0 | -0.03 | 183551.09 | 4.05 | skipped_fast |
| ZBCNUSDT | IDLE | 0.86 | 1.65 | 0.43 | -0.06 | 220593.9 | 23.19 | skipped_fast |
| BIOUSDT | IDLE | 1.39 | 2.46 | 2.09 | -0.02 | 57197.99 | 9.09 | skipped_fast |
| WAXLUSDT | IDLE | 2.89 | 5.14 | 4.28 | -0.04 | 53746.44 | 51.18 | skipped_fast |
| REDUSDT | IDLE | 1.29 | 2.34 | 1.62 | 0.0 | 63154.72 | 15.77 | skipped_fast |
| FLUIDUSDT | IDLE | 2.56 | 4.86 | 1.72 | -0.0 | 1743.21 | 21.09 | skipped_fast |
| KITEUSDT | IDLE | 0.67 | 1.24 | 0.66 | 0.01 | 53768.63 | 14.05 | skipped_fast |
| HBARUSDT | IDLE | 0.74 | 1.34 | 1.0 | -0.02 | 234163.99 | 6.53 | skipped_fast |
| IOTAUSDT | IDLE | 1.38 | 2.44 | 2.19 | -0.02 | 86418.71 | 26.22 | skipped_fast |
| LAUSDT | IDLE | 1.03 | 2.07 | 1.24 | 0.02 | 66052.05 | 24.0 | skipped_fast |
| RWAUSDT | IDLE | 0.73 | 1.37 | 0.63 | -0.0 | 53647.32 | 7.98 | skipped_fast |
| MNSRYUSDT | IDLE | 0.41 | 0.74 | 0.56 | -0.0 | 41422.19 | 76.46 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
