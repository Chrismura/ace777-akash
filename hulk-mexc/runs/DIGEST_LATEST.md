# Hulk DIGEST — 2026-08-22T04:20:02Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.84 | 13.13 | 0.4 | 0.2 | 10572545.26 | 20.2 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.14 | 12.22 | 1.33 | 0.2 | 167994472.38 | 4.44 | skipped_fast |
| CCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.12 | 11.56 | 0.77 | 0.21 | 727995.97 | 10.6 | skipped_fast |
| HBARUSDT | IDLE | 2.28 | 7.14 | 0.85 | 0.12 | 1018625.08 | 1.2 | skipped_fast |
| CHIPUSDT | IDLE | 2.78 | 5.36 | 1.35 | 0.01 | 441095.88 | 17.9 | skipped_fast |
| BIOUSDT | IDLE | 3.01 | 7.36 | 2.34 | 0.07 | 199961.99 | 3.0 | skipped_fast |
| WUSDT | IDLE | 1.96 | 7.18 | 0.51 | 0.14 | 434568.17 | 11.63 | skipped_fast |
| ZBCNUSDT | IDLE | 1.46 | 4.29 | 1.78 | 0.11 | 535633.54 | 25.32 | skipped_fast |
| EDELUSDT | IDLE | 2.08 | 4.07 | 3.58 | -0.05 | 80181.38 | 22.5 | skipped_fast |
| RIZEUSDT | IDLE | 1.85 | 7.71 | 4.88 | 0.1 | 59155.63 | 44.52 | skipped_fast |
| REDUSDT | IDLE | 0.94 | 7.96 | 5.0 | 0.2 | 159830.11 | 19.2 | skipped_fast |
| KITEUSDT | IDLE | 1.61 | 5.55 | 0.77 | 0.13 | 67597.03 | 11.55 | skipped_fast |
| RWAINCUSDT | IDLE | 2.01 | 3.6 | 2.74 | 0.01 | 9375.63 | 59.44 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3389.73 | 63.67 | skipped_fast |
| QNTUSDT | IDLE | 1.54 | 3.8 | 0.6 | 0.09 | 178550.67 | 5.93 | skipped_fast |
| RWAUSDT | IDLE | 1.54 | 3.05 | 0.24 | 0.06 | 56322.71 | 8.02 | skipped_fast |
| TELUSDT | IDLE | 1.17 | 2.76 | 0.61 | 0.07 | 174874.0 | 30.61 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.08 | 3702.43 | 21.75 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
