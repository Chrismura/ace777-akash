# Hulk DIGEST — 2026-08-22T04:33:38Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.87 | 13.61 | 0.33 | 0.2 | 11265373.61 | 3.65 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.2 | 13.48 | 0.12 | 0.24 | 170838668.77 | 1.24 | skipped_fast |
| CCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.14 | 11.56 | 1.46 | 0.2 | 733889.0 | 9.04 | skipped_fast |
| HBARUSDT | IDLE | 2.26 | 7.14 | 0.36 | 0.12 | 1034045.53 | 1.19 | skipped_fast |
| CHIPUSDT | IDLE | 2.74 | 5.36 | 0.82 | 0.02 | 450228.7 | 2.97 | skipped_fast |
| BIOUSDT | IDLE | 2.98 | 7.36 | 1.79 | 0.07 | 200387.87 | 2.98 | skipped_fast |
| WUSDT | IDLE | 1.96 | 7.29 | 0.05 | 0.14 | 435024.22 | 11.59 | skipped_fast |
| ZBCNUSDT | IDLE | 1.43 | 4.29 | 1.16 | 0.13 | 535285.03 | 27.96 | skipped_fast |
| EDELUSDT | IDLE | 2.07 | 4.07 | 3.37 | -0.04 | 80046.23 | 33.69 | skipped_fast |
| RIZEUSDT | IDLE | 1.86 | 7.71 | 5.04 | 0.09 | 58547.52 | 44.52 | skipped_fast |
| REDUSDT | IDLE | 0.94 | 7.96 | 4.88 | 0.2 | 158353.53 | 8.78 | skipped_fast |
| KITEUSDT | IDLE | 1.6 | 5.55 | 0.54 | 0.13 | 67965.11 | 10.62 | skipped_fast |
| RWAINCUSDT | IDLE | 2.05 | 3.6 | 3.27 | -0.0 | 9264.44 | 65.18 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3389.73 | 63.67 | skipped_fast |
| QNTUSDT | IDLE | 1.53 | 3.8 | 0.31 | 0.1 | 179054.12 | 2.96 | skipped_fast |
| RWAUSDT | IDLE | 1.56 | 3.05 | 0.48 | 0.06 | 56342.81 | 8.04 | skipped_fast |
| TELUSDT | IDLE | 1.3 | 3.12 | 0.25 | 0.09 | 176717.22 | 55.74 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.08 | 3702.43 | 21.53 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
