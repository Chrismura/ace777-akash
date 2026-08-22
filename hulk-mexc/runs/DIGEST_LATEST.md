# Hulk DIGEST — 2026-08-22T04:43:27Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.92 | 14.81 | 0.23 | 0.21 | 11713585.22 | 1.81 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.35 | 16.14 | 0.24 | 0.26 | 174749133.19 | 4.85 | skipped_fast |
| HBARUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.44 | 8.85 | 0.21 | 0.14 | 1068715.52 | 1.17 | skipped_fast |
| CCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.13 | 11.56 | 1.02 | 0.2 | 736739.09 | 5.72 | skipped_fast |
| CHIPUSDT | IDLE | 2.77 | 5.36 | 1.26 | 0.02 | 451144.62 | 5.96 | skipped_fast |
| WUSDT | IDLE | 2.0 | 7.62 | 0.04 | 0.15 | 435273.97 | 12.51 | skipped_fast |
| BIOUSDT | IDLE | 2.95 | 7.36 | 1.35 | 0.06 | 200819.88 | 2.97 | skipped_fast |
| ZBCNUSDT | IDLE | 1.41 | 4.29 | 0.91 | 0.13 | 537747.87 | 26.0 | skipped_fast |
| EDELUSDT | IDLE | 2.03 | 4.07 | 2.82 | -0.03 | 80261.64 | 11.17 | skipped_fast |
| RIZEUSDT | IDLE | 1.84 | 7.71 | 4.6 | 0.09 | 58587.71 | 23.89 | skipped_fast |
| QNTUSDT | IDLE | 2.43 | 8.56 | 4.26 | 0.1 | 181862.07 | 2.95 | skipped_fast |
| REDUSDT | IDLE | 0.94 | 7.96 | 4.63 | 0.2 | 158182.54 | 12.75 | skipped_fast |
| KITEUSDT | IDLE | 1.59 | 5.55 | 0.26 | 0.13 | 68012.33 | 11.49 | skipped_fast |
| RWAINCUSDT | IDLE | 1.99 | 3.6 | 2.48 | 0.01 | 9348.0 | 27.23 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3417.27 | 35.86 | skipped_fast |
| TELUSDT | IDLE | 1.81 | 4.9 | 0.0 | 0.1 | 178524.05 | 104.4 | skipped_fast |
| RWAUSDT | IDLE | 1.52 | 3.05 | 0.0 | 0.06 | 56655.53 | 24.01 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.08 | 3702.43 | 22.14 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
