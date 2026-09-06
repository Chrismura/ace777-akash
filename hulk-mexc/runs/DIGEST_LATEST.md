# Hulk DIGEST — 2026-09-06T12:31:59Z

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
| XRPUSDT | IDLE | 0.59 | 1.17 | 0.01 | 0.01 | 25734240.91 | 1.4 | skipped_fast |
| ETHUSDT | IDLE | 0.49 | 0.96 | 0.15 | 0.02 | 232720043.3 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.27 | 0.54 | 0.05 | 0.0 | 405806133.21 | 0.0 | skipped_fast |
| CHIPUSDT | IDLE | 2.9 | 7.32 | 3.8 | 0.07 | 406462.44 | 1.69 | skipped_fast |
| PYTHUSDT | IDLE | 1.61 | 3.1 | 0.77 | 0.03 | 452492.1 | 1.79 | skipped_fast |
| WUSDT | IDLE | 2.31 | 4.39 | 1.53 | 0.03 | 205436.78 | 8.77 | skipped_fast |
| RWAINCUSDT | IDLE | 2.87 | 6.17 | 3.51 | 0.04 | 7549.11 | 25.99 | skipped_fast |
| REDUSDT | IDLE | 2.44 | 4.59 | 1.89 | 0.02 | 61091.06 | 12.47 | skipped_fast |
| CCUSDT | IDLE | 1.09 | 2.07 | 0.74 | 0.01 | 318653.56 | 10.85 | skipped_fast |
| RIZEUSDT | IDLE | 1.75 | 9.49 | 6.02 | -0.03 | 86748.6 | 59.68 | skipped_fast |
| ZBCNUSDT | IDLE | 1.31 | 2.37 | 1.73 | -0.01 | 198920.27 | 21.23 | skipped_fast |
| KITEUSDT | IDLE | 1.47 | 2.57 | 2.43 | -0.03 | 65169.28 | 12.68 | skipped_fast |
| EDELUSDT | IDLE | 1.41 | 2.63 | 1.28 | 0.02 | 66911.14 | 18.55 | skipped_fast |
| HBARUSDT | IDLE | 0.71 | 1.37 | 0.33 | 0.01 | 462754.94 | 1.23 | skipped_fast |
| BIOUSDT | IDLE | 0.91 | 1.78 | 0.32 | 0.01 | 92665.44 | 10.75 | skipped_fast |
| QNTUSDT | IDLE | 0.82 | 1.53 | 0.78 | 0.03 | 39377.86 | 4.56 | skipped_fast |
| TELUSDT | IDLE | 0.9 | 1.65 | 0.98 | 0.01 | 69020.02 | 58.34 | skipped_fast |
| MNSRYUSDT | IDLE | 0.61 | 1.15 | 0.51 | 0.02 | 42613.07 | 12.07 | skipped_fast |
| RWAUSDT | IDLE | 0.49 | 0.93 | 0.35 | 0.0 | 52604.08 | 7.12 | skipped_fast |
| FLUIDUSDT | IDLE | 0.0 | 0.0 | 0.0 | 0.02 | 353.17 | 21.89 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
