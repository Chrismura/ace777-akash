# Hulk DIGEST — 2026-09-23T20:08:40Z

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
| XRPUSDT | IDLE | 1.33 | 3.46 | 2.83 | -0.06 | 113059114.14 | 2.01 | skipped_fast |
| ETHUSDT | IDLE | 0.95 | 1.85 | 0.36 | -0.03 | 501581732.89 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.79 | 1.5 | 0.51 | -0.02 | 846706204.74 | 0.64 | skipped_fast |
| PYTHUSDT | IDLE | 1.98 | 6.48 | 2.53 | -0.05 | 1332158.19 | 6.41 | skipped_fast |
| HBARUSDT | IDLE | 1.14 | 3.63 | 2.14 | -0.09 | 1370531.38 | 1.11 | skipped_fast |
| CCUSDT | IDLE | 1.33 | 3.32 | 0.2 | -0.04 | 534302.31 | 10.06 | skipped_fast |
| WUSDT | IDLE | 1.72 | 4.4 | 3.66 | -0.05 | 391150.0 | 4.44 | skipped_fast |
| EDELUSDT | IDLE | 2.46 | 6.6 | 5.44 | -0.09 | 179356.88 | 21.56 | skipped_fast |
| CHIPUSDT | IDLE | 1.97 | 5.98 | 5.1 | -0.07 | 218664.39 | 19.11 | skipped_fast |
| KITEUSDT | IDLE | 2.26 | 4.29 | 3.91 | -0.06 | 175427.17 | 11.48 | skipped_fast |
| REDUSDT | IDLE | 2.29 | 4.34 | 4.07 | -0.04 | 58828.62 | 14.56 | skipped_fast |
| BIOUSDT | IDLE | 1.95 | 5.04 | 2.66 | -0.04 | 96129.49 | 10.65 | skipped_fast |
| ZBCNUSDT | IDLE | 1.45 | 3.75 | 1.34 | 0.01 | 230055.38 | 19.73 | skipped_fast |
| RIZEUSDT | IDLE | 1.3 | 11.55 | 8.93 | 0.27 | 73286.52 | 74.57 | skipped_fast |
| QNTUSDT | IDLE | 1.64 | 3.7 | 3.2 | -0.01 | 178887.65 | 7.04 | skipped_fast |
| FLUIDUSDT | IDLE | 1.71 | 3.58 | 2.53 | -0.05 | 4371.31 | 21.65 | skipped_fast |
| RWAUSDT | IDLE | 1.41 | 2.64 | 1.18 | -0.03 | 56221.69 | 14.88 | skipped_fast |
| RWAINCUSDT | IDLE | 0.65 | 1.25 | 0.32 | -0.03 | 18487.28 | 59.41 | skipped_fast |
| TELUSDT | IDLE | 0.82 | 2.31 | 0.69 | -0.04 | 155886.77 | 34.97 | skipped_fast |
| MNSRYUSDT | IDLE | 0.4 | 0.77 | 0.25 | -0.01 | 40970.95 | 35.09 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
