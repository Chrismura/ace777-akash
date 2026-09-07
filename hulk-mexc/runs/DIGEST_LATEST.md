# Hulk DIGEST — 2026-09-07T11:35:27Z

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
| XRPUSDT | IDLE | 0.9 | 1.65 | 0.98 | -0.02 | 33243678.06 | 2.14 | skipped_fast |
| ETHUSDT | IDLE | 0.74 | 1.37 | 0.7 | -0.0 | 319966483.96 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.56 | 1.05 | 0.48 | -0.01 | 406784433.52 | 0.0 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 2.62 | 7.14 | 5.23 | -0.1 | 355395.05 | 9.23 | skipped_fast |
| CCUSDT | IDLE | 2.29 | 4.05 | 3.5 | -0.03 | 422508.85 | 0.94 | skipped_fast |
| PYTHUSDT | IDLE | 1.58 | 3.09 | 0.5 | 0.0 | 594089.24 | 1.79 | skipped_fast |
| WUSDT | IDLE | 1.79 | 3.3 | 1.9 | -0.01 | 449908.61 | 12.63 | skipped_fast |
| EDELUSDT | IDLE | 2.75 | 7.33 | 4.4 | -0.05 | 73446.7 | 39.06 | skipped_fast |
| KITEUSDT | IDLE | 2.56 | 4.52 | 3.98 | -0.05 | 57682.82 | 9.1 | skipped_fast |
| REDUSDT | IDLE | 2.43 | 4.77 | 0.54 | 0.02 | 64377.19 | 11.38 | skipped_fast |
| RIZEUSDT | IDLE | 1.73 | 8.73 | 6.67 | -0.14 | 72527.92 | 34.94 | skipped_fast |
| ZBCNUSDT | IDLE | 1.62 | 3.08 | 1.11 | -0.01 | 176324.31 | 8.51 | skipped_fast |
| BIOUSDT | IDLE | 1.12 | 2.16 | 0.55 | -0.02 | 70390.81 | 7.34 | skipped_fast |
| HBARUSDT | IDLE | 0.91 | 1.79 | 0.17 | -0.0 | 370230.01 | 1.23 | skipped_fast |
| TELUSDT | IDLE | 1.75 | 3.11 | 2.56 | -0.01 | 106093.16 | 17.5 | skipped_fast |
| RWAINCUSDT | IDLE | 0.91 | 2.83 | 1.88 | 0.04 | 6014.3 | 73.62 | skipped_fast |
| QNTUSDT | IDLE | 1.46 | 2.61 | 2.09 | -0.0 | 41577.79 | 4.58 | skipped_fast |
| FLUIDUSDT | IDLE | 0.81 | 1.58 | 0.25 | -0.01 | 1152.45 | 21.9 | skipped_fast |
| RWAUSDT | IDLE | 0.33 | 0.58 | 0.5 | -0.01 | 53351.83 | 7.25 | skipped_fast |
| MNSRYUSDT | IDLE | 0.16 | 0.3 | 0.16 | -0.0 | 38307.42 | 5.38 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
