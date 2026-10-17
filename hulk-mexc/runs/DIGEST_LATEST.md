# Hulk DIGEST — 2026-10-17T14:59:23Z

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
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.33 | 11.6 | 6.37 | -0.04 | 1311522.15 | 16.13 | skipped_fast |
| XRPUSDT | IDLE | 0.71 | 1.33 | 0.56 | -0.02 | 19997193.1 | 0.77 | skipped_fast |
| ETHUSDT | IDLE | 0.47 | 0.85 | 0.55 | -0.01 | 112659328.44 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.17 | 0.32 | 0.19 | -0.01 | 220524301.87 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 0.96 | 1.79 | 0.88 | -0.05 | 1137451.69 | 2.36 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 3.2 | 12.81 | 9.0 | -0.01 | 23666.44 | 5.4 | skipped_fast |
| CHIPUSDT | IDLE | 2.5 | 4.46 | 3.62 | -0.06 | 90360.76 | 2.24 | skipped_fast |
| ZBCNUSDT | IDLE | 2.29 | 4.76 | 0.91 | -0.04 | 225172.01 | 41.41 | skipped_fast |
| KITEUSDT | IDLE | 2.59 | 4.58 | 4.06 | -0.02 | 61661.47 | 9.25 | skipped_fast |
| QNTUSDT | IDLE | 1.09 | 1.97 | 1.45 | -0.01 | 628106.51 | 2.96 | skipped_fast |
| CCUSDT | IDLE | 0.95 | 1.83 | 0.41 | -0.0 | 282993.35 | 7.67 | skipped_fast |
| EDELUSDT | IDLE | 1.06 | 1.88 | 1.64 | -0.07 | 156417.56 | 10.44 | skipped_fast |
| BIOUSDT | IDLE | 1.33 | 2.42 | 1.64 | -0.04 | 70092.23 | 8.14 | skipped_fast |
| REDUSDT | IDLE | 1.21 | 2.53 | 1.29 | -0.07 | 68357.56 | 9.24 | skipped_fast |
| FLUIDUSDT | IDLE | 2.66 | 4.89 | 3.0 | 0.03 | 3563.31 | 18.37 | skipped_fast |
| RIZEUSDT | IDLE | 0.53 | 1.04 | 0.29 | -0.03 | 42953.67 | 27.45 | skipped_fast |
| HBARUSDT | IDLE | 0.87 | 1.66 | 0.54 | -0.03 | 168877.35 | 8.38 | skipped_fast |
| RWAUSDT | IDLE | 1.19 | 2.35 | 0.16 | -0.01 | 51864.74 | 15.9 | skipped_fast |
| TELUSDT | IDLE | 0.66 | 1.19 | 0.82 | -0.06 | 84045.87 | 17.79 | skipped_fast |
| MNSRYUSDT | IDLE | 0.14 | 0.26 | 0.11 | -0.0 | 27265.92 | 8.49 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
