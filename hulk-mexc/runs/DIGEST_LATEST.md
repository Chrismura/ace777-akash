# Hulk DIGEST — 2026-10-02T09:21:36Z

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
| QNTUSDT | IDLE | 2.28 | 15.33 | 9.21 | -0.2 | 6632056.04 | 9.82 | skipped_fast |
| XRPUSDT | IDLE | 1.27 | 2.49 | 0.29 | 0.03 | 46490018.84 | 0.65 | skipped_fast |
| ETHUSDT | IDLE | 1.21 | 2.3 | 0.86 | 0.02 | 415468776.73 | 0.07 | skipped_fast |
| BTCUSDT | IDLE | 0.9 | 1.68 | 0.77 | 0.03 | 761047077.61 | 0.0 | skipped_fast |
| ZBCNUSDT | IDLE | 2.92 | 8.56 | 4.7 | -0.02 | 294241.82 | 15.42 | skipped_fast |
| CCUSDT | IDLE | 1.5 | 2.85 | 1.05 | -0.02 | 563999.74 | 6.62 | skipped_fast |
| WUSDT | IDLE | 2.07 | 3.93 | 1.41 | 0.01 | 431097.71 | 9.54 | skipped_fast |
| PYTHUSDT | IDLE | 1.51 | 2.95 | 0.52 | -0.0 | 424133.79 | 2.59 | skipped_fast |
| BIOUSDT | IDLE | 2.42 | 4.69 | 0.98 | 0.02 | 85864.83 | 6.41 | skipped_fast |
| EDELUSDT | IDLE | 1.37 | 9.07 | 1.07 | 0.21 | 232648.02 | 14.62 | skipped_fast |
| HBARUSDT | IDLE | 1.14 | 2.24 | 0.25 | 0.0 | 613119.21 | 9.51 | skipped_fast |
| REDUSDT | IDLE | 1.69 | 3.1 | 1.9 | -0.05 | 63891.88 | 12.69 | skipped_fast |
| KITEUSDT | IDLE | 1.53 | 3.42 | 0.63 | 0.04 | 93682.17 | 8.72 | skipped_fast |
| CHIPUSDT | IDLE | 1.63 | 3.14 | 0.81 | 0.02 | 91275.5 | 20.42 | skipped_fast |
| TELUSDT | IDLE | 1.74 | 3.4 | 0.5 | -0.02 | 144345.72 | 22.94 | skipped_fast |
| RIZEUSDT | IDLE | 0.91 | 4.25 | 0.59 | 0.03 | 41240.55 | 51.21 | skipped_fast |
| FLUIDUSDT | IDLE | 2.11 | 6.96 | 0.2 | 0.1 | 5213.5 | 21.63 | skipped_fast |
| RWAINCUSDT | IDLE | 0.99 | 1.73 | 1.7 | -0.01 | 12641.15 | 54.59 | skipped_fast |
| MNSRYUSDT | IDLE | 0.86 | 1.65 | 0.41 | 0.02 | 37026.81 | 8.98 | skipped_fast |
| RWAUSDT | IDLE | 0.55 | 1.09 | 0.07 | 0.02 | 53936.21 | 21.62 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
