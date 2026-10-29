# Hulk DIGEST — 2026-10-29T09:18:35Z

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
| XRPUSDT | IDLE | 0.74 | 1.35 | 0.87 | -0.03 | 24000272.55 | 2.32 | skipped_fast |
| ETHUSDT | IDLE | 0.7 | 1.31 | 0.57 | -0.02 | 237043119.11 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.48 | 0.91 | 0.37 | -0.02 | 347606144.72 | 0.0 | skipped_fast |
| WUSDT | IDLE | 1.88 | 3.52 | 1.66 | -0.03 | 502370.35 | 17.75 | skipped_fast |
| PYTHUSDT | IDLE | 1.61 | 2.97 | 1.64 | -0.03 | 456328.64 | 2.84 | skipped_fast |
| CCUSDT | IDLE | 0.6 | 1.41 | 0.34 | -0.04 | 427853.52 | 9.29 | skipped_fast |
| QNTUSDT | IDLE | 1.61 | 2.91 | 2.05 | -0.04 | 431894.18 | 1.56 | skipped_fast |
| LAUSDT | IDLE | 3.21 | 5.76 | 4.4 | -0.04 | 56860.64 | 19.35 | skipped_fast |
| EDELUSDT | IDLE | 1.39 | 2.57 | 1.44 | -0.04 | 177820.97 | 9.57 | skipped_fast |
| HBARUSDT | IDLE | 1.01 | 1.89 | 0.93 | -0.04 | 559518.83 | 6.77 | skipped_fast |
| CHIPUSDT | IDLE | 0.68 | 3.55 | 1.47 | -0.12 | 242615.57 | 12.56 | skipped_fast |
| REDUSDT | IDLE | 1.56 | 2.85 | 1.85 | -0.04 | 64135.67 | 15.63 | skipped_fast |
| ZBCNUSDT | IDLE | 0.77 | 1.43 | 0.76 | -0.01 | 256522.12 | 17.04 | skipped_fast |
| BIOUSDT | IDLE | 1.5 | 2.85 | 1.03 | -0.03 | 67807.57 | 9.03 | skipped_fast |
| RWAINCUSDT | IDLE | 1.13 | 4.82 | 1.32 | -0.06 | 28740.71 | 7.09 | skipped_fast |
| RIZEUSDT | IDLE | 1.08 | 2.12 | 0.33 | -0.03 | 37667.46 | 11.71 | skipped_fast |
| KITEUSDT | IDLE | 0.81 | 1.51 | 0.75 | -0.04 | 60576.65 | 14.25 | skipped_fast |
| FLUIDUSDT | IDLE | 2.3 | 4.39 | 3.06 | -0.06 | 6071.6 | 21.72 | skipped_fast |
| WAXLUSDT | IDLE | 1.69 | 4.01 | 1.9 | -0.06 | 54018.39 | 39.15 | skipped_fast |
| IOTAUSDT | IDLE | 1.09 | 2.11 | 0.79 | -0.05 | 101721.79 | 22.37 | skipped_fast |
| RWAUSDT | IDLE | 1.1 | 2.01 | 1.26 | 0.0 | 56253.7 | 8.0 | skipped_fast |
| MNSRYUSDT | IDLE | 0.28 | 0.53 | 0.25 | -0.01 | 37199.94 | 56.07 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
