# Hulk DIGEST — 2026-09-11T16:20:44Z

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
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.7 | 128.05 | 28.5 | 0.4 | 155721.87 | 63.14 | skipped_fast |
| ETHUSDT | IDLE | 4.24 | 9.44 | 4.3 | 0.05 | 604171238.19 | 0.16 | skipped_fast |
| XRPUSDT | IDLE | 4.27 | 8.82 | 4.15 | 0.02 | 52855490.79 | 1.46 | skipped_fast |
| BTCUSDT | IDLE | 2.68 | 4.93 | 2.87 | 0.01 | 535159700.79 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 4.22 | 8.34 | 2.94 | 0.03 | 379650.24 | 1.9 | skipped_fast |
| CCUSDT | IDLE | 3.64 | 6.77 | 3.35 | -0.01 | 483588.84 | 10.16 | skipped_fast |
| WUSDT | IDLE | 4.14 | 8.47 | 2.09 | 0.04 | 192174.73 | 17.31 | skipped_fast |
| EDELUSDT | IDLE | 4.12 | 7.66 | 3.91 | -0.02 | 157948.2 | 18.48 | skipped_fast |
| CHIPUSDT | IDLE | 3.75 | 11.97 | 2.04 | 0.05 | 147857.67 | 16.33 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 4.28 | 8.51 | 5.77 | 0.03 | 10237.99 | 5.51 | skipped_fast |
| REDUSDT | IDLE | 3.84 | 7.49 | 1.31 | 0.04 | 61975.88 | 19.08 | skipped_fast |
| ZBCNUSDT | IDLE | 3.04 | 5.61 | 3.15 | -0.0 | 181036.52 | 4.9 | skipped_fast |
| BIOUSDT | IDLE | 3.42 | 6.49 | 2.31 | 0.01 | 81032.77 | 7.9 | skipped_fast |
| TELUSDT | IDLE | 4.29 | 8.79 | 4.26 | -0.0 | 103482.54 | 50.69 | skipped_fast |
| KITEUSDT | IDLE | 2.22 | 4.0 | 2.96 | -0.01 | 60071.79 | 0.93 | skipped_fast |
| HBARUSDT | IDLE | 2.68 | 5.04 | 2.08 | 0.01 | 219137.28 | 1.33 | skipped_fast |
| QNTUSDT | IDLE | 2.88 | 5.19 | 3.77 | -0.01 | 40990.61 | 1.55 | skipped_fast |
| FLUIDUSDT | IDLE | 2.47 | 4.94 | 0.0 | 0.03 | 1301.56 | 21.5 | skipped_fast |
| RWAUSDT | IDLE | 1.65 | 3.2 | 0.67 | 0.02 | 51590.11 | 22.31 | skipped_fast |
| MNSRYUSDT | IDLE | 1.66 | 3.1 | 1.46 | 0.01 | 37898.32 | 49.74 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
