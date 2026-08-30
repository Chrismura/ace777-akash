# Hulk DIGEST — 2026-08-30T20:07:50Z

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
| XRPUSDT | IDLE | 1.47 | 2.71 | 1.49 | 0.01 | 22194675.59 | 2.13 | skipped_fast |
| ETHUSDT | IDLE | 1.34 | 2.51 | 1.14 | 0.02 | 220740313.52 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.54 | 0.97 | 0.69 | 0.01 | 281526366.49 | 0.01 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 2.78 | 5.97 | 5.12 | -0.05 | 493122.04 | 2.57 | skipped_fast |
| PYTHUSDT | IDLE | 1.97 | 3.62 | 2.15 | 0.02 | 407373.93 | 2.03 | skipped_fast |
| ZBCNUSDT | IDLE | 2.84 | 5.98 | 4.05 | -0.05 | 196516.75 | 11.44 | skipped_fast |
| KITEUSDT | IDLE | 2.02 | 3.6 | 2.99 | -0.02 | 60754.9 | 8.75 | skipped_fast |
| WUSDT | IDLE | 1.15 | 2.08 | 1.49 | 0.03 | 226515.76 | 10.56 | skipped_fast |
| RIZEUSDT | IDLE | 1.85 | 5.3 | 2.57 | -0.0 | 43701.98 | 49.98 | skipped_fast |
| REDUSDT | IDLE | 1.56 | 2.74 | 2.5 | 0.01 | 63740.29 | 11.93 | skipped_fast |
| EDELUSDT | IDLE | 1.51 | 4.54 | 1.39 | 0.07 | 74794.87 | 24.89 | skipped_fast |
| CCUSDT | IDLE | 0.57 | 1.05 | 0.61 | 0.0 | 241913.1 | 7.62 | skipped_fast |
| BIOUSDT | IDLE | 1.05 | 1.94 | 1.08 | -0.0 | 80903.13 | 3.64 | skipped_fast |
| TELUSDT | IDLE | 1.91 | 3.61 | 1.37 | -0.01 | 85684.85 | 46.3 | skipped_fast |
| HBARUSDT | IDLE | 0.83 | 1.6 | 0.42 | 0.0 | 167694.45 | 1.32 | skipped_fast |
| RWAINCUSDT | IDLE | 1.12 | 2.24 | 0.0 | 0.02 | 1480.3 | 120.81 | skipped_fast |
| QNTUSDT | IDLE | 0.86 | 1.57 | 0.95 | 0.01 | 38458.67 | 1.62 | skipped_fast |
| RWAUSDT | IDLE | 0.66 | 1.3 | 0.08 | 0.02 | 53000.97 | 16.09 | skipped_fast |
| FLUIDUSDT | IDLE | 0.89 | 1.73 | 0.37 | 0.03 | 3286.72 | 20.87 | skipped_fast |
| MNSRYUSDT | IDLE | 0.25 | 0.47 | 0.19 | 0.01 | 31942.64 | 4.0 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
