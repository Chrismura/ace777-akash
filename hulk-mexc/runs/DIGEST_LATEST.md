# Hulk DIGEST — 2026-09-05T23:45:24Z

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
| XRPUSDT | IDLE | 0.97 | 1.78 | 1.11 | 0.01 | 23064881.79 | 2.83 | skipped_fast |
| ETHUSDT | IDLE | 0.43 | 0.78 | 0.47 | 0.01 | 161327409.5 | 0.6 | skipped_fast |
| BTCUSDT | IDLE | 0.27 | 0.49 | 0.33 | 0.0 | 364867673.42 | 0.37 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.29 | 20.43 | 14.39 | -0.01 | 133059.33 | 54.38 | skipped_fast |
| CHIPUSDT | IDLE | 1.48 | 3.82 | 1.53 | 0.08 | 428281.46 | 3.38 | skipped_fast |
| ZBCNUSDT | IDLE | 2.13 | 4.0 | 1.67 | -0.01 | 209582.18 | 16.75 | skipped_fast |
| PYTHUSDT | IDLE | 1.01 | 1.91 | 0.69 | 0.01 | 340413.97 | 1.82 | skipped_fast |
| RWAINCUSDT | IDLE | 2.78 | 5.2 | 2.34 | 0.01 | 8230.33 | 59.0 | skipped_fast |
| CCUSDT | IDLE | 0.95 | 1.69 | 1.34 | 0.02 | 273012.13 | 8.25 | skipped_fast |
| WUSDT | IDLE | 1.29 | 2.53 | 0.32 | 0.05 | 152927.83 | 5.97 | skipped_fast |
| REDUSDT | IDLE | 1.03 | 1.92 | 0.89 | 0.04 | 60980.99 | 10.29 | skipped_fast |
| BIOUSDT | IDLE | 0.86 | 1.51 | 1.42 | 0.03 | 82087.48 | 3.6 | skipped_fast |
| HBARUSDT | IDLE | 0.9 | 1.59 | 1.43 | 0.02 | 362554.63 | 1.25 | skipped_fast |
| EDELUSDT | IDLE | 0.13 | 2.37 | 0.28 | -0.01 | 167293.84 | 18.59 | skipped_fast |
| KITEUSDT | IDLE | 0.52 | 1.21 | 0.83 | -0.07 | 64269.19 | 11.92 | skipped_fast |
| TELUSDT | IDLE | 1.96 | 3.58 | 2.24 | -0.01 | 72200.14 | 35.29 | skipped_fast |
| RWAUSDT | IDLE | 1.63 | 2.96 | 2.05 | 0.04 | 52639.6 | 20.94 | skipped_fast |
| QNTUSDT | IDLE | 0.82 | 1.5 | 0.92 | 0.02 | 36431.67 | 1.54 | skipped_fast |
| MNSRYUSDT | IDLE | 0.13 | 0.26 | 0.05 | 0.0 | 38322.38 | 2.73 | skipped_fast |
| FLUIDUSDT | IDLE | 0.4 | 0.79 | 0.1 | 0.02 | 524.28 | 22.38 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
