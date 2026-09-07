# Hulk DIGEST — 2026-09-07T02:34:19Z

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
| XRPUSDT | IDLE | 1.01 | 1.84 | 1.18 | -0.0 | 26367708.45 | 2.13 | skipped_fast |
| ETHUSDT | IDLE | 0.76 | 1.43 | 0.61 | 0.0 | 265929370.54 | 0.4 | skipped_fast |
| BTCUSDT | IDLE | 0.61 | 1.12 | 0.64 | 0.0 | 367754874.23 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.49 | 4.69 | 1.96 | 0.03 | 602134.56 | 1.77 | skipped_fast |
| CHIPUSDT | IDLE | 1.75 | 3.59 | 2.41 | -0.02 | 399587.91 | 1.72 | skipped_fast |
| CCUSDT | IDLE | 1.63 | 3.03 | 1.54 | -0.0 | 378065.02 | 8.16 | skipped_fast |
| WUSDT | IDLE | 1.44 | 2.76 | 0.83 | 0.03 | 401444.03 | 11.5 | skipped_fast |
| RWAINCUSDT | IDLE | 2.6 | 10.32 | 4.07 | 0.12 | 6209.61 | 67.31 | skipped_fast |
| ZBCNUSDT | IDLE | 1.79 | 3.35 | 1.54 | 0.01 | 135701.85 | 8.58 | skipped_fast |
| REDUSDT | IDLE | 1.88 | 3.35 | 2.7 | 0.01 | 67194.8 | 11.84 | skipped_fast |
| BIOUSDT | IDLE | 1.65 | 2.95 | 2.37 | -0.03 | 79553.43 | 3.67 | skipped_fast |
| TELUSDT | IDLE | 3.1 | 5.56 | 4.23 | 0.02 | 94979.13 | 45.87 | skipped_fast |
| RIZEUSDT | IDLE | 1.3 | 11.02 | 6.2 | -0.19 | 69140.16 | 64.56 | skipped_fast |
| EDELUSDT | IDLE | 1.65 | 3.29 | 0.09 | 0.01 | 49508.38 | 9.37 | skipped_fast |
| HBARUSDT | IDLE | 1.1 | 2.01 | 1.24 | -0.0 | 448621.43 | 1.23 | skipped_fast |
| KITEUSDT | IDLE | 1.02 | 1.9 | 0.98 | -0.02 | 58112.99 | 11.1 | skipped_fast |
| FLUIDUSDT | IDLE | 0.98 | 1.7 | 1.67 | 0.0 | 893.17 | 21.18 | skipped_fast |
| QNTUSDT | IDLE | 0.63 | 1.19 | 0.51 | 0.01 | 38252.62 | 1.5 | skipped_fast |
| RWAUSDT | IDLE | 0.48 | 0.87 | 0.64 | -0.01 | 53502.34 | 14.4 | skipped_fast |
| MNSRYUSDT | IDLE | 0.09 | 0.17 | 0.07 | 0.01 | 40241.68 | 6.72 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
