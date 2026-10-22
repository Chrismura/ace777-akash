# Hulk DIGEST — 2026-10-22T10:28:00Z

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
| WUSDT | IDLE | 1.32 | 5.89 | 3.93 | -0.04 | 3468048.11 | 16.74 | skipped_fast |
| ETHUSDT | IDLE | 1.21 | 2.2 | 1.46 | -0.02 | 231518457.44 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 1.11 | 2.02 | 1.29 | -0.01 | 33583670.58 | 1.5 | skipped_fast |
| BTCUSDT | IDLE | 0.89 | 1.62 | 1.1 | -0.01 | 515811539.27 | 0.0 | skipped_fast |
| HBARUSDT | IDLE | 1.57 | 2.81 | 2.22 | -0.04 | 1375807.32 | 6.19 | skipped_fast |
| QNTUSDT | IDLE | 1.26 | 3.11 | 1.71 | -0.0 | 1317921.09 | 2.03 | skipped_fast |
| CHIPUSDT | IDLE | 2.41 | 9.7 | 7.89 | -0.03 | 343358.94 | 11.48 | skipped_fast |
| PYTHUSDT | IDLE | 1.46 | 4.01 | 2.46 | -0.07 | 649845.65 | 1.34 | skipped_fast |
| EDELUSDT | IDLE | 1.62 | 2.96 | 1.86 | -0.02 | 553947.82 | 17.77 | skipped_fast |
| ZBCNUSDT | IDLE | 1.39 | 4.29 | 0.19 | -0.03 | 247297.31 | 27.37 | skipped_fast |
| CCUSDT | IDLE | 0.6 | 1.69 | 0.78 | -0.02 | 393665.6 | 9.54 | skipped_fast |
| BIOUSDT | IDLE | 1.44 | 3.04 | 1.84 | -0.03 | 78335.37 | 4.17 | skipped_fast |
| REDUSDT | IDLE | 1.47 | 2.79 | 2.02 | -0.02 | 81357.35 | 16.15 | skipped_fast |
| RWAINCUSDT | IDLE | 1.69 | 3.21 | 1.11 | -0.01 | 61004.95 | 50.46 | skipped_fast |
| KITEUSDT | IDLE | 1.01 | 1.82 | 1.33 | -0.03 | 59911.37 | 9.22 | skipped_fast |
| RIZEUSDT | IDLE | 1.33 | 2.86 | 0.33 | 0.05 | 44978.16 | 58.68 | skipped_fast |
| WAXLUSDT | IDLE | 1.76 | 6.13 | 3.58 | -0.07 | 58418.63 | 56.9 | skipped_fast |
| IOTAUSDT | IDLE | 1.6 | 3.08 | 2.27 | -0.04 | 78446.35 | 33.22 | skipped_fast |
| LAUSDT | IDLE | 1.32 | 3.52 | 1.74 | -0.04 | 58821.2 | 23.32 | skipped_fast |
| FLUIDUSDT | IDLE | 0.56 | 2.8 | 2.65 | -0.02 | 19867.3 | 21.16 | skipped_fast |
| RWAUSDT | IDLE | 0.31 | 0.55 | 0.47 | -0.01 | 52445.09 | 23.63 | skipped_fast |
| MNSRYUSDT | IDLE | 0.48 | 0.86 | 0.68 | -0.0 | 39919.63 | 55.51 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
