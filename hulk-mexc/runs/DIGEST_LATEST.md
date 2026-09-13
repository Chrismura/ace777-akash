# Hulk DIGEST — 2026-09-13T22:40:53Z

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
| XRPUSDT | IDLE | 1.17 | 2.12 | 1.53 | -0.02 | 16862301.4 | 2.24 | skipped_fast |
| ETHUSDT | IDLE | 0.95 | 1.68 | 1.49 | -0.02 | 263597999.16 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.52 | 0.92 | 0.79 | -0.0 | 259618898.21 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.36 | 4.44 | 3.56 | 0.02 | 464930.31 | 1.79 | skipped_fast |
| RIZEUSDT | IDLE | 2.21 | 32.04 | 19.57 | -0.05 | 65350.29 | 88.28 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 3.27 | 5.79 | 5.05 | -0.02 | 221093.97 | 13.3 | skipped_fast |
| RWAINCUSDT | IDLE | 4.18 | 7.78 | 3.9 | -0.0 | 9807.67 | 21.95 | skipped_fast |
| ZBCNUSDT | IDLE | 1.86 | 3.32 | 2.67 | -0.02 | 193210.52 | 20.49 | skipped_fast |
| BIOUSDT | IDLE | 2.27 | 4.08 | 3.11 | -0.02 | 68350.99 | 8.02 | skipped_fast |
| EDELUSDT | IDLE | 1.68 | 5.84 | 1.84 | 0.11 | 201842.61 | 22.45 | skipped_fast |
| CCUSDT | IDLE | 1.19 | 2.17 | 1.34 | -0.02 | 320357.16 | 8.42 | skipped_fast |
| CHIPUSDT | IDLE | 1.72 | 6.0 | 5.48 | -0.13 | 98509.7 | 19.16 | skipped_fast |
| HBARUSDT | IDLE | 2.06 | 3.62 | 3.36 | 0.0 | 244229.7 | 1.34 | skipped_fast |
| KITEUSDT | IDLE | 1.53 | 2.76 | 2.03 | -0.02 | 60539.45 | 10.41 | skipped_fast |
| REDUSDT | IDLE | 1.51 | 2.65 | 2.43 | -0.01 | 63968.5 | 18.66 | skipped_fast |
| QNTUSDT | IDLE | 2.39 | 4.21 | 3.83 | -0.01 | 37641.64 | 1.59 | skipped_fast |
| TELUSDT | IDLE | 1.24 | 2.17 | 2.12 | -0.05 | 82349.56 | 44.57 | skipped_fast |
| FLUIDUSDT | IDLE | 1.15 | 2.0 | 1.96 | -0.02 | 1658.48 | 14.64 | skipped_fast |
| RWAUSDT | IDLE | 0.33 | 0.6 | 0.37 | 0.0 | 54531.31 | 22.3 | skipped_fast |
| MNSRYUSDT | IDLE | 0.26 | 0.46 | 0.37 | -0.0 | 30732.89 | 15.3 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
