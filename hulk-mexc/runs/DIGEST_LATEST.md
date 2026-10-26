# Hulk DIGEST — 2026-10-26T16:48:16Z

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
| ETHUSDT | IDLE | 1.16 | 2.11 | 1.34 | -0.01 | 138495502.83 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 1.11 | 2.01 | 1.36 | -0.01 | 24622781.12 | 0.78 | skipped_fast |
| BTCUSDT | IDLE | 0.93 | 1.69 | 1.13 | -0.01 | 339633784.43 | 0.04 | skipped_fast |
| QNTUSDT | IDLE | 1.84 | 7.75 | 6.98 | 0.11 | 1504602.76 | 6.73 | skipped_fast |
| PYTHUSDT | IDLE | 2.02 | 3.76 | 1.82 | 0.06 | 947376.09 | 5.3 | skipped_fast |
| WUSDT | IDLE | 3.11 | 5.99 | 1.54 | 0.01 | 586811.91 | 41.84 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 3.21 | 13.37 | 11.33 | -0.15 | 63504.87 | 25.89 | skipped_fast |
| CHIPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.36 | 13.6 | 1.43 | 0.17 | 229701.16 | 26.94 | skipped_fast |
| ZBCNUSDT | IDLE | 1.3 | 3.05 | 1.88 | -0.06 | 211894.46 | 27.91 | skipped_fast |
| BIOUSDT | IDLE | 1.82 | 3.28 | 2.43 | -0.01 | 59864.71 | 9.04 | skipped_fast |
| REDUSDT | IDLE | 1.65 | 2.98 | 2.14 | 0.02 | 62873.32 | 16.44 | skipped_fast |
| CCUSDT | IDLE | 0.98 | 1.74 | 1.49 | -0.02 | 188897.23 | 6.99 | skipped_fast |
| KITEUSDT | IDLE | 1.46 | 2.63 | 1.95 | 0.01 | 53599.94 | 12.42 | skipped_fast |
| EDELUSDT | IDLE | 1.27 | 3.4 | 0.49 | 0.09 | 129841.76 | 33.63 | skipped_fast |
| RIZEUSDT | IDLE | 1.7 | 3.33 | 0.5 | 0.01 | 28466.03 | 45.79 | skipped_fast |
| HBARUSDT | IDLE | 1.1 | 1.93 | 1.74 | -0.01 | 243830.02 | 7.83 | skipped_fast |
| LAUSDT | IDLE | 1.88 | 3.75 | 2.37 | 0.01 | 67169.27 | 18.95 | skipped_fast |
| WAXLUSDT | IDLE | 2.11 | 4.01 | 1.36 | -0.02 | 53560.12 | 51.42 | skipped_fast |
| IOTAUSDT | IDLE | 1.4 | 2.44 | 2.34 | -0.02 | 74402.5 | 18.93 | skipped_fast |
| FLUIDUSDT | IDLE | 1.31 | 2.35 | 2.0 | -0.04 | 1388.64 | 21.41 | skipped_fast |
| RWAUSDT | IDLE | 0.78 | 1.44 | 0.79 | -0.0 | 54651.55 | 31.87 | skipped_fast |
| MNSRYUSDT | IDLE | 0.42 | 0.74 | 0.72 | -0.01 | 42952.85 | 76.46 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
