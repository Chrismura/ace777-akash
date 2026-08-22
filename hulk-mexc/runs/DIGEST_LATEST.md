# Hulk DIGEST — 2026-08-22T01:37:34Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.87 | 10.86 | 0.93 | 0.16 | 6777025.98 | 1.95 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.26 | 9.29 | 0.19 | 0.15 | 151294568.41 | 5.37 | skipped_fast |
| HBARUSDT | IDLE | 2.97 | 6.36 | 0.15 | 0.09 | 960366.57 | 1.24 | skipped_fast |
| ZBCNUSDT | IDLE | 2.6 | 10.08 | 2.75 | 0.09 | 551489.85 | 18.88 | skipped_fast |
| CCUSDT | IDLE | 1.78 | 7.36 | 0.18 | 0.17 | 662342.51 | 9.61 | skipped_fast |
| WUSDT | IDLE | 2.7 | 6.65 | 0.68 | 0.09 | 391964.73 | 11.21 | skipped_fast |
| CHIPUSDT | IDLE | 1.59 | 3.56 | 0.82 | 0.01 | 513143.85 | 3.07 | skipped_fast |
| BIOUSDT | IDLE | 2.53 | 5.57 | 1.1 | 0.04 | 186411.69 | 6.16 | skipped_fast |
| EDELUSDT | IDLE | 2.62 | 5.5 | 1.95 | -0.02 | 79491.14 | 11.07 | skipped_fast |
| RIZEUSDT | IDLE | 1.98 | 8.52 | 4.1 | 0.11 | 60795.07 | 45.81 | skipped_fast |
| REDUSDT | IDLE | 0.98 | 8.27 | 5.38 | 0.17 | 158702.14 | 20.08 | skipped_fast |
| KITEUSDT | IDLE | 1.58 | 5.12 | 0.0 | 0.13 | 61113.59 | 8.96 | skipped_fast |
| QNTUSDT | IDLE | 2.4 | 5.18 | 0.72 | 0.07 | 170053.21 | 6.02 | skipped_fast |
| QAITUSDT | IDLE | 2.04 | 4.02 | 0.43 | 0.01 | 3870.41 | 31.31 | skipped_fast |
| TELUSDT | IDLE | 2.57 | 6.19 | 0.82 | 0.05 | 181992.79 | 46.5 | skipped_fast |
| RWAINCUSDT | IDLE | 1.71 | 3.27 | 1.0 | 0.05 | 9647.88 | 47.99 | skipped_fast |
| FLUIDUSDT | IDLE | 1.35 | 3.74 | 0.0 | 0.1 | 4798.05 | 21.16 | skipped_fast |
| RWAUSDT | IDLE | 1.08 | 2.08 | 0.57 | 0.04 | 54805.96 | 16.41 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
