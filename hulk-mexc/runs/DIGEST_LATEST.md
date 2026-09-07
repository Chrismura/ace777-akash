# Hulk DIGEST — 2026-09-07T17:47:48Z

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
| XRPUSDT | IDLE | 1.36 | 2.55 | 1.07 | -0.01 | 36230473.02 | 2.15 | skipped_fast |
| ETHUSDT | IDLE | 0.95 | 1.79 | 0.72 | 0.0 | 342323061.79 | 0.2 | skipped_fast |
| BTCUSDT | IDLE | 0.63 | 1.18 | 0.58 | -0.01 | 453820698.08 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.76 | 5.01 | 3.38 | 0.01 | 567626.81 | 1.82 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 4.14 | 11.12 | 5.85 | -0.04 | 215062.97 | 80.16 | skipped_fast |
| CCUSDT | IDLE | 1.99 | 3.58 | 2.66 | -0.03 | 436802.5 | 7.54 | skipped_fast |
| CHIPUSDT | IDLE | 2.17 | 8.22 | 5.73 | -0.11 | 242451.34 | 19.18 | skipped_fast |
| WUSDT | IDLE | 1.92 | 3.62 | 1.43 | -0.03 | 356456.83 | 12.6 | skipped_fast |
| HBARUSDT | IDLE | 1.72 | 3.34 | 0.7 | 0.03 | 572324.88 | 1.21 | skipped_fast |
| RIZEUSDT | IDLE | 2.16 | 9.74 | 8.17 | -0.07 | 69814.42 | 35.78 | skipped_fast |
| REDUSDT | IDLE | 2.2 | 4.06 | 2.32 | 0.04 | 64217.62 | 8.33 | skipped_fast |
| EDELUSDT | IDLE | 1.98 | 6.26 | 4.93 | -0.06 | 87541.3 | 40.57 | skipped_fast |
| KITEUSDT | IDLE | 2.05 | 3.65 | 2.95 | -0.06 | 60181.99 | 12.56 | skipped_fast |
| BIOUSDT | IDLE | 1.8 | 3.39 | 1.44 | -0.01 | 67924.8 | 3.66 | skipped_fast |
| MNSRYUSDT | IDLE | 2.73 | 5.31 | 1.05 | -0.01 | 37355.96 | 61.3 | skipped_fast |
| RWAINCUSDT | IDLE | 1.36 | 4.06 | 3.85 | 0.03 | 5145.8 | 137.59 | skipped_fast |
| QNTUSDT | IDLE | 0.87 | 1.62 | 0.81 | 0.0 | 46383.39 | 3.03 | skipped_fast |
| TELUSDT | IDLE | 0.91 | 1.71 | 0.7 | -0.01 | 114521.87 | 46.87 | skipped_fast |
| RWAUSDT | IDLE | 0.62 | 1.09 | 1.01 | -0.01 | 52458.84 | 7.28 | skipped_fast |
| FLUIDUSDT | IDLE | 0.07 | 0.14 | 0.0 | 0.0 | 1172.4 | 21.85 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
