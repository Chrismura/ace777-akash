# Hulk DIGEST — 2026-10-29T03:47:31Z

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
| XRPUSDT | IDLE | 1.93 | 3.38 | 3.14 | -0.04 | 23858902.74 | 1.55 | skipped_fast |
| ETHUSDT | IDLE | 1.79 | 3.19 | 2.57 | -0.03 | 230718586.17 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 1.21 | 2.13 | 1.92 | -0.02 | 332577969.03 | 0.0 | skipped_fast |
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 3.82 | 6.74 | 6.01 | -0.05 | 471667.36 | 2.86 | skipped_fast |
| WUSDT | IDLE | 2.87 | 5.15 | 3.94 | -0.04 | 457676.89 | 16.25 | skipped_fast |
| CCUSDT | IDLE | 2.65 | 5.7 | 4.75 | -0.03 | 450866.16 | 6.21 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 3.66 | 6.45 | 5.75 | -0.04 | 452206.41 | 2.62 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 3.52 | 6.27 | 5.12 | -0.04 | 93200.03 | 9.14 | skipped_fast |
| HBARUSDT | IDLE | 2.33 | 4.15 | 3.37 | -0.05 | 608590.78 | 6.82 | skipped_fast |
| KITEUSDT | IDLE | 2.55 | 4.48 | 4.1 | -0.05 | 60332.34 | 12.48 | skipped_fast |
| ZBCNUSDT | IDLE | 1.84 | 3.31 | 2.51 | -0.02 | 268445.65 | 30.66 | skipped_fast |
| EDELUSDT | IDLE | 2.14 | 3.78 | 3.3 | -0.05 | 164358.06 | 19.15 | skipped_fast |
| WAXLUSDT | WATCH_PULLBACK — tension haute + reflux | 3.99 | 7.05 | 6.22 | -0.06 | 52933.52 | 56.13 | skipped_fast |
| CHIPUSDT | IDLE | 1.16 | 5.29 | 4.32 | -0.12 | 234138.33 | 8.36 | skipped_fast |
| IOTAUSDT | IDLE | 2.98 | 5.23 | 4.8 | -0.06 | 103562.51 | 9.98 | skipped_fast |
| REDUSDT | IDLE | 1.41 | 2.46 | 2.4 | -0.03 | 62805.5 | 9.42 | skipped_fast |
| RWAINCUSDT | IDLE | 1.17 | 4.49 | 2.91 | -0.05 | 31314.94 | 14.36 | skipped_fast |
| FLUIDUSDT | IDLE | 2.74 | 4.79 | 4.56 | -0.04 | 5952.1 | 21.26 | skipped_fast |
| LAUSDT | IDLE | 2.3 | 4.11 | 3.32 | -0.05 | 55041.23 | 22.91 | skipped_fast |
| RIZEUSDT | IDLE | 0.81 | 1.53 | 0.8 | -0.03 | 39165.69 | 64.28 | skipped_fast |
| RWAUSDT | IDLE | 0.86 | 1.53 | 1.27 | 0.0 | 55275.66 | 32.08 | skipped_fast |
| MNSRYUSDT | IDLE | 0.88 | 1.58 | 1.14 | 0.0 | 36497.09 | 56.07 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
