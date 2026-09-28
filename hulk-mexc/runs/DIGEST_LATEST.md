# Hulk DIGEST — 2026-09-28T13:23:24Z

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
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 3.46 | 29.05 | 5.23 | 0.26 | 6598074.58 | 4.22 | skipped_fast |
| QNTUSDT | IDLE | 1.27 | 39.28 | 13.01 | 0.48 | 20333819.25 | 5.93 | skipped_fast |
| CCUSDT | WATCH_PULLBACK — tension haute + reflux | 4.43 | 14.75 | 10.55 | -0.04 | 1230709.83 | 13.71 | skipped_fast |
| WUSDT | IDLE | 1.36 | 6.03 | 0.92 | -0.01 | 3202825.99 | 7.64 | skipped_fast |
| XRPUSDT | IDLE | 1.92 | 3.79 | 0.39 | -0.0 | 57312162.3 | 1.97 | skipped_fast |
| PYTHUSDT | IDLE | 1.99 | 4.53 | 1.97 | -0.05 | 1506890.68 | 2.47 | skipped_fast |
| ETHUSDT | IDLE | 1.08 | 2.11 | 0.33 | -0.01 | 326654798.81 | 0.11 | skipped_fast |
| BTCUSDT | IDLE | 0.62 | 1.21 | 0.23 | -0.02 | 694699546.78 | 0.0 | skipped_fast |
| EDELUSDT | IDLE | 3.63 | 24.05 | 4.6 | 0.03 | 192203.79 | 6.78 | skipped_fast |
| ZBCNUSDT | IDLE | 1.2 | 2.32 | 0.52 | -0.04 | 226108.85 | 34.01 | skipped_fast |
| CHIPUSDT | IDLE | 1.58 | 3.89 | 0.2 | -0.04 | 82704.88 | 17.68 | skipped_fast |
| REDUSDT | IDLE | 1.62 | 3.38 | 1.03 | -0.03 | 61698.9 | 14.08 | skipped_fast |
| KITEUSDT | IDLE | 1.17 | 3.84 | 1.38 | -0.06 | 103405.15 | 7.92 | skipped_fast |
| BIOUSDT | IDLE | 1.15 | 2.94 | 1.13 | -0.05 | 95250.91 | 3.36 | skipped_fast |
| TELUSDT | IDLE | 1.71 | 3.41 | 0.11 | 0.02 | 163099.49 | 38.56 | skipped_fast |
| RWAINCUSDT | IDLE | 0.55 | 5.69 | 1.01 | 0.16 | 34350.14 | 55.51 | skipped_fast |
| RIZEUSDT | IDLE | 0.48 | 2.89 | 1.14 | -0.15 | 60021.21 | 99.59 | skipped_fast |
| RWAUSDT | IDLE | 0.7 | 1.31 | 0.65 | -0.02 | 59547.45 | 28.88 | skipped_fast |
| MNSRYUSDT | IDLE | 0.38 | 0.73 | 0.15 | -0.02 | 34713.63 | 6.41 | skipped_fast |
| FLUIDUSDT | IDLE | 0.61 | 1.5 | 0.0 | -0.05 | 3101.03 | 20.48 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
