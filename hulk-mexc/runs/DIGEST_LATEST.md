# Hulk DIGEST — 2026-09-10T15:13:57Z

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
| ETHUSDT | IDLE | 1.47 | 2.77 | 1.19 | -0.02 | 425783970.37 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 1.38 | 2.51 | 1.7 | -0.04 | 45056572.98 | 2.21 | skipped_fast |
| BTCUSDT | IDLE | 0.94 | 1.74 | 0.93 | -0.01 | 553830124.88 | 0.05 | skipped_fast |
| PYTHUSDT | IDLE | 1.42 | 4.14 | 1.38 | -0.05 | 977224.25 | 1.92 | skipped_fast |
| RIZEUSDT | IDLE | 1.23 | 68.27 | 12.63 | -0.48 | 124628.98 | 105.72 | skipped_fast |
| CCUSDT | IDLE | 1.44 | 2.68 | 1.36 | -0.03 | 676633.91 | 9.89 | skipped_fast |
| ZBCNUSDT | IDLE | 2.48 | 4.54 | 2.79 | 0.03 | 184684.98 | 29.37 | skipped_fast |
| EDELUSDT | IDLE | 1.72 | 6.28 | 4.35 | 0.03 | 227491.15 | 27.24 | skipped_fast |
| WUSDT | IDLE | 0.87 | 2.5 | 0.21 | -0.04 | 240976.05 | 3.12 | skipped_fast |
| BIOUSDT | IDLE | 1.51 | 2.96 | 2.06 | -0.06 | 78216.7 | 7.94 | skipped_fast |
| KITEUSDT | IDLE | 1.21 | 2.62 | 0.96 | -0.05 | 56139.07 | 11.91 | skipped_fast |
| HBARUSDT | IDLE | 1.21 | 2.27 | 1.05 | -0.03 | 318340.65 | 1.32 | skipped_fast |
| CHIPUSDT | IDLE | 0.67 | 3.6 | 2.43 | -0.17 | 92005.52 | 14.77 | skipped_fast |
| REDUSDT | IDLE | 1.0 | 2.57 | 0.72 | -0.06 | 66601.8 | 19.55 | skipped_fast |
| RWAINCUSDT | IDLE | 1.09 | 1.93 | 1.61 | -0.03 | 5010.44 | 45.25 | skipped_fast |
| TELUSDT | IDLE | 1.87 | 3.48 | 1.71 | -0.03 | 82190.38 | 50.52 | skipped_fast |
| FLUIDUSDT | IDLE | 1.75 | 3.36 | 2.33 | -0.08 | 2246.54 | 21.78 | skipped_fast |
| RWAUSDT | IDLE | 1.31 | 2.37 | 1.72 | -0.04 | 53924.2 | 7.6 | skipped_fast |
| QNTUSDT | IDLE | 1.36 | 2.53 | 1.25 | -0.02 | 39736.41 | 9.15 | skipped_fast |
| MNSRYUSDT | IDLE | 0.99 | 1.76 | 1.42 | -0.03 | 26568.89 | 51.71 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
