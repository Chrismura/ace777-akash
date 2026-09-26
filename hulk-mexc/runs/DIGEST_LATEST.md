# Hulk DIGEST — 2026-09-26T21:03:27Z

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
| XRPUSDT | IDLE | 1.9 | 3.42 | 2.52 | -0.03 | 40746938.45 | 0.66 | skipped_fast |
| ETHUSDT | IDLE | 0.6 | 1.1 | 0.62 | -0.0 | 116012354.98 | 0.07 | skipped_fast |
| BTCUSDT | IDLE | 0.21 | 0.4 | 0.16 | 0.0 | 330786944.35 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.35 | 6.03 | 2.32 | 0.07 | 1059752.15 | 8.9 | skipped_fast |
| QNTUSDT | IDLE | 1.31 | 8.9 | 3.45 | 0.23 | 1482094.76 | 9.97 | skipped_fast |
| CCUSDT | WATCH_PULLBACK — tension haute + reflux | 2.63 | 6.12 | 5.18 | 0.04 | 851251.8 | 10.51 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.48 | 10.33 | 8.18 | -0.02 | 107544.59 | 18.79 | skipped_fast |
| WUSDT | IDLE | 2.44 | 5.22 | 3.58 | 0.05 | 564340.5 | 18.03 | skipped_fast |
| RWAINCUSDT | IDLE | 3.8 | 13.77 | 4.25 | 0.04 | 10109.18 | 39.1 | skipped_fast |
| BIOUSDT | IDLE | 2.8 | 5.06 | 3.66 | -0.03 | 112348.88 | 6.29 | skipped_fast |
| ZBCNUSDT | IDLE | 2.81 | 5.06 | 3.75 | -0.03 | 196013.98 | 51.41 | skipped_fast |
| HBARUSDT | IDLE | 2.1 | 3.78 | 2.86 | -0.02 | 541311.35 | 1.08 | skipped_fast |
| EDELUSDT | IDLE | 2.5 | 4.42 | 3.82 | 0.02 | 169034.23 | 29.98 | skipped_fast |
| KITEUSDT | IDLE | 2.14 | 7.42 | 2.56 | 0.1 | 108668.85 | 8.85 | skipped_fast |
| REDUSDT | IDLE | 1.65 | 2.99 | 2.02 | -0.04 | 59511.52 | 13.74 | skipped_fast |
| RIZEUSDT | IDLE | 1.13 | 2.9 | 0.42 | 0.07 | 48742.7 | 39.45 | skipped_fast |
| TELUSDT | IDLE | 1.55 | 2.95 | 0.98 | -0.02 | 120702.92 | 67.88 | skipped_fast |
| FLUIDUSDT | IDLE | 1.31 | 2.29 | 2.21 | -0.01 | 763.76 | 21.71 | skipped_fast |
| RWAUSDT | IDLE | 0.67 | 1.23 | 0.78 | 0.03 | 56799.6 | 7.18 | skipped_fast |
| MNSRYUSDT | IDLE | 0.27 | 0.51 | 0.14 | -0.0 | 38733.95 | 16.57 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
