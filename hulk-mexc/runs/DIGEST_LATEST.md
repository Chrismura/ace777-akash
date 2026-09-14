# Hulk DIGEST — 2026-09-14T13:42:53Z

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
| XRPUSDT | IDLE | 1.11 | 2.06 | 1.06 | 0.04 | 38837600.37 | 1.43 | skipped_fast |
| ETHUSDT | IDLE | 1.04 | 1.89 | 1.22 | 0.01 | 327244978.66 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.6 | 1.13 | 0.47 | 0.02 | 417263389.56 | 0.0 | skipped_fast |
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.19 | 7.52 | 5.78 | 0.0 | 509851.62 | 1.81 | skipped_fast |
| REDUSDT | IDLE | 2.48 | 7.43 | 0.49 | 0.09 | 170063.04 | 16.07 | skipped_fast |
| WUSDT | IDLE | 2.21 | 3.93 | 3.21 | -0.0 | 228206.38 | 12.13 | skipped_fast |
| CHIPUSDT | IDLE | 2.46 | 5.43 | 3.87 | -0.06 | 103193.94 | 21.82 | skipped_fast |
| EDELUSDT | IDLE | 1.69 | 7.11 | 1.85 | 0.15 | 241859.21 | 34.93 | skipped_fast |
| CCUSDT | IDLE | 1.04 | 1.96 | 0.84 | 0.01 | 246799.27 | 10.41 | skipped_fast |
| BIOUSDT | IDLE | 1.39 | 2.5 | 1.82 | 0.0 | 77733.91 | 3.93 | skipped_fast |
| ZBCNUSDT | IDLE | 1.0 | 1.97 | 0.24 | 0.01 | 204031.73 | 16.26 | skipped_fast |
| RIZEUSDT | IDLE | 1.1 | 12.23 | 9.13 | 0.08 | 67890.2 | 93.06 | skipped_fast |
| KITEUSDT | IDLE | 1.25 | 2.23 | 1.81 | -0.03 | 61700.59 | 10.41 | skipped_fast |
| RWAINCUSDT | IDLE | 1.41 | 2.56 | 1.68 | 0.02 | 8671.1 | 22.03 | skipped_fast |
| HBARUSDT | IDLE | 1.0 | 1.87 | 0.9 | 0.01 | 288594.27 | 1.3 | skipped_fast |
| TELUSDT | IDLE | 1.61 | 3.05 | 1.11 | 0.02 | 89893.56 | 31.16 | skipped_fast |
| FLUIDUSDT | IDLE | 1.39 | 2.53 | 1.67 | 0.01 | 887.72 | 0.84 | skipped_fast |
| QNTUSDT | IDLE | 0.81 | 1.56 | 0.39 | 0.0 | 40308.86 | 9.33 | skipped_fast |
| RWAUSDT | IDLE | 0.29 | 0.52 | 0.37 | 0.01 | 54316.98 | 22.25 | skipped_fast |
| MNSRYUSDT | IDLE | 0.21 | 0.38 | 0.24 | -0.0 | 28859.69 | 33.52 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
