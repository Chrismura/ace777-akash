# Hulk DIGEST — 2026-10-17T10:16:39Z

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
| WUSDT | IDLE | 3.05 | 6.47 | 3.36 | 0.0 | 1342984.7 | 14.26 | skipped_fast |
| XRPUSDT | IDLE | 0.38 | 0.67 | 0.6 | -0.02 | 23210540.36 | 2.3 | skipped_fast |
| ETHUSDT | IDLE | 0.3 | 0.57 | 0.23 | -0.01 | 152557233.24 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.15 | 0.27 | 0.22 | -0.0 | 288797597.66 | 0.32 | skipped_fast |
| PYTHUSDT | IDLE | 0.65 | 1.71 | 0.87 | -0.09 | 1553499.79 | 2.37 | skipped_fast |
| ZBCNUSDT | IDLE | 2.09 | 5.29 | 1.17 | -0.03 | 220070.48 | 6.94 | skipped_fast |
| KITEUSDT | IDLE | 2.18 | 3.85 | 3.46 | -0.0 | 56467.25 | 9.01 | skipped_fast |
| CCUSDT | IDLE | 1.03 | 1.81 | 1.66 | -0.0 | 313267.26 | 6.78 | skipped_fast |
| QNTUSDT | IDLE | 0.86 | 1.64 | 0.48 | -0.01 | 651938.23 | 3.42 | skipped_fast |
| EDELUSDT | IDLE | 1.41 | 2.49 | 2.16 | -0.04 | 156515.85 | 10.34 | skipped_fast |
| RWAINCUSDT | IDLE | 1.48 | 6.18 | 0.47 | -0.05 | 22833.93 | 5.27 | skipped_fast |
| CHIPUSDT | IDLE | 1.1 | 2.63 | 2.56 | -0.08 | 102772.07 | 13.14 | skipped_fast |
| BIOUSDT | IDLE | 0.84 | 1.49 | 1.27 | -0.04 | 66657.74 | 4.02 | skipped_fast |
| REDUSDT | IDLE | 0.83 | 1.6 | 1.34 | -0.04 | 74493.52 | 18.32 | skipped_fast |
| RIZEUSDT | IDLE | 0.97 | 1.91 | 0.34 | 0.01 | 48566.02 | 36.01 | skipped_fast |
| HBARUSDT | IDLE | 0.51 | 0.89 | 0.82 | -0.03 | 237494.6 | 8.38 | skipped_fast |
| FLUIDUSDT | IDLE | 1.52 | 3.05 | 0.0 | 0.04 | 3684.02 | 21.33 | skipped_fast |
| TELUSDT | IDLE | 0.97 | 1.72 | 1.51 | -0.05 | 84792.99 | 23.63 | skipped_fast |
| RWAUSDT | IDLE | 0.58 | 1.12 | 0.24 | -0.01 | 51837.11 | 15.9 | skipped_fast |
| MNSRYUSDT | IDLE | 0.15 | 0.28 | 0.14 | -0.0 | 28718.85 | 9.91 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
