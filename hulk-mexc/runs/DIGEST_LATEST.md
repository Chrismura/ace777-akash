# Hulk DIGEST — 2026-09-12T06:21:40Z

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
| XRPUSDT | IDLE | 0.36 | 0.77 | 0.18 | 0.01 | 51226719.38 | 0.73 | skipped_fast |
| ETHUSDT | IDLE | 0.15 | 0.32 | 0.18 | 0.02 | 615232692.42 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.14 | 0.26 | 0.19 | -0.0 | 571228166.36 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.58 | 3.21 | 0.47 | 0.01 | 428233.08 | 3.81 | skipped_fast |
| CCUSDT | IDLE | 1.49 | 2.79 | 1.3 | 0.0 | 417335.48 | 5.06 | skipped_fast |
| RWAINCUSDT | IDLE | 1.92 | 3.83 | 1.74 | 0.01 | 15545.41 | 5.53 | skipped_fast |
| REDUSDT | IDLE | 1.62 | 4.03 | 3.41 | 0.04 | 65345.39 | 17.28 | skipped_fast |
| ZBCNUSDT | IDLE | 1.21 | 2.4 | 0.07 | -0.01 | 187539.41 | 8.87 | skipped_fast |
| CHIPUSDT | IDLE | 1.21 | 3.3 | 2.33 | 0.04 | 115075.0 | 14.75 | skipped_fast |
| KITEUSDT | IDLE | 1.49 | 2.6 | 2.53 | -0.01 | 58857.85 | 12.23 | skipped_fast |
| WUSDT | IDLE | 0.77 | 1.55 | 0.53 | 0.01 | 194835.14 | 9.2 | skipped_fast |
| EDELUSDT | IDLE | 0.91 | 2.6 | 0.87 | 0.06 | 166949.12 | 26.44 | skipped_fast |
| BIOUSDT | IDLE | 0.68 | 1.23 | 0.86 | 0.01 | 81127.37 | 7.89 | skipped_fast |
| RIZEUSDT | IDLE | 0.12 | 7.74 | 4.88 | 0.72 | 186683.82 | 102.62 | skipped_fast |
| HBARUSDT | IDLE | 0.45 | 0.82 | 0.56 | -0.01 | 264829.47 | 1.35 | skipped_fast |
| TELUSDT | IDLE | 0.71 | 1.6 | 1.34 | -0.03 | 94608.86 | 35.55 | skipped_fast |
| QNTUSDT | IDLE | 0.6 | 1.1 | 0.61 | -0.01 | 43721.48 | 4.68 | skipped_fast |
| RWAUSDT | IDLE | 0.38 | 0.74 | 0.15 | 0.03 | 53202.37 | 7.4 | skipped_fast |
| MNSRYUSDT | IDLE | 0.38 | 0.7 | 0.4 | 0.01 | 28987.46 | 13.89 | skipped_fast |
| FLUIDUSDT | IDLE | 0.0 | 0.0 | 0.0 | 0.01 | 1927.49 | 20.47 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
