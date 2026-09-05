# Hulk DIGEST — 2026-09-05T20:28:06Z

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
| XRPUSDT | IDLE | 0.68 | 1.25 | 0.77 | 0.01 | 22387242.45 | 2.12 | skipped_fast |
| ETHUSDT | IDLE | 0.59 | 1.16 | 0.2 | 0.01 | 159509219.15 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.36 | 0.65 | 0.49 | 0.0 | 354417987.82 | 0.0 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.64 | 23.78 | 7.93 | -0.01 | 142889.18 | 58.29 | skipped_fast |
| CHIPUSDT | IDLE | 2.34 | 6.2 | 1.64 | 0.06 | 462864.08 | 3.37 | skipped_fast |
| ZBCNUSDT | IDLE | 2.69 | 4.95 | 2.81 | -0.03 | 196410.95 | 8.68 | skipped_fast |
| CCUSDT | IDLE | 1.4 | 2.5 | 2.05 | 0.03 | 300675.04 | 2.75 | skipped_fast |
| RWAINCUSDT | IDLE | 2.7 | 5.31 | 0.57 | 0.02 | 7749.16 | 21.15 | skipped_fast |
| PYTHUSDT | IDLE | 1.07 | 2.0 | 0.96 | 0.0 | 328001.48 | 1.82 | skipped_fast |
| WUSDT | IDLE | 1.45 | 2.65 | 1.64 | 0.04 | 139009.83 | 12.08 | skipped_fast |
| REDUSDT | IDLE | 1.09 | 2.13 | 0.31 | 0.04 | 60563.48 | 11.81 | skipped_fast |
| BIOUSDT | IDLE | 0.87 | 1.69 | 0.32 | 0.05 | 82852.55 | 3.56 | skipped_fast |
| KITEUSDT | IDLE | 0.7 | 1.73 | 0.56 | -0.06 | 62625.09 | 10.27 | skipped_fast |
| HBARUSDT | IDLE | 0.63 | 1.2 | 0.39 | 0.04 | 327833.49 | 1.24 | skipped_fast |
| EDELUSDT | IDLE | 0.16 | 2.89 | 0.75 | -0.0 | 165786.47 | 37.74 | skipped_fast |
| QNTUSDT | IDLE | 1.38 | 2.63 | 0.89 | 0.02 | 42367.44 | 4.63 | skipped_fast |
| RWAUSDT | IDLE | 0.8 | 1.49 | 0.77 | 0.03 | 52094.93 | 14.06 | skipped_fast |
| TELUSDT | IDLE | 0.94 | 1.82 | 0.46 | 0.01 | 66901.07 | 40.45 | skipped_fast |
| FLUIDUSDT | IDLE | 0.51 | 0.99 | 0.19 | 0.01 | 497.42 | 20.11 | skipped_fast |
| MNSRYUSDT | IDLE | 0.14 | 0.27 | 0.04 | 0.0 | 37911.71 | 27.3 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
