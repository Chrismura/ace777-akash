# Hulk DIGEST — 2026-09-22T22:15:40Z

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
| XRPUSDT | IDLE | 1.97 | 3.48 | 3.02 | -0.0 | 110441199.21 | 1.92 | skipped_fast |
| PYTHUSDT | IDLE | 0.85 | 3.79 | 3.1 | 0.04 | 1674749.3 | 3.05 | skipped_fast |
| HBARUSDT | IDLE | 2.23 | 5.46 | 2.31 | 0.06 | 1677081.49 | 2.03 | skipped_fast |
| ETHUSDT | IDLE | 0.58 | 1.02 | 0.9 | -0.01 | 416900406.26 | 0.07 | skipped_fast |
| BTCUSDT | IDLE | 0.44 | 0.77 | 0.73 | -0.01 | 914229837.32 | 0.0 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.55 | 11.13 | 9.37 | -0.03 | 234929.43 | 33.94 | skipped_fast |
| ZBCNUSDT | IDLE | 2.49 | 4.41 | 3.78 | -0.03 | 217965.65 | 28.0 | skipped_fast |
| CCUSDT | IDLE | 1.23 | 2.33 | 0.89 | -0.02 | 488845.45 | 7.92 | skipped_fast |
| RWAINCUSDT | IDLE | 3.5 | 9.03 | 3.23 | 0.03 | 18881.84 | 99.61 | skipped_fast |
| WUSDT | IDLE | 1.31 | 2.42 | 1.34 | 0.02 | 323934.63 | 5.83 | skipped_fast |
| RIZEUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.1 | 22.49 | 0.04 | 0.05 | 46427.66 | 95.18 | skipped_fast |
| CHIPUSDT | IDLE | 1.74 | 3.39 | 1.92 | -0.01 | 138737.86 | 19.8 | skipped_fast |
| BIOUSDT | IDLE | 1.08 | 2.02 | 0.87 | 0.03 | 135711.32 | 16.96 | skipped_fast |
| KITEUSDT | IDLE | 0.8 | 3.45 | 1.11 | 0.17 | 112377.59 | 9.4 | skipped_fast |
| QNTUSDT | IDLE | 1.48 | 4.82 | 1.99 | 0.1 | 202821.88 | 1.36 | skipped_fast |
| REDUSDT | IDLE | 0.7 | 1.29 | 0.71 | 0.05 | 63406.57 | 14.57 | skipped_fast |
| TELUSDT | IDLE | 1.39 | 5.5 | 0.71 | 0.1 | 103729.14 | 38.26 | skipped_fast |
| RWAUSDT | IDLE | 0.66 | 1.24 | 0.51 | -0.01 | 53099.88 | 7.25 | skipped_fast |
| FLUIDUSDT | IDLE | 0.44 | 0.86 | 0.13 | 0.01 | 5966.82 | 21.22 | skipped_fast |
| MNSRYUSDT | IDLE | 0.03 | 0.06 | 0.06 | -0.01 | 39919.0 | 9.02 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
