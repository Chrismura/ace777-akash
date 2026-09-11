# Hulk DIGEST — 2026-09-11T19:21:57Z

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
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.29 | 6.41 | 5.71 | -0.0 | 53839580.52 | 2.22 | skipped_fast |
| ETHUSDT | IDLE | 2.56 | 5.39 | 4.74 | 0.03 | 635704811.71 | 1.1 | skipped_fast |
| BTCUSDT | IDLE | 2.15 | 3.79 | 3.34 | 0.0 | 558639528.29 | 0.02 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.91 | 93.24 | 11.15 | 0.98 | 187700.45 | 90.45 | skipped_fast |
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 3.63 | 6.68 | 5.8 | -0.01 | 408898.11 | 1.96 | skipped_fast |
| CCUSDT | IDLE | 2.68 | 4.74 | 4.09 | -0.01 | 418212.35 | 8.18 | skipped_fast |
| EDELUSDT | IDLE | 3.38 | 7.46 | 0.26 | 0.02 | 155716.05 | 17.61 | skipped_fast |
| RWAINCUSDT | IDLE | 4.07 | 8.33 | 3.84 | 0.04 | 11883.82 | 48.58 | skipped_fast |
| WUSDT | IDLE | 2.57 | 4.84 | 4.04 | 0.0 | 196176.46 | 15.55 | skipped_fast |
| BIOUSDT | IDLE | 2.65 | 4.68 | 4.13 | -0.01 | 82337.61 | 4.02 | skipped_fast |
| CHIPUSDT | IDLE | 2.19 | 6.38 | 5.24 | -0.01 | 149903.52 | 18.99 | skipped_fast |
| ZBCNUSDT | IDLE | 2.12 | 3.73 | 3.35 | 0.0 | 190017.45 | 5.99 | skipped_fast |
| HBARUSDT | IDLE | 2.41 | 4.25 | 3.76 | -0.01 | 236793.06 | 1.35 | skipped_fast |
| KITEUSDT | IDLE | 1.71 | 3.05 | 2.43 | -0.02 | 59411.82 | 13.86 | skipped_fast |
| REDUSDT | IDLE | 1.67 | 3.16 | 1.22 | 0.05 | 61350.37 | 18.99 | skipped_fast |
| TELUSDT | IDLE | 3.04 | 5.94 | 4.96 | -0.01 | 93228.89 | 68.07 | skipped_fast |
| QNTUSDT | IDLE | 1.79 | 3.13 | 3.03 | -0.03 | 40794.07 | 4.69 | skipped_fast |
| FLUIDUSDT | IDLE | 1.53 | 2.66 | 2.6 | -0.0 | 1306.32 | 21.75 | skipped_fast |
| MNSRYUSDT | IDLE | 1.23 | 2.19 | 1.83 | 0.0 | 36829.68 | 41.68 | skipped_fast |
| RWAUSDT | IDLE | 0.74 | 1.35 | 0.81 | 0.02 | 52113.89 | 7.45 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
