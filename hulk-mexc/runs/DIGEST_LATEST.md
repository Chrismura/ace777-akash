# Hulk DIGEST — 2026-10-11T01:07:02Z

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
| XRPUSDT | IDLE | 0.52 | 0.93 | 0.79 | -0.0 | 12763500.0 | 1.43 | skipped_fast |
| ETHUSDT | IDLE | 0.26 | 0.46 | 0.34 | 0.01 | 128829959.54 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.11 | 0.2 | 0.15 | 0.0 | 148756373.23 | 0.0 | skipped_fast |
| WUSDT | IDLE | 1.28 | 4.02 | 2.94 | -0.0 | 1255610.4 | 7.41 | skipped_fast |
| QNTUSDT | IDLE | 1.04 | 1.88 | 1.38 | -0.04 | 1275103.29 | 1.26 | skipped_fast |
| PYTHUSDT | IDLE | 1.73 | 3.03 | 2.82 | -0.04 | 752299.46 | 2.59 | skipped_fast |
| EDELUSDT | IDLE | 2.52 | 4.54 | 3.28 | -0.04 | 257712.25 | 5.22 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.65 | 7.24 | 6.69 | -0.11 | 34326.44 | 57.45 | skipped_fast |
| CHIPUSDT | IDLE | 1.13 | 9.76 | 2.88 | 0.31 | 268145.04 | 21.96 | skipped_fast |
| BIOUSDT | IDLE | 1.66 | 2.91 | 2.72 | 0.01 | 87625.16 | 6.91 | skipped_fast |
| TELUSDT | IDLE | 2.64 | 5.07 | 4.56 | -0.06 | 144384.79 | 34.5 | skipped_fast |
| CCUSDT | IDLE | 0.53 | 1.02 | 0.33 | -0.03 | 237991.01 | 7.56 | skipped_fast |
| ZBCNUSDT | IDLE | 0.68 | 1.34 | 0.1 | 0.02 | 170313.58 | 9.94 | skipped_fast |
| KITEUSDT | IDLE | 0.78 | 1.61 | 1.59 | 0.04 | 75427.34 | 8.7 | skipped_fast |
| REDUSDT | IDLE | 0.68 | 1.21 | 1.04 | 0.0 | 56472.04 | 7.35 | skipped_fast |
| RWAINCUSDT | IDLE | 0.74 | 1.29 | 1.22 | -0.02 | 11222.49 | 14.8 | skipped_fast |
| HBARUSDT | IDLE | 0.59 | 1.06 | 0.78 | -0.0 | 307528.31 | 6.52 | skipped_fast |
| MNSRYUSDT | IDLE | 1.01 | 1.8 | 1.51 | -0.02 | 36848.45 | 28.8 | skipped_fast |
| FLUIDUSDT | IDLE | 0.71 | 1.36 | 0.43 | 0.02 | 7774.46 | 21.55 | skipped_fast |
| RWAUSDT | IDLE | 0.18 | 0.32 | 0.24 | 0.0 | 53830.39 | 15.75 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
