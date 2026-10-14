# Hulk DIGEST — 2026-10-14T17:21:09Z

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
| PYTHUSDT | IDLE | 3.8 | 8.84 | 4.59 | 0.02 | 2102871.78 | 1.23 | skipped_fast |
| WUSDT | IDLE | 1.64 | 7.15 | 3.61 | -0.06 | 3034036.05 | 1.3 | skipped_fast |
| XRPUSDT | IDLE | 2.41 | 4.34 | 3.26 | -0.02 | 42724505.85 | 2.24 | skipped_fast |
| ETHUSDT | IDLE | 2.33 | 4.22 | 2.94 | -0.02 | 191043095.78 | 0.41 | skipped_fast |
| BTCUSDT | IDLE | 1.58 | 2.82 | 2.3 | -0.01 | 423291507.08 | 0.0 | skipped_fast |
| QNTUSDT | IDLE | 2.05 | 4.8 | 2.05 | 0.03 | 1452333.06 | 2.41 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 4.18 | 22.88 | 17.62 | 0.02 | 49689.31 | 61.51 | skipped_fast |
| ZBCNUSDT | IDLE | 3.92 | 7.17 | 4.45 | -0.03 | 187162.63 | 20.2 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.3 | 9.7 | 6.85 | -0.07 | 109918.33 | 9.37 | skipped_fast |
| CCUSDT | IDLE | 1.68 | 3.9 | 1.81 | -0.07 | 452729.92 | 6.7 | skipped_fast |
| KITEUSDT | IDLE | 2.55 | 7.14 | 4.79 | 0.03 | 87214.6 | 10.02 | skipped_fast |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.82 | 13.1 | 8.21 | 0.05 | 17743.71 | 21.4 | skipped_fast |
| HBARUSDT | IDLE | 2.25 | 4.11 | 2.56 | -0.03 | 489271.68 | 8.25 | skipped_fast |
| BIOUSDT | IDLE | 2.57 | 4.67 | 3.08 | -0.03 | 69038.46 | 3.74 | skipped_fast |
| REDUSDT | IDLE | 2.52 | 4.95 | 0.57 | 0.02 | 62312.02 | 15.29 | skipped_fast |
| EDELUSDT | IDLE | 1.92 | 3.55 | 1.89 | -0.0 | 170100.0 | 32.44 | skipped_fast |
| RWAINCUSDT | IDLE | 1.63 | 5.27 | 4.08 | -0.11 | 31529.39 | 5.39 | skipped_fast |
| TELUSDT | IDLE | 2.22 | 4.39 | 0.28 | 0.03 | 114186.91 | 22.2 | skipped_fast |
| RWAUSDT | IDLE | 1.27 | 2.23 | 2.1 | -0.03 | 56427.76 | 7.95 | skipped_fast |
| MNSRYUSDT | IDLE | 0.55 | 0.99 | 0.68 | -0.01 | 38274.36 | 39.35 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
