# Hulk DIGEST — 2026-09-12T13:37:29Z

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
| ETHUSDT | IDLE | 0.46 | 0.89 | 0.22 | 0.02 | 509793174.96 | 0.2 | skipped_fast |
| XRPUSDT | IDLE | 0.37 | 0.67 | 0.49 | 0.01 | 38849241.91 | 2.92 | skipped_fast |
| BTCUSDT | IDLE | 0.09 | 0.17 | 0.1 | -0.0 | 493055010.77 | 0.0 | skipped_fast |
| ZBCNUSDT | IDLE | 3.75 | 9.06 | 4.4 | 0.01 | 234829.92 | 23.13 | skipped_fast |
| PYTHUSDT | IDLE | 1.39 | 2.68 | 0.73 | 0.03 | 375402.0 | 1.87 | skipped_fast |
| RWAINCUSDT | IDLE | 3.53 | 6.94 | 3.32 | 0.04 | 15999.98 | 107.3 | skipped_fast |
| CCUSDT | IDLE | 0.92 | 1.61 | 1.59 | 0.0 | 319578.23 | 1.02 | skipped_fast |
| EDELUSDT | IDLE | 1.44 | 3.57 | 1.29 | 0.07 | 168924.04 | 17.47 | skipped_fast |
| CHIPUSDT | IDLE | 1.66 | 3.42 | 1.21 | 0.05 | 79216.74 | 16.55 | skipped_fast |
| REDUSDT | IDLE | 1.37 | 2.6 | 0.87 | 0.06 | 64159.33 | 20.24 | skipped_fast |
| BIOUSDT | IDLE | 1.03 | 1.97 | 0.62 | 0.03 | 77761.72 | 3.89 | skipped_fast |
| WUSDT | IDLE | 0.54 | 0.99 | 0.65 | 0.02 | 178736.3 | 10.24 | skipped_fast |
| KITEUSDT | IDLE | 0.77 | 1.45 | 0.62 | -0.01 | 60073.01 | 14.12 | skipped_fast |
| RIZEUSDT | IDLE | 0.18 | 9.97 | 1.32 | 0.97 | 172205.57 | 129.94 | skipped_fast |
| TELUSDT | IDLE | 1.06 | 2.96 | 1.7 | -0.04 | 100343.83 | 23.89 | skipped_fast |
| HBARUSDT | IDLE | 0.34 | 0.63 | 0.33 | -0.01 | 227394.43 | 1.34 | skipped_fast |
| QNTUSDT | IDLE | 0.81 | 1.54 | 0.51 | -0.0 | 41448.17 | 7.76 | skipped_fast |
| MNSRYUSDT | IDLE | 0.62 | 1.22 | 0.11 | -0.0 | 25741.85 | 40.32 | skipped_fast |
| RWAUSDT | IDLE | 0.41 | 0.74 | 0.59 | 0.01 | 54960.45 | 37.0 | skipped_fast |
| FLUIDUSDT | IDLE | 0.0 | 0.0 | 0.0 | 0.05 | 1339.83 | 22.02 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
