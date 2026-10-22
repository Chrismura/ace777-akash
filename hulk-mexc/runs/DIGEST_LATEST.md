# Hulk DIGEST — 2026-10-22T07:10:31Z

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
| WUSDT | IDLE | 1.53 | 6.02 | 5.61 | 0.0 | 3476503.7 | 19.68 | skipped_fast |
| BTCUSDT | IDLE | 0.78 | 1.37 | 1.33 | -0.0 | 504038645.91 | 0.0 | skipped_fast |
| XRPUSDT | IDLE | 0.69 | 1.23 | 0.98 | 0.0 | 35546382.1 | 2.24 | skipped_fast |
| ETHUSDT | IDLE | 0.57 | 0.99 | 0.94 | -0.0 | 255279736.99 | 0.25 | skipped_fast |
| QNTUSDT | IDLE | 2.27 | 5.42 | 4.21 | -0.02 | 1167157.93 | 2.03 | skipped_fast |
| PYTHUSDT | IDLE | 2.15 | 4.45 | 4.22 | -0.05 | 634335.67 | 1.33 | skipped_fast |
| HBARUSDT | IDLE | 1.87 | 3.34 | 2.66 | -0.03 | 1007598.61 | 4.9 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 2.72 | 8.25 | 7.5 | -0.01 | 374294.43 | 13.42 | skipped_fast |
| EDELUSDT | IDLE | 2.06 | 3.67 | 2.99 | -0.02 | 514059.16 | 17.77 | skipped_fast |
| CCUSDT | IDLE | 2.0 | 5.19 | 4.72 | -0.01 | 416715.63 | 7.67 | skipped_fast |
| BIOUSDT | IDLE | 2.04 | 3.63 | 3.42 | -0.03 | 78023.74 | 8.35 | skipped_fast |
| REDUSDT | IDLE | 1.78 | 3.2 | 2.46 | 0.0 | 82376.59 | 11.12 | skipped_fast |
| ZBCNUSDT | IDLE | 0.83 | 2.22 | 0.59 | -0.03 | 258783.38 | 18.06 | skipped_fast |
| KITEUSDT | IDLE | 1.61 | 2.99 | 1.47 | -0.02 | 59684.21 | 10.78 | skipped_fast |
| WAXLUSDT | IDLE | 2.39 | 7.51 | 5.59 | -0.07 | 58111.86 | 61.0 | skipped_fast |
| RWAINCUSDT | IDLE | 0.87 | 3.81 | 0.39 | -0.01 | 66496.78 | 22.28 | skipped_fast |
| RIZEUSDT | IDLE | 1.15 | 2.32 | 0.13 | 0.05 | 44935.37 | 27.35 | skipped_fast |
| LAUSDT | IDLE | 1.95 | 4.42 | 4.15 | -0.03 | 64017.36 | 21.68 | skipped_fast |
| IOTAUSDT | IDLE | 1.93 | 3.39 | 3.19 | -0.02 | 80242.15 | 28.61 | skipped_fast |
| RWAUSDT | IDLE | 0.35 | 0.63 | 0.47 | -0.0 | 53446.83 | 23.58 | skipped_fast |
| FLUIDUSDT | IDLE | 0.27 | 1.42 | 0.26 | 0.01 | 19781.35 | 21.39 | skipped_fast |
| MNSRYUSDT | IDLE | 0.52 | 0.96 | 0.52 | 0.0 | 39530.76 | 62.61 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
