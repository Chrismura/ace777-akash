# Hulk DIGEST — 2026-10-19T19:02:44Z

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
| ETHUSDT | IDLE | 0.87 | 1.6 | 0.99 | 0.01 | 160308362.23 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.86 | 1.57 | 0.97 | 0.02 | 28258613.3 | 1.54 | skipped_fast |
| BTCUSDT | IDLE | 0.54 | 0.96 | 0.75 | 0.01 | 362709782.58 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.31 | 4.17 | 2.97 | -0.02 | 947580.98 | 1.37 | skipped_fast |
| WUSDT | IDLE | 2.58 | 5.05 | 0.74 | 0.04 | 649519.6 | 17.91 | skipped_fast |
| QNTUSDT | IDLE | 1.3 | 3.59 | 2.75 | 0.03 | 786055.49 | 3.61 | skipped_fast |
| CCUSDT | IDLE | 1.5 | 3.34 | 2.37 | 0.05 | 418680.93 | 7.71 | skipped_fast |
| RIZEUSDT | IDLE | 3.08 | 10.58 | 4.25 | -0.07 | 53254.64 | 57.54 | skipped_fast |
| RWAINCUSDT | IDLE | 2.18 | 5.11 | 1.32 | 0.04 | 83370.71 | 25.63 | skipped_fast |
| KITEUSDT | IDLE | 1.95 | 5.44 | 2.82 | 0.08 | 67693.11 | 10.78 | skipped_fast |
| EDELUSDT | IDLE | 1.36 | 2.86 | 0.95 | 0.03 | 216038.12 | 14.76 | skipped_fast |
| HBARUSDT | IDLE | 0.98 | 1.78 | 1.22 | -0.02 | 555511.63 | 1.21 | skipped_fast |
| CHIPUSDT | IDLE | 1.61 | 4.45 | 1.28 | 0.05 | 70589.93 | 2.4 | skipped_fast |
| ZBCNUSDT | IDLE | 0.86 | 3.07 | 1.31 | 0.03 | 257979.82 | 18.07 | skipped_fast |
| REDUSDT | IDLE | 1.62 | 2.87 | 2.51 | 0.01 | 58605.14 | 17.7 | skipped_fast |
| BIOUSDT | IDLE | 1.17 | 2.15 | 1.31 | 0.01 | 71481.4 | 4.27 | skipped_fast |
| WAXLUSDT | IDLE | 1.56 | 3.66 | 2.7 | -0.0 | 78415.9 | 26.82 | skipped_fast |
| IOTAUSDT | IDLE | 1.06 | 1.95 | 1.07 | 0.01 | 93970.4 | 15.73 | skipped_fast |
| LAUSDT | IDLE | 1.13 | 2.07 | 1.29 | 0.01 | 56657.09 | 23.01 | skipped_fast |
| FLUIDUSDT | IDLE | 0.83 | 2.04 | 2.0 | 0.02 | 5620.08 | 21.6 | skipped_fast |
| RWAUSDT | IDLE | 0.36 | 0.71 | 0.08 | 0.02 | 54972.84 | 7.87 | skipped_fast |
| MNSRYUSDT | IDLE | 0.21 | 0.41 | 0.11 | -0.0 | 40184.28 | 15.67 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
