# Hulk DIGEST — 2026-09-26T00:48:02Z

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
| XRPUSDT | IDLE | 0.9 | 1.7 | 0.71 | 0.01 | 112353281.53 | 0.64 | skipped_fast |
| ETHUSDT | IDLE | 0.38 | 0.71 | 0.36 | -0.0 | 319728358.51 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.35 | 0.65 | 0.33 | -0.01 | 685466033.23 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.95 | 5.19 | 1.98 | 0.08 | 1248866.13 | 5.42 | skipped_fast |
| CCUSDT | IDLE | 1.23 | 4.89 | 1.21 | 0.15 | 886348.67 | 8.39 | skipped_fast |
| HBARUSDT | IDLE | 1.34 | 2.48 | 1.36 | 0.01 | 916114.39 | 1.05 | skipped_fast |
| WUSDT | IDLE | 1.98 | 3.86 | 1.19 | 0.04 | 453411.51 | 10.52 | skipped_fast |
| ZBCNUSDT | IDLE | 2.0 | 4.37 | 4.13 | 0.05 | 237518.61 | 36.82 | skipped_fast |
| EDELUSDT | IDLE | 1.8 | 3.25 | 2.32 | -0.01 | 179847.75 | 6.78 | skipped_fast |
| CHIPUSDT | IDLE | 1.75 | 4.72 | 2.17 | 0.04 | 157042.55 | 18.11 | skipped_fast |
| QNTUSDT | IDLE | 0.76 | 3.26 | 1.18 | 0.09 | 565332.93 | 9.14 | skipped_fast |
| RIZEUSDT | IDLE | 0.79 | 11.71 | 8.08 | -0.0 | 107963.1 | 41.86 | skipped_fast |
| BIOUSDT | IDLE | 1.14 | 3.35 | 1.35 | 0.07 | 116495.17 | 6.08 | skipped_fast |
| REDUSDT | IDLE | 0.87 | 1.86 | 1.08 | 0.08 | 112590.53 | 14.38 | skipped_fast |
| KITEUSDT | IDLE | 0.93 | 1.86 | 0.04 | 0.03 | 79176.64 | 9.71 | skipped_fast |
| RWAINCUSDT | IDLE | 0.68 | 2.15 | 0.75 | -0.09 | 13425.63 | 76.05 | skipped_fast |
| TELUSDT | IDLE | 1.2 | 2.15 | 1.68 | 0.01 | 113681.5 | 60.83 | skipped_fast |
| MNSRYUSDT | IDLE | 0.49 | 0.88 | 0.73 | 0.02 | 41350.63 | 5.09 | skipped_fast |
| RWAUSDT | IDLE | 0.67 | 1.26 | 0.51 | -0.01 | 54342.05 | 59.04 | skipped_fast |
| FLUIDUSDT | IDLE | 0.23 | 0.4 | 0.4 | 0.03 | 3306.61 | 21.41 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
