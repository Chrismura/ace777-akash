# Hulk DIGEST — 2026-09-20T00:00:07Z

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
| XRPUSDT | IDLE | 1.46 | 2.66 | 1.75 | 0.01 | 58501567.94 | 1.42 | skipped_fast |
| ETHUSDT | IDLE | 0.6 | 1.11 | 0.55 | 0.01 | 237077155.6 | 0.15 | skipped_fast |
| BTCUSDT | IDLE | 0.41 | 0.77 | 0.33 | 0.0 | 449628087.74 | 0.29 | skipped_fast |
| PYTHUSDT | IDLE | 1.32 | 2.57 | 0.46 | 0.01 | 634154.96 | 3.27 | skipped_fast |
| WUSDT | IDLE | 1.69 | 3.28 | 0.69 | 0.0 | 526524.8 | 6.32 | skipped_fast |
| CCUSDT | IDLE | 1.74 | 3.14 | 2.2 | -0.01 | 328158.26 | 8.22 | skipped_fast |
| HBARUSDT | IDLE | 1.53 | 2.88 | 1.18 | 0.03 | 614446.06 | 1.23 | skipped_fast |
| EDELUSDT | IDLE | 2.04 | 6.05 | 5.28 | -0.08 | 132215.61 | 39.92 | skipped_fast |
| ZBCNUSDT | IDLE | 1.07 | 4.16 | 2.18 | 0.1 | 221267.59 | 22.52 | skipped_fast |
| CHIPUSDT | IDLE | 1.21 | 3.65 | 0.25 | -0.02 | 125712.8 | 13.68 | skipped_fast |
| BIOUSDT | IDLE | 1.32 | 2.46 | 1.24 | 0.02 | 89556.55 | 3.57 | skipped_fast |
| RWAINCUSDT | IDLE | 1.95 | 4.31 | 3.39 | -0.03 | 7001.47 | 77.04 | skipped_fast |
| KITEUSDT | IDLE | 1.21 | 2.31 | 0.7 | 0.03 | 78704.37 | 11.31 | skipped_fast |
| REDUSDT | IDLE | 0.47 | 2.16 | 0.53 | 0.02 | 136612.74 | 14.73 | skipped_fast |
| TELUSDT | IDLE | 1.66 | 4.02 | 3.54 | -0.09 | 104920.46 | 40.87 | skipped_fast |
| QNTUSDT | IDLE | 1.36 | 2.53 | 1.23 | 0.04 | 58514.82 | 3.05 | skipped_fast |
| RIZEUSDT | IDLE | 1.04 | 4.2 | 2.57 | 0.02 | 38256.01 | 225.66 | skipped_fast |
| FLUIDUSDT | IDLE | 0.83 | 1.54 | 0.81 | 0.02 | 9072.55 | 19.6 | skipped_fast |
| RWAUSDT | IDLE | 0.85 | 1.48 | 1.45 | 0.01 | 52811.56 | 51.64 | skipped_fast |
| MNSRYUSDT | IDLE | 0.33 | 0.63 | 0.21 | -0.01 | 34553.05 | 63.64 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
