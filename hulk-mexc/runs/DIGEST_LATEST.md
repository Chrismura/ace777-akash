# Hulk DIGEST — 2026-10-20T13:15:13Z

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
| ETHUSDT | IDLE | 0.58 | 1.09 | 0.42 | -0.01 | 123918733.84 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.56 | 1.05 | 0.45 | -0.01 | 18756692.48 | 1.54 | skipped_fast |
| BTCUSDT | IDLE | 0.29 | 0.53 | 0.39 | -0.01 | 293421281.49 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.53 | 2.92 | 0.93 | 0.01 | 888966.8 | 4.08 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 4.45 | 12.27 | 9.31 | 0.01 | 80538.51 | 5.24 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.83 | 17.51 | 11.55 | -0.04 | 72689.42 | 27.59 | skipped_fast |
| WUSDT | IDLE | 1.98 | 3.49 | 3.19 | -0.02 | 692566.22 | 17.21 | skipped_fast |
| CCUSDT | IDLE | 1.19 | 2.18 | 1.31 | -0.01 | 455758.76 | 9.66 | skipped_fast |
| QNTUSDT | IDLE | 1.58 | 2.95 | 1.39 | -0.03 | 525880.94 | 0.52 | skipped_fast |
| EDELUSDT | IDLE | 0.93 | 5.0 | 2.01 | 0.17 | 299236.9 | 22.07 | skipped_fast |
| CHIPUSDT | IDLE | 1.69 | 4.18 | 3.03 | 0.04 | 93629.64 | 11.49 | skipped_fast |
| KITEUSDT | IDLE | 1.67 | 3.1 | 1.58 | 0.01 | 90594.69 | 10.78 | skipped_fast |
| ZBCNUSDT | IDLE | 1.18 | 2.14 | 1.4 | -0.03 | 198349.06 | 19.85 | skipped_fast |
| HBARUSDT | IDLE | 0.97 | 1.76 | 1.24 | -0.02 | 361705.93 | 3.64 | skipped_fast |
| BIOUSDT | IDLE | 0.95 | 1.84 | 0.42 | 0.01 | 65731.16 | 8.43 | skipped_fast |
| REDUSDT | IDLE | 0.94 | 1.65 | 1.6 | -0.01 | 57700.69 | 16.31 | skipped_fast |
| WAXLUSDT | IDLE | 1.99 | 3.82 | 2.99 | -0.08 | 56436.13 | 48.83 | skipped_fast |
| LAUSDT | IDLE | 1.15 | 2.06 | 1.58 | -0.03 | 56594.01 | 21.3 | skipped_fast |
| IOTAUSDT | IDLE | 0.86 | 1.67 | 0.35 | 0.02 | 85505.94 | 26.36 | skipped_fast |
| RWAUSDT | IDLE | 0.72 | 1.34 | 0.62 | 0.0 | 50890.35 | 15.71 | skipped_fast |
| MNSRYUSDT | IDLE | 0.84 | 1.52 | 1.03 | -0.01 | 39271.1 | 62.92 | skipped_fast |
| FLUIDUSDT | IDLE | 0.19 | 0.38 | 0.0 | 0.01 | 4452.44 | 21.33 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
