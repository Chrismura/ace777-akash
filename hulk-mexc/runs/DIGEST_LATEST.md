# Hulk DIGEST — 2026-08-31T08:09:03Z

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
| XRPUSDT | IDLE | 1.2 | 2.34 | 0.36 | -0.02 | 37973002.7 | 1.46 | skipped_fast |
| ETHUSDT | IDLE | 0.89 | 1.71 | 0.41 | -0.01 | 412162387.0 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.59 | 1.15 | 0.25 | -0.0 | 466637841.83 | 0.0 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.97 | 25.42 | 18.79 | 0.04 | 121446.44 | 24.84 | skipped_fast |
| CHIPUSDT | IDLE | 1.88 | 6.23 | 0.3 | 0.02 | 552750.89 | 4.96 | skipped_fast |
| PYTHUSDT | IDLE | 1.36 | 3.43 | 0.36 | -0.0 | 557201.96 | 2.11 | skipped_fast |
| ZBCNUSDT | IDLE | 1.73 | 5.3 | 3.35 | -0.08 | 228691.78 | 18.05 | skipped_fast |
| CCUSDT | IDLE | 1.52 | 2.9 | 0.89 | 0.01 | 220706.94 | 5.85 | skipped_fast |
| WUSDT | IDLE | 1.4 | 2.54 | 2.06 | 0.01 | 229303.9 | 8.61 | skipped_fast |
| REDUSDT | IDLE | 1.9 | 3.58 | 1.41 | 0.01 | 70274.61 | 19.91 | skipped_fast |
| BIOUSDT | IDLE | 1.36 | 2.68 | 0.37 | -0.02 | 86402.18 | 3.74 | skipped_fast |
| KITEUSDT | IDLE | 1.21 | 3.22 | 1.57 | -0.05 | 92404.88 | 10.7 | skipped_fast |
| FLUIDUSDT | IDLE | 2.51 | 5.02 | 0.0 | 0.03 | 3792.7 | 21.69 | skipped_fast |
| TELUSDT | IDLE | 2.21 | 4.18 | 1.61 | 0.02 | 93338.24 | 46.59 | skipped_fast |
| RIZEUSDT | IDLE | 1.1 | 2.01 | 1.24 | -0.03 | 36898.04 | 62.7 | skipped_fast |
| HBARUSDT | IDLE | 0.92 | 1.79 | 0.34 | -0.01 | 215057.37 | 1.35 | skipped_fast |
| QNTUSDT | IDLE | 1.12 | 2.19 | 0.34 | -0.01 | 38718.87 | 4.92 | skipped_fast |
| RWAINCUSDT | IDLE | 0.69 | 1.37 | 0.0 | 0.01 | 2256.88 | 96.4 | skipped_fast |
| RWAUSDT | IDLE | 0.55 | 1.06 | 0.32 | 0.01 | 53130.44 | 24.26 | skipped_fast |
| MNSRYUSDT | IDLE | 0.38 | 0.67 | 0.58 | -0.01 | 29745.02 | 28.49 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
