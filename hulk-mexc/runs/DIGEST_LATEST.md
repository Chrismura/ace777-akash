# Hulk DIGEST — 2026-08-21T20:52:29Z

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
| PYTHUSDT | IDLE | 1.31 | 4.78 | 2.46 | 0.08 | 5561545.71 | 2.1 | skipped_fast |
| XRPUSDT | IDLE | 1.26 | 4.21 | 3.47 | 0.1 | 128477201.89 | 1.46 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.01 | 25.8 | 12.74 | 0.17 | 153009.82 | 13.0 | skipped_fast |
| ZBCNUSDT | IDLE | 2.47 | 10.86 | 5.42 | 0.13 | 478965.33 | 26.96 | skipped_fast |
| CCUSDT | IDLE | 1.41 | 3.91 | 0.29 | 0.1 | 642160.77 | 6.44 | skipped_fast |
| HBARUSDT | IDLE | 1.72 | 3.23 | 1.84 | 0.06 | 809569.4 | 1.3 | skipped_fast |
| CHIPUSDT | IDLE | 1.34 | 4.81 | 3.58 | 0.08 | 514548.0 | 6.19 | skipped_fast |
| WUSDT | IDLE | 2.04 | 3.92 | 1.13 | 0.07 | 367754.9 | 15.78 | skipped_fast |
| BIOUSDT | IDLE | 2.51 | 5.33 | 2.39 | 0.01 | 188224.55 | 3.15 | skipped_fast |
| EDELUSDT | IDLE | 2.89 | 5.73 | 4.44 | -0.06 | 82433.18 | 45.51 | skipped_fast |
| RIZEUSDT | IDLE | 1.88 | 9.71 | 0.42 | 0.02 | 56250.33 | 46.99 | skipped_fast |
| RWAINCUSDT | IDLE | 2.22 | 4.3 | 0.95 | 0.02 | 10901.49 | 26.83 | skipped_fast |
| KITEUSDT | IDLE | 1.24 | 4.0 | 2.25 | 0.11 | 61209.4 | 9.29 | skipped_fast |
| TELUSDT | IDLE | 1.38 | 3.39 | 1.27 | 0.02 | 181330.61 | 42.94 | skipped_fast |
| QNTUSDT | IDLE | 1.45 | 2.65 | 1.65 | 0.04 | 60041.94 | 1.56 | skipped_fast |
| QAITUSDT | IDLE | 1.72 | 3.0 | 2.88 | -0.02 | 2798.65 | 175.02 | skipped_fast |
| RWAUSDT | IDLE | 0.71 | 1.25 | 1.15 | 0.03 | 53945.77 | 8.32 | skipped_fast |
| FLUIDUSDT | IDLE | 0.58 | 1.15 | 1.1 | 0.07 | 4286.4 | 22.22 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
