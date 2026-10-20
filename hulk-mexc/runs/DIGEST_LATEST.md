# Hulk DIGEST — 2026-10-20T12:14:20Z

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
| ETHUSDT | IDLE | 0.52 | 0.94 | 0.6 | -0.01 | 123337074.93 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.52 | 0.98 | 0.46 | -0.01 | 18992713.8 | 0.77 | skipped_fast |
| BTCUSDT | IDLE | 0.35 | 0.63 | 0.53 | -0.01 | 291992655.74 | 0.0 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 4.19 | 11.14 | 10.02 | -0.05 | 83558.73 | 15.84 | skipped_fast |
| WUSDT | IDLE | 1.81 | 3.24 | 2.56 | 0.01 | 698948.11 | 16.31 | skipped_fast |
| PYTHUSDT | IDLE | 0.75 | 1.39 | 0.73 | -0.01 | 906404.65 | 1.38 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.57 | 9.76 | 6.37 | -0.05 | 67914.6 | 51.03 | skipped_fast |
| CCUSDT | IDLE | 0.99 | 1.9 | 0.49 | 0.01 | 446249.33 | 5.76 | skipped_fast |
| EDELUSDT | IDLE | 1.3 | 7.37 | 0.56 | 0.19 | 296537.02 | 12.44 | skipped_fast |
| ZBCNUSDT | IDLE | 1.66 | 3.02 | 2.04 | -0.03 | 185114.45 | 15.45 | skipped_fast |
| CHIPUSDT | IDLE | 1.73 | 4.18 | 3.68 | 0.03 | 93129.69 | 11.57 | skipped_fast |
| KITEUSDT | IDLE | 1.71 | 3.1 | 2.09 | 0.02 | 90349.88 | 10.84 | skipped_fast |
| QNTUSDT | IDLE | 1.26 | 2.43 | 0.59 | -0.03 | 484721.72 | 1.55 | skipped_fast |
| HBARUSDT | IDLE | 1.32 | 2.34 | 1.97 | -0.01 | 353618.29 | 8.5 | skipped_fast |
| REDUSDT | IDLE | 1.12 | 1.97 | 1.82 | -0.01 | 57777.92 | 16.21 | skipped_fast |
| BIOUSDT | IDLE | 0.63 | 1.2 | 0.42 | 0.0 | 65885.76 | 8.49 | skipped_fast |
| WAXLUSDT | IDLE | 1.93 | 4.21 | 3.3 | -0.08 | 57371.19 | 46.98 | skipped_fast |
| LAUSDT | IDLE | 1.17 | 2.12 | 1.43 | -0.02 | 56647.21 | 25.12 | skipped_fast |
| IOTAUSDT | IDLE | 1.03 | 1.91 | 1.0 | 0.02 | 84637.2 | 30.95 | skipped_fast |
| RWAUSDT | IDLE | 0.5 | 0.95 | 0.31 | 0.01 | 51120.5 | 7.86 | skipped_fast |
| MNSRYUSDT | IDLE | 0.13 | 0.24 | 0.09 | -0.0 | 39288.47 | 5.7 | skipped_fast |
| FLUIDUSDT | IDLE | 0.35 | 0.65 | 0.27 | 0.01 | 4452.44 | 22.55 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
