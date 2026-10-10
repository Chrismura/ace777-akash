# Hulk DIGEST — 2026-10-10T18:55:42Z

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
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 3.18 | 10.11 | 6.66 | 0.03 | 1220671.53 | 6.22 | skipped_fast |
| ETHUSDT | IDLE | 0.43 | 0.84 | 0.17 | 0.01 | 91878661.09 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.39 | 0.7 | 0.58 | 0.01 | 14410206.84 | 2.14 | skipped_fast |
| BTCUSDT | IDLE | 0.24 | 0.46 | 0.14 | 0.01 | 175943980.15 | 0.0 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 3.68 | 6.57 | 5.32 | -0.01 | 1135272.07 | 1.24 | skipped_fast |
| CHIPUSDT | IDLE | 3.38 | 24.51 | 3.21 | 0.25 | 156368.07 | 16.16 | skipped_fast |
| PYTHUSDT | IDLE | 1.23 | 2.34 | 0.83 | -0.02 | 835478.22 | 1.27 | skipped_fast |
| CCUSDT | IDLE | 1.49 | 2.64 | 2.33 | -0.04 | 334983.87 | 5.92 | skipped_fast |
| EDELUSDT | IDLE | 1.66 | 3.39 | 2.28 | -0.05 | 224087.12 | 2.62 | skipped_fast |
| BIOUSDT | IDLE | 1.83 | 3.46 | 1.35 | 0.05 | 87749.28 | 23.95 | skipped_fast |
| ZBCNUSDT | IDLE | 1.03 | 1.96 | 0.7 | 0.01 | 201107.75 | 12.63 | skipped_fast |
| RWAINCUSDT | IDLE | 2.23 | 4.24 | 1.45 | -0.03 | 9591.46 | 63.87 | skipped_fast |
| KITEUSDT | IDLE | 1.19 | 3.16 | 1.7 | 0.09 | 71934.97 | 10.78 | skipped_fast |
| TELUSDT | IDLE | 2.24 | 4.09 | 2.62 | -0.03 | 131187.32 | 39.23 | skipped_fast |
| HBARUSDT | IDLE | 0.87 | 1.55 | 1.32 | 0.02 | 341031.25 | 2.16 | skipped_fast |
| REDUSDT | IDLE | 0.66 | 1.21 | 0.68 | 0.02 | 54451.04 | 15.94 | skipped_fast |
| RIZEUSDT | IDLE | 0.52 | 1.16 | 0.85 | -0.01 | 43472.35 | 39.86 | skipped_fast |
| FLUIDUSDT | IDLE | 0.88 | 2.85 | 0.02 | 0.03 | 14842.99 | 21.48 | skipped_fast |
| RWAUSDT | IDLE | 0.4 | 0.71 | 0.63 | 0.0 | 54288.42 | 15.75 | skipped_fast |
| MNSRYUSDT | IDLE | 0.14 | 0.26 | 0.12 | 0.0 | 38505.02 | 13.53 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
