# Hulk DIGEST — 2026-09-22T20:15:50Z

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
| XRPUSDT | IDLE | 2.17 | 4.05 | 1.98 | 0.04 | 122220512.06 | 2.54 | skipped_fast |
| PYTHUSDT | IDLE | 0.88 | 4.01 | 2.73 | 0.03 | 1666408.0 | 3.04 | skipped_fast |
| ETHUSDT | IDLE | 0.66 | 1.24 | 0.49 | -0.01 | 441315017.56 | 0.58 | skipped_fast |
| HBARUSDT | IDLE | 2.32 | 5.48 | 0.37 | 0.09 | 1589358.61 | 2.01 | skipped_fast |
| BTCUSDT | IDLE | 0.4 | 0.71 | 0.56 | -0.01 | 940788243.44 | 0.0 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.42 | 14.88 | 8.86 | -0.0 | 288153.04 | 32.57 | skipped_fast |
| CCUSDT | IDLE | 2.02 | 3.72 | 2.1 | -0.03 | 492589.25 | 10.55 | skipped_fast |
| RWAINCUSDT | IDLE | 3.73 | 9.63 | 3.43 | 0.1 | 26254.71 | 46.89 | skipped_fast |
| ZBCNUSDT | IDLE | 2.54 | 4.6 | 3.23 | -0.02 | 218702.08 | 29.81 | skipped_fast |
| WUSDT | IDLE | 1.58 | 2.81 | 2.33 | 0.01 | 356200.96 | 5.89 | skipped_fast |
| CHIPUSDT | IDLE | 2.13 | 3.97 | 3.48 | -0.05 | 140371.32 | 13.33 | skipped_fast |
| RIZEUSDT | IDLE | 1.73 | 19.63 | 8.18 | -0.17 | 44209.22 | 109.19 | skipped_fast |
| BIOUSDT | IDLE | 1.74 | 3.23 | 1.71 | 0.02 | 139505.58 | 10.26 | skipped_fast |
| TELUSDT | IDLE | 2.15 | 6.87 | 0.0 | 0.07 | 104848.79 | 5.59 | skipped_fast |
| KITEUSDT | IDLE | 0.83 | 3.77 | 0.46 | 0.18 | 116203.71 | 9.34 | skipped_fast |
| REDUSDT | IDLE | 1.15 | 2.15 | 0.94 | 0.04 | 64292.78 | 14.61 | skipped_fast |
| QNTUSDT | IDLE | 0.9 | 2.7 | 1.96 | 0.08 | 187036.09 | 5.54 | skipped_fast |
| RWAUSDT | IDLE | 0.63 | 1.24 | 0.14 | 0.0 | 54268.92 | 21.7 | skipped_fast |
| FLUIDUSDT | IDLE | 0.7 | 1.33 | 0.45 | 0.01 | 7765.95 | 21.26 | skipped_fast |
| MNSRYUSDT | IDLE | 0.05 | 0.08 | 0.08 | 0.0 | 40232.03 | 9.02 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
