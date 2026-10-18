# Hulk DIGEST — 2026-10-18T13:03:52Z

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
| XRPUSDT | IDLE | 0.65 | 1.2 | 0.68 | -0.0 | 19433524.91 | 1.54 | skipped_fast |
| ETHUSDT | IDLE | 0.5 | 0.92 | 0.59 | -0.0 | 89174438.28 | 0.5 | skipped_fast |
| BTCUSDT | IDLE | 0.42 | 0.77 | 0.4 | 0.01 | 195503861.23 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.25 | 3.23 | 2.13 | -0.08 | 1399750.36 | 2.56 | skipped_fast |
| WUSDT | IDLE | 1.76 | 3.28 | 2.59 | -0.08 | 1053557.37 | 15.86 | skipped_fast |
| WAXLUSDT | WATCH_PULLBACK — tension haute + reflux | 3.98 | 14.22 | 10.79 | -0.01 | 71520.53 | 36.95 | skipped_fast |
| HBARUSDT | IDLE | 1.76 | 3.84 | 1.67 | 0.07 | 552312.78 | 10.19 | skipped_fast |
| QNTUSDT | IDLE | 1.76 | 3.24 | 1.91 | -0.03 | 502234.21 | 1.53 | skipped_fast |
| RWAINCUSDT | IDLE | 2.73 | 6.37 | 1.53 | 0.05 | 16259.12 | 29.78 | skipped_fast |
| EDELUSDT | IDLE | 1.23 | 3.33 | 0.85 | -0.08 | 230983.84 | 14.95 | skipped_fast |
| REDUSDT | IDLE | 1.51 | 2.75 | 1.76 | -0.01 | 76982.63 | 7.97 | skipped_fast |
| CHIPUSDT | IDLE | 1.54 | 2.74 | 2.2 | -0.07 | 68543.45 | 9.56 | skipped_fast |
| CCUSDT | IDLE | 0.64 | 1.13 | 0.94 | -0.03 | 258690.72 | 2.98 | skipped_fast |
| RIZEUSDT | IDLE | 1.92 | 3.83 | 0.0 | 0.03 | 46465.18 | 59.53 | skipped_fast |
| KITEUSDT | IDLE | 1.14 | 2.1 | 1.16 | -0.04 | 68019.83 | 12.22 | skipped_fast |
| BIOUSDT | IDLE | 0.92 | 1.65 | 1.25 | -0.03 | 81288.45 | 4.21 | skipped_fast |
| ZBCNUSDT | IDLE | 0.63 | 1.2 | 0.39 | -0.02 | 160416.49 | 14.28 | skipped_fast |
| IOTAUSDT | IDLE | 1.2 | 2.11 | 2.0 | -0.04 | 68318.69 | 26.69 | skipped_fast |
| LAUSDT | IDLE | 0.96 | 1.68 | 1.62 | -0.05 | 54406.89 | 24.28 | skipped_fast |
| FLUIDUSDT | IDLE | 0.98 | 1.71 | 1.68 | -0.04 | 2785.76 | 21.8 | skipped_fast |
| MNSRYUSDT | IDLE | 0.35 | 0.69 | 0.09 | -0.0 | 34023.79 | 12.78 | skipped_fast |
| RWAUSDT | IDLE | 0.13 | 0.24 | 0.16 | -0.0 | 49969.91 | 15.94 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
