# Hulk DIGEST — 2026-09-28T11:40:04Z

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
| QNTUSDT | IDLE | 1.47 | 48.63 | 13.22 | 0.52 | 19556644.18 | 9.93 | skipped_fast |
| HBARUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.44 | 23.82 | 1.28 | 0.24 | 5620980.16 | 10.21 | skipped_fast |
| WUSDT | IDLE | 1.34 | 5.74 | 2.36 | -0.04 | 3414865.01 | 7.06 | skipped_fast |
| CCUSDT | WATCH_PULLBACK — tension haute + reflux | 4.39 | 14.75 | 9.77 | -0.03 | 1174447.72 | 7.53 | skipped_fast |
| PYTHUSDT | IDLE | 1.7 | 4.6 | 2.62 | -0.08 | 1574411.75 | 1.24 | skipped_fast |
| XRPUSDT | IDLE | 0.85 | 1.7 | 0.02 | -0.03 | 53361735.0 | 1.34 | skipped_fast |
| ETHUSDT | IDLE | 0.57 | 1.14 | 0.0 | -0.01 | 305332555.61 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.45 | 0.85 | 0.3 | -0.02 | 654341795.68 | 0.0 | skipped_fast |
| EDELUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.45 | 18.3 | 0.99 | 0.01 | 186133.9 | 3.43 | skipped_fast |
| KITEUSDT | IDLE | 2.19 | 6.75 | 5.69 | -0.08 | 104213.72 | 8.06 | skipped_fast |
| BIOUSDT | IDLE | 1.48 | 3.69 | 2.21 | -0.07 | 104919.66 | 3.37 | skipped_fast |
| ZBCNUSDT | IDLE | 1.23 | 2.35 | 0.72 | -0.04 | 204352.03 | 17.28 | skipped_fast |
| CHIPUSDT | IDLE | 1.17 | 3.43 | 2.08 | -0.1 | 87080.4 | 13.56 | skipped_fast |
| REDUSDT | IDLE | 1.35 | 2.82 | 0.79 | -0.05 | 60874.14 | 12.89 | skipped_fast |
| TELUSDT | IDLE | 2.22 | 4.04 | 2.68 | -0.0 | 165479.41 | 39.34 | skipped_fast |
| RWAINCUSDT | IDLE | 0.65 | 6.39 | 2.95 | 0.15 | 32732.73 | 64.18 | skipped_fast |
| RIZEUSDT | IDLE | 0.39 | 2.34 | 1.05 | -0.15 | 59757.9 | 75.84 | skipped_fast |
| RWAUSDT | IDLE | 0.84 | 1.53 | 1.0 | -0.02 | 59866.68 | 7.22 | skipped_fast |
| FLUIDUSDT | IDLE | 1.02 | 2.38 | 0.86 | -0.05 | 3474.62 | 22.03 | skipped_fast |
| MNSRYUSDT | IDLE | 0.4 | 0.73 | 0.44 | -0.02 | 35234.15 | 66.81 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
