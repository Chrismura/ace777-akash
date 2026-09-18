# Hulk DIGEST — 2026-09-18T21:56:06Z

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
| XRPUSDT | IDLE | 1.24 | 2.92 | 0.88 | 0.08 | 64407200.69 | 0.71 | skipped_fast |
| ETHUSDT | IDLE | 1.26 | 2.6 | 0.7 | 0.07 | 616315466.19 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.52 | 1.0 | 0.22 | 0.06 | 748511024.06 | 0.0 | skipped_fast |
| WUSDT | IDLE | 1.88 | 6.58 | 4.64 | 0.1 | 883860.15 | 4.6 | skipped_fast |
| PYTHUSDT | IDLE | 1.17 | 2.89 | 0.31 | 0.09 | 759346.18 | 3.29 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.93 | 11.76 | 8.12 | 0.05 | 185175.97 | 56.58 | skipped_fast |
| CCUSDT | IDLE | 0.81 | 2.55 | 0.08 | 0.11 | 667309.2 | 6.3 | skipped_fast |
| HBARUSDT | IDLE | 1.25 | 2.46 | 0.39 | 0.06 | 614100.26 | 1.26 | skipped_fast |
| ZBCNUSDT | IDLE | 1.54 | 2.77 | 2.09 | 0.02 | 221939.58 | 7.77 | skipped_fast |
| CHIPUSDT | IDLE | 1.41 | 8.61 | 2.96 | 0.21 | 189138.96 | 26.53 | skipped_fast |
| RWAINCUSDT | IDLE | 1.6 | 3.12 | 0.57 | 0.04 | 7342.35 | 5.75 | skipped_fast |
| BIOUSDT | IDLE | 0.84 | 2.19 | 1.05 | 0.09 | 88238.81 | 14.65 | skipped_fast |
| KITEUSDT | IDLE | 0.88 | 1.75 | 0.04 | 0.06 | 77133.74 | 11.67 | skipped_fast |
| REDUSDT | IDLE | 0.55 | 1.8 | 0.36 | 0.13 | 63299.07 | 21.2 | skipped_fast |
| FLUIDUSDT | IDLE | 1.74 | 7.3 | 0.5 | 0.16 | 2457.56 | 21.64 | skipped_fast |
| TELUSDT | IDLE | 0.94 | 2.7 | 1.09 | 0.08 | 105025.57 | 45.32 | skipped_fast |
| MNSRYUSDT | IDLE | 1.02 | 2.03 | 0.05 | 0.07 | 43032.2 | 18.33 | skipped_fast |
| QNTUSDT | IDLE | 0.7 | 1.31 | 0.55 | 0.05 | 72695.42 | 4.72 | skipped_fast |
| RIZEUSDT | IDLE | 0.2 | 3.39 | 0.6 | -0.09 | 57613.67 | 117.17 | skipped_fast |
| RWAUSDT | IDLE | 0.83 | 1.49 | 1.1 | 0.01 | 58201.99 | 51.76 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
