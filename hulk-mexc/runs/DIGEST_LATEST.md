# Hulk DIGEST — 2026-09-26T09:54:25Z

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
| XRPUSDT | IDLE | 0.95 | 1.69 | 1.42 | -0.01 | 108224881.42 | 1.95 | skipped_fast |
| ETHUSDT | IDLE | 0.37 | 0.66 | 0.58 | -0.01 | 261960713.71 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.3 | 0.54 | 0.38 | -0.01 | 565726105.64 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.22 | 4.76 | 1.43 | 0.07 | 1206483.39 | 2.66 | skipped_fast |
| CCUSDT | IDLE | 1.7 | 7.25 | 2.99 | 0.15 | 1045716.79 | 7.4 | skipped_fast |
| WUSDT | IDLE | 2.26 | 4.98 | 1.77 | 0.06 | 480574.18 | 3.18 | skipped_fast |
| QNTUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.29 | 9.16 | 0.58 | 0.1 | 753178.65 | 18.65 | skipped_fast |
| HBARUSDT | IDLE | 0.81 | 1.46 | 1.09 | 0.01 | 811641.37 | 1.07 | skipped_fast |
| KITEUSDT | IDLE | 2.04 | 4.32 | 3.85 | 0.03 | 74879.3 | 8.18 | skipped_fast |
| ZBCNUSDT | IDLE | 1.3 | 2.69 | 1.35 | 0.03 | 250237.53 | 27.39 | skipped_fast |
| EDELUSDT | IDLE | 1.54 | 3.07 | 0.13 | 0.02 | 175714.43 | 13.27 | skipped_fast |
| CHIPUSDT | IDLE | 1.62 | 2.89 | 2.36 | -0.01 | 145538.88 | 16.53 | skipped_fast |
| RWAINCUSDT | IDLE | 2.38 | 4.42 | 2.29 | -0.01 | 7657.58 | 89.42 | skipped_fast |
| REDUSDT | IDLE | 1.01 | 1.78 | 1.58 | 0.0 | 59624.0 | 14.17 | skipped_fast |
| BIOUSDT | IDLE | 0.54 | 1.3 | 0.67 | 0.04 | 121326.06 | 3.07 | skipped_fast |
| RIZEUSDT | IDLE | 0.36 | 3.21 | 1.19 | -0.23 | 51540.19 | 33.25 | skipped_fast |
| TELUSDT | IDLE | 1.03 | 1.8 | 1.71 | -0.02 | 123773.41 | 43.41 | skipped_fast |
| RWAUSDT | IDLE | 0.72 | 1.34 | 0.66 | -0.01 | 53060.7 | 7.38 | skipped_fast |
| FLUIDUSDT | IDLE | 0.91 | 1.82 | 0.0 | 0.01 | 3396.54 | 22.21 | skipped_fast |
| MNSRYUSDT | IDLE | 0.33 | 0.63 | 0.18 | 0.01 | 40517.59 | 8.92 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
