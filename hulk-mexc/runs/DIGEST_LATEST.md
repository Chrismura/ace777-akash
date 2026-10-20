# Hulk DIGEST — 2026-10-20T22:27:20Z

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
| XRPUSDT | IDLE | 0.83 | 1.65 | 0.01 | 0.02 | 24348249.13 | 1.49 | skipped_fast |
| ETHUSDT | IDLE | 0.81 | 1.6 | 0.07 | 0.02 | 170109321.88 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.46 | 0.91 | 0.03 | 0.01 | 326285184.01 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.36 | 7.56 | 1.13 | 0.08 | 1185644.03 | 3.74 | skipped_fast |
| WUSDT | IDLE | 2.02 | 3.99 | 0.32 | 0.02 | 670811.21 | 11.79 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 3.25 | 9.94 | 7.91 | -0.04 | 75892.32 | 16.0 | skipped_fast |
| QNTUSDT | IDLE | 1.79 | 3.39 | 1.2 | 0.0 | 803355.11 | 1.02 | skipped_fast |
| CHIPUSDT | IDLE | 1.62 | 5.69 | 3.08 | 0.06 | 404046.67 | 15.57 | skipped_fast |
| ZBCNUSDT | IDLE | 2.02 | 3.67 | 2.51 | 0.02 | 200947.26 | 11.78 | skipped_fast |
| CCUSDT | IDLE | 1.02 | 1.86 | 1.25 | 0.01 | 384492.15 | 4.75 | skipped_fast |
| RIZEUSDT | IDLE | 2.22 | 8.84 | 5.79 | 0.06 | 75017.62 | 64.24 | skipped_fast |
| EDELUSDT | IDLE | 0.53 | 4.76 | 1.78 | 0.33 | 362492.39 | 22.32 | skipped_fast |
| REDUSDT | IDLE | 1.45 | 2.68 | 1.41 | 0.02 | 58790.27 | 17.1 | skipped_fast |
| BIOUSDT | IDLE | 1.24 | 2.34 | 0.88 | 0.05 | 62838.62 | 12.13 | skipped_fast |
| HBARUSDT | IDLE | 0.93 | 1.83 | 0.14 | 0.01 | 365585.56 | 7.12 | skipped_fast |
| KITEUSDT | IDLE | 0.54 | 0.98 | 0.68 | -0.01 | 72383.95 | 11.48 | skipped_fast |
| FLUIDUSDT | IDLE | 1.84 | 3.98 | 0.0 | 0.09 | 7267.9 | 21.19 | skipped_fast |
| WAXLUSDT | IDLE | 1.74 | 3.1 | 2.56 | -0.05 | 56136.17 | 50.75 | skipped_fast |
| LAUSDT | IDLE | 1.3 | 2.56 | 0.24 | 0.03 | 55009.57 | 23.93 | skipped_fast |
| IOTAUSDT | IDLE | 1.08 | 2.06 | 0.68 | 0.04 | 73094.79 | 27.82 | skipped_fast |
| RWAUSDT | IDLE | 0.5 | 0.95 | 0.31 | 0.0 | 52186.7 | 31.3 | skipped_fast |
| MNSRYUSDT | IDLE | 0.32 | 0.59 | 0.38 | -0.0 | 39131.89 | 19.97 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
