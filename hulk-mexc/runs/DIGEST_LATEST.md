# Hulk DIGEST — 2026-10-17T22:22:54Z

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
| ETHUSDT | IDLE | 1.5 | 2.79 | 1.4 | -0.01 | 86639149.59 | 0.08 | skipped_fast |
| XRPUSDT | IDLE | 1.45 | 2.74 | 1.11 | -0.01 | 16759053.11 | 1.55 | skipped_fast |
| BTCUSDT | IDLE | 0.57 | 1.06 | 0.5 | -0.01 | 182316532.87 | 0.0 | skipped_fast |
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 3.02 | 9.68 | 6.95 | -0.11 | 988468.57 | 21.69 | skipped_fast |
| WUSDT | IDLE | 1.92 | 5.68 | 3.51 | -0.05 | 984330.83 | 16.75 | skipped_fast |
| QNTUSDT | IDLE | 2.92 | 5.39 | 3.0 | -0.04 | 611878.52 | 2.05 | skipped_fast |
| BIOUSDT | IDLE | 2.37 | 4.41 | 2.23 | -0.04 | 75193.51 | 4.15 | skipped_fast |
| CCUSDT | IDLE | 1.47 | 2.74 | 1.27 | -0.0 | 260703.35 | 4.81 | skipped_fast |
| CHIPUSDT | IDLE | 2.11 | 5.85 | 3.36 | -0.07 | 82828.64 | 13.98 | skipped_fast |
| ZBCNUSDT | IDLE | 1.85 | 3.39 | 2.01 | -0.02 | 187377.81 | 16.85 | skipped_fast |
| EDELUSDT | IDLE | 1.54 | 2.68 | 2.61 | -0.05 | 152682.66 | 14.27 | skipped_fast |
| REDUSDT | IDLE | 1.86 | 3.41 | 2.05 | -0.05 | 62184.23 | 9.38 | skipped_fast |
| KITEUSDT | IDLE | 1.67 | 4.14 | 2.73 | -0.05 | 68557.58 | 12.99 | skipped_fast |
| HBARUSDT | IDLE | 2.38 | 4.47 | 1.91 | 0.01 | 201875.74 | 3.56 | skipped_fast |
| RIZEUSDT | IDLE | 1.39 | 2.58 | 1.27 | -0.02 | 50206.89 | 59.03 | skipped_fast |
| TELUSDT | IDLE | 1.98 | 3.59 | 2.51 | -0.07 | 104017.54 | 12.25 | skipped_fast |
| RWAINCUSDT | IDLE | 0.45 | 1.52 | 0.98 | 0.08 | 20108.11 | 36.51 | skipped_fast |
| RWAUSDT | IDLE | 1.34 | 2.52 | 1.03 | -0.01 | 51389.62 | 8.0 | skipped_fast |
| FLUIDUSDT | IDLE | 1.42 | 2.69 | 0.97 | -0.01 | 1899.19 | 20.8 | skipped_fast |
| MNSRYUSDT | IDLE | 0.32 | 0.57 | 0.42 | -0.0 | 31174.49 | 16.96 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
