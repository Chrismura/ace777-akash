# Hulk DIGEST — 2026-10-17T15:19:29Z

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
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 3.52 | 9.31 | 5.95 | -0.05 | 1289317.19 | 17.09 | skipped_fast |
| XRPUSDT | IDLE | 0.72 | 1.33 | 0.76 | -0.01 | 18814718.18 | 1.54 | skipped_fast |
| ETHUSDT | IDLE | 0.48 | 0.85 | 0.74 | -0.01 | 107868201.82 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.13 | 0.25 | 0.12 | -0.0 | 213346686.48 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.03 | 1.81 | 1.64 | -0.03 | 1106537.0 | 2.38 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 3.17 | 12.81 | 8.16 | -0.0 | 23641.44 | 5.35 | skipped_fast |
| ZBCNUSDT | IDLE | 2.45 | 4.76 | 0.93 | -0.03 | 225143.74 | 19.06 | skipped_fast |
| QNTUSDT | IDLE | 1.11 | 1.94 | 1.89 | -0.02 | 647571.69 | 4.47 | skipped_fast |
| CHIPUSDT | IDLE | 1.95 | 3.43 | 3.12 | -0.04 | 87888.15 | 11.25 | skipped_fast |
| KITEUSDT | IDLE | 1.96 | 3.42 | 3.27 | -0.02 | 61936.3 | 10.99 | skipped_fast |
| CCUSDT | IDLE | 1.05 | 2.08 | 0.11 | 0.02 | 273872.51 | 9.52 | skipped_fast |
| BIOUSDT | IDLE | 1.29 | 2.3 | 1.88 | -0.04 | 70083.11 | 8.18 | skipped_fast |
| EDELUSDT | IDLE | 1.02 | 1.88 | 1.13 | -0.05 | 153069.68 | 17.32 | skipped_fast |
| REDUSDT | IDLE | 1.2 | 2.28 | 0.77 | -0.06 | 68170.35 | 10.63 | skipped_fast |
| FLUIDUSDT | IDLE | 2.59 | 4.89 | 2.05 | 0.03 | 3603.53 | 21.37 | skipped_fast |
| RIZEUSDT | IDLE | 0.44 | 0.87 | 0.13 | -0.03 | 42969.77 | 48.52 | skipped_fast |
| HBARUSDT | IDLE | 0.69 | 1.32 | 0.44 | -0.02 | 145542.2 | 3.6 | skipped_fast |
| RWAUSDT | IDLE | 1.22 | 2.44 | 0.0 | -0.0 | 51807.67 | 31.72 | skipped_fast |
| TELUSDT | IDLE | 0.75 | 1.31 | 1.3 | -0.07 | 85519.96 | 11.93 | skipped_fast |
| MNSRYUSDT | IDLE | 0.14 | 0.26 | 0.18 | -0.0 | 27356.74 | 22.67 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
