# Hulk DIGEST — 2026-10-20T12:00:51Z

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
| ETHUSDT | IDLE | 0.52 | 0.94 | 0.63 | -0.01 | 123912868.67 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.52 | 0.98 | 0.39 | -0.0 | 19039761.75 | 1.54 | skipped_fast |
| BTCUSDT | IDLE | 0.35 | 0.63 | 0.42 | -0.01 | 292476294.11 | 0.0 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 3.99 | 10.61 | 9.55 | 0.01 | 84820.46 | 5.25 | skipped_fast |
| WUSDT | IDLE | 1.83 | 3.24 | 2.82 | 0.01 | 703671.07 | 17.91 | skipped_fast |
| PYTHUSDT | IDLE | 0.73 | 1.39 | 0.47 | -0.01 | 911351.33 | 5.5 | skipped_fast |
| CCUSDT | IDLE | 0.97 | 1.9 | 0.29 | 0.01 | 448087.91 | 11.49 | skipped_fast |
| EDELUSDT | IDLE | 1.3 | 7.37 | 0.65 | 0.19 | 297633.46 | 15.56 | skipped_fast |
| ZBCNUSDT | IDLE | 1.67 | 3.02 | 2.14 | -0.03 | 182228.78 | 5.8 | skipped_fast |
| CHIPUSDT | IDLE | 1.73 | 4.18 | 3.72 | 0.03 | 90885.77 | 13.89 | skipped_fast |
| QNTUSDT | IDLE | 1.26 | 2.43 | 0.56 | -0.03 | 507250.02 | 0.52 | skipped_fast |
| KITEUSDT | IDLE | 1.73 | 3.1 | 2.46 | 0.01 | 88595.76 | 12.56 | skipped_fast |
| HBARUSDT | IDLE | 1.33 | 2.34 | 2.11 | -0.01 | 354845.05 | 7.3 | skipped_fast |
| REDUSDT | IDLE | 1.09 | 1.96 | 1.46 | 0.01 | 58032.8 | 15.43 | skipped_fast |
| BIOUSDT | IDLE | 0.62 | 1.2 | 0.3 | 0.01 | 65705.71 | 8.46 | skipped_fast |
| WAXLUSDT | IDLE | 1.93 | 4.21 | 3.39 | -0.07 | 57204.86 | 28.16 | skipped_fast |
| IOTAUSDT | IDLE | 1.02 | 1.91 | 0.85 | 0.03 | 84446.85 | 17.62 | skipped_fast |
| LAUSDT | IDLE | 1.17 | 2.12 | 1.48 | -0.01 | 56123.02 | 23.19 | skipped_fast |
| RIZEUSDT | IDLE | 2.24 | 8.45 | 6.01 | -0.07 | 66008.24 | 557.01 | skipped_fast |
| RWAUSDT | IDLE | 0.49 | 0.95 | 0.24 | 0.01 | 51201.8 | 7.86 | skipped_fast |
| MNSRYUSDT | IDLE | 0.13 | 0.24 | 0.1 | -0.0 | 39411.15 | 5.7 | skipped_fast |
| FLUIDUSDT | IDLE | 0.35 | 0.65 | 0.27 | 0.01 | 4452.44 | 21.17 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
