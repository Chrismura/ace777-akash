# Hulk DIGEST — 2026-08-21T21:24:48Z

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
| PYTHUSDT | IDLE | 1.18 | 4.51 | 0.82 | 0.1 | 5622154.22 | 6.21 | skipped_fast |
| XRPUSDT | IDLE | 1.12 | 3.73 | 1.42 | 0.11 | 128897839.22 | 1.43 | skipped_fast |
| ZBCNUSDT | IDLE | 1.96 | 8.19 | 4.04 | 0.1 | 484531.75 | 4.54 | skipped_fast |
| CHIPUSDT | IDLE | 1.92 | 5.61 | 4.65 | 0.05 | 517325.91 | 6.24 | skipped_fast |
| CCUSDT | IDLE | 1.13 | 3.14 | 0.1 | 0.1 | 644408.96 | 6.43 | skipped_fast |
| HBARUSDT | IDLE | 1.55 | 3.04 | 0.37 | 0.07 | 809755.86 | 2.57 | skipped_fast |
| WUSDT | IDLE | 1.93 | 3.83 | 0.22 | 0.07 | 367679.26 | 15.62 | skipped_fast |
| BIOUSDT | IDLE | 2.43 | 5.2 | 2.15 | 0.02 | 186828.11 | 6.27 | skipped_fast |
| REDUSDT | IDLE | 1.35 | 11.01 | 9.41 | 0.17 | 153768.73 | 47.52 | skipped_fast |
| EDELUSDT | IDLE | 2.02 | 4.12 | 2.31 | -0.05 | 82641.58 | 33.73 | skipped_fast |
| RWAINCUSDT | IDLE | 2.27 | 4.3 | 1.64 | 0.03 | 10270.17 | 21.49 | skipped_fast |
| RIZEUSDT | IDLE | 1.87 | 9.54 | 1.34 | 0.02 | 56202.43 | 45.77 | skipped_fast |
| KITEUSDT | IDLE | 1.3 | 4.0 | 1.83 | 0.11 | 61014.47 | 11.1 | skipped_fast |
| QAITUSDT | IDLE | 2.33 | 4.38 | 1.83 | -0.01 | 3754.88 | 119.76 | skipped_fast |
| TELUSDT | IDLE | 1.34 | 3.39 | 0.58 | 0.02 | 178900.99 | 37.24 | skipped_fast |
| QNTUSDT | IDLE | 1.39 | 2.65 | 0.8 | 0.04 | 62110.82 | 13.97 | skipped_fast |
| RWAUSDT | IDLE | 0.62 | 1.17 | 0.49 | 0.03 | 53893.19 | 41.44 | skipped_fast |
| FLUIDUSDT | IDLE | 0.51 | 1.15 | 0.09 | 0.09 | 4171.26 | 21.99 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
