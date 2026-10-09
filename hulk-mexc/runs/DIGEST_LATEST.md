# Hulk DIGEST — 2026-10-09T22:33:38Z

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
| WUSDT | IDLE | 1.25 | 6.46 | 5.69 | 0.11 | 2153674.37 | 9.46 | skipped_fast |
| PYTHUSDT | IDLE | 2.17 | 5.42 | 3.44 | -0.03 | 1817076.78 | 2.48 | skipped_fast |
| XRPUSDT | IDLE | 0.51 | 1.02 | 0.01 | 0.01 | 26902555.21 | 0.72 | skipped_fast |
| ETHUSDT | IDLE | 0.39 | 0.75 | 0.17 | 0.01 | 197379263.42 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.33 | 0.62 | 0.26 | 0.01 | 275697642.76 | 0.0 | skipped_fast |
| QNTUSDT | IDLE | 1.21 | 2.79 | 0.1 | 0.05 | 1326648.53 | 4.82 | skipped_fast |
| CCUSDT | IDLE | 1.61 | 3.38 | 1.95 | 0.04 | 599707.11 | 4.91 | skipped_fast |
| CHIPUSDT | IDLE | 2.33 | 5.28 | 0.21 | 0.06 | 86368.38 | 13.56 | skipped_fast |
| ZBCNUSDT | IDLE | 1.46 | 4.37 | 3.35 | -0.04 | 237228.54 | 20.03 | skipped_fast |
| RIZEUSDT | IDLE | 1.67 | 9.39 | 5.09 | 0.15 | 71586.02 | 28.73 | skipped_fast |
| KITEUSDT | IDLE | 1.45 | 2.63 | 1.8 | -0.05 | 77626.12 | 11.73 | skipped_fast |
| HBARUSDT | IDLE | 1.08 | 2.15 | 0.09 | 0.0 | 369721.82 | 4.39 | skipped_fast |
| BIOUSDT | IDLE | 1.03 | 1.99 | 0.53 | -0.0 | 65394.36 | 3.56 | skipped_fast |
| EDELUSDT | IDLE | 0.5 | 2.67 | 0.44 | 0.19 | 224376.46 | 37.08 | skipped_fast |
| RWAINCUSDT | IDLE | 1.56 | 3.33 | 3.22 | -0.02 | 9806.98 | 72.2 | skipped_fast |
| FLUIDUSDT | IDLE | 1.85 | 12.05 | 0.16 | 0.08 | 18736.74 | 19.65 | skipped_fast |
| REDUSDT | IDLE | 0.75 | 1.41 | 0.66 | 0.02 | 62937.42 | 7.49 | skipped_fast |
| TELUSDT | IDLE | 2.0 | 3.6 | 2.62 | -0.01 | 109236.62 | 32.91 | skipped_fast |
| RWAUSDT | IDLE | 0.84 | 1.51 | 1.09 | -0.01 | 52543.54 | 7.9 | skipped_fast |
| MNSRYUSDT | IDLE | 0.25 | 0.48 | 0.15 | 0.0 | 39491.19 | 33.96 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
