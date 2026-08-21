# Hulk DIGEST — 2026-08-21T19:57:04Z

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
| PYTHUSDT | IDLE | 1.36 | 4.99 | 4.1 | 0.07 | 5441067.64 | 2.13 | skipped_fast |
| XRPUSDT | IDLE | 1.17 | 4.21 | 3.62 | 0.12 | 128929475.95 | 2.19 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.15 | 26.97 | 13.89 | 0.16 | 153928.2 | 18.93 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 2.56 | 11.37 | 9.3 | 0.07 | 481575.51 | 14.51 | skipped_fast |
| CCUSDT | IDLE | 2.04 | 5.44 | 1.84 | 0.07 | 632851.61 | 2.8 | skipped_fast |
| HBARUSDT | IDLE | 1.62 | 3.1 | 2.99 | 0.06 | 793650.58 | 1.31 | skipped_fast |
| WUSDT | IDLE | 2.16 | 3.92 | 2.95 | 0.05 | 363554.43 | 7.5 | skipped_fast |
| CHIPUSDT | IDLE | 1.25 | 4.81 | 4.21 | 0.09 | 513918.2 | 6.22 | skipped_fast |
| BIOUSDT | IDLE | 2.64 | 5.33 | 4.42 | -0.0 | 190643.89 | 3.21 | skipped_fast |
| EDELUSDT | IDLE | 2.43 | 4.29 | 3.79 | -0.05 | 79684.71 | 22.52 | skipped_fast |
| RIZEUSDT | IDLE | 2.24 | 11.27 | 2.82 | 0.03 | 56432.16 | 45.77 | skipped_fast |
| RWAINCUSDT | IDLE | 2.23 | 4.3 | 1.11 | 0.04 | 11032.33 | 64.34 | skipped_fast |
| KITEUSDT | IDLE | 1.28 | 4.0 | 3.21 | 0.1 | 61317.35 | 9.39 | skipped_fast |
| QAITUSDT | IDLE | 1.65 | 3.0 | 1.98 | -0.01 | 2868.1 | 63.29 | skipped_fast |
| TELUSDT | IDLE | 1.85 | 4.46 | 2.42 | 0.01 | 183609.79 | 43.36 | skipped_fast |
| QNTUSDT | IDLE | 1.66 | 3.01 | 2.01 | 0.04 | 59917.9 | 6.27 | skipped_fast |
| RWAUSDT | IDLE | 0.65 | 1.16 | 0.99 | 0.04 | 54274.02 | 8.31 | skipped_fast |
| FLUIDUSDT | IDLE | 0.73 | 1.48 | 1.14 | 0.07 | 4276.39 | 21.69 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
