# Hulk DIGEST — 2026-08-22T00:37:03Z

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
| PYTHUSDT | IDLE | 1.77 | 6.5 | 0.89 | 0.11 | 6419983.79 | 2.03 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.09 | 8.72 | 1.82 | 0.15 | 145986923.98 | 2.75 | skipped_fast |
| HBARUSDT | IDLE | 2.81 | 6.36 | 1.75 | 0.07 | 939215.78 | 1.26 | skipped_fast |
| ZBCNUSDT | IDLE | 2.89 | 11.25 | 2.97 | 0.11 | 542522.33 | 25.2 | skipped_fast |
| CCUSDT | IDLE | 1.93 | 7.42 | 0.67 | 0.15 | 639546.57 | 6.2 | skipped_fast |
| WUSDT | IDLE | 2.73 | 6.91 | 0.82 | 0.08 | 388085.71 | 12.22 | skipped_fast |
| CHIPUSDT | IDLE | 1.61 | 3.56 | 1.06 | 0.03 | 553739.1 | 3.07 | skipped_fast |
| BIOUSDT | IDLE | 2.24 | 5.04 | 0.31 | 0.03 | 186051.73 | 3.09 | skipped_fast |
| RIZEUSDT | IDLE | 2.22 | 9.82 | 2.88 | 0.13 | 59938.68 | 45.4 | skipped_fast |
| EDELUSDT | IDLE | 2.58 | 5.5 | 1.41 | -0.02 | 79698.15 | 65.86 | skipped_fast |
| QAITUSDT | IDLE | 2.27 | 4.22 | 2.14 | -0.01 | 3715.41 | 19.88 | skipped_fast |
| TELUSDT | IDLE | 2.83 | 6.89 | 0.56 | 0.06 | 186236.89 | 30.9 | skipped_fast |
| QNTUSDT | IDLE | 2.55 | 5.42 | 1.33 | 0.06 | 170468.07 | 6.06 | skipped_fast |
| REDUSDT | IDLE | 0.71 | 6.54 | 0.32 | 0.24 | 157939.43 | 17.84 | skipped_fast |
| KITEUSDT | IDLE | 1.06 | 3.12 | 0.2 | 0.1 | 61069.34 | 11.01 | skipped_fast |
| RWAINCUSDT | IDLE | 1.59 | 2.99 | 1.22 | 0.05 | 9739.47 | 48.48 | skipped_fast |
| RWAUSDT | IDLE | 1.08 | 2.08 | 0.57 | 0.03 | 54639.55 | 8.21 | skipped_fast |
| FLUIDUSDT | IDLE | 1.17 | 2.87 | 0.66 | 0.09 | 4845.77 | 21.69 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
