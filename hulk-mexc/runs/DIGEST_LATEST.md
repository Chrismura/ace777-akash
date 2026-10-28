# Hulk DIGEST — 2026-10-28T10:32:57Z

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
| ETHUSDT | IDLE | 0.84 | 1.57 | 0.74 | 0.03 | 247710092.03 | 0.17 | skipped_fast |
| XRPUSDT | IDLE | 0.68 | 1.24 | 0.76 | 0.03 | 20240061.55 | 1.5 | skipped_fast |
| BTCUSDT | IDLE | 0.6 | 1.15 | 0.34 | 0.02 | 309611523.76 | 0.0 | skipped_fast |
| CCUSDT | IDLE | 2.99 | 6.2 | 1.39 | 0.07 | 286783.15 | 7.75 | skipped_fast |
| WUSDT | IDLE | 0.69 | 1.36 | 0.78 | 0.04 | 622912.59 | 17.15 | skipped_fast |
| RWAINCUSDT | IDLE | 2.81 | 5.62 | 0.06 | 0.03 | 54587.84 | 6.49 | skipped_fast |
| PYTHUSDT | IDLE | 0.82 | 1.57 | 0.52 | 0.0 | 396616.49 | 1.38 | skipped_fast |
| EDELUSDT | IDLE | 1.19 | 2.1 | 1.91 | 0.01 | 305551.41 | 24.68 | skipped_fast |
| QNTUSDT | IDLE | 1.44 | 2.75 | 0.85 | -0.0 | 515612.59 | 4.96 | skipped_fast |
| ZBCNUSDT | IDLE | 1.62 | 3.17 | 1.37 | -0.03 | 213473.83 | 29.28 | skipped_fast |
| RIZEUSDT | IDLE | 2.44 | 4.52 | 2.44 | 0.03 | 36300.96 | 61.37 | skipped_fast |
| CHIPUSDT | IDLE | 1.26 | 2.33 | 1.31 | 0.08 | 123258.15 | 16.63 | skipped_fast |
| REDUSDT | IDLE | 1.02 | 1.81 | 1.54 | 0.05 | 55010.83 | 15.73 | skipped_fast |
| KITEUSDT | IDLE | 0.87 | 1.55 | 1.25 | 0.04 | 60210.13 | 12.01 | skipped_fast |
| BIOUSDT | IDLE | 0.77 | 1.5 | 0.31 | 0.05 | 82922.24 | 8.75 | skipped_fast |
| HBARUSDT | IDLE | 0.69 | 1.32 | 0.36 | 0.01 | 387842.48 | 5.22 | skipped_fast |
| WAXLUSDT | IDLE | 1.09 | 2.15 | 0.2 | 0.02 | 55709.71 | 56.92 | skipped_fast |
| LAUSDT | IDLE | 0.71 | 1.38 | 0.65 | 0.04 | 60136.46 | 21.98 | skipped_fast |
| IOTAUSDT | IDLE | 0.68 | 1.31 | 0.31 | 0.02 | 71876.16 | 25.91 | skipped_fast |
| RWAUSDT | IDLE | 0.7 | 1.29 | 0.79 | 0.01 | 55447.82 | 48.0 | skipped_fast |
| FLUIDUSDT | IDLE | 0.46 | 1.42 | 0.46 | 0.01 | 6654.9 | 18.96 | skipped_fast |
| MNSRYUSDT | IDLE | 0.65 | 1.25 | 0.38 | 0.0 | 35960.78 | 54.03 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
