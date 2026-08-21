# Hulk DIGEST — 2026-08-21T19:56:18Z

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
| PYTHUSDT | IDLE | 1.36 | 4.99 | 3.92 | 0.07 | 5440182.77 | 2.12 | skipped_fast |
| XRPUSDT | IDLE | 1.17 | 4.21 | 3.55 | 0.12 | 129143404.89 | 2.92 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.15 | 26.97 | 13.91 | 0.16 | 153975.85 | 18.93 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 2.56 | 11.37 | 9.31 | 0.07 | 481593.58 | 17.62 | skipped_fast |
| CCUSDT | IDLE | 2.05 | 5.44 | 2.02 | 0.06 | 633492.18 | 7.48 | skipped_fast |
| HBARUSDT | IDLE | 1.6 | 3.1 | 2.72 | 0.05 | 793576.22 | 1.31 | skipped_fast |
| CHIPUSDT | IDLE | 1.24 | 4.81 | 4.0 | 0.09 | 513935.78 | 6.21 | skipped_fast |
| WUSDT | IDLE | 2.16 | 3.92 | 2.91 | 0.05 | 363544.45 | 13.91 | skipped_fast |
| BIOUSDT | IDLE | 2.63 | 5.33 | 4.29 | -0.0 | 190666.92 | 3.2 | skipped_fast |
| RIZEUSDT | IDLE | 2.24 | 11.27 | 2.82 | 0.02 | 56438.52 | 45.77 | skipped_fast |
| EDELUSDT | IDLE | 2.43 | 4.29 | 3.79 | -0.05 | 79659.71 | 33.76 | skipped_fast |
| KITEUSDT | IDLE | 1.28 | 4.0 | 3.18 | 0.1 | 61311.7 | 11.26 | skipped_fast |
| RWAINCUSDT | IDLE | 2.23 | 4.3 | 1.11 | 0.04 | 11032.33 | 80.49 | skipped_fast |
| QAITUSDT | IDLE | 1.65 | 3.0 | 1.98 | -0.0 | 2888.48 | 63.29 | skipped_fast |
| TELUSDT | IDLE | 1.85 | 4.46 | 2.42 | 0.01 | 183490.08 | 54.2 | skipped_fast |
| QNTUSDT | IDLE | 1.64 | 3.01 | 1.85 | 0.04 | 59894.98 | 7.83 | skipped_fast |
| RWAUSDT | IDLE | 0.65 | 1.16 | 0.99 | 0.04 | 54254.31 | 8.31 | skipped_fast |
| FLUIDUSDT | IDLE | 0.73 | 1.48 | 1.14 | 0.07 | 4276.39 | 22.45 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
