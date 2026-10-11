# Hulk DIGEST — 2026-10-11T20:56:03Z

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
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 3.79 | 33.42 | 13.33 | 0.13 | 3764299.3 | 19.77 | skipped_fast |
| XRPUSDT | IDLE | 1.08 | 1.97 | 1.21 | 0.0 | 14957470.39 | 2.13 | skipped_fast |
| ETHUSDT | IDLE | 1.03 | 1.95 | 0.71 | 0.01 | 205208295.46 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.68 | 1.27 | 0.66 | 0.01 | 154890210.37 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.44 | 4.5 | 2.52 | -0.02 | 881728.75 | 5.12 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.54 | 21.91 | 11.54 | 0.02 | 39770.17 | 57.18 | skipped_fast |
| EDELUSDT | IDLE | 2.76 | 4.96 | 3.74 | -0.03 | 406695.29 | 23.74 | skipped_fast |
| ZBCNUSDT | IDLE | 2.88 | 5.28 | 3.25 | 0.01 | 197539.98 | 19.91 | skipped_fast |
| TELUSDT | IDLE | 4.04 | 7.35 | 4.81 | -0.05 | 178774.06 | 52.28 | skipped_fast |
| QNTUSDT | IDLE | 1.11 | 2.0 | 1.51 | 0.01 | 773909.1 | 0.41 | skipped_fast |
| CCUSDT | IDLE | 1.41 | 2.76 | 2.16 | 0.05 | 339282.09 | 8.79 | skipped_fast |
| CHIPUSDT | IDLE | 1.33 | 5.39 | 2.15 | 0.03 | 316050.54 | 11.58 | skipped_fast |
| RWAINCUSDT | IDLE | 1.51 | 4.08 | 2.72 | 0.01 | 28756.01 | 29.46 | skipped_fast |
| BIOUSDT | IDLE | 0.92 | 1.68 | 1.09 | 0.01 | 89007.62 | 3.34 | skipped_fast |
| REDUSDT | IDLE | 1.13 | 2.09 | 1.16 | 0.01 | 58274.95 | 13.84 | skipped_fast |
| HBARUSDT | IDLE | 1.2 | 2.34 | 0.45 | 0.02 | 294971.8 | 8.49 | skipped_fast |
| KITEUSDT | IDLE | 0.7 | 1.28 | 0.83 | -0.01 | 75120.1 | 10.21 | skipped_fast |
| RWAUSDT | IDLE | 1.7 | 3.13 | 1.82 | 0.02 | 52755.53 | 15.47 | skipped_fast |
| MNSRYUSDT | IDLE | 0.97 | 1.79 | 0.96 | -0.01 | 32033.99 | 42.45 | skipped_fast |
| FLUIDUSDT | IDLE | 0.35 | 2.54 | 1.3 | 0.07 | 59627.59 | 21.73 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
