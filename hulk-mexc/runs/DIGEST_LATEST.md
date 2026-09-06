# Hulk DIGEST — 2026-09-06T01:28:57Z

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
| XRPUSDT | IDLE | 0.73 | 1.41 | 0.29 | 0.01 | 23765857.17 | 0.7 | skipped_fast |
| ETHUSDT | IDLE | 0.51 | 0.98 | 0.2 | 0.02 | 174362649.66 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.21 | 0.4 | 0.09 | 0.0 | 370199311.24 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.96 | 3.73 | 1.26 | 0.03 | 394237.13 | 8.97 | skipped_fast |
| CHIPUSDT | IDLE | 1.31 | 3.41 | 1.05 | 0.06 | 420580.18 | 6.74 | skipped_fast |
| RWAINCUSDT | IDLE | 2.97 | 5.2 | 4.95 | -0.02 | 8342.38 | 59.73 | skipped_fast |
| CCUSDT | IDLE | 1.32 | 2.52 | 0.79 | 0.03 | 285228.34 | 9.96 | skipped_fast |
| RIZEUSDT | IDLE | 1.7 | 11.01 | 4.15 | -0.08 | 127001.89 | 60.79 | skipped_fast |
| ZBCNUSDT | IDLE | 1.56 | 2.87 | 1.6 | -0.01 | 223928.58 | 25.93 | skipped_fast |
| WUSDT | IDLE | 1.67 | 3.34 | 0.04 | 0.05 | 163958.07 | 2.93 | skipped_fast |
| KITEUSDT | IDLE | 0.93 | 1.98 | 0.48 | -0.07 | 64501.71 | 10.19 | skipped_fast |
| BIOUSDT | IDLE | 0.76 | 1.44 | 0.57 | 0.03 | 83759.13 | 3.57 | skipped_fast |
| REDUSDT | IDLE | 0.84 | 1.68 | 0.06 | 0.04 | 59990.6 | 8.59 | skipped_fast |
| HBARUSDT | IDLE | 0.68 | 1.33 | 0.25 | 0.02 | 363826.81 | 1.24 | skipped_fast |
| EDELUSDT | IDLE | 0.24 | 3.05 | 2.68 | 0.01 | 116413.63 | 28.5 | skipped_fast |
| RWAUSDT | IDLE | 1.82 | 3.18 | 3.01 | 0.04 | 53207.56 | 14.1 | skipped_fast |
| TELUSDT | IDLE | 1.88 | 3.46 | 1.96 | -0.01 | 72750.22 | 58.82 | skipped_fast |
| QNTUSDT | IDLE | 0.99 | 1.98 | 0.0 | 0.03 | 36782.41 | 1.52 | skipped_fast |
| FLUIDUSDT | IDLE | 0.4 | 0.79 | 0.1 | 0.01 | 385.8 | 0.79 | skipped_fast |
| MNSRYUSDT | IDLE | 0.14 | 0.26 | 0.16 | 0.0 | 38836.74 | 20.48 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
