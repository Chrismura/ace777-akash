# Hulk DIGEST — 2026-10-26T10:45:16Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| XRPUSDT | IDLE | 0.84 | 1.63 | 0.28 | -0.0 | 19800962.54 | 0.77 | skipped_fast |
| ETHUSDT | IDLE | 0.75 | 1.45 | 0.31 | 0.0 | 111013583.53 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.57 | 1.11 | 0.17 | 0.0 | 227938807.82 | 0.0 | skipped_fast |
| QNTUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.59 | 11.23 | 0.41 | 0.16 | 1063418.2 | 0.47 | skipped_fast |
| PYTHUSDT | IDLE | 1.97 | 3.91 | 0.26 | 0.06 | 837545.98 | 6.64 | skipped_fast |
| ZBCNUSDT | IDLE | 2.79 | 6.09 | 4.77 | -0.01 | 213391.02 | 20.25 | skipped_fast |
| WUSDT | IDLE | 1.64 | 3.06 | 1.46 | -0.01 | 498406.9 | 14.39 | skipped_fast |
| CHIPUSDT | IDLE | 2.26 | 6.29 | 2.31 | 0.05 | 110962.16 | 19.35 | skipped_fast |
| REDUSDT | IDLE | 1.99 | 3.98 | 0.06 | 0.03 | 60505.08 | 14.88 | skipped_fast |
| RWAINCUSDT | IDLE | 1.59 | 2.95 | 2.52 | -0.07 | 67933.68 | 5.87 | skipped_fast |
| CCUSDT | IDLE | 0.95 | 1.77 | 0.92 | 0.01 | 163221.57 | 7.9 | skipped_fast |
| KITEUSDT | IDLE | 1.41 | 2.61 | 1.4 | 0.01 | 53723.14 | 11.57 | skipped_fast |
| BIOUSDT | IDLE | 1.24 | 2.33 | 1.03 | -0.0 | 59487.22 | 9.03 | skipped_fast |
| EDELUSDT | IDLE | 1.0 | 2.57 | 1.18 | 0.08 | 137764.07 | 31.29 | skipped_fast |
| LAUSDT | IDLE | 2.44 | 4.96 | 2.33 | 0.02 | 64525.01 | 22.29 | skipped_fast |
| WAXLUSDT | IDLE | 2.11 | 3.86 | 2.36 | -0.0 | 51906.88 | 35.78 | skipped_fast |
| MNSRYUSDT | IDLE | 2.43 | 4.38 | 3.16 | -0.01 | 41284.47 | 76.46 | skipped_fast |
| HBARUSDT | IDLE | 0.9 | 1.78 | 0.19 | 0.01 | 179620.18 | 5.16 | skipped_fast |
| RIZEUSDT | IDLE | 0.5 | 0.97 | 0.14 | 0.01 | 33229.45 | 57.54 | skipped_fast |
| IOTAUSDT | IDLE | 1.1 | 2.1 | 0.63 | -0.0 | 63900.65 | 23.56 | skipped_fast |
| FLUIDUSDT | IDLE | 0.19 | 0.86 | 0.86 | -0.03 | 19098.64 | 21.78 | skipped_fast |
| RWAUSDT | IDLE | 0.12 | 0.24 | 0.0 | -0.01 | 53008.77 | 23.89 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
