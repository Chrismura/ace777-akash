# Hulk DIGEST — 2026-09-06T23:46:35Z

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
| ETHUSDT | IDLE | 0.68 | 1.34 | 0.09 | 0.02 | 276235059.91 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.64 | 1.25 | 0.25 | 0.01 | 24217165.52 | 2.11 | skipped_fast |
| BTCUSDT | IDLE | 0.52 | 1.03 | 0.08 | 0.01 | 346055986.51 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.56 | 5.04 | 0.55 | 0.02 | 597117.67 | 3.53 | skipped_fast |
| WUSDT | IDLE | 2.49 | 4.56 | 2.76 | 0.03 | 410416.96 | 11.55 | skipped_fast |
| CHIPUSDT | IDLE | 1.83 | 4.0 | 0.98 | -0.01 | 413875.63 | 1.7 | skipped_fast |
| RIZEUSDT | IDLE | 2.44 | 20.29 | 13.64 | -0.16 | 73521.7 | 140.28 | skipped_fast |
| CCUSDT | IDLE | 1.45 | 2.74 | 1.1 | 0.01 | 364663.3 | 9.95 | skipped_fast |
| RWAINCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.82 | 10.47 | 0.52 | 0.11 | 5753.61 | 38.04 | skipped_fast |
| ZBCNUSDT | IDLE | 1.81 | 3.35 | 1.84 | 0.0 | 154966.43 | 17.75 | skipped_fast |
| TELUSDT | IDLE | 3.42 | 6.24 | 3.95 | 0.03 | 94240.19 | 45.61 | skipped_fast |
| REDUSDT | IDLE | 1.43 | 2.52 | 2.23 | 0.01 | 67359.25 | 17.28 | skipped_fast |
| HBARUSDT | IDLE | 1.0 | 1.93 | 0.45 | 0.02 | 421557.76 | 1.23 | skipped_fast |
| EDELUSDT | IDLE | 1.66 | 3.09 | 1.5 | -0.02 | 50657.14 | 57.14 | skipped_fast |
| KITEUSDT | IDLE | 1.03 | 2.02 | 0.32 | 0.01 | 57768.31 | 10.26 | skipped_fast |
| BIOUSDT | IDLE | 0.81 | 1.57 | 0.29 | -0.0 | 92040.62 | 3.59 | skipped_fast |
| QNTUSDT | IDLE | 1.21 | 2.38 | 0.33 | 0.03 | 37692.14 | 5.97 | skipped_fast |
| FLUIDUSDT | IDLE | 0.8 | 1.59 | 0.0 | 0.03 | 309.53 | 21.68 | skipped_fast |
| RWAUSDT | IDLE | 0.47 | 0.87 | 0.5 | -0.03 | 53769.28 | 14.38 | skipped_fast |
| MNSRYUSDT | IDLE | 0.1 | 0.19 | 0.05 | 0.02 | 40886.3 | 9.41 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
