# Hulk DIGEST — 2026-09-22T20:15:09Z

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
| XRPUSDT | IDLE | 2.18 | 4.05 | 2.01 | 0.04 | 122337871.9 | 2.54 | skipped_fast |
| PYTHUSDT | IDLE | 0.88 | 4.01 | 2.76 | 0.03 | 1665442.04 | 4.56 | skipped_fast |
| ETHUSDT | IDLE | 0.66 | 1.24 | 0.51 | -0.01 | 441413063.61 | 0.07 | skipped_fast |
| HBARUSDT | IDLE | 2.33 | 5.48 | 0.6 | 0.09 | 1588858.66 | 2.01 | skipped_fast |
| BTCUSDT | IDLE | 0.4 | 0.71 | 0.57 | -0.01 | 940865363.49 | 0.0 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.42 | 14.88 | 8.86 | -0.0 | 288155.24 | 32.56 | skipped_fast |
| CCUSDT | IDLE | 2.02 | 3.72 | 2.14 | -0.03 | 492610.04 | 3.52 | skipped_fast |
| RWAINCUSDT | IDLE | 3.73 | 9.63 | 3.43 | 0.1 | 26254.71 | 46.89 | skipped_fast |
| ZBCNUSDT | IDLE | 2.54 | 4.6 | 3.22 | -0.02 | 218992.41 | 29.31 | skipped_fast |
| WUSDT | IDLE | 1.58 | 2.81 | 2.35 | 0.01 | 356197.29 | 2.53 | skipped_fast |
| CHIPUSDT | IDLE | 2.14 | 3.97 | 3.61 | -0.05 | 140337.28 | 20.04 | skipped_fast |
| RIZEUSDT | IDLE | 1.73 | 19.63 | 8.18 | -0.17 | 44205.13 | 109.19 | skipped_fast |
| BIOUSDT | IDLE | 1.75 | 3.23 | 1.82 | 0.02 | 139538.86 | 10.27 | skipped_fast |
| TELUSDT | IDLE | 2.15 | 6.87 | 0.0 | 0.07 | 104905.17 | 5.59 | skipped_fast |
| KITEUSDT | IDLE | 0.83 | 3.77 | 0.35 | 0.18 | 116208.38 | 7.9 | skipped_fast |
| REDUSDT | IDLE | 1.16 | 2.15 | 1.08 | 0.04 | 64308.87 | 15.89 | skipped_fast |
| QNTUSDT | IDLE | 0.9 | 2.7 | 1.96 | 0.07 | 187021.64 | 5.55 | skipped_fast |
| RWAUSDT | IDLE | 0.64 | 1.24 | 0.22 | 0.0 | 54294.07 | 21.7 | skipped_fast |
| FLUIDUSDT | IDLE | 0.7 | 1.33 | 0.45 | 0.01 | 7765.95 | 21.27 | skipped_fast |
| MNSRYUSDT | IDLE | 0.04 | 0.08 | 0.01 | 0.0 | 40217.73 | 9.02 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
