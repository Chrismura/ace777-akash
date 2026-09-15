# Hulk DIGEST — 2026-09-15T07:44:51Z

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
| XRPUSDT | IDLE | 1.41 | 2.49 | 2.24 | 0.01 | 75460229.28 | 2.15 | skipped_fast |
| ETHUSDT | IDLE | 1.01 | 1.77 | 1.64 | -0.02 | 466675899.33 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.74 | 1.29 | 1.22 | -0.01 | 529593066.06 | 0.0 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 4.43 | 22.32 | 15.83 | 0.02 | 171514.11 | 23.43 | skipped_fast |
| EDELUSDT | IDLE | 2.36 | 36.33 | 10.0 | 0.33 | 455739.41 | 48.61 | skipped_fast |
| PYTHUSDT | IDLE | 2.58 | 4.51 | 4.32 | -0.04 | 307097.85 | 1.83 | skipped_fast |
| RIZEUSDT | IDLE | 2.35 | 22.63 | 7.47 | -0.17 | 50561.06 | 109.0 | skipped_fast |
| CHIPUSDT | IDLE | 2.51 | 4.47 | 3.67 | -0.03 | 67499.7 | 17.09 | skipped_fast |
| CCUSDT | IDLE | 1.17 | 2.05 | 1.93 | -0.01 | 338799.21 | 3.17 | skipped_fast |
| WUSDT | IDLE | 1.99 | 3.51 | 3.2 | -0.04 | 164538.87 | 15.46 | skipped_fast |
| ZBCNUSDT | IDLE | 1.28 | 2.3 | 1.67 | 0.01 | 211994.65 | 13.37 | skipped_fast |
| HBARUSDT | IDLE | 1.55 | 2.74 | 2.35 | 0.0 | 375558.14 | 1.3 | skipped_fast |
| KITEUSDT | IDLE | 1.14 | 2.13 | 0.95 | -0.01 | 63227.74 | 10.33 | skipped_fast |
| BIOUSDT | IDLE | 0.9 | 1.62 | 1.24 | -0.0 | 92766.61 | 7.86 | skipped_fast |
| TELUSDT | IDLE | 1.9 | 4.11 | 3.83 | 0.0 | 98709.61 | 44.21 | skipped_fast |
| RWAINCUSDT | IDLE | 0.6 | 1.06 | 0.94 | -0.01 | 6459.01 | 5.57 | skipped_fast |
| FLUIDUSDT | IDLE | 1.96 | 3.43 | 3.32 | -0.02 | 2085.62 | 21.44 | skipped_fast |
| QNTUSDT | IDLE | 1.47 | 2.59 | 2.35 | -0.0 | 44791.65 | 6.3 | skipped_fast |
| RWAUSDT | IDLE | 0.29 | 0.52 | 0.45 | -0.01 | 53719.03 | 7.47 | skipped_fast |
| MNSRYUSDT | IDLE | 0.4 | 0.72 | 0.55 | 0.01 | 34534.43 | 29.12 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
