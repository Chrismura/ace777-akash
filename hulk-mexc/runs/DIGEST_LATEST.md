# Hulk DIGEST — 2026-09-12T22:37:39Z

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
| ETHUSDT | IDLE | 0.41 | 0.75 | 0.52 | 0.0 | 217696564.83 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.4 | 0.7 | 0.63 | 0.01 | 15472287.36 | 1.47 | skipped_fast |
| BTCUSDT | IDLE | 0.24 | 0.44 | 0.26 | 0.0 | 358133513.25 | 0.0 | skipped_fast |
| RIZEUSDT | IDLE | 1.69 | 29.23 | 17.0 | 0.4 | 92329.49 | 68.55 | skipped_fast |
| PYTHUSDT | IDLE | 1.22 | 3.0 | 2.04 | 0.09 | 398684.9 | 1.83 | skipped_fast |
| WUSDT | IDLE | 2.02 | 3.63 | 2.78 | 0.04 | 171190.59 | 12.08 | skipped_fast |
| EDELUSDT | IDLE | 1.82 | 4.01 | 1.31 | 0.08 | 165851.34 | 24.87 | skipped_fast |
| ZBCNUSDT | IDLE | 1.41 | 3.49 | 1.69 | -0.01 | 216540.95 | 18.43 | skipped_fast |
| CHIPUSDT | IDLE | 1.88 | 4.14 | 3.55 | 0.02 | 74683.18 | 12.56 | skipped_fast |
| RWAINCUSDT | IDLE | 2.15 | 4.25 | 1.93 | -0.0 | 9853.98 | 5.47 | skipped_fast |
| CCUSDT | IDLE | 0.75 | 1.42 | 0.57 | 0.0 | 206784.87 | 8.21 | skipped_fast |
| REDUSDT | IDLE | 0.97 | 1.71 | 1.57 | 0.02 | 56755.64 | 8.48 | skipped_fast |
| BIOUSDT | IDLE | 0.83 | 1.46 | 1.32 | 0.02 | 68758.92 | 3.94 | skipped_fast |
| KITEUSDT | IDLE | 0.93 | 1.85 | 0.06 | -0.0 | 62923.43 | 12.99 | skipped_fast |
| HBARUSDT | IDLE | 0.58 | 1.09 | 0.4 | 0.01 | 138060.74 | 1.34 | skipped_fast |
| TELUSDT | IDLE | 0.85 | 1.52 | 1.19 | -0.05 | 88998.42 | 36.28 | skipped_fast |
| QNTUSDT | IDLE | 0.78 | 1.38 | 1.26 | 0.01 | 35818.49 | 7.86 | skipped_fast |
| RWAUSDT | IDLE | 0.34 | 0.6 | 0.52 | 0.0 | 53105.96 | 14.88 | skipped_fast |
| MNSRYUSDT | IDLE | 0.2 | 0.38 | 0.17 | -0.0 | 26623.22 | 11.12 | skipped_fast |
| FLUIDUSDT | IDLE | 0.0 | 0.0 | 0.0 | 0.03 | 1375.44 | 21.45 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
