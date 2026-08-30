# Hulk DIGEST — 2026-08-30T17:41:27Z

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
| ETHUSDT | IDLE | 1.61 | 3.05 | 1.19 | 0.02 | 217152206.13 | 0.08 | skipped_fast |
| XRPUSDT | IDLE | 1.28 | 2.44 | 0.74 | 0.02 | 20720365.8 | 2.83 | skipped_fast |
| BTCUSDT | IDLE | 0.83 | 1.58 | 0.49 | 0.01 | 278693753.38 | 0.0 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.91 | 7.33 | 6.08 | -0.03 | 516107.28 | 2.51 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 4.27 | 9.26 | 5.77 | -0.06 | 197432.77 | 11.29 | skipped_fast |
| PYTHUSDT | IDLE | 3.05 | 5.66 | 2.97 | 0.02 | 389583.8 | 4.1 | skipped_fast |
| EDELUSDT | IDLE | 2.08 | 5.99 | 3.55 | 0.07 | 72786.5 | 8.38 | skipped_fast |
| WUSDT | IDLE | 1.61 | 3.02 | 1.3 | 0.04 | 222882.41 | 10.54 | skipped_fast |
| CCUSDT | IDLE | 0.99 | 1.74 | 1.54 | 0.01 | 255016.87 | 10.18 | skipped_fast |
| KITEUSDT | IDLE | 1.69 | 2.96 | 2.83 | -0.03 | 61239.42 | 11.92 | skipped_fast |
| REDUSDT | IDLE | 1.18 | 2.06 | 1.98 | 0.01 | 62912.12 | 13.7 | skipped_fast |
| BIOUSDT | IDLE | 0.87 | 1.65 | 0.65 | -0.0 | 80322.66 | 3.63 | skipped_fast |
| RIZEUSDT | IDLE | 1.28 | 4.02 | 3.66 | -0.07 | 37301.02 | 62.12 | skipped_fast |
| TELUSDT | IDLE | 2.21 | 4.37 | 0.34 | 0.0 | 83543.52 | 23.04 | skipped_fast |
| RWAINCUSDT | IDLE | 1.81 | 3.63 | 0.0 | 0.02 | 1921.2 | 120.81 | skipped_fast |
| HBARUSDT | IDLE | 0.62 | 1.21 | 0.17 | 0.01 | 142579.65 | 1.32 | skipped_fast |
| RWAUSDT | IDLE | 0.62 | 1.22 | 0.16 | 0.02 | 52889.16 | 8.07 | skipped_fast |
| MNSRYUSDT | IDLE | 0.76 | 1.41 | 0.7 | 0.01 | 32140.64 | 17.34 | skipped_fast |
| FLUIDUSDT | IDLE | 0.87 | 1.73 | 0.04 | 0.03 | 3186.73 | 21.57 | skipped_fast |
| QNTUSDT | IDLE | 0.51 | 0.97 | 0.39 | 0.01 | 38397.12 | 4.84 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
