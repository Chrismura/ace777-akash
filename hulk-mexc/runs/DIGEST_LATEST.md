# Hulk DIGEST — 2026-10-28T14:36:54Z

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
| ETHUSDT | IDLE | 1.25 | 2.21 | 1.93 | -0.0 | 236978150.29 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 1.04 | 1.83 | 1.7 | -0.01 | 19937324.21 | 1.53 | skipped_fast |
| BTCUSDT | IDLE | 0.83 | 1.46 | 1.31 | 0.0 | 311450367.92 | 0.0 | skipped_fast |
| CCUSDT | WATCH_PULLBACK — tension haute + reflux | 4.43 | 9.68 | 6.97 | -0.03 | 370334.66 | 9.24 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.52 | 12.9 | 11.27 | -0.04 | 184272.19 | 15.74 | skipped_fast |
| RWAINCUSDT | IDLE | 4.2 | 10.56 | 3.6 | 0.06 | 44247.69 | 6.43 | skipped_fast |
| QNTUSDT | IDLE | 3.12 | 5.52 | 4.85 | -0.04 | 463239.0 | 2.58 | skipped_fast |
| WUSDT | IDLE | 1.53 | 2.74 | 2.08 | -0.04 | 543548.55 | 16.62 | skipped_fast |
| PYTHUSDT | IDLE | 1.56 | 2.78 | 2.22 | -0.02 | 435345.84 | 5.61 | skipped_fast |
| ZBCNUSDT | IDLE | 2.1 | 3.94 | 2.8 | -0.05 | 232061.43 | 20.93 | skipped_fast |
| EDELUSDT | IDLE | 1.6 | 2.83 | 2.51 | -0.01 | 240209.8 | 21.7 | skipped_fast |
| BIOUSDT | IDLE | 1.85 | 3.29 | 2.79 | 0.0 | 88204.24 | 8.97 | skipped_fast |
| HBARUSDT | IDLE | 1.3 | 2.32 | 1.85 | -0.01 | 516154.13 | 7.97 | skipped_fast |
| KITEUSDT | IDLE | 1.28 | 2.24 | 2.12 | -0.04 | 58058.2 | 11.37 | skipped_fast |
| REDUSDT | IDLE | 1.21 | 2.15 | 1.85 | -0.02 | 53145.64 | 14.64 | skipped_fast |
| IOTAUSDT | IDLE | 1.96 | 3.45 | 3.12 | -0.02 | 75507.42 | 24.24 | skipped_fast |
| RIZEUSDT | IDLE | 1.0 | 1.79 | 1.4 | 0.02 | 36455.17 | 64.06 | skipped_fast |
| LAUSDT | IDLE | 1.8 | 3.17 | 2.84 | -0.02 | 59912.74 | 24.2 | skipped_fast |
| WAXLUSDT | IDLE | 1.86 | 3.26 | 3.02 | -0.02 | 55983.39 | 70.82 | skipped_fast |
| FLUIDUSDT | IDLE | 1.16 | 3.48 | 2.83 | -0.0 | 6563.17 | 21.6 | skipped_fast |
| RWAUSDT | IDLE | 0.63 | 1.12 | 0.87 | 0.01 | 54839.58 | 32.03 | skipped_fast |
| MNSRYUSDT | IDLE | 0.26 | 0.51 | 0.13 | 0.01 | 36384.65 | 48.2 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
