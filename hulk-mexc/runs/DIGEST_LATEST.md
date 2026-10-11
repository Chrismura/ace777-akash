# Hulk DIGEST — 2026-10-11T22:29:27Z

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
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 3.05 | 27.54 | 6.15 | 0.25 | 4325092.84 | 8.22 | skipped_fast |
| XRPUSDT | IDLE | 1.0 | 1.84 | 1.04 | 0.0 | 15841449.24 | 2.13 | skipped_fast |
| ETHUSDT | IDLE | 0.79 | 1.47 | 0.73 | 0.01 | 214114392.46 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.58 | 1.07 | 0.62 | 0.01 | 153854309.76 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.35 | 4.34 | 2.42 | -0.01 | 913174.75 | 1.28 | skipped_fast |
| QNTUSDT | IDLE | 2.17 | 3.86 | 3.14 | -0.01 | 776898.24 | 1.26 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.0 | 18.15 | 12.6 | 0.01 | 39909.34 | 55.84 | skipped_fast |
| ZBCNUSDT | IDLE | 2.7 | 4.73 | 4.41 | -0.01 | 209519.72 | 3.5 | skipped_fast |
| EDELUSDT | IDLE | 1.6 | 2.88 | 2.13 | -0.01 | 377700.7 | 2.65 | skipped_fast |
| CCUSDT | IDLE | 1.65 | 3.32 | 1.9 | 0.05 | 354153.85 | 6.38 | skipped_fast |
| CHIPUSDT | IDLE | 1.08 | 4.13 | 3.42 | 0.0 | 284999.83 | 13.36 | skipped_fast |
| BIOUSDT | IDLE | 1.37 | 2.54 | 1.39 | 0.02 | 96080.06 | 3.35 | skipped_fast |
| TELUSDT | IDLE | 2.49 | 4.51 | 3.12 | -0.04 | 176012.91 | 29.27 | skipped_fast |
| RWAINCUSDT | IDLE | 1.23 | 3.21 | 3.01 | -0.01 | 28720.92 | 24.61 | skipped_fast |
| KITEUSDT | IDLE | 0.96 | 1.83 | 0.62 | -0.0 | 76058.08 | 8.62 | skipped_fast |
| HBARUSDT | IDLE | 1.15 | 2.13 | 1.09 | 0.01 | 302645.99 | 6.41 | skipped_fast |
| REDUSDT | IDLE | 0.91 | 1.63 | 1.29 | 0.0 | 57206.64 | 14.56 | skipped_fast |
| RWAUSDT | IDLE | 1.43 | 2.57 | 1.9 | 0.02 | 53155.18 | 7.74 | skipped_fast |
| MNSRYUSDT | IDLE | 0.69 | 1.24 | 0.88 | -0.01 | 33549.48 | 12.31 | skipped_fast |
| FLUIDUSDT | IDLE | 0.34 | 2.51 | 1.35 | 0.06 | 61764.44 | 20.87 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
