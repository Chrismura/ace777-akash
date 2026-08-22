# Hulk DIGEST — 2026-08-22T04:26:02Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.9 | 13.61 | 1.33 | 0.19 | 10883894.91 | 3.69 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.12 | 12.39 | 0.06 | 0.22 | 169661429.63 | 4.38 | skipped_fast |
| CCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.15 | 11.56 | 1.9 | 0.19 | 732421.71 | 7.41 | skipped_fast |
| HBARUSDT | IDLE | 2.26 | 7.14 | 0.47 | 0.12 | 1034454.25 | 1.19 | skipped_fast |
| CHIPUSDT | IDLE | 2.77 | 5.36 | 1.15 | 0.01 | 442437.3 | 2.98 | skipped_fast |
| BIOUSDT | IDLE | 3.01 | 7.36 | 2.34 | 0.07 | 200060.76 | 3.0 | skipped_fast |
| WUSDT | IDLE | 1.96 | 7.18 | 0.38 | 0.14 | 434558.12 | 11.63 | skipped_fast |
| ZBCNUSDT | IDLE | 1.43 | 4.29 | 1.21 | 0.12 | 536329.97 | 28.92 | skipped_fast |
| EDELUSDT | IDLE | 2.08 | 4.07 | 3.47 | -0.04 | 80098.21 | 11.24 | skipped_fast |
| RIZEUSDT | IDLE | 1.85 | 7.71 | 4.99 | 0.09 | 59189.91 | 44.52 | skipped_fast |
| REDUSDT | IDLE | 0.93 | 7.96 | 4.33 | 0.21 | 158520.72 | 11.92 | skipped_fast |
| KITEUSDT | IDLE | 1.61 | 5.55 | 0.73 | 0.13 | 67828.61 | 11.55 | skipped_fast |
| RWAINCUSDT | IDLE | 2.05 | 3.6 | 3.27 | -0.0 | 9290.79 | 70.63 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3389.73 | 63.67 | skipped_fast |
| QNTUSDT | IDLE | 1.54 | 3.8 | 0.5 | 0.09 | 178582.08 | 8.9 | skipped_fast |
| TELUSDT | IDLE | 1.31 | 3.12 | 0.4 | 0.08 | 176551.56 | 40.57 | skipped_fast |
| RWAUSDT | IDLE | 1.55 | 3.05 | 0.4 | 0.06 | 56333.75 | 8.02 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.08 | 3702.43 | 21.7 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
