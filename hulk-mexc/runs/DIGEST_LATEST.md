# Hulk DIGEST — 2026-09-18T12:14:40Z

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
| XRPUSDT | IDLE | 1.01 | 1.81 | 1.4 | 0.01 | 41311924.29 | 2.27 | skipped_fast |
| ETHUSDT | IDLE | 0.76 | 1.42 | 0.66 | 0.02 | 389340770.42 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.62 | 1.17 | 0.53 | 0.02 | 569618582.8 | 0.12 | skipped_fast |
| CCUSDT | IDLE | 1.95 | 6.0 | 4.89 | 0.08 | 647513.34 | 8.4 | skipped_fast |
| PYTHUSDT | IDLE | 1.61 | 4.64 | 3.97 | 0.08 | 679589.15 | 1.71 | skipped_fast |
| WUSDT | IDLE | 0.98 | 2.78 | 1.81 | 0.09 | 424416.25 | 19.59 | skipped_fast |
| CHIPUSDT | IDLE | 1.66 | 7.46 | 6.41 | 0.09 | 162497.39 | 19.18 | skipped_fast |
| ZBCNUSDT | IDLE | 1.52 | 2.84 | 1.28 | 0.03 | 270418.51 | 0.56 | skipped_fast |
| BIOUSDT | IDLE | 1.87 | 4.65 | 3.94 | 0.06 | 86667.15 | 7.52 | skipped_fast |
| HBARUSDT | IDLE | 1.47 | 2.74 | 1.31 | 0.03 | 487746.18 | 1.3 | skipped_fast |
| REDUSDT | IDLE | 1.61 | 3.87 | 1.74 | 0.06 | 64356.51 | 16.44 | skipped_fast |
| TELUSDT | IDLE | 2.98 | 6.08 | 0.59 | 0.04 | 88236.74 | 33.17 | skipped_fast |
| EDELUSDT | IDLE | 0.54 | 5.21 | 3.33 | -0.05 | 256884.18 | 38.82 | skipped_fast |
| RWAINCUSDT | IDLE | 1.62 | 3.15 | 0.65 | -0.01 | 11001.43 | 23.63 | skipped_fast |
| KITEUSDT | IDLE | 1.19 | 2.35 | 0.58 | 0.06 | 76005.29 | 9.05 | skipped_fast |
| FLUIDUSDT | IDLE | 2.44 | 4.83 | 0.4 | 0.06 | 248.11 | 21.63 | skipped_fast |
| QNTUSDT | IDLE | 1.16 | 2.11 | 1.37 | 0.01 | 45888.2 | 6.39 | skipped_fast |
| RIZEUSDT | IDLE | 0.24 | 3.05 | 1.88 | 0.16 | 53542.84 | 91.15 | skipped_fast |
| RWAUSDT | IDLE | 1.24 | 2.23 | 1.68 | 0.01 | 58839.49 | 96.47 | skipped_fast |
| MNSRYUSDT | IDLE | 0.15 | 0.29 | 0.03 | 0.03 | 42576.13 | 8.17 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
