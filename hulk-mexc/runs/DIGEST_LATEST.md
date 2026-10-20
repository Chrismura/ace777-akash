# Hulk DIGEST — 2026-10-20T23:28:00Z

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
| XRPUSDT | IDLE | 1.08 | 2.08 | 0.6 | 0.02 | 24755442.39 | 0.75 | skipped_fast |
| ETHUSDT | IDLE | 0.85 | 1.6 | 0.72 | 0.02 | 175527252.07 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.49 | 0.94 | 0.29 | 0.01 | 331041646.4 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.75 | 5.49 | 1.53 | 0.09 | 1181468.03 | 2.51 | skipped_fast |
| WUSDT | IDLE | 1.48 | 2.76 | 1.34 | 0.02 | 656804.67 | 8.19 | skipped_fast |
| QNTUSDT | IDLE | 1.86 | 3.39 | 2.22 | -0.0 | 814090.19 | 1.03 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 3.25 | 9.94 | 7.86 | -0.03 | 76676.64 | 5.34 | skipped_fast |
| CHIPUSDT | IDLE | 1.16 | 4.01 | 2.72 | 0.05 | 444957.14 | 6.75 | skipped_fast |
| CCUSDT | IDLE | 0.9 | 1.63 | 1.12 | 0.0 | 383098.45 | 9.51 | skipped_fast |
| RIZEUSDT | IDLE | 2.13 | 8.6 | 4.92 | 0.06 | 75093.62 | 50.49 | skipped_fast |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.27 | 13.83 | 11.0 | 0.06 | 17162.46 | 56.18 | skipped_fast |
| ZBCNUSDT | IDLE | 1.52 | 2.86 | 1.15 | 0.02 | 192928.68 | 26.69 | skipped_fast |
| EDELUSDT | IDLE | 0.4 | 3.73 | 0.75 | 0.33 | 363207.17 | 16.72 | skipped_fast |
| BIOUSDT | IDLE | 1.15 | 2.17 | 0.92 | 0.05 | 62252.66 | 8.1 | skipped_fast |
| HBARUSDT | IDLE | 0.92 | 1.83 | 0.01 | 0.02 | 353581.15 | 2.37 | skipped_fast |
| REDUSDT | IDLE | 0.92 | 1.8 | 0.3 | 0.01 | 58343.29 | 9.95 | skipped_fast |
| KITEUSDT | IDLE | 0.7 | 1.23 | 1.14 | -0.01 | 73690.45 | 11.54 | skipped_fast |
| LAUSDT | IDLE | 1.31 | 2.56 | 0.4 | 0.04 | 54556.68 | 25.81 | skipped_fast |
| IOTAUSDT | IDLE | 1.11 | 2.06 | 1.06 | 0.03 | 72985.63 | 25.78 | skipped_fast |
| WAXLUSDT | IDLE | 1.1 | 2.01 | 1.28 | -0.03 | 55833.08 | 69.44 | skipped_fast |
| RWAUSDT | IDLE | 0.49 | 0.95 | 0.23 | 0.0 | 52020.75 | 23.46 | skipped_fast |
| MNSRYUSDT | IDLE | 0.23 | 0.43 | 0.16 | 0.0 | 39257.27 | 11.4 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
