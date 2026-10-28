# Hulk DIGEST — 2026-10-28T08:29:51Z

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
| XRPUSDT | IDLE | 0.83 | 1.54 | 0.77 | 0.02 | 20014737.57 | 0.75 | skipped_fast |
| ETHUSDT | IDLE | 0.6 | 1.18 | 0.14 | 0.03 | 241338159.82 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.39 | 0.77 | 0.04 | 0.02 | 293234948.32 | 0.0 | skipped_fast |
| WUSDT | IDLE | 0.64 | 1.36 | 0.28 | 0.04 | 620601.58 | 19.39 | skipped_fast |
| EDELUSDT | IDLE | 1.58 | 2.81 | 2.29 | 0.01 | 346513.23 | 24.66 | skipped_fast |
| PYTHUSDT | IDLE | 1.22 | 2.23 | 1.37 | -0.01 | 377759.89 | 6.9 | skipped_fast |
| QNTUSDT | IDLE | 1.34 | 2.45 | 1.48 | -0.04 | 541451.59 | 5.03 | skipped_fast |
| CCUSDT | IDLE | 1.1 | 2.18 | 0.09 | 0.03 | 260380.93 | 5.97 | skipped_fast |
| RIZEUSDT | IDLE | 2.47 | 4.52 | 2.86 | 0.03 | 36199.77 | 63.84 | skipped_fast |
| ZBCNUSDT | IDLE | 1.33 | 2.55 | 1.76 | -0.06 | 214225.69 | 30.54 | skipped_fast |
| CHIPUSDT | IDLE | 1.38 | 3.45 | 2.74 | 0.04 | 123500.32 | 14.8 | skipped_fast |
| HBARUSDT | IDLE | 0.96 | 1.79 | 0.87 | 0.0 | 401971.57 | 6.53 | skipped_fast |
| RWAINCUSDT | IDLE | 1.13 | 2.05 | 1.41 | -0.06 | 57767.13 | 6.82 | skipped_fast |
| KITEUSDT | IDLE | 0.91 | 1.64 | 1.26 | 0.03 | 60920.74 | 9.41 | skipped_fast |
| BIOUSDT | IDLE | 0.81 | 1.55 | 0.52 | 0.03 | 83852.77 | 8.76 | skipped_fast |
| REDUSDT | IDLE | 0.82 | 1.64 | 1.26 | 0.04 | 58154.12 | 8.5 | skipped_fast |
| IOTAUSDT | IDLE | 1.16 | 2.09 | 1.47 | 0.01 | 72924.82 | 30.71 | skipped_fast |
| LAUSDT | IDLE | 0.87 | 1.75 | 0.5 | 0.05 | 59373.39 | 25.23 | skipped_fast |
| RWAUSDT | IDLE | 0.49 | 0.88 | 0.64 | 0.01 | 55792.78 | 8.02 | skipped_fast |
| WAXLUSDT | IDLE | 0.86 | 1.63 | 0.57 | -0.0 | 56712.68 | 51.21 | skipped_fast |
| MNSRYUSDT | IDLE | 0.73 | 1.39 | 0.45 | 0.0 | 35580.98 | 55.48 | skipped_fast |
| FLUIDUSDT | IDLE | 0.4 | 1.19 | 0.72 | -0.0 | 7682.58 | 21.69 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
