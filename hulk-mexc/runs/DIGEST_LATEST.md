# Hulk DIGEST — 2026-09-12T09:18:47Z

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
| ETHUSDT | IDLE | 0.47 | 1.11 | 0.07 | 0.02 | 611614382.25 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.29 | 0.63 | 0.14 | 0.01 | 51148306.82 | 1.46 | skipped_fast |
| BTCUSDT | IDLE | 0.13 | 0.26 | 0.03 | 0.0 | 559753357.3 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.09 | 2.21 | 0.36 | 0.03 | 413251.92 | 1.89 | skipped_fast |
| CCUSDT | IDLE | 0.57 | 1.06 | 0.53 | -0.0 | 383541.57 | 8.1 | skipped_fast |
| KITEUSDT | IDLE | 1.59 | 2.88 | 1.99 | -0.03 | 60191.99 | 10.37 | skipped_fast |
| RWAINCUSDT | IDLE | 1.92 | 3.83 | 1.79 | 0.01 | 15864.22 | 38.6 | skipped_fast |
| ZBCNUSDT | IDLE | 0.77 | 1.5 | 0.2 | -0.0 | 213833.83 | 8.3 | skipped_fast |
| WUSDT | IDLE | 0.7 | 1.31 | 1.1 | 0.02 | 200071.65 | 12.3 | skipped_fast |
| CHIPUSDT | IDLE | 1.09 | 3.08 | 1.42 | 0.05 | 89340.79 | 14.64 | skipped_fast |
| EDELUSDT | IDLE | 0.87 | 2.5 | 0.7 | 0.06 | 169328.6 | 26.33 | skipped_fast |
| REDUSDT | IDLE | 0.95 | 2.4 | 1.71 | 0.05 | 65229.21 | 8.64 | skipped_fast |
| BIOUSDT | IDLE | 0.61 | 1.15 | 0.51 | 0.02 | 82204.24 | 7.87 | skipped_fast |
| RIZEUSDT | IDLE | 0.14 | 9.79 | 2.17 | 1.0 | 188671.82 | 98.01 | skipped_fast |
| HBARUSDT | IDLE | 0.42 | 0.78 | 0.37 | 0.0 | 248279.43 | 1.34 | skipped_fast |
| TELUSDT | IDLE | 0.72 | 1.73 | 1.11 | -0.03 | 100125.35 | 35.46 | skipped_fast |
| QNTUSDT | IDLE | 0.54 | 1.02 | 0.34 | -0.01 | 48498.92 | 10.89 | skipped_fast |
| MNSRYUSDT | IDLE | 0.58 | 1.1 | 0.43 | -0.0 | 27029.19 | 13.95 | skipped_fast |
| RWAUSDT | IDLE | 0.31 | 0.59 | 0.15 | 0.03 | 53346.34 | 7.4 | skipped_fast |
| FLUIDUSDT | IDLE | 0.0 | 0.0 | 0.0 | 0.03 | 1625.5 | 22.17 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
