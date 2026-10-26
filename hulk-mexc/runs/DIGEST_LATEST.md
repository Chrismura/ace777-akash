# Hulk DIGEST — 2026-10-26T22:50:51Z

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
| ETHUSDT | IDLE | 0.76 | 1.38 | 0.95 | -0.01 | 145300538.66 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.69 | 1.25 | 0.93 | -0.01 | 24100106.5 | 2.32 | skipped_fast |
| BTCUSDT | IDLE | 0.5 | 0.89 | 0.67 | -0.01 | 360999638.8 | 0.0 | skipped_fast |
| QNTUSDT | IDLE | 1.32 | 5.55 | 4.43 | 0.06 | 1423420.88 | 2.96 | skipped_fast |
| PYTHUSDT | IDLE | 2.06 | 3.75 | 2.52 | -0.02 | 782427.49 | 5.41 | skipped_fast |
| WUSDT | IDLE | 1.74 | 3.36 | 2.37 | 0.04 | 646322.96 | 22.73 | skipped_fast |
| CHIPUSDT | IDLE | 1.62 | 12.1 | 10.37 | 0.15 | 324942.29 | 11.73 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 2.58 | 9.21 | 7.36 | -0.12 | 56597.02 | 25.62 | skipped_fast |
| EDELUSDT | IDLE | 2.25 | 3.98 | 3.52 | 0.0 | 119701.15 | 21.82 | skipped_fast |
| CCUSDT | IDLE | 1.43 | 2.58 | 1.8 | -0.03 | 185145.55 | 8.09 | skipped_fast |
| RIZEUSDT | IDLE | 2.28 | 4.28 | 1.83 | -0.0 | 44727.45 | 62.8 | skipped_fast |
| ZBCNUSDT | IDLE | 0.91 | 1.65 | 1.07 | -0.06 | 220013.91 | 25.23 | skipped_fast |
| WAXLUSDT | IDLE | 2.9 | 5.14 | 4.38 | -0.05 | 53760.76 | 38.36 | skipped_fast |
| BIOUSDT | IDLE | 1.37 | 2.46 | 1.83 | -0.01 | 56914.4 | 4.53 | skipped_fast |
| REDUSDT | IDLE | 1.27 | 2.34 | 1.37 | 0.01 | 63361.32 | 15.04 | skipped_fast |
| FLUIDUSDT | IDLE | 2.56 | 4.86 | 1.72 | -0.0 | 1743.21 | 21.34 | skipped_fast |
| KITEUSDT | IDLE | 0.66 | 1.24 | 0.51 | 0.02 | 53656.57 | 9.64 | skipped_fast |
| HBARUSDT | IDLE | 0.73 | 1.34 | 0.75 | -0.02 | 233940.86 | 11.73 | skipped_fast |
| IOTAUSDT | IDLE | 1.37 | 2.44 | 1.96 | -0.02 | 86392.68 | 26.16 | skipped_fast |
| LAUSDT | IDLE | 1.06 | 2.07 | 1.66 | 0.02 | 65860.3 | 22.36 | skipped_fast |
| RWAUSDT | IDLE | 0.72 | 1.37 | 0.4 | -0.0 | 53671.4 | 23.91 | skipped_fast |
| MNSRYUSDT | IDLE | 0.38 | 0.74 | 0.19 | -0.0 | 41502.7 | 76.46 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
