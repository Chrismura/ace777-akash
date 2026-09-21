# Hulk DIGEST — 2026-09-21T23:07:40Z

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
| XRPUSDT | IDLE | 1.84 | 5.52 | 0.37 | 0.11 | 108708418.95 | 1.91 | skipped_fast |
| ETHUSDT | IDLE | 1.33 | 2.55 | 0.76 | 0.06 | 738159347.17 | 1.08 | skipped_fast |
| BTCUSDT | IDLE | 0.99 | 1.87 | 0.89 | 0.07 | 1052651141.61 | 0.0 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.01 | 18.24 | 13.65 | 0.09 | 264210.01 | 23.24 | skipped_fast |
| HBARUSDT | IDLE | 1.36 | 3.38 | 0.06 | 0.08 | 1133968.46 | 1.07 | skipped_fast |
| PYTHUSDT | IDLE | 1.53 | 3.83 | 0.95 | 0.04 | 713061.71 | 1.57 | skipped_fast |
| CCUSDT | IDLE | 1.46 | 3.27 | 0.36 | 0.09 | 595460.2 | 7.63 | skipped_fast |
| ZBCNUSDT | IDLE | 2.52 | 6.77 | 2.81 | 0.08 | 255568.39 | 40.97 | skipped_fast |
| WUSDT | IDLE | 0.9 | 2.18 | 0.01 | 0.02 | 554389.36 | 7.59 | skipped_fast |
| RIZEUSDT | IDLE | 1.54 | 11.17 | 8.95 | -0.18 | 48489.32 | 47.53 | skipped_fast |
| RWAINCUSDT | IDLE | 2.55 | 7.23 | 1.02 | 0.1 | 19713.32 | 87.58 | skipped_fast |
| CHIPUSDT | IDLE | 1.02 | 5.1 | 1.14 | 0.1 | 147150.94 | 17.06 | skipped_fast |
| BIOUSDT | IDLE | 1.01 | 2.03 | 0.0 | 0.05 | 101337.93 | 3.44 | skipped_fast |
| KITEUSDT | IDLE | 1.0 | 1.98 | 0.09 | 0.04 | 81224.52 | 9.19 | skipped_fast |
| REDUSDT | IDLE | 0.78 | 1.52 | 0.28 | 0.0 | 103495.79 | 14.48 | skipped_fast |
| QNTUSDT | IDLE | 1.5 | 2.84 | 1.01 | 0.05 | 108630.92 | 4.46 | skipped_fast |
| TELUSDT | IDLE | 1.1 | 3.18 | 1.95 | 0.09 | 115619.96 | 42.39 | skipped_fast |
| FLUIDUSDT | IDLE | 1.07 | 2.43 | 1.7 | 0.07 | 11627.45 | 17.78 | skipped_fast |
| RWAUSDT | IDLE | 0.61 | 1.16 | 0.36 | 0.01 | 57852.73 | 14.42 | skipped_fast |
| MNSRYUSDT | IDLE | 0.77 | 1.5 | 0.2 | 0.04 | 42360.9 | 61.48 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
