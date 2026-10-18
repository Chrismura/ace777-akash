# Hulk DIGEST — 2026-10-18T05:28:03Z

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
| ETHUSDT | IDLE | 0.71 | 1.31 | 0.74 | -0.01 | 90492978.79 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.59 | 1.04 | 0.88 | -0.01 | 18346712.67 | 1.55 | skipped_fast |
| BTCUSDT | IDLE | 0.43 | 0.8 | 0.39 | 0.0 | 185814040.96 | 0.08 | skipped_fast |
| PYTHUSDT | IDLE | 1.39 | 3.45 | 3.16 | -0.09 | 1285210.8 | 3.89 | skipped_fast |
| WUSDT | IDLE | 1.02 | 2.89 | 2.69 | -0.06 | 1179679.23 | 14.75 | skipped_fast |
| EDELUSDT | IDLE | 2.59 | 8.34 | 4.54 | -0.09 | 183635.62 | 18.6 | skipped_fast |
| ZBCNUSDT | IDLE | 2.25 | 4.03 | 3.14 | -0.04 | 176739.46 | 17.69 | skipped_fast |
| QNTUSDT | IDLE | 1.65 | 2.9 | 2.6 | -0.05 | 573772.53 | 5.68 | skipped_fast |
| REDUSDT | IDLE | 1.9 | 3.31 | 3.2 | -0.05 | 60212.9 | 9.56 | skipped_fast |
| CCUSDT | IDLE | 1.04 | 1.82 | 1.74 | -0.02 | 254159.89 | 6.85 | skipped_fast |
| CHIPUSDT | IDLE | 1.21 | 3.15 | 2.48 | -0.08 | 74480.71 | 11.69 | skipped_fast |
| BIOUSDT | IDLE | 1.27 | 2.22 | 2.13 | -0.05 | 70487.95 | 8.36 | skipped_fast |
| KITEUSDT | IDLE | 0.85 | 2.02 | 1.98 | -0.07 | 70444.66 | 13.08 | skipped_fast |
| HBARUSDT | IDLE | 1.23 | 2.16 | 2.04 | 0.01 | 273454.97 | 5.87 | skipped_fast |
| RIZEUSDT | IDLE | 1.18 | 2.2 | 1.09 | 0.01 | 45663.29 | 61.33 | skipped_fast |
| RWAINCUSDT | IDLE | 0.41 | 1.28 | 0.21 | 0.05 | 18568.9 | 10.51 | skipped_fast |
| TELUSDT | IDLE | 1.03 | 1.81 | 1.72 | -0.07 | 104324.72 | 24.95 | skipped_fast |
| RWAUSDT | IDLE | 0.41 | 0.8 | 0.16 | 0.0 | 50823.6 | 15.94 | skipped_fast |
| FLUIDUSDT | IDLE | 0.34 | 0.6 | 0.6 | -0.01 | 1217.0 | 20.5 | skipped_fast |
| MNSRYUSDT | IDLE | 0.47 | 0.84 | 0.69 | -0.01 | 29203.01 | 49.73 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
