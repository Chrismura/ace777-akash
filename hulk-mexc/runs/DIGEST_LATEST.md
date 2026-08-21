# Hulk DIGEST — 2026-08-21T22:17:24Z

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
| PYTHUSDT | IDLE | 1.36 | 5.17 | 0.24 | 0.11 | 5734127.77 | 2.04 | skipped_fast |
| XRPUSDT | IDLE | 1.51 | 5.44 | 0.17 | 0.14 | 131755299.93 | 5.58 | skipped_fast |
| CCUSDT | IDLE | 1.76 | 6.45 | 0.21 | 0.14 | 644577.85 | 10.69 | skipped_fast |
| HBARUSDT | IDLE | 2.19 | 4.71 | 0.4 | 0.09 | 849745.14 | 6.31 | skipped_fast |
| WUSDT | IDLE | 2.45 | 5.3 | 0.06 | 0.08 | 369714.72 | 13.35 | skipped_fast |
| CHIPUSDT | IDLE | 1.49 | 4.54 | 1.33 | 0.06 | 534677.34 | 3.06 | skipped_fast |
| ZBCNUSDT | IDLE | 1.51 | 6.5 | 0.19 | 0.11 | 499534.51 | 22.65 | skipped_fast |
| BIOUSDT | IDLE | 2.26 | 5.04 | 0.55 | 0.03 | 187805.25 | 3.1 | skipped_fast |
| REDUSDT | IDLE | 1.33 | 11.01 | 8.05 | 0.18 | 156324.94 | 19.38 | skipped_fast |
| EDELUSDT | IDLE | 1.94 | 4.24 | 0.33 | -0.03 | 82337.16 | 22.03 | skipped_fast |
| QAITUSDT | IDLE | 2.37 | 4.38 | 2.37 | -0.02 | 3827.91 | 63.67 | skipped_fast |
| TELUSDT | IDLE | 2.51 | 6.45 | 0.56 | 0.06 | 186809.51 | 36.15 | skipped_fast |
| KITEUSDT | IDLE | 1.19 | 3.58 | 0.6 | 0.12 | 61412.45 | 10.11 | skipped_fast |
| RWAINCUSDT | IDLE | 2.13 | 4.07 | 1.27 | 0.03 | 10238.87 | 86.25 | skipped_fast |
| RIZEUSDT | IDLE | 0.95 | 4.7 | 1.72 | 0.06 | 56362.3 | 45.14 | skipped_fast |
| QNTUSDT | IDLE | 1.65 | 3.3 | 0.0 | 0.05 | 65400.9 | 7.66 | skipped_fast |
| RWAUSDT | IDLE | 0.91 | 1.75 | 0.41 | 0.04 | 54119.79 | 24.68 | skipped_fast |
| FLUIDUSDT | IDLE | 0.51 | 1.15 | 0.08 | 0.09 | 4171.26 | 21.08 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
