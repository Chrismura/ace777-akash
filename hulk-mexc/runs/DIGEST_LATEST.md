# Hulk DIGEST — 2026-10-10T10:47:44Z

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
| XRPUSDT | IDLE | 0.44 | 0.79 | 0.56 | 0.01 | 22030943.2 | 1.42 | skipped_fast |
| BTCUSDT | IDLE | 0.2 | 0.37 | 0.15 | 0.0 | 237335244.32 | 0.0 | skipped_fast |
| ETHUSDT | IDLE | 0.15 | 0.27 | 0.14 | 0.0 | 107436073.69 | 0.04 | skipped_fast |
| WUSDT | IDLE | 1.87 | 3.79 | 2.31 | -0.04 | 1277234.94 | 8.89 | skipped_fast |
| PYTHUSDT | IDLE | 1.07 | 2.92 | 2.56 | -0.07 | 1331844.28 | 2.56 | skipped_fast |
| QNTUSDT | IDLE | 1.95 | 3.57 | 2.19 | 0.02 | 1222971.41 | 1.21 | skipped_fast |
| EDELUSDT | IDLE | 2.46 | 7.89 | 2.31 | 0.1 | 236490.95 | 2.52 | skipped_fast |
| CCUSDT | IDLE | 1.16 | 2.08 | 1.6 | -0.01 | 470389.69 | 10.8 | skipped_fast |
| KITEUSDT | IDLE | 2.34 | 4.47 | 1.34 | 0.02 | 77277.51 | 8.75 | skipped_fast |
| ZBCNUSDT | IDLE | 0.72 | 1.51 | 0.47 | -0.06 | 261937.79 | 13.99 | skipped_fast |
| CHIPUSDT | IDLE | 1.17 | 3.78 | 2.77 | 0.08 | 98863.53 | 11.4 | skipped_fast |
| REDUSDT | IDLE | 1.46 | 2.64 | 1.84 | 0.02 | 56167.33 | 14.76 | skipped_fast |
| RWAINCUSDT | IDLE | 1.99 | 3.65 | 2.24 | 0.01 | 13251.17 | 73.51 | skipped_fast |
| BIOUSDT | IDLE | 1.02 | 1.82 | 1.48 | 0.03 | 71894.41 | 3.49 | skipped_fast |
| HBARUSDT | IDLE | 0.84 | 1.51 | 1.1 | 0.02 | 336681.55 | 3.25 | skipped_fast |
| RWAUSDT | IDLE | 1.66 | 2.92 | 2.68 | -0.01 | 53118.09 | 7.87 | skipped_fast |
| TELUSDT | IDLE | 1.63 | 2.95 | 2.07 | -0.02 | 115252.68 | 43.36 | skipped_fast |
| RIZEUSDT | IDLE | 0.31 | 1.72 | 0.69 | 0.12 | 62188.08 | 55.52 | skipped_fast |
| MNSRYUSDT | IDLE | 0.39 | 0.77 | 0.13 | 0.01 | 40750.98 | 4.05 | skipped_fast |
| FLUIDUSDT | IDLE | 0.24 | 1.42 | 0.83 | 0.02 | 17321.99 | 21.24 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
