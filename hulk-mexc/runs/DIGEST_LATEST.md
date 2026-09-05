# Hulk DIGEST — 2026-09-05T17:29:32Z

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
| XRPUSDT | IDLE | 0.72 | 1.4 | 0.3 | 0.01 | 21663970.25 | 1.41 | skipped_fast |
| ETHUSDT | IDLE | 0.65 | 1.28 | 0.18 | 0.01 | 174484830.51 | 1.09 | skipped_fast |
| BTCUSDT | IDLE | 0.42 | 0.81 | 0.26 | 0.01 | 341759797.07 | 0.0 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 2.59 | 8.91 | 5.04 | 0.06 | 481936.99 | 24.49 | skipped_fast |
| RWAINCUSDT | IDLE | 2.87 | 5.2 | 3.64 | -0.01 | 7555.5 | 5.4 | skipped_fast |
| KITEUSDT | IDLE | 2.31 | 5.35 | 4.15 | -0.06 | 61359.15 | 8.72 | skipped_fast |
| PYTHUSDT | IDLE | 1.26 | 2.38 | 0.97 | 0.01 | 326163.29 | 1.82 | skipped_fast |
| CCUSDT | IDLE | 1.49 | 2.8 | 1.25 | 0.03 | 282923.29 | 9.08 | skipped_fast |
| ZBCNUSDT | IDLE | 1.47 | 2.67 | 1.83 | -0.01 | 169625.44 | 14.32 | skipped_fast |
| WUSDT | IDLE | 1.45 | 2.65 | 1.7 | 0.02 | 150459.82 | 7.05 | skipped_fast |
| BIOUSDT | IDLE | 1.56 | 3.0 | 0.75 | 0.04 | 78350.0 | 7.16 | skipped_fast |
| EDELUSDT | IDLE | 0.27 | 4.79 | 2.15 | -0.02 | 175820.17 | 19.05 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.52 | 23.03 | 6.01 | 0.26 | 146578.32 | 445.85 | skipped_fast |
| REDUSDT | IDLE | 0.9 | 1.65 | 0.97 | 0.02 | 61040.24 | 10.39 | skipped_fast |
| HBARUSDT | IDLE | 0.86 | 1.52 | 1.32 | 0.04 | 314343.84 | 1.24 | skipped_fast |
| RWAUSDT | IDLE | 1.54 | 3.02 | 0.42 | 0.03 | 52027.12 | 14.0 | skipped_fast |
| TELUSDT | IDLE | 1.12 | 2.2 | 0.23 | -0.01 | 68765.7 | 46.62 | skipped_fast |
| QNTUSDT | IDLE | 0.62 | 1.21 | 0.17 | 0.0 | 40192.82 | 6.21 | skipped_fast |
| FLUIDUSDT | IDLE | 0.76 | 1.43 | 0.62 | 0.01 | 897.41 | 21.83 | skipped_fast |
| MNSRYUSDT | IDLE | 0.16 | 0.3 | 0.07 | 0.0 | 38398.75 | 12.28 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
