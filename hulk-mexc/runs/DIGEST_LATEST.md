# Hulk DIGEST — 2026-08-21T22:32:37Z

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
| PYTHUSDT | IDLE | 1.39 | 5.17 | 1.02 | 0.1 | 5807607.92 | 2.06 | skipped_fast |
| XRPUSDT | IDLE | 1.55 | 5.68 | 0.29 | 0.14 | 134266813.56 | 2.79 | skipped_fast |
| HBARUSDT | IDLE | 2.27 | 4.71 | 1.52 | 0.07 | 865372.43 | 1.28 | skipped_fast |
| CCUSDT | IDLE | 1.77 | 6.48 | 0.36 | 0.13 | 657725.22 | 10.7 | skipped_fast |
| WUSDT | IDLE | 2.51 | 5.3 | 0.93 | 0.08 | 370964.51 | 14.49 | skipped_fast |
| CHIPUSDT | IDLE | 1.5 | 4.54 | 1.72 | 0.06 | 533888.5 | 6.13 | skipped_fast |
| ZBCNUSDT | IDLE | 1.6 | 6.77 | 0.74 | 0.11 | 502334.1 | 23.2 | skipped_fast |
| BIOUSDT | IDLE | 2.34 | 5.04 | 1.75 | 0.02 | 188344.75 | 12.52 | skipped_fast |
| REDUSDT | IDLE | 1.33 | 11.01 | 8.27 | 0.18 | 155908.85 | 12.96 | skipped_fast |
| EDELUSDT | IDLE | 2.33 | 5.04 | 0.76 | -0.03 | 82619.41 | 32.88 | skipped_fast |
| RWAINCUSDT | IDLE | 2.22 | 4.07 | 2.43 | 0.02 | 10212.45 | 16.17 | skipped_fast |
| TELUSDT | IDLE | 2.53 | 6.45 | 0.77 | 0.05 | 187039.27 | 15.54 | skipped_fast |
| QAITUSDT | IDLE | 2.37 | 4.38 | 2.37 | -0.02 | 3827.91 | 63.67 | skipped_fast |
| KITEUSDT | IDLE | 1.23 | 3.58 | 1.43 | 0.11 | 61449.35 | 11.1 | skipped_fast |
| RIZEUSDT | IDLE | 0.95 | 4.7 | 1.81 | 0.06 | 56363.91 | 45.14 | skipped_fast |
| QNTUSDT | IDLE | 1.86 | 3.72 | 0.0 | 0.06 | 72051.43 | 1.52 | skipped_fast |
| RWAUSDT | IDLE | 0.89 | 1.75 | 0.16 | 0.04 | 54133.25 | 8.21 | skipped_fast |
| FLUIDUSDT | IDLE | 0.51 | 1.15 | 0.08 | 0.09 | 4171.26 | 21.88 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
