# Hulk DIGEST — 2026-08-21T22:27:28Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : XRPUSDT, HBARUSDT, QAITUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT
- Watch only : QNTUSDT, FLUIDUSDT, RWAUSDT

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| PYTHUSDT | IDLE | 1.36 | 5.17 | 0.24 | 0.11 | 5776731.87 | 2.04 | skipped_fast |
| XRPUSDT | IDLE | 1.55 | 5.68 | 0.23 | 0.14 | 133911469.61 | 3.48 | skipped_fast |
| CCUSDT | IDLE | 1.76 | 6.48 | 0.14 | 0.13 | 650087.39 | 8.01 | skipped_fast |
| HBARUSDT | IDLE | 2.2 | 4.71 | 0.62 | 0.08 | 857164.46 | 1.26 | skipped_fast |
| WUSDT | IDLE | 2.46 | 5.3 | 0.24 | 0.08 | 370795.04 | 11.31 | skipped_fast |
| CHIPUSDT | IDLE | 1.48 | 4.54 | 1.21 | 0.06 | 534234.72 | 3.05 | skipped_fast |
| ZBCNUSDT | IDLE | 1.54 | 6.64 | 0.12 | 0.11 | 502741.1 | 18.18 | skipped_fast |
| BIOUSDT | IDLE | 2.28 | 5.04 | 0.89 | 0.03 | 187956.75 | 6.21 | skipped_fast |
| REDUSDT | IDLE | 1.32 | 11.01 | 8.0 | 0.18 | 156144.34 | 11.31 | skipped_fast |
| EDELUSDT | IDLE | 2.3 | 5.04 | 0.33 | -0.03 | 82605.33 | 32.8 | skipped_fast |
| TELUSDT | IDLE | 2.54 | 6.45 | 0.98 | 0.05 | 186907.48 | 15.54 | skipped_fast |
| QAITUSDT | IDLE | 2.37 | 4.38 | 2.37 | -0.02 | 3827.91 | 63.67 | skipped_fast |
| KITEUSDT | IDLE | 1.22 | 3.58 | 1.19 | 0.11 | 61373.96 | 12.92 | skipped_fast |
| RWAINCUSDT | IDLE | 2.13 | 4.07 | 1.27 | 0.03 | 10212.76 | 86.25 | skipped_fast |
| RIZEUSDT | IDLE | 0.95 | 4.7 | 1.69 | 0.06 | 56370.54 | 45.14 | skipped_fast |
| QNTUSDT | IDLE | 1.85 | 3.71 | 0.0 | 0.05 | 65341.98 | 6.09 | skipped_fast |
| RWAUSDT | IDLE | 0.88 | 1.75 | 0.08 | 0.03 | 54089.43 | 24.64 | skipped_fast |
| FLUIDUSDT | IDLE | 0.51 | 1.15 | 0.08 | 0.09 | 4171.26 | 7.02 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
