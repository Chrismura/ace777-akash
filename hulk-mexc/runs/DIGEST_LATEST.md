# Hulk DIGEST — 2026-09-16T19:13:59Z

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
| XRPUSDT | IDLE | 1.96 | 3.78 | 0.87 | -0.02 | 67861539.19 | 2.33 | skipped_fast |
| ETHUSDT | IDLE | 1.37 | 2.56 | 1.21 | -0.0 | 375802067.4 | 0.08 | skipped_fast |
| BTCUSDT | IDLE | 1.06 | 1.96 | 1.03 | -0.0 | 515484271.87 | 0.0 | skipped_fast |
| CCUSDT | IDLE | 3.94 | 7.86 | 0.19 | 0.03 | 473747.41 | 11.48 | skipped_fast |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 4.36 | 15.0 | 8.93 | -0.0 | 65252.53 | 12.78 | skipped_fast |
| RIZEUSDT | IDLE | 1.83 | 28.34 | 16.18 | 0.32 | 60223.03 | 36.07 | skipped_fast |
| PYTHUSDT | IDLE | 2.15 | 4.01 | 1.88 | -0.01 | 415249.21 | 1.92 | skipped_fast |
| CHIPUSDT | IDLE | 2.39 | 4.89 | 2.78 | -0.05 | 87738.15 | 13.86 | skipped_fast |
| WUSDT | IDLE | 1.9 | 3.55 | 1.71 | -0.05 | 202937.53 | 11.35 | skipped_fast |
| ZBCNUSDT | IDLE | 1.94 | 3.8 | 0.56 | 0.02 | 191822.43 | 27.49 | skipped_fast |
| BIOUSDT | IDLE | 2.03 | 3.88 | 1.17 | -0.01 | 76218.9 | 8.14 | skipped_fast |
| EDELUSDT | IDLE | 0.54 | 4.71 | 1.12 | 0.08 | 351620.32 | 37.79 | skipped_fast |
| REDUSDT | IDLE | 1.8 | 3.64 | 1.64 | -0.04 | 67780.73 | 17.26 | skipped_fast |
| RWAINCUSDT | IDLE | 1.63 | 2.88 | 2.57 | -0.04 | 12100.57 | 59.92 | skipped_fast |
| HBARUSDT | IDLE | 1.22 | 2.29 | 1.01 | -0.04 | 288888.85 | 1.37 | skipped_fast |
| TELUSDT | IDLE | 1.57 | 3.95 | 0.35 | -0.02 | 110874.72 | 41.58 | skipped_fast |
| QNTUSDT | IDLE | 1.28 | 2.45 | 0.7 | -0.03 | 37982.08 | 8.35 | skipped_fast |
| FLUIDUSDT | IDLE | 1.45 | 2.89 | 0.0 | -0.03 | 1611.03 | 22.28 | skipped_fast |
| RWAUSDT | IDLE | 0.63 | 1.21 | 0.3 | 0.0 | 51235.58 | 29.92 | skipped_fast |
| MNSRYUSDT | IDLE | 0.35 | 0.62 | 0.54 | -0.01 | 31993.35 | 17.03 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
