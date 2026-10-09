# Hulk DIGEST — 2026-10-09T19:33:07Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.26 | 10.24 | 9.19 | -0.03 | 2162546.09 | 2.52 | skipped_fast |
| WUSDT | IDLE | 1.08 | 5.84 | 4.77 | 0.13 | 2208307.01 | 12.89 | skipped_fast |
| XRPUSDT | IDLE | 0.75 | 1.42 | 0.55 | 0.01 | 28556946.25 | 2.16 | skipped_fast |
| BTCUSDT | IDLE | 0.65 | 1.16 | 0.98 | 0.01 | 286040205.76 | 0.0 | skipped_fast |
| ETHUSDT | IDLE | 0.55 | 0.99 | 0.77 | 0.01 | 225443150.05 | 0.04 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 2.68 | 5.73 | 5.04 | 0.05 | 1440617.03 | 3.29 | skipped_fast |
| CCUSDT | IDLE | 1.57 | 3.5 | 1.03 | 0.05 | 580834.89 | 10.53 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.51 | 14.04 | 7.8 | 0.04 | 72720.27 | 57.18 | skipped_fast |
| CHIPUSDT | IDLE | 2.48 | 4.9 | 0.46 | 0.02 | 81826.21 | 14.06 | skipped_fast |
| EDELUSDT | IDLE | 1.27 | 8.03 | 1.1 | 0.25 | 269582.8 | 17.35 | skipped_fast |
| KITEUSDT | IDLE | 2.14 | 3.75 | 3.52 | -0.06 | 67796.61 | 12.6 | skipped_fast |
| ZBCNUSDT | IDLE | 1.31 | 3.6 | 2.48 | 0.0 | 245114.8 | 13.19 | skipped_fast |
| HBARUSDT | IDLE | 1.13 | 1.98 | 1.93 | -0.02 | 379155.79 | 1.11 | skipped_fast |
| BIOUSDT | IDLE | 1.12 | 1.98 | 1.7 | -0.01 | 68674.24 | 3.6 | skipped_fast |
| REDUSDT | IDLE | 0.99 | 1.83 | 0.99 | 0.02 | 62297.93 | 8.88 | skipped_fast |
| TELUSDT | IDLE | 1.72 | 3.25 | 1.23 | -0.0 | 119176.94 | 43.24 | skipped_fast |
| RWAINCUSDT | IDLE | 1.74 | 3.87 | 2.56 | 0.0 | 9934.1 | 153.11 | skipped_fast |
| RWAUSDT | IDLE | 0.85 | 1.5 | 1.4 | 0.0 | 52948.06 | 7.91 | skipped_fast |
| MNSRYUSDT | IDLE | 0.4 | 0.74 | 0.34 | 0.0 | 38965.95 | 5.43 | skipped_fast |
| FLUIDUSDT | IDLE | 0.24 | 1.47 | 0.99 | 0.1 | 12636.22 | 18.48 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
