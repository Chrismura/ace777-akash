# Hulk DIGEST — 2026-10-22T10:12:13Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| WUSDT | IDLE | 1.33 | 5.89 | 4.45 | -0.04 | 3474418.44 | 18.29 | skipped_fast |
| ETHUSDT | IDLE | 1.22 | 2.2 | 1.61 | -0.02 | 231857889.25 | 0.12 | skipped_fast |
| XRPUSDT | IDLE | 1.12 | 2.02 | 1.52 | -0.02 | 33649237.24 | 2.25 | skipped_fast |
| BTCUSDT | IDLE | 0.9 | 1.62 | 1.19 | -0.02 | 515589120.69 | 0.0 | skipped_fast |
| HBARUSDT | IDLE | 1.56 | 2.81 | 2.1 | -0.04 | 1375769.97 | 7.42 | skipped_fast |
| QNTUSDT | IDLE | 1.27 | 3.11 | 1.96 | -0.01 | 1265272.42 | 1.02 | skipped_fast |
| PYTHUSDT | IDLE | 1.47 | 4.01 | 2.57 | -0.06 | 654266.12 | 2.68 | skipped_fast |
| CHIPUSDT | IDLE | 2.42 | 9.7 | 8.21 | -0.03 | 343120.46 | 20.73 | skipped_fast |
| EDELUSDT | IDLE | 1.62 | 2.96 | 1.92 | -0.02 | 555002.03 | 20.74 | skipped_fast |
| CCUSDT | IDLE | 0.6 | 1.69 | 0.8 | -0.02 | 392884.39 | 9.54 | skipped_fast |
| ZBCNUSDT | IDLE | 1.12 | 3.33 | 1.02 | -0.05 | 245469.76 | 20.79 | skipped_fast |
| RWAINCUSDT | IDLE | 1.79 | 3.21 | 2.5 | -0.03 | 60877.45 | 17.11 | skipped_fast |
| BIOUSDT | IDLE | 1.45 | 3.04 | 1.92 | -0.03 | 78310.36 | 8.35 | skipped_fast |
| REDUSDT | IDLE | 1.47 | 2.79 | 1.95 | -0.02 | 81241.36 | 15.44 | skipped_fast |
| KITEUSDT | IDLE | 0.99 | 1.82 | 1.01 | -0.02 | 59628.27 | 9.19 | skipped_fast |
| RIZEUSDT | IDLE | 1.31 | 2.86 | 0.13 | 0.05 | 45029.92 | 58.68 | skipped_fast |
| WAXLUSDT | IDLE | 1.76 | 6.13 | 3.6 | -0.07 | 58626.13 | 50.82 | skipped_fast |
| IOTAUSDT | IDLE | 1.61 | 3.08 | 2.49 | -0.04 | 78273.34 | 33.22 | skipped_fast |
| LAUSDT | IDLE | 1.33 | 3.52 | 1.8 | -0.04 | 58952.22 | 23.32 | skipped_fast |
| FLUIDUSDT | IDLE | 0.5 | 2.46 | 2.4 | -0.02 | 19847.28 | 21.16 | skipped_fast |
| RWAUSDT | IDLE | 0.3 | 0.55 | 0.39 | -0.01 | 52837.42 | 15.75 | skipped_fast |
| MNSRYUSDT | IDLE | 0.46 | 0.86 | 0.4 | 0.0 | 40025.03 | 55.51 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
