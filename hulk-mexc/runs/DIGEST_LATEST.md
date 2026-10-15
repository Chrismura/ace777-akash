# Hulk DIGEST — 2026-10-15T22:18:14Z

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
| WUSDT | IDLE | 1.3 | 3.68 | 2.0 | -0.04 | 2893064.96 | 6.12 | skipped_fast |
| PYTHUSDT | IDLE | 0.89 | 5.32 | 1.72 | 0.11 | 4452494.3 | 3.16 | skipped_fast |
| BTCUSDT | IDLE | 0.81 | 1.59 | 0.21 | 0.01 | 502361048.13 | 0.0 | skipped_fast |
| ETHUSDT | IDLE | 0.75 | 1.47 | 0.22 | 0.02 | 313188104.4 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.51 | 0.95 | 0.46 | 0.01 | 47940103.62 | 2.24 | skipped_fast |
| QNTUSDT | IDLE | 1.36 | 3.97 | 3.52 | 0.01 | 1359001.09 | 6.8 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.77 | 10.86 | 7.5 | -0.11 | 237584.28 | 88.14 | skipped_fast |
| CCUSDT | IDLE | 1.29 | 2.98 | 1.83 | -0.07 | 460904.8 | 7.47 | skipped_fast |
| ZBCNUSDT | IDLE | 1.65 | 3.22 | 2.79 | 0.01 | 216991.49 | 30.23 | skipped_fast |
| RIZEUSDT | IDLE | 2.04 | 8.01 | 2.58 | 0.03 | 82600.31 | 47.18 | skipped_fast |
| RWAINCUSDT | IDLE | 1.82 | 3.81 | 2.56 | 0.02 | 28810.3 | 4.97 | skipped_fast |
| CHIPUSDT | IDLE | 0.82 | 4.2 | 0.52 | -0.09 | 153289.58 | 14.72 | skipped_fast |
| KITEUSDT | IDLE | 1.21 | 2.2 | 1.61 | -0.03 | 69025.16 | 10.49 | skipped_fast |
| HBARUSDT | IDLE | 1.48 | 2.88 | 0.58 | 0.01 | 300337.28 | 10.58 | skipped_fast |
| REDUSDT | IDLE | 0.77 | 2.22 | 2.15 | -0.0 | 72819.03 | 13.44 | skipped_fast |
| BIOUSDT | IDLE | 0.56 | 1.33 | 0.35 | -0.02 | 84519.58 | 7.73 | skipped_fast |
| RWAUSDT | IDLE | 0.96 | 1.76 | 1.1 | 0.01 | 55153.02 | 15.86 | skipped_fast |
| TELUSDT | IDLE | 1.0 | 1.94 | 0.39 | 0.01 | 91461.21 | 39.29 | skipped_fast |
| FLUIDUSDT | IDLE | 0.98 | 2.38 | 0.85 | -0.04 | 8879.41 | 21.46 | skipped_fast |
| MNSRYUSDT | IDLE | 0.18 | 0.35 | 0.11 | 0.0 | 34574.55 | 8.46 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
