# Hulk DIGEST — 2026-09-17T05:15:48Z

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
| XRPUSDT | IDLE | 0.82 | 1.49 | 1.05 | 0.0 | 55396953.31 | 2.31 | skipped_fast |
| ETHUSDT | IDLE | 0.68 | 1.33 | 0.19 | 0.02 | 385824712.97 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.47 | 0.89 | 0.37 | 0.01 | 514472403.75 | 0.0 | skipped_fast |
| CCUSDT | IDLE | 1.98 | 7.04 | 5.1 | 0.07 | 576337.87 | 7.17 | skipped_fast |
| PYTHUSDT | IDLE | 1.97 | 3.82 | 0.84 | 0.02 | 510545.28 | 1.84 | skipped_fast |
| EDELUSDT | IDLE | 2.21 | 5.25 | 3.87 | 0.02 | 259467.04 | 31.0 | skipped_fast |
| ZBCNUSDT | IDLE | 2.31 | 4.35 | 1.79 | 0.02 | 171343.46 | 19.03 | skipped_fast |
| WUSDT | IDLE | 1.63 | 3.06 | 1.44 | 0.02 | 225962.28 | 2.17 | skipped_fast |
| RIZEUSDT | IDLE | 1.72 | 16.51 | 11.5 | -0.01 | 61215.59 | 82.09 | skipped_fast |
| CHIPUSDT | IDLE | 2.02 | 4.48 | 2.79 | -0.03 | 80942.9 | 16.43 | skipped_fast |
| REDUSDT | IDLE | 1.85 | 3.35 | 2.4 | -0.03 | 60452.17 | 8.46 | skipped_fast |
| KITEUSDT | IDLE | 1.22 | 4.49 | 0.49 | 0.07 | 66684.32 | 11.04 | skipped_fast |
| BIOUSDT | IDLE | 1.01 | 1.88 | 0.94 | 0.02 | 77689.14 | 11.88 | skipped_fast |
| RWAINCUSDT | IDLE | 1.06 | 2.0 | 0.81 | -0.02 | 19857.53 | 23.13 | skipped_fast |
| HBARUSDT | IDLE | 0.74 | 1.38 | 0.69 | -0.01 | 320879.4 | 1.35 | skipped_fast |
| QNTUSDT | IDLE | 0.81 | 1.47 | 0.96 | -0.0 | 37849.87 | 4.94 | skipped_fast |
| TELUSDT | IDLE | 0.7 | 1.32 | 0.55 | -0.02 | 115753.55 | 55.36 | skipped_fast |
| MNSRYUSDT | IDLE | 0.75 | 1.45 | 0.35 | 0.01 | 35323.94 | 29.56 | skipped_fast |
| RWAUSDT | IDLE | 0.51 | 0.98 | 0.22 | 0.02 | 55992.42 | 44.88 | skipped_fast |
| FLUIDUSDT | IDLE | 0.0 | 0.0 | 0.0 | -0.02 | 1571.52 | 21.98 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
