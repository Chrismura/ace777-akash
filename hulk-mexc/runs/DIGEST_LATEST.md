# Hulk DIGEST — 2026-10-17T23:23:24Z

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
| ETHUSDT | IDLE | 1.49 | 2.79 | 1.22 | -0.01 | 87905975.79 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 1.46 | 2.74 | 1.22 | -0.02 | 17023122.27 | 0.77 | skipped_fast |
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 3.15 | 9.68 | 5.82 | -0.09 | 1071668.74 | 1.26 | skipped_fast |
| BTCUSDT | IDLE | 0.56 | 1.06 | 0.46 | -0.01 | 177060100.12 | 0.0 | skipped_fast |
| WUSDT | IDLE | 1.93 | 5.68 | 3.73 | -0.04 | 975959.89 | 16.03 | skipped_fast |
| QNTUSDT | IDLE | 2.92 | 5.39 | 3.01 | -0.03 | 605425.27 | 2.57 | skipped_fast |
| BIOUSDT | IDLE | 2.32 | 4.41 | 1.58 | -0.04 | 75401.93 | 4.13 | skipped_fast |
| CHIPUSDT | IDLE | 2.1 | 5.85 | 3.23 | -0.07 | 84322.67 | 11.66 | skipped_fast |
| CCUSDT | IDLE | 1.48 | 2.74 | 1.45 | -0.0 | 260879.67 | 8.68 | skipped_fast |
| ZBCNUSDT | IDLE | 1.71 | 3.07 | 2.27 | -0.02 | 188945.33 | 8.45 | skipped_fast |
| EDELUSDT | IDLE | 1.52 | 2.68 | 2.37 | -0.05 | 150247.0 | 7.13 | skipped_fast |
| REDUSDT | IDLE | 1.86 | 3.41 | 2.06 | -0.05 | 62026.39 | 9.38 | skipped_fast |
| KITEUSDT | IDLE | 1.66 | 4.14 | 2.69 | -0.05 | 68872.1 | 12.99 | skipped_fast |
| HBARUSDT | IDLE | 1.96 | 3.74 | 1.2 | 0.01 | 205992.96 | 5.9 | skipped_fast |
| RIZEUSDT | IDLE | 1.36 | 2.58 | 1.0 | -0.02 | 50289.3 | 25.18 | skipped_fast |
| TELUSDT | IDLE | 1.99 | 3.59 | 2.57 | -0.06 | 102646.16 | 6.13 | skipped_fast |
| RWAINCUSDT | IDLE | 1.08 | 3.53 | 3.2 | 0.06 | 20841.91 | 26.7 | skipped_fast |
| RWAUSDT | IDLE | 1.34 | 2.52 | 1.03 | -0.0 | 51676.98 | 16.0 | skipped_fast |
| FLUIDUSDT | IDLE | 1.42 | 2.69 | 0.97 | -0.01 | 1899.19 | 21.25 | skipped_fast |
| MNSRYUSDT | IDLE | 0.33 | 0.58 | 0.55 | -0.0 | 31277.67 | 12.72 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
