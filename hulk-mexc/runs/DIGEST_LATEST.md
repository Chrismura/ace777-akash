# Hulk DIGEST — 2026-10-16T19:04:16Z

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
| PYTHUSDT | IDLE | 2.26 | 7.92 | 6.45 | -0.12 | 2149771.67 | 1.19 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 3.1 | 7.66 | 6.13 | -0.05 | 1702811.24 | 17.0 | skipped_fast |
| XRPUSDT | IDLE | 2.26 | 3.97 | 3.63 | -0.04 | 27366896.98 | 3.09 | skipped_fast |
| ETHUSDT | IDLE | 2.03 | 3.61 | 3.02 | -0.02 | 213070028.23 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 1.14 | 2.05 | 1.58 | -0.02 | 356951794.24 | 0.45 | skipped_fast |
| QNTUSDT | IDLE | 2.47 | 4.44 | 3.33 | -0.05 | 838863.05 | 1.49 | skipped_fast |
| CCUSDT | IDLE | 2.24 | 4.04 | 2.93 | -0.05 | 386732.28 | 6.79 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.02 | 7.28 | 6.69 | -0.1 | 97538.54 | 10.49 | skipped_fast |
| ZBCNUSDT | IDLE | 2.79 | 4.89 | 4.55 | -0.05 | 214728.04 | 18.5 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 3.43 | 6.06 | 5.38 | -0.03 | 307618.91 | 6.07 | skipped_fast |
| RWAINCUSDT | IDLE | 2.28 | 10.27 | 9.31 | -0.14 | 25108.29 | 11.54 | skipped_fast |
| EDELUSDT | IDLE | 2.34 | 4.3 | 2.53 | 0.04 | 181818.56 | 26.62 | skipped_fast |
| CHIPUSDT | IDLE | 1.94 | 6.94 | 5.51 | -0.02 | 152674.58 | 13.2 | skipped_fast |
| BIOUSDT | IDLE | 2.42 | 4.32 | 3.53 | -0.04 | 61632.04 | 8.04 | skipped_fast |
| KITEUSDT | IDLE | 1.45 | 2.54 | 2.45 | -0.05 | 56524.0 | 10.88 | skipped_fast |
| RWAUSDT | IDLE | 2.08 | 3.9 | 1.72 | 0.0 | 53708.05 | 23.86 | skipped_fast |
| RIZEUSDT | IDLE | 1.07 | 2.4 | 1.03 | 0.04 | 47586.3 | 57.14 | skipped_fast |
| TELUSDT | IDLE | 1.28 | 2.27 | 1.94 | -0.0 | 92205.08 | 11.29 | skipped_fast |
| FLUIDUSDT | IDLE | 1.23 | 2.36 | 0.62 | -0.03 | 7117.24 | 18.97 | skipped_fast |
| MNSRYUSDT | IDLE | 0.4 | 0.71 | 0.55 | -0.01 | 35786.15 | 28.41 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
