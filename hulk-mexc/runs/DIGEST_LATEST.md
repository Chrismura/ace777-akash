# Hulk DIGEST — 2026-09-02T14:29:02Z

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
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.47 | 14.29 | 11.18 | -0.06 | 942066.47 | 2.41 | skipped_fast |
| XRPUSDT | IDLE | 1.42 | 2.79 | 0.32 | -0.03 | 39309807.72 | 1.49 | skipped_fast |
| ETHUSDT | IDLE | 1.36 | 2.63 | 0.65 | -0.02 | 407178804.9 | 0.33 | skipped_fast |
| BTCUSDT | IDLE | 0.81 | 1.59 | 0.22 | -0.01 | 519614078.71 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.85 | 7.47 | 1.06 | 0.14 | 976151.1 | 3.52 | skipped_fast |
| CCUSDT | IDLE | 2.1 | 3.69 | 3.37 | -0.06 | 354639.75 | 5.45 | skipped_fast |
| REDUSDT | IDLE | 2.79 | 5.41 | 1.09 | 0.05 | 160976.16 | 10.44 | skipped_fast |
| WUSDT | IDLE | 1.57 | 2.91 | 1.58 | -0.02 | 396428.59 | 12.64 | skipped_fast |
| KITEUSDT | IDLE | 1.64 | 6.19 | 1.72 | 0.11 | 88176.57 | 11.67 | skipped_fast |
| RIZEUSDT | IDLE | 2.23 | 7.8 | 1.87 | -0.08 | 45441.58 | 78.33 | skipped_fast |
| RWAINCUSDT | IDLE | 2.01 | 5.69 | 4.54 | 0.05 | 11117.42 | 38.79 | skipped_fast |
| ZBCNUSDT | IDLE | 0.92 | 1.87 | 1.36 | -0.03 | 198233.92 | 24.34 | skipped_fast |
| BIOUSDT | IDLE | 1.16 | 2.2 | 0.74 | -0.03 | 72880.42 | 3.95 | skipped_fast |
| EDELUSDT | IDLE | 0.65 | 3.7 | 0.97 | 0.08 | 171901.88 | 40.93 | skipped_fast |
| HBARUSDT | IDLE | 0.94 | 1.84 | 0.24 | -0.01 | 207551.76 | 1.35 | skipped_fast |
| TELUSDT | IDLE | 1.75 | 3.44 | 0.35 | -0.0 | 74563.49 | 35.09 | skipped_fast |
| FLUIDUSDT | IDLE | 1.67 | 2.91 | 2.83 | -0.06 | 1663.98 | 22.17 | skipped_fast |
| QNTUSDT | IDLE | 1.24 | 2.48 | 0.0 | 0.02 | 69386.39 | 3.09 | skipped_fast |
| RWAUSDT | IDLE | 0.5 | 0.93 | 0.46 | -0.0 | 51137.16 | 46.05 | skipped_fast |
| MNSRYUSDT | IDLE | 0.38 | 0.72 | 0.32 | -0.01 | 34778.73 | 39.89 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
