# Hulk DIGEST — 2026-08-28T01:06:57Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : XRPUSDT, HBARUSDT, QAITUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT
- Watch only : QNTUSDT, FLUIDUSDT, RWAUSDT

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| PYTHUSDT | IDLE | 1.34 | 3.51 | 0.14 | 0.02 | 23077596.48 | 2.01 | skipped_fast |
| XRPUSDT | IDLE | 0.72 | 1.35 | 0.55 | 0.04 | 52947492.0 | 2.75 | skipped_fast |
| CHIPUSDT | IDLE | 0.91 | 5.11 | 1.61 | 0.12 | 808416.53 | 2.52 | skipped_fast |
| QAITUSDT | IDLE | 0.9 | 38.43 | 25.89 | -0.13 | 60196.75 | 18.42 | skipped_fast |
| RWAINCUSDT | IDLE | 3.84 | 14.05 | 4.04 | 0.01 | 22426.66 | 16.03 | skipped_fast |
| KITEUSDT | IDLE | 2.96 | 5.78 | 0.88 | 0.02 | 74534.27 | 9.24 | skipped_fast |
| REDUSDT | IDLE | 2.59 | 4.89 | 1.92 | 0.01 | 86085.05 | 11.87 | skipped_fast |
| CCUSDT | IDLE | 1.05 | 2.08 | 0.2 | -0.02 | 431630.11 | 2.64 | skipped_fast |
| ZBCNUSDT | IDLE | 0.78 | 2.75 | 1.35 | 0.08 | 248539.07 | 22.02 | skipped_fast |
| WUSDT | IDLE | 1.02 | 1.9 | 0.89 | 0.02 | 186174.61 | 13.42 | skipped_fast |
| BIOUSDT | IDLE | 1.25 | 2.44 | 0.4 | 0.04 | 98599.2 | 3.37 | skipped_fast |
| RIZEUSDT | IDLE | 0.76 | 9.57 | 1.06 | -0.17 | 112915.39 | 36.36 | skipped_fast |
| TELUSDT | IDLE | 1.93 | 3.65 | 2.86 | 0.04 | 121996.45 | 15.79 | skipped_fast |
| HBARUSDT | IDLE | 0.66 | 1.3 | 0.18 | 0.02 | 339395.95 | 1.26 | skipped_fast |
| EDELUSDT | IDLE | 0.39 | 2.91 | 1.75 | 0.12 | 26512.75 | 50.8 | skipped_fast |
| QNTUSDT | IDLE | 0.62 | 1.14 | 0.71 | 0.0 | 44602.87 | 4.75 | skipped_fast |
| RWAUSDT | IDLE | 0.43 | 0.83 | 0.25 | 0.01 | 53885.18 | 8.3 | skipped_fast |
| FLUIDUSDT | IDLE | 0.34 | 1.1 | 0.0 | -0.0 | 8417.31 | 21.71 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
