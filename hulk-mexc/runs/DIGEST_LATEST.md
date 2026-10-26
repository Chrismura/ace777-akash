# Hulk DIGEST — 2026-10-26T05:14:13Z

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
| XRPUSDT | IDLE | 1.09 | 2.09 | 0.65 | -0.02 | 17043984.19 | 1.55 | skipped_fast |
| ETHUSDT | IDLE | 1.02 | 1.95 | 0.56 | -0.02 | 106969514.8 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.65 | 1.26 | 0.28 | -0.01 | 200587265.55 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.35 | 2.86 | 2.06 | 0.03 | 759356.96 | 1.35 | skipped_fast |
| CHIPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 4.06 | 8.54 | 0.65 | 0.02 | 101801.28 | 21.7 | skipped_fast |
| WUSDT | IDLE | 1.34 | 2.61 | 0.41 | -0.03 | 584908.4 | 19.36 | skipped_fast |
| QNTUSDT | IDLE | 0.81 | 2.47 | 0.05 | 0.05 | 731774.9 | 3.11 | skipped_fast |
| ZBCNUSDT | IDLE | 1.65 | 3.18 | 1.07 | 0.03 | 189802.15 | 17.19 | skipped_fast |
| RWAINCUSDT | IDLE | 1.7 | 3.01 | 2.59 | -0.06 | 65817.27 | 5.78 | skipped_fast |
| REDUSDT | IDLE | 1.69 | 3.37 | 0.06 | -0.01 | 60877.49 | 15.68 | skipped_fast |
| KITEUSDT | IDLE | 1.61 | 3.13 | 0.63 | 0.0 | 54374.17 | 11.47 | skipped_fast |
| BIOUSDT | IDLE | 1.41 | 2.75 | 0.4 | -0.02 | 61304.92 | 4.48 | skipped_fast |
| EDELUSDT | IDLE | 0.88 | 2.13 | 1.37 | 0.05 | 192442.65 | 18.91 | skipped_fast |
| LAUSDT | IDLE | 2.76 | 6.57 | 0.0 | -0.02 | 61309.08 | 20.5 | skipped_fast |
| CCUSDT | IDLE | 0.8 | 1.58 | 0.19 | 0.01 | 173747.62 | 9.83 | skipped_fast |
| WAXLUSDT | IDLE | 2.34 | 4.3 | 2.59 | -0.03 | 54017.56 | 49.92 | skipped_fast |
| HBARUSDT | IDLE | 1.04 | 1.99 | 0.62 | -0.01 | 183276.61 | 5.17 | skipped_fast |
| RIZEUSDT | IDLE | 0.5 | 0.9 | 0.69 | -0.0 | 33017.89 | 20.78 | skipped_fast |
| IOTAUSDT | IDLE | 1.65 | 3.13 | 1.18 | -0.03 | 60978.22 | 28.14 | skipped_fast |
| FLUIDUSDT | IDLE | 0.83 | 3.99 | 2.42 | -0.02 | 19231.26 | 21.66 | skipped_fast |
| RWAUSDT | IDLE | 0.17 | 0.32 | 0.16 | -0.01 | 52843.21 | 23.89 | skipped_fast |
| MNSRYUSDT | IDLE | 0.3 | 0.57 | 0.19 | -0.01 | 38065.32 | 54.29 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
