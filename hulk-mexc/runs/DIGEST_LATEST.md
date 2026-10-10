# Hulk DIGEST — 2026-10-10T10:38:58Z

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
| XRPUSDT | IDLE | 0.44 | 0.79 | 0.64 | 0.01 | 22397750.95 | 0.71 | skipped_fast |
| BTCUSDT | IDLE | 0.2 | 0.37 | 0.15 | 0.0 | 239050252.93 | 0.0 | skipped_fast |
| ETHUSDT | IDLE | 0.15 | 0.27 | 0.18 | 0.0 | 109163844.62 | 0.04 | skipped_fast |
| WUSDT | IDLE | 1.86 | 3.79 | 2.13 | -0.03 | 1293677.7 | 7.7 | skipped_fast |
| PYTHUSDT | IDLE | 1.07 | 2.92 | 2.51 | -0.06 | 1337078.59 | 1.28 | skipped_fast |
| QNTUSDT | IDLE | 1.96 | 3.57 | 2.33 | 0.02 | 1222060.3 | 2.83 | skipped_fast |
| EDELUSDT | IDLE | 2.47 | 7.89 | 2.46 | 0.1 | 243611.03 | 25.28 | skipped_fast |
| CCUSDT | IDLE | 1.16 | 2.08 | 1.65 | -0.0 | 472523.35 | 5.82 | skipped_fast |
| KITEUSDT | IDLE | 2.35 | 4.47 | 1.52 | 0.01 | 77371.4 | 11.17 | skipped_fast |
| ZBCNUSDT | IDLE | 0.72 | 1.51 | 0.39 | -0.06 | 262263.51 | 9.61 | skipped_fast |
| CHIPUSDT | IDLE | 1.17 | 3.78 | 2.81 | 0.08 | 99037.82 | 15.22 | skipped_fast |
| REDUSDT | IDLE | 1.46 | 2.64 | 1.85 | 0.02 | 55949.93 | 10.08 | skipped_fast |
| RWAINCUSDT | IDLE | 1.99 | 3.65 | 2.24 | 0.01 | 13251.17 | 63.74 | skipped_fast |
| BIOUSDT | IDLE | 1.03 | 1.82 | 1.55 | 0.02 | 71948.43 | 6.98 | skipped_fast |
| HBARUSDT | IDLE | 0.83 | 1.51 | 1.04 | 0.02 | 337580.56 | 5.41 | skipped_fast |
| RWAUSDT | IDLE | 1.66 | 2.92 | 2.61 | -0.01 | 53120.99 | 7.87 | skipped_fast |
| TELUSDT | IDLE | 1.64 | 2.95 | 2.23 | -0.02 | 115184.97 | 37.97 | skipped_fast |
| RIZEUSDT | IDLE | 0.32 | 1.72 | 0.87 | 0.1 | 64340.08 | 55.52 | skipped_fast |
| MNSRYUSDT | IDLE | 0.39 | 0.77 | 0.13 | 0.01 | 40724.75 | 4.05 | skipped_fast |
| FLUIDUSDT | IDLE | 0.24 | 1.42 | 1.05 | 0.01 | 17330.96 | 21.21 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
