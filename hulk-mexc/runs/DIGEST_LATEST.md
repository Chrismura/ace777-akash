# Hulk DIGEST — 2026-10-28T13:35:17Z

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
| ETHUSDT | IDLE | 1.27 | 2.25 | 1.97 | 0.01 | 236722967.86 | 0.3 | skipped_fast |
| XRPUSDT | IDLE | 1.14 | 2.04 | 1.63 | 0.01 | 19955658.91 | 1.52 | skipped_fast |
| BTCUSDT | IDLE | 0.85 | 1.51 | 1.32 | 0.01 | 311564884.8 | 0.1 | skipped_fast |
| CCUSDT | WATCH_PULLBACK — tension haute + reflux | 4.54 | 9.68 | 8.64 | -0.03 | 355487.86 | 10.45 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.5 | 11.76 | 9.77 | -0.01 | 179629.33 | 19.37 | skipped_fast |
| RWAINCUSDT | IDLE | 4.14 | 10.56 | 2.42 | 0.06 | 47158.19 | 6.36 | skipped_fast |
| WUSDT | IDLE | 1.4 | 2.52 | 1.93 | -0.01 | 579761.47 | 14.2 | skipped_fast |
| PYTHUSDT | IDLE | 1.4 | 2.52 | 1.81 | -0.02 | 426315.92 | 1.4 | skipped_fast |
| QNTUSDT | IDLE | 2.47 | 4.45 | 3.28 | -0.01 | 454909.27 | 6.1 | skipped_fast |
| ZBCNUSDT | IDLE | 2.08 | 3.94 | 2.64 | -0.04 | 229106.91 | 10.21 | skipped_fast |
| EDELUSDT | IDLE | 1.48 | 2.58 | 2.51 | -0.01 | 255600.18 | 21.7 | skipped_fast |
| HBARUSDT | IDLE | 1.27 | 2.26 | 1.91 | -0.01 | 461505.88 | 5.3 | skipped_fast |
| BIOUSDT | IDLE | 1.42 | 2.5 | 2.22 | 0.02 | 87105.19 | 8.92 | skipped_fast |
| KITEUSDT | IDLE | 0.98 | 1.72 | 1.55 | -0.03 | 59852.42 | 12.16 | skipped_fast |
| REDUSDT | IDLE | 0.79 | 1.38 | 1.33 | 0.01 | 52934.65 | 14.56 | skipped_fast |
| RIZEUSDT | IDLE | 1.01 | 1.79 | 1.49 | 0.02 | 36396.83 | 66.34 | skipped_fast |
| IOTAUSDT | IDLE | 1.56 | 2.78 | 2.21 | -0.0 | 76369.51 | 24.01 | skipped_fast |
| LAUSDT | IDLE | 1.31 | 2.28 | 2.22 | 0.01 | 59742.01 | 22.35 | skipped_fast |
| WAXLUSDT | IDLE | 1.38 | 2.45 | 2.02 | -0.02 | 56037.47 | 35.13 | skipped_fast |
| FLUIDUSDT | IDLE | 0.67 | 1.84 | 1.81 | 0.01 | 6424.69 | 21.41 | skipped_fast |
| RWAUSDT | IDLE | 0.67 | 1.29 | 0.32 | 0.01 | 54381.08 | 39.76 | skipped_fast |
| MNSRYUSDT | IDLE | 0.64 | 1.25 | 0.19 | 0.01 | 36399.01 | 54.03 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
