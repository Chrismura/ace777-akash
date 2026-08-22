# Hulk DIGEST — 2026-08-22T16:04:41Z

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
| PYTHUSDT | IDLE | 1.51 | 7.24 | 1.56 | 0.04 | 51469323.11 | 1.98 | skipped_fast |
| XRPUSDT | IDLE | 1.37 | 7.64 | 5.37 | 0.03 | 215659034.94 | 2.76 | skipped_fast |
| HBARUSDT | IDLE | 0.85 | 3.03 | 2.3 | -0.02 | 1149623.35 | 6.54 | skipped_fast |
| CCUSDT | IDLE | 0.96 | 4.14 | 1.97 | 0.1 | 762259.22 | 10.19 | skipped_fast |
| CHIPUSDT | IDLE | 0.58 | 3.36 | 1.43 | -0.09 | 624749.59 | 3.37 | skipped_fast |
| WUSDT | IDLE | 0.66 | 2.58 | 2.08 | -0.02 | 551992.06 | 8.57 | skipped_fast |
| ZBCNUSDT | IDLE | 1.3 | 3.49 | 1.7 | -0.06 | 319701.7 | 5.13 | skipped_fast |
| BIOUSDT | IDLE | 0.97 | 6.58 | 4.66 | -0.06 | 218767.95 | 3.31 | skipped_fast |
| KITEUSDT | IDLE | 1.89 | 4.35 | 1.54 | 0.03 | 85450.12 | 12.47 | skipped_fast |
| EDELUSDT | IDLE | 1.35 | 2.41 | 1.9 | -0.02 | 75081.99 | 22.81 | skipped_fast |
| REDUSDT | IDLE | 0.52 | 5.67 | 4.44 | -0.15 | 133629.75 | 21.98 | skipped_fast |
| RIZEUSDT | IDLE | 1.32 | 3.21 | 0.19 | 0.03 | 56517.62 | 45.5 | skipped_fast |
| QAITUSDT | IDLE | 1.67 | 3.19 | 0.94 | 0.01 | 2320.37 | 67.45 | skipped_fast |
| QNTUSDT | IDLE | 0.87 | 2.69 | 2.19 | -0.02 | 183559.18 | 6.31 | skipped_fast |
| RWAINCUSDT | IDLE | 0.77 | 1.53 | 0.0 | 0.02 | 8954.22 | 64.45 | skipped_fast |
| TELUSDT | IDLE | 0.97 | 2.37 | 1.52 | -0.0 | 138518.86 | 42.69 | skipped_fast |
| RWAUSDT | IDLE | 0.55 | 1.06 | 0.24 | 0.02 | 56453.59 | 16.23 | skipped_fast |
| FLUIDUSDT | IDLE | 0.0 | 0.0 | 0.0 | -0.04 | 4625.53 | 22.45 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
