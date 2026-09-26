# Hulk DIGEST — 2026-09-26T01:49:24Z

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
| XRPUSDT | IDLE | 1.06 | 2.08 | 0.22 | 0.02 | 112540183.06 | 1.27 | skipped_fast |
| ETHUSDT | IDLE | 0.36 | 0.7 | 0.08 | 0.0 | 319174888.5 | 0.07 | skipped_fast |
| BTCUSDT | IDLE | 0.34 | 0.65 | 0.16 | -0.01 | 674848433.25 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.83 | 4.78 | 2.62 | 0.07 | 1255526.49 | 4.09 | skipped_fast |
| CCUSDT | IDLE | 1.53 | 6.93 | 1.33 | 0.16 | 897019.43 | 10.5 | skipped_fast |
| WUSDT | IDLE | 1.91 | 3.62 | 1.82 | 0.05 | 457789.79 | 8.14 | skipped_fast |
| HBARUSDT | IDLE | 1.31 | 2.43 | 1.21 | 0.02 | 857053.58 | 2.11 | skipped_fast |
| CHIPUSDT | IDLE | 1.86 | 4.72 | 4.25 | 0.04 | 154430.6 | 22.63 | skipped_fast |
| ZBCNUSDT | IDLE | 1.3 | 2.91 | 2.25 | 0.05 | 248113.88 | 26.47 | skipped_fast |
| QNTUSDT | IDLE | 0.97 | 4.29 | 0.69 | 0.11 | 564897.68 | 5.99 | skipped_fast |
| KITEUSDT | IDLE | 1.6 | 3.54 | 0.15 | 0.07 | 78887.95 | 11.77 | skipped_fast |
| BIOUSDT | IDLE | 1.15 | 3.32 | 1.86 | 0.07 | 112760.07 | 3.06 | skipped_fast |
| EDELUSDT | IDLE | 0.78 | 1.5 | 0.34 | -0.0 | 182891.04 | 6.76 | skipped_fast |
| REDUSDT | IDLE | 0.84 | 1.83 | 0.85 | 0.07 | 111778.07 | 13.78 | skipped_fast |
| RIZEUSDT | IDLE | 0.25 | 3.9 | 0.18 | 0.04 | 93822.31 | 33.67 | skipped_fast |
| TELUSDT | IDLE | 1.11 | 1.96 | 1.74 | -0.01 | 111801.2 | 12.25 | skipped_fast |
| RWAINCUSDT | IDLE | 0.42 | 1.27 | 0.75 | -0.08 | 13283.08 | 65.94 | skipped_fast |
| RWAUSDT | IDLE | 0.68 | 1.26 | 0.66 | -0.01 | 53434.76 | 22.16 | skipped_fast |
| MNSRYUSDT | IDLE | 0.57 | 1.02 | 0.75 | 0.02 | 41452.25 | 10.18 | skipped_fast |
| FLUIDUSDT | IDLE | 0.21 | 0.36 | 0.36 | 0.02 | 3296.62 | 21.42 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
