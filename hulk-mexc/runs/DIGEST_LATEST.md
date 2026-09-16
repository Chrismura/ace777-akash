# Hulk DIGEST — 2026-09-16T23:15:09Z

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
| XRPUSDT | IDLE | 2.92 | 5.48 | 2.34 | -0.01 | 57942327.78 | 2.33 | skipped_fast |
| ETHUSDT | IDLE | 1.38 | 2.56 | 1.31 | -0.0 | 363056991.77 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 1.05 | 1.96 | 0.97 | -0.0 | 502503741.49 | 0.0 | skipped_fast |
| CCUSDT | IDLE | 3.09 | 7.07 | 0.67 | 0.06 | 467913.82 | 9.33 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 4.32 | 7.81 | 5.56 | -0.03 | 20558.62 | 71.22 | skipped_fast |
| PYTHUSDT | IDLE | 1.82 | 3.28 | 2.37 | -0.03 | 409741.2 | 1.93 | skipped_fast |
| CHIPUSDT | IDLE | 2.61 | 5.67 | 4.37 | -0.05 | 75246.14 | 11.26 | skipped_fast |
| WUSDT | IDLE | 1.95 | 3.82 | 0.54 | -0.02 | 213338.42 | 14.47 | skipped_fast |
| BIOUSDT | IDLE | 1.85 | 3.61 | 0.64 | -0.02 | 78934.75 | 12.1 | skipped_fast |
| ZBCNUSDT | IDLE | 1.3 | 2.31 | 1.97 | 0.01 | 192764.78 | 17.43 | skipped_fast |
| EDELUSDT | IDLE | 0.51 | 3.78 | 1.64 | 0.17 | 312726.3 | 30.21 | skipped_fast |
| KITEUSDT | IDLE | 1.43 | 5.35 | 0.0 | 0.04 | 68051.47 | 12.29 | skipped_fast |
| REDUSDT | IDLE | 1.51 | 3.11 | 1.0 | -0.03 | 64849.8 | 18.69 | skipped_fast |
| TELUSDT | IDLE | 2.53 | 4.87 | 1.3 | -0.04 | 113091.92 | 34.61 | skipped_fast |
| HBARUSDT | IDLE | 1.45 | 2.65 | 1.66 | -0.03 | 261490.05 | 1.37 | skipped_fast |
| RWAUSDT | IDLE | 1.97 | 3.87 | 0.52 | 0.01 | 54327.91 | 22.48 | skipped_fast |
| QNTUSDT | IDLE | 1.83 | 3.62 | 0.29 | -0.01 | 37041.25 | 6.56 | skipped_fast |
| RIZEUSDT | IDLE | 0.66 | 9.65 | 6.93 | 0.24 | 60259.52 | 202.15 | skipped_fast |
| FLUIDUSDT | IDLE | 0.95 | 1.9 | 0.0 | -0.02 | 1573.23 | 22.24 | skipped_fast |
| MNSRYUSDT | IDLE | 0.26 | 0.51 | 0.13 | -0.01 | 31193.66 | 15.62 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
