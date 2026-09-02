# Hulk DIGEST — 2026-09-02T13:43:48Z

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
| XRPUSDT | IDLE | 1.44 | 2.78 | 0.66 | -0.02 | 38865605.35 | 2.24 | skipped_fast |
| ETHUSDT | IDLE | 1.41 | 2.69 | 0.88 | -0.02 | 402468990.34 | 0.04 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.78 | 10.87 | 9.51 | 0.03 | 925362.55 | 9.49 | skipped_fast |
| BTCUSDT | IDLE | 0.87 | 1.66 | 0.49 | -0.0 | 523517779.45 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 0.99 | 3.44 | 0.38 | 0.11 | 884093.22 | 3.63 | skipped_fast |
| WUSDT | IDLE | 1.85 | 3.33 | 2.46 | -0.01 | 412255.71 | 13.75 | skipped_fast |
| CCUSDT | IDLE | 1.8 | 3.19 | 2.76 | -0.06 | 352012.99 | 8.12 | skipped_fast |
| REDUSDT | IDLE | 2.5 | 5.23 | 0.0 | 0.06 | 151789.12 | 10.34 | skipped_fast |
| KITEUSDT | IDLE | 1.58 | 6.19 | 1.28 | 0.15 | 87642.3 | 9.42 | skipped_fast |
| ZBCNUSDT | IDLE | 0.94 | 1.99 | 0.93 | -0.01 | 207549.78 | 13.76 | skipped_fast |
| EDELUSDT | IDLE | 1.01 | 5.46 | 3.11 | 0.06 | 172450.67 | 49.38 | skipped_fast |
| RIZEUSDT | IDLE | 1.68 | 6.78 | 2.46 | -0.08 | 39822.99 | 74.39 | skipped_fast |
| BIOUSDT | IDLE | 1.26 | 2.4 | 0.82 | -0.03 | 72336.33 | 19.74 | skipped_fast |
| QNTUSDT | IDLE | 2.06 | 3.77 | 2.38 | 0.02 | 70048.49 | 3.12 | skipped_fast |
| RWAINCUSDT | IDLE | 1.35 | 3.84 | 2.85 | 0.07 | 11101.7 | 87.58 | skipped_fast |
| HBARUSDT | IDLE | 0.92 | 1.79 | 0.39 | -0.01 | 223045.48 | 1.35 | skipped_fast |
| TELUSDT | IDLE | 1.47 | 2.9 | 0.29 | -0.01 | 84552.56 | 41.14 | skipped_fast |
| FLUIDUSDT | IDLE | 1.44 | 2.52 | 2.4 | -0.05 | 427.28 | 20.45 | skipped_fast |
| RWAUSDT | IDLE | 0.4 | 0.77 | 0.23 | -0.0 | 51055.57 | 23.07 | skipped_fast |
| MNSRYUSDT | IDLE | 0.4 | 0.73 | 0.49 | -0.01 | 35345.45 | 31.7 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
