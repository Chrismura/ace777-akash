# Hulk DIGEST — 2026-08-21T22:11:06Z

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
| PYTHUSDT | IDLE | 1.33 | 5.06 | 0.14 | 0.11 | 5706270.62 | 6.14 | skipped_fast |
| XRPUSDT | IDLE | 1.55 | 5.44 | 1.16 | 0.13 | 131450825.0 | 3.52 | skipped_fast |
| HBARUSDT | IDLE | 2.19 | 4.71 | 0.43 | 0.09 | 845491.68 | 2.53 | skipped_fast |
| CCUSDT | IDLE | 1.6 | 5.5 | 0.0 | 0.13 | 644182.3 | 11.67 | skipped_fast |
| CHIPUSDT | IDLE | 1.49 | 4.54 | 1.48 | 0.06 | 534044.2 | 3.06 | skipped_fast |
| WUSDT | IDLE | 2.37 | 4.87 | 0.04 | 0.08 | 368034.82 | 18.54 | skipped_fast |
| ZBCNUSDT | IDLE | 1.51 | 6.5 | 0.16 | 0.12 | 496978.1 | 26.58 | skipped_fast |
| BIOUSDT | IDLE | 2.22 | 5.04 | 0.06 | 0.03 | 185674.15 | 6.16 | skipped_fast |
| REDUSDT | IDLE | 1.33 | 11.01 | 8.57 | 0.18 | 155123.74 | 19.51 | skipped_fast |
| TELUSDT | IDLE | 2.52 | 6.45 | 0.62 | 0.06 | 186834.18 | 5.17 | skipped_fast |
| EDELUSDT | IDLE | 1.87 | 4.12 | 0.11 | -0.03 | 82404.05 | 33.09 | skipped_fast |
| QAITUSDT | IDLE | 2.37 | 4.38 | 2.37 | -0.02 | 3827.91 | 63.67 | skipped_fast |
| RWAINCUSDT | IDLE | 2.17 | 4.07 | 1.8 | 0.01 | 10246.19 | 58.87 | skipped_fast |
| KITEUSDT | IDLE | 1.2 | 3.58 | 0.72 | 0.12 | 61274.06 | 10.11 | skipped_fast |
| RIZEUSDT | IDLE | 0.95 | 4.7 | 1.69 | 0.06 | 56400.92 | 45.14 | skipped_fast |
| QNTUSDT | IDLE | 1.51 | 3.0 | 0.14 | 0.05 | 65326.24 | 36.8 | skipped_fast |
| RWAUSDT | IDLE | 0.91 | 1.75 | 0.49 | 0.04 | 54200.24 | 16.47 | skipped_fast |
| FLUIDUSDT | IDLE | 0.51 | 1.15 | 0.08 | 0.09 | 4171.26 | 16.08 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
