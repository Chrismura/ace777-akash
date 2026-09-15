# Hulk DIGEST — 2026-09-15T15:36:27Z

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
| XRPUSDT | IDLE | 3.26 | 6.39 | 4.6 | -0.01 | 83542617.1 | 2.15 | skipped_fast |
| ETHUSDT | IDLE | 1.9 | 4.09 | 2.36 | -0.03 | 505865376.64 | 0.49 | skipped_fast |
| BTCUSDT | IDLE | 1.16 | 2.15 | 1.08 | -0.03 | 576749752.27 | 0.0 | skipped_fast |
| EDELUSDT | IDLE | 1.83 | 24.22 | 13.55 | 0.34 | 467970.83 | 10.33 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 4.27 | 8.73 | 5.02 | -0.02 | 206812.1 | 23.16 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.46 | 10.37 | 9.03 | -0.1 | 90071.24 | 18.56 | skipped_fast |
| CCUSDT | IDLE | 1.83 | 3.41 | 1.65 | -0.02 | 345507.03 | 11.71 | skipped_fast |
| HBARUSDT | IDLE | 2.23 | 4.08 | 2.5 | 0.01 | 458591.74 | 1.28 | skipped_fast |
| PYTHUSDT | IDLE | 1.63 | 3.22 | 1.08 | -0.02 | 294970.83 | 1.86 | skipped_fast |
| KITEUSDT | IDLE | 2.37 | 4.4 | 2.32 | -0.0 | 62588.86 | 12.41 | skipped_fast |
| RWAINCUSDT | IDLE | 2.45 | 4.29 | 4.11 | -0.06 | 9546.66 | 28.93 | skipped_fast |
| WUSDT | IDLE | 1.61 | 3.44 | 1.76 | -0.04 | 149432.46 | 10.5 | skipped_fast |
| REDUSDT | IDLE | 1.18 | 6.22 | 3.51 | -0.03 | 108555.86 | 19.22 | skipped_fast |
| BIOUSDT | IDLE | 1.5 | 2.84 | 1.03 | -0.02 | 82452.71 | 3.99 | skipped_fast |
| RIZEUSDT | IDLE | 1.23 | 10.82 | 9.58 | -0.02 | 54191.48 | 100.95 | skipped_fast |
| FLUIDUSDT | IDLE | 1.79 | 3.21 | 2.57 | -0.04 | 2071.8 | 21.06 | skipped_fast |
| QNTUSDT | IDLE | 1.19 | 2.31 | 0.44 | -0.03 | 50738.33 | 1.59 | skipped_fast |
| TELUSDT | IDLE | 1.34 | 4.37 | 3.11 | -0.05 | 99429.87 | 71.92 | skipped_fast |
| RWAUSDT | IDLE | 0.53 | 0.98 | 0.52 | -0.01 | 51847.16 | 14.98 | skipped_fast |
| MNSRYUSDT | IDLE | 0.56 | 1.04 | 0.55 | -0.0 | 33522.08 | 58.58 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
