# Hulk DIGEST — 2026-09-26T10:54:34Z

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
| XRPUSDT | IDLE | 0.72 | 1.37 | 0.48 | -0.01 | 107073863.4 | 1.94 | skipped_fast |
| ETHUSDT | IDLE | 0.36 | 0.66 | 0.38 | -0.01 | 254820584.75 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.27 | 0.51 | 0.19 | -0.01 | 554049635.09 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.9 | 4.32 | 0.04 | 0.07 | 1179355.39 | 1.31 | skipped_fast |
| CCUSDT | IDLE | 1.68 | 6.64 | 2.66 | 0.13 | 1022733.12 | 7.37 | skipped_fast |
| QNTUSDT | IDLE | 2.53 | 11.38 | 2.75 | 0.09 | 774918.32 | 12.15 | skipped_fast |
| WUSDT | IDLE | 2.31 | 5.86 | 0.22 | 0.07 | 491312.98 | 10.1 | skipped_fast |
| HBARUSDT | IDLE | 0.77 | 1.5 | 0.24 | 0.01 | 792119.53 | 1.06 | skipped_fast |
| RWAINCUSDT | IDLE | 3.37 | 7.06 | 0.52 | 0.06 | 5604.48 | 75.97 | skipped_fast |
| EDELUSDT | IDLE | 1.56 | 3.11 | 0.03 | 0.02 | 177456.04 | 3.31 | skipped_fast |
| CHIPUSDT | IDLE | 1.56 | 2.89 | 1.53 | -0.02 | 143927.49 | 14.34 | skipped_fast |
| ZBCNUSDT | IDLE | 1.12 | 2.17 | 0.49 | -0.02 | 228430.42 | 16.94 | skipped_fast |
| BIOUSDT | IDLE | 1.42 | 3.31 | 1.17 | 0.05 | 122516.94 | 6.06 | skipped_fast |
| RIZEUSDT | IDLE | 1.05 | 9.26 | 4.47 | -0.18 | 53274.7 | 25.03 | skipped_fast |
| KITEUSDT | IDLE | 1.33 | 2.89 | 1.95 | 0.03 | 76680.03 | 11.09 | skipped_fast |
| REDUSDT | IDLE | 0.99 | 1.78 | 1.37 | 0.01 | 59462.05 | 12.96 | skipped_fast |
| RWAUSDT | IDLE | 2.39 | 4.31 | 3.13 | -0.01 | 55727.06 | 29.39 | skipped_fast |
| TELUSDT | IDLE | 1.05 | 1.87 | 1.53 | -0.04 | 121486.16 | 43.49 | skipped_fast |
| FLUIDUSDT | IDLE | 0.91 | 1.82 | 0.0 | 0.01 | 3396.54 | 21.41 | skipped_fast |
| MNSRYUSDT | IDLE | 0.19 | 0.37 | 0.04 | 0.01 | 40247.2 | 8.92 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
