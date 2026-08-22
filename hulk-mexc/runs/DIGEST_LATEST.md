# Hulk DIGEST — 2026-08-22T15:35:27Z

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
| PYTHUSDT | IDLE | 1.56 | 7.62 | 0.7 | 0.05 | 51501927.59 | 1.96 | skipped_fast |
| XRPUSDT | IDLE | 1.34 | 7.49 | 5.19 | 0.03 | 215255059.71 | 2.07 | skipped_fast |
| CCUSDT | IDLE | 1.35 | 5.65 | 3.59 | 0.08 | 796059.03 | 11.24 | skipped_fast |
| HBARUSDT | IDLE | 0.85 | 3.03 | 2.25 | -0.02 | 1160114.47 | 6.53 | skipped_fast |
| CHIPUSDT | IDLE | 0.62 | 3.51 | 2.09 | -0.09 | 604367.7 | 3.39 | skipped_fast |
| WUSDT | IDLE | 0.77 | 3.17 | 1.5 | -0.02 | 554914.15 | 15.98 | skipped_fast |
| KITEUSDT | IDLE | 2.73 | 6.37 | 1.65 | 0.03 | 85200.44 | 10.7 | skipped_fast |
| ZBCNUSDT | IDLE | 1.3 | 3.49 | 1.63 | -0.04 | 321927.02 | 7.69 | skipped_fast |
| BIOUSDT | IDLE | 0.97 | 6.58 | 4.73 | -0.07 | 221136.1 | 3.3 | skipped_fast |
| REDUSDT | IDLE | 0.53 | 5.67 | 4.79 | -0.08 | 146289.6 | 11.96 | skipped_fast |
| EDELUSDT | IDLE | 1.39 | 2.52 | 1.79 | -0.04 | 78974.96 | 34.15 | skipped_fast |
| QAITUSDT | IDLE | 1.99 | 3.76 | 1.48 | 0.01 | 2320.37 | 67.45 | skipped_fast |
| RIZEUSDT | IDLE | 0.79 | 3.28 | 0.29 | 0.03 | 56478.71 | 23.62 | skipped_fast |
| QNTUSDT | IDLE | 0.86 | 2.69 | 2.04 | -0.02 | 185204.73 | 3.15 | skipped_fast |
| RWAINCUSDT | IDLE | 0.77 | 1.53 | 0.0 | 0.01 | 9767.54 | 69.84 | skipped_fast |
| TELUSDT | IDLE | 1.11 | 2.75 | 1.58 | -0.01 | 140612.56 | 48.04 | skipped_fast |
| FLUIDUSDT | IDLE | 0.98 | 1.87 | 1.32 | -0.04 | 4625.53 | 15.7 | skipped_fast |
| RWAUSDT | IDLE | 0.65 | 1.23 | 0.4 | 0.02 | 57392.46 | 8.12 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
