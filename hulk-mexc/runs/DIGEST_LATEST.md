# Hulk DIGEST — 2026-08-21T22:51:45Z

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
| PYTHUSDT | IDLE | 1.35 | 5.17 | 0.06 | 0.11 | 5892034.44 | 2.04 | skipped_fast |
| XRPUSDT | IDLE | 1.66 | 6.41 | 0.36 | 0.15 | 136043173.61 | 4.84 | skipped_fast |
| CCUSDT | IDLE | 1.89 | 7.44 | 0.3 | 0.14 | 659178.67 | 8.83 | skipped_fast |
| HBARUSDT | IDLE | 2.19 | 4.73 | 0.4 | 0.08 | 875843.95 | 1.26 | skipped_fast |
| ZBCNUSDT | IDLE | 1.93 | 8.3 | 0.0 | 0.14 | 508528.44 | 6.76 | skipped_fast |
| WUSDT | IDLE | 2.63 | 6.46 | 0.21 | 0.09 | 371663.12 | 13.22 | skipped_fast |
| CHIPUSDT | IDLE | 1.52 | 4.54 | 2.05 | 0.05 | 534827.52 | 3.07 | skipped_fast |
| BIOUSDT | IDLE | 2.29 | 5.04 | 1.08 | 0.03 | 187964.94 | 3.11 | skipped_fast |
| REDUSDT | IDLE | 1.32 | 11.01 | 8.03 | 0.18 | 157214.58 | 11.33 | skipped_fast |
| EDELUSDT | IDLE | 2.3 | 5.04 | 0.22 | -0.03 | 82543.54 | 21.83 | skipped_fast |
| RWAINCUSDT | IDLE | 2.18 | 4.07 | 1.96 | 0.02 | 10244.46 | 16.16 | skipped_fast |
| TELUSDT | IDLE | 2.52 | 6.45 | 0.72 | 0.06 | 186843.77 | 20.7 | skipped_fast |
| QAITUSDT | IDLE | 2.34 | 4.38 | 1.94 | -0.02 | 3835.98 | 67.45 | skipped_fast |
| KITEUSDT | IDLE | 1.22 | 3.58 | 1.12 | 0.1 | 61340.39 | 10.14 | skipped_fast |
| QNTUSDT | IDLE | 2.25 | 4.51 | 0.0 | 0.06 | 88100.32 | 1.51 | skipped_fast |
| RIZEUSDT | IDLE | 0.96 | 4.7 | 2.05 | 0.06 | 56394.77 | 46.99 | skipped_fast |
| RWAUSDT | IDLE | 0.92 | 1.83 | 0.0 | 0.04 | 54111.09 | 16.38 | skipped_fast |
| FLUIDUSDT | IDLE | 0.51 | 1.15 | 0.08 | 0.09 | 4171.26 | 18.29 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
