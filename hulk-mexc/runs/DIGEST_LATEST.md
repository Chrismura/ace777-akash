# Hulk DIGEST — 2026-09-23T00:16:00Z

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
| XRPUSDT | IDLE | 1.88 | 3.48 | 1.89 | 0.03 | 105575298.31 | 1.9 | skipped_fast |
| PYTHUSDT | IDLE | 0.75 | 3.76 | 0.13 | 0.06 | 1716671.81 | 2.96 | skipped_fast |
| ETHUSDT | IDLE | 0.74 | 1.4 | 0.59 | -0.01 | 423809039.16 | 0.11 | skipped_fast |
| HBARUSDT | IDLE | 1.46 | 3.58 | 1.42 | 0.07 | 1742335.05 | 1.01 | skipped_fast |
| BTCUSDT | IDLE | 0.37 | 0.69 | 0.28 | -0.0 | 897837847.68 | 0.0 | skipped_fast |
| RIZEUSDT | IDLE | 2.35 | 39.3 | 6.49 | 0.16 | 49784.74 | 97.01 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 3.64 | 9.03 | 5.86 | 0.02 | 20090.81 | 5.38 | skipped_fast |
| WUSDT | IDLE | 2.06 | 4.04 | 0.59 | 0.03 | 316906.01 | 7.33 | skipped_fast |
| CCUSDT | IDLE | 1.33 | 2.57 | 0.63 | -0.03 | 465740.13 | 8.69 | skipped_fast |
| CHIPUSDT | IDLE | 2.73 | 5.6 | 1.08 | 0.01 | 139916.24 | 14.96 | skipped_fast |
| EDELUSDT | IDLE | 1.56 | 7.18 | 5.76 | -0.03 | 257872.39 | 33.99 | skipped_fast |
| BIOUSDT | IDLE | 1.62 | 3.22 | 0.1 | 0.03 | 135980.37 | 13.31 | skipped_fast |
| ZBCNUSDT | IDLE | 0.88 | 1.74 | 0.1 | -0.01 | 206639.9 | 36.94 | skipped_fast |
| REDUSDT | IDLE | 1.11 | 2.17 | 0.34 | 0.04 | 63799.86 | 8.76 | skipped_fast |
| KITEUSDT | IDLE | 0.62 | 2.75 | 0.64 | 0.17 | 114005.11 | 10.04 | skipped_fast |
| QNTUSDT | IDLE | 1.36 | 4.66 | 0.36 | 0.12 | 208877.75 | 5.35 | skipped_fast |
| TELUSDT | IDLE | 1.35 | 5.33 | 2.53 | 0.1 | 103579.66 | 44.2 | skipped_fast |
| RWAUSDT | IDLE | 0.45 | 0.87 | 0.22 | 0.0 | 53210.22 | 14.42 | skipped_fast |
| FLUIDUSDT | IDLE | 0.44 | 0.86 | 0.13 | 0.01 | 5612.51 | 21.63 | skipped_fast |
| MNSRYUSDT | IDLE | 0.03 | 0.06 | 0.0 | -0.01 | 39708.62 | 9.02 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
