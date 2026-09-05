# Hulk DIGEST — 2026-09-05T20:45:41Z

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
| XRPUSDT | IDLE | 0.68 | 1.25 | 0.76 | 0.01 | 22654647.29 | 0.71 | skipped_fast |
| ETHUSDT | IDLE | 0.59 | 1.16 | 0.19 | 0.01 | 159989541.99 | 0.56 | skipped_fast |
| BTCUSDT | IDLE | 0.37 | 0.65 | 0.54 | 0.0 | 364811404.64 | 0.01 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.68 | 23.78 | 9.89 | 0.04 | 141543.23 | 63.29 | skipped_fast |
| CHIPUSDT | IDLE | 2.36 | 6.2 | 1.97 | 0.06 | 457473.28 | 5.08 | skipped_fast |
| ZBCNUSDT | IDLE | 2.58 | 4.95 | 1.45 | -0.01 | 195986.77 | 13.38 | skipped_fast |
| CCUSDT | IDLE | 1.41 | 2.5 | 2.13 | 0.03 | 301199.99 | 7.33 | skipped_fast |
| PYTHUSDT | IDLE | 1.05 | 2.0 | 0.69 | 0.0 | 331221.74 | 1.82 | skipped_fast |
| RWAINCUSDT | IDLE | 2.87 | 5.31 | 2.91 | 0.01 | 7793.74 | 90.64 | skipped_fast |
| WUSDT | IDLE | 1.45 | 2.65 | 1.71 | 0.04 | 139580.79 | 11.08 | skipped_fast |
| REDUSDT | IDLE | 1.12 | 2.13 | 0.75 | 0.04 | 60998.65 | 8.7 | skipped_fast |
| BIOUSDT | IDLE | 0.88 | 1.69 | 0.46 | 0.05 | 83157.12 | 3.56 | skipped_fast |
| KITEUSDT | IDLE | 0.7 | 1.73 | 0.63 | -0.06 | 62622.69 | 8.7 | skipped_fast |
| EDELUSDT | IDLE | 0.16 | 2.89 | 0.56 | -0.01 | 165437.43 | 18.83 | skipped_fast |
| HBARUSDT | IDLE | 0.64 | 1.2 | 0.52 | 0.04 | 328141.05 | 1.24 | skipped_fast |
| QNTUSDT | IDLE | 1.42 | 2.63 | 1.34 | 0.01 | 42550.9 | 6.19 | skipped_fast |
| RWAUSDT | IDLE | 0.81 | 1.49 | 0.84 | 0.03 | 52005.94 | 7.03 | skipped_fast |
| TELUSDT | IDLE | 0.96 | 1.82 | 0.63 | 0.01 | 66977.94 | 46.32 | skipped_fast |
| FLUIDUSDT | IDLE | 0.51 | 0.99 | 0.19 | 0.01 | 497.42 | 21.71 | skipped_fast |
| MNSRYUSDT | IDLE | 0.14 | 0.27 | 0.08 | 0.0 | 37987.47 | 27.3 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
