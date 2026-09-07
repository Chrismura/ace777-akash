# Hulk DIGEST — 2026-09-07T14:47:34Z

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
| XRPUSDT | IDLE | 0.9 | 1.6 | 1.36 | -0.01 | 34145559.71 | 2.15 | skipped_fast |
| ETHUSDT | IDLE | 0.75 | 1.34 | 1.11 | 0.0 | 322926293.98 | 0.36 | skipped_fast |
| BTCUSDT | IDLE | 0.47 | 0.84 | 0.71 | -0.01 | 421966687.3 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.81 | 3.26 | 2.45 | 0.02 | 559070.85 | 1.81 | skipped_fast |
| CHIPUSDT | IDLE | 1.75 | 4.89 | 4.21 | -0.07 | 325799.08 | 13.15 | skipped_fast |
| REDUSDT | IDLE | 3.0 | 5.6 | 2.72 | 0.04 | 63537.67 | 9.11 | skipped_fast |
| CCUSDT | IDLE | 1.47 | 2.79 | 0.98 | -0.01 | 424532.61 | 12.99 | skipped_fast |
| WUSDT | IDLE | 1.28 | 2.26 | 2.03 | 0.01 | 408090.57 | 14.61 | skipped_fast |
| HBARUSDT | IDLE | 1.81 | 3.44 | 1.15 | 0.02 | 456388.84 | 1.22 | skipped_fast |
| ZBCNUSDT | IDLE | 1.59 | 2.81 | 2.48 | -0.01 | 193486.97 | 4.31 | skipped_fast |
| RIZEUSDT | IDLE | 1.82 | 8.34 | 5.77 | -0.1 | 61132.01 | 64.79 | skipped_fast |
| EDELUSDT | IDLE | 1.62 | 4.33 | 3.77 | -0.05 | 81241.27 | 30.11 | skipped_fast |
| BIOUSDT | IDLE | 1.19 | 2.14 | 1.66 | 0.01 | 69026.98 | 7.32 | skipped_fast |
| KITEUSDT | IDLE | 1.21 | 2.19 | 1.48 | -0.04 | 59124.46 | 11.54 | skipped_fast |
| MNSRYUSDT | IDLE | 2.78 | 5.37 | 1.32 | -0.01 | 38720.39 | 68.16 | skipped_fast |
| RWAINCUSDT | IDLE | 1.21 | 3.8 | 2.19 | 0.06 | 5765.37 | 53.31 | skipped_fast |
| TELUSDT | IDLE | 1.88 | 3.29 | 3.07 | 0.0 | 108826.59 | 35.21 | skipped_fast |
| QNTUSDT | IDLE | 1.16 | 2.12 | 1.28 | 0.0 | 46870.13 | 7.61 | skipped_fast |
| RWAUSDT | IDLE | 0.4 | 0.73 | 0.43 | -0.0 | 53002.12 | 28.92 | skipped_fast |
| FLUIDUSDT | IDLE | 0.0 | 0.0 | 0.0 | -0.01 | 1152.45 | 21.8 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
