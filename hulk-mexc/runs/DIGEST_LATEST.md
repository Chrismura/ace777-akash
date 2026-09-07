# Hulk DIGEST — 2026-09-07T00:33:02Z

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
| ETHUSDT | IDLE | 0.75 | 1.47 | 0.23 | 0.01 | 282361556.03 | 0.12 | skipped_fast |
| XRPUSDT | IDLE | 0.64 | 1.25 | 0.18 | 0.01 | 24654207.09 | 2.81 | skipped_fast |
| BTCUSDT | IDLE | 0.59 | 1.12 | 0.38 | 0.0 | 359785906.52 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 3.03 | 5.95 | 0.71 | 0.02 | 606158.53 | 3.5 | skipped_fast |
| CHIPUSDT | IDLE | 1.95 | 4.31 | 0.59 | -0.01 | 413164.33 | 3.38 | skipped_fast |
| RWAINCUSDT | IDLE | 3.08 | 13.68 | 2.73 | 0.13 | 5876.28 | 57.03 | skipped_fast |
| WUSDT | IDLE | 1.48 | 2.9 | 0.44 | 0.03 | 406732.96 | 12.41 | skipped_fast |
| CCUSDT | IDLE | 1.56 | 3.03 | 0.66 | 0.02 | 371362.79 | 8.98 | skipped_fast |
| ZBCNUSDT | IDLE | 1.79 | 3.35 | 1.54 | 0.01 | 146099.12 | 14.48 | skipped_fast |
| TELUSDT | IDLE | 3.32 | 5.99 | 4.39 | 0.02 | 96280.61 | 28.68 | skipped_fast |
| RIZEUSDT | IDLE | 2.38 | 20.29 | 10.07 | -0.14 | 72496.51 | 221.69 | skipped_fast |
| EDELUSDT | IDLE | 1.73 | 3.09 | 2.44 | -0.01 | 48959.35 | 19.27 | skipped_fast |
| REDUSDT | IDLE | 1.59 | 2.77 | 2.7 | -0.0 | 67691.21 | 18.96 | skipped_fast |
| HBARUSDT | IDLE | 1.09 | 2.18 | 0.0 | 0.02 | 446477.03 | 1.22 | skipped_fast |
| KITEUSDT | IDLE | 1.19 | 2.25 | 0.83 | 0.0 | 57481.82 | 10.29 | skipped_fast |
| BIOUSDT | IDLE | 0.8 | 1.57 | 0.18 | -0.01 | 92586.69 | 3.6 | skipped_fast |
| QNTUSDT | IDLE | 1.04 | 2.02 | 0.34 | 0.03 | 37634.89 | 8.96 | skipped_fast |
| FLUIDUSDT | IDLE | 0.8 | 1.59 | 0.0 | 0.03 | 309.53 | 21.78 | skipped_fast |
| RWAUSDT | IDLE | 0.35 | 0.65 | 0.36 | -0.03 | 53742.91 | 14.36 | skipped_fast |
| MNSRYUSDT | IDLE | 0.1 | 0.19 | 0.04 | 0.02 | 40687.0 | 5.37 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
