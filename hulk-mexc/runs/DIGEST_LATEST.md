# Hulk DIGEST — 2026-09-07T21:37:44Z

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
| XRPUSDT | IDLE | 0.75 | 1.45 | 0.38 | -0.02 | 36084311.41 | 2.15 | skipped_fast |
| ETHUSDT | IDLE | 0.61 | 1.18 | 0.26 | -0.01 | 340077380.08 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.4 | 0.77 | 0.26 | -0.01 | 451753338.33 | 0.0 | skipped_fast |
| ZBCNUSDT | IDLE | 3.21 | 8.9 | 2.79 | -0.03 | 216825.29 | 27.71 | skipped_fast |
| CCUSDT | IDLE | 1.59 | 2.99 | 1.96 | -0.05 | 475148.46 | 4.78 | skipped_fast |
| PYTHUSDT | IDLE | 0.85 | 1.57 | 0.82 | -0.02 | 529749.9 | 1.83 | skipped_fast |
| CHIPUSDT | IDLE | 1.96 | 7.86 | 2.23 | -0.07 | 224972.51 | 14.84 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 3.27 | 10.08 | 9.16 | -0.04 | 4686.96 | 94.59 | skipped_fast |
| HBARUSDT | IDLE | 1.48 | 2.86 | 0.69 | 0.01 | 582471.15 | 1.21 | skipped_fast |
| EDELUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.29 | 8.84 | 0.96 | -0.01 | 100668.56 | 57.8 | skipped_fast |
| WUSDT | IDLE | 1.17 | 2.28 | 0.38 | -0.01 | 260986.83 | 2.91 | skipped_fast |
| RIZEUSDT | IDLE | 1.87 | 5.63 | 2.34 | -0.08 | 59461.88 | 35.65 | skipped_fast |
| REDUSDT | IDLE | 1.26 | 2.38 | 0.94 | 0.02 | 58715.58 | 16.65 | skipped_fast |
| BIOUSDT | IDLE | 0.97 | 1.89 | 0.36 | -0.02 | 65436.35 | 10.97 | skipped_fast |
| KITEUSDT | IDLE | 0.97 | 1.74 | 1.3 | -0.05 | 61382.17 | 13.44 | skipped_fast |
| QNTUSDT | IDLE | 1.12 | 2.2 | 0.27 | -0.0 | 48006.39 | 3.0 | skipped_fast |
| TELUSDT | IDLE | 1.03 | 1.89 | 1.16 | -0.05 | 107076.04 | 35.19 | skipped_fast |
| FLUIDUSDT | IDLE | 0.7 | 1.41 | 0.0 | 0.0 | 1656.62 | 0.78 | skipped_fast |
| RWAUSDT | IDLE | 0.4 | 0.73 | 0.51 | -0.01 | 54455.89 | 14.53 | skipped_fast |
| MNSRYUSDT | IDLE | 0.42 | 0.74 | 0.61 | -0.02 | 37411.87 | 66.75 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
