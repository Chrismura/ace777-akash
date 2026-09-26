# Hulk DIGEST — 2026-09-26T14:30:42Z

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
| XRPUSDT | IDLE | 0.56 | 1.03 | 0.55 | -0.02 | 57206200.02 | 1.94 | skipped_fast |
| ETHUSDT | IDLE | 0.24 | 0.46 | 0.13 | 0.0 | 166873142.04 | 0.22 | skipped_fast |
| BTCUSDT | IDLE | 0.23 | 0.42 | 0.28 | 0.0 | 412202277.44 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.16 | 6.02 | 1.99 | 0.08 | 1190715.29 | 3.86 | skipped_fast |
| CCUSDT | IDLE | 1.55 | 5.28 | 2.35 | 0.1 | 982659.31 | 5.1 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 4.53 | 13.4 | 11.82 | -0.06 | 7497.61 | 112.39 | skipped_fast |
| QNTUSDT | IDLE | 1.73 | 6.75 | 2.78 | 0.14 | 798549.55 | 3.74 | skipped_fast |
| WUSDT | IDLE | 1.8 | 3.94 | 2.78 | 0.06 | 451731.47 | 7.12 | skipped_fast |
| EDELUSDT | IDLE | 2.77 | 5.22 | 2.14 | 0.03 | 158898.71 | 22.98 | skipped_fast |
| BIOUSDT | IDLE | 2.08 | 3.66 | 3.32 | -0.01 | 105678.53 | 6.2 | skipped_fast |
| ZBCNUSDT | IDLE | 1.66 | 3.28 | 0.23 | 0.01 | 227106.07 | 9.29 | skipped_fast |
| HBARUSDT | IDLE | 0.97 | 1.78 | 1.11 | 0.0 | 584125.14 | 1.07 | skipped_fast |
| CHIPUSDT | IDLE | 1.4 | 2.54 | 1.7 | -0.01 | 126725.18 | 12.37 | skipped_fast |
| RIZEUSDT | IDLE | 1.46 | 7.38 | 3.8 | -0.1 | 46771.97 | 61.89 | skipped_fast |
| REDUSDT | IDLE | 1.09 | 1.96 | 1.42 | -0.01 | 58348.28 | 14.25 | skipped_fast |
| KITEUSDT | IDLE | 0.97 | 1.84 | 1.01 | 0.04 | 74946.75 | 10.33 | skipped_fast |
| RWAUSDT | IDLE | 2.16 | 4.23 | 0.57 | 0.02 | 55911.89 | 7.17 | skipped_fast |
| TELUSDT | IDLE | 1.57 | 2.78 | 2.34 | -0.05 | 122518.13 | 31.54 | skipped_fast |
| FLUIDUSDT | IDLE | 0.95 | 1.9 | 0.0 | 0.02 | 2919.51 | 22.08 | skipped_fast |
| MNSRYUSDT | IDLE | 0.04 | 0.08 | 0.0 | 0.0 | 39108.65 | 7.64 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
