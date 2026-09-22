# Hulk DIGEST — 2026-09-22T19:15:52Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 3.65 | 16.78 | 9.92 | 0.05 | 1636957.92 | 3.01 | skipped_fast |
| XRPUSDT | IDLE | 2.02 | 3.98 | 0.45 | 0.06 | 117648557.22 | 1.89 | skipped_fast |
| ETHUSDT | IDLE | 0.79 | 1.57 | 0.09 | -0.0 | 453751721.29 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.73 | 1.42 | 0.24 | 0.01 | 940712070.18 | 0.0 | skipped_fast |
| HBARUSDT | IDLE | 2.13 | 4.46 | 0.46 | 0.09 | 1510301.8 | 1.02 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.56 | 15.46 | 9.44 | -0.01 | 298161.27 | 32.57 | skipped_fast |
| CCUSDT | IDLE | 2.8 | 5.07 | 3.56 | -0.01 | 491585.39 | 9.69 | skipped_fast |
| WUSDT | IDLE | 2.06 | 3.87 | 1.63 | 0.02 | 355329.81 | 5.85 | skipped_fast |
| ZBCNUSDT | IDLE | 2.55 | 4.6 | 3.29 | -0.01 | 222694.71 | 19.4 | skipped_fast |
| RIZEUSDT | IDLE | 2.29 | 26.82 | 8.4 | -0.16 | 43999.12 | 109.19 | skipped_fast |
| BIOUSDT | IDLE | 2.37 | 4.57 | 1.14 | 0.02 | 137676.14 | 3.4 | skipped_fast |
| CHIPUSDT | IDLE | 1.94 | 3.44 | 2.9 | -0.01 | 140511.47 | 17.68 | skipped_fast |
| KITEUSDT | IDLE | 1.47 | 6.79 | 0.93 | 0.17 | 116149.0 | 7.94 | skipped_fast |
| REDUSDT | IDLE | 1.87 | 3.67 | 0.45 | 0.05 | 64893.08 | 15.17 | skipped_fast |
| TELUSDT | IDLE | 2.33 | 6.81 | 0.17 | 0.07 | 104508.76 | 11.3 | skipped_fast |
| QNTUSDT | IDLE | 1.11 | 3.39 | 2.04 | 0.08 | 187744.1 | 1.39 | skipped_fast |
| RWAINCUSDT | IDLE | 0.36 | 0.72 | 0.0 | 0.05 | 19957.17 | 5.51 | skipped_fast |
| RWAUSDT | IDLE | 0.64 | 1.24 | 0.29 | -0.0 | 54191.39 | 7.23 | skipped_fast |
| FLUIDUSDT | IDLE | 0.7 | 1.33 | 0.47 | 0.02 | 7769.26 | 21.9 | skipped_fast |
| MNSRYUSDT | IDLE | 0.04 | 0.08 | 0.06 | -0.0 | 40185.68 | 9.02 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
