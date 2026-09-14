# Hulk DIGEST — 2026-09-14T23:44:09Z

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
| ETHUSDT | IDLE | 2.22 | 3.92 | 3.53 | 0.02 | 444503346.87 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 1.95 | 5.03 | 4.52 | 0.06 | 74757543.53 | 2.11 | skipped_fast |
| BTCUSDT | IDLE | 0.95 | 1.67 | 1.57 | 0.02 | 564625596.75 | 0.0 | skipped_fast |
| EDELUSDT | IDLE | 2.69 | 26.79 | 4.93 | 0.3 | 347052.13 | 40.33 | skipped_fast |
| ZBCNUSDT | IDLE | 2.5 | 4.79 | 1.36 | 0.03 | 210695.45 | 15.22 | skipped_fast |
| CCUSDT | IDLE | 1.68 | 2.98 | 2.53 | 0.02 | 310266.43 | 5.15 | skipped_fast |
| PYTHUSDT | IDLE | 1.06 | 1.92 | 1.39 | -0.01 | 399245.33 | 3.58 | skipped_fast |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.36 | 8.53 | 5.49 | 0.04 | 104878.18 | 24.48 | skipped_fast |
| WUSDT | IDLE | 1.63 | 2.92 | 2.33 | 0.02 | 209265.5 | 10.0 | skipped_fast |
| KITEUSDT | IDLE | 2.15 | 4.01 | 2.0 | 0.01 | 65248.22 | 12.13 | skipped_fast |
| BIOUSDT | IDLE | 1.5 | 2.72 | 1.89 | 0.03 | 99694.76 | 7.72 | skipped_fast |
| REDUSDT | IDLE | 0.89 | 3.09 | 1.83 | 0.09 | 189434.17 | 17.12 | skipped_fast |
| HBARUSDT | IDLE | 1.39 | 2.48 | 1.98 | 0.04 | 359239.95 | 1.29 | skipped_fast |
| CHIPUSDT | IDLE | 1.17 | 2.3 | 0.9 | 0.02 | 75969.86 | 16.71 | skipped_fast |
| RWAINCUSDT | IDLE | 0.78 | 1.5 | 0.38 | 0.0 | 5416.44 | 5.49 | skipped_fast |
| RIZEUSDT | IDLE | 0.41 | 4.78 | 1.87 | -0.04 | 56567.66 | 54.07 | skipped_fast |
| FLUIDUSDT | IDLE | 1.36 | 2.37 | 2.31 | 0.02 | 1523.93 | 15.2 | skipped_fast |
| QNTUSDT | IDLE | 0.92 | 1.82 | 0.17 | 0.03 | 43591.43 | 6.19 | skipped_fast |
| MNSRYUSDT | IDLE | 0.85 | 1.58 | 0.79 | 0.01 | 30838.0 | 46.92 | skipped_fast |
| RWAUSDT | IDLE | 0.58 | 1.05 | 0.67 | -0.0 | 55379.27 | 37.19 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
