# Hulk DIGEST — 2026-09-06T13:32:02Z

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
| XRPUSDT | IDLE | 0.55 | 0.96 | 0.9 | -0.0 | 25460019.3 | 2.12 | skipped_fast |
| ETHUSDT | IDLE | 0.34 | 0.6 | 0.57 | 0.01 | 231186193.44 | 0.2 | skipped_fast |
| BTCUSDT | IDLE | 0.19 | 0.33 | 0.27 | 0.0 | 398934595.17 | 0.0 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.66 | 6.82 | 6.08 | 0.03 | 402687.4 | 1.73 | skipped_fast |
| PYTHUSDT | IDLE | 1.5 | 2.65 | 2.31 | 0.0 | 455009.0 | 1.82 | skipped_fast |
| WUSDT | IDLE | 2.4 | 4.58 | 1.4 | 0.04 | 236759.56 | 13.53 | skipped_fast |
| RIZEUSDT | IDLE | 1.92 | 10.46 | 9.23 | -0.08 | 73994.09 | 53.14 | skipped_fast |
| RWAINCUSDT | IDLE | 2.47 | 5.39 | 2.51 | 0.05 | 6374.45 | 10.28 | skipped_fast |
| CCUSDT | IDLE | 0.98 | 1.72 | 1.54 | -0.0 | 326087.37 | 5.47 | skipped_fast |
| ZBCNUSDT | IDLE | 1.39 | 2.48 | 2.06 | -0.01 | 197347.53 | 12.76 | skipped_fast |
| EDELUSDT | IDLE | 1.97 | 3.61 | 2.2 | 0.0 | 68262.92 | 18.76 | skipped_fast |
| REDUSDT | IDLE | 1.71 | 3.15 | 1.76 | 0.03 | 62225.6 | 10.11 | skipped_fast |
| KITEUSDT | IDLE | 1.54 | 2.75 | 2.14 | -0.0 | 61779.16 | 10.27 | skipped_fast |
| HBARUSDT | IDLE | 0.68 | 1.19 | 1.13 | -0.01 | 453130.08 | 3.71 | skipped_fast |
| BIOUSDT | IDLE | 0.77 | 1.38 | 1.07 | -0.0 | 91677.2 | 3.61 | skipped_fast |
| TELUSDT | IDLE | 0.92 | 1.65 | 1.27 | 0.0 | 67618.24 | 23.45 | skipped_fast |
| QNTUSDT | IDLE | 0.7 | 1.25 | 1.03 | 0.02 | 38223.01 | 4.58 | skipped_fast |
| MNSRYUSDT | IDLE | 0.58 | 1.08 | 0.57 | 0.02 | 42242.51 | 14.77 | skipped_fast |
| RWAUSDT | IDLE | 0.48 | 0.86 | 0.64 | -0.01 | 52083.67 | 21.44 | skipped_fast |
| FLUIDUSDT | IDLE | 0.0 | 0.0 | 0.0 | 0.02 | 353.17 | 21.98 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
