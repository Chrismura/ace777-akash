# Hulk DIGEST — 2026-08-22T02:59:53Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.65 | 11.02 | 1.3 | 0.14 | 7392905.45 | 11.48 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.54 | 13.33 | 0.6 | 0.2 | 159528039.08 | 2.59 | skipped_fast |
| HBARUSDT | IDLE | 2.58 | 6.77 | 0.12 | 0.1 | 990493.21 | 2.43 | skipped_fast |
| CCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.13 | 9.99 | 0.29 | 0.18 | 664754.91 | 15.18 | skipped_fast |
| ZBCNUSDT | IDLE | 2.47 | 9.63 | 2.22 | 0.11 | 540946.99 | 27.43 | skipped_fast |
| CHIPUSDT | IDLE | 2.59 | 5.98 | 0.0 | -0.0 | 450633.83 | 2.97 | skipped_fast |
| BIOUSDT | IDLE | 3.2 | 8.18 | 2.08 | 0.08 | 194346.25 | 2.99 | skipped_fast |
| WUSDT | IDLE | 2.06 | 6.35 | 0.05 | 0.12 | 416177.53 | 20.77 | skipped_fast |
| EDELUSDT | IDLE | 2.43 | 5.02 | 2.39 | -0.03 | 79918.55 | 22.27 | skipped_fast |
| RIZEUSDT | IDLE | 1.99 | 8.52 | 4.41 | 0.1 | 61379.78 | 44.22 | skipped_fast |
| REDUSDT | IDLE | 0.97 | 8.27 | 4.66 | 0.2 | 157988.83 | 8.75 | skipped_fast |
| QNTUSDT | IDLE | 2.32 | 5.48 | 0.03 | 0.09 | 172676.47 | 7.43 | skipped_fast |
| KITEUSDT | IDLE | 1.32 | 4.09 | 0.16 | 0.12 | 62462.38 | 10.74 | skipped_fast |
| RWAINCUSDT | IDLE | 1.83 | 3.27 | 2.58 | 0.0 | 9385.21 | 43.36 | skipped_fast |
| QAITUSDT | IDLE | 1.88 | 3.57 | 1.22 | 0.0 | 3930.15 | 63.67 | skipped_fast |
| TELUSDT | IDLE | 2.13 | 5.11 | 0.92 | 0.06 | 173328.92 | 51.68 | skipped_fast |
| RWAUSDT | IDLE | 1.68 | 3.33 | 0.24 | 0.05 | 56226.46 | 16.17 | skipped_fast |
| FLUIDUSDT | IDLE | 1.44 | 3.69 | 2.03 | 0.07 | 4710.05 | 21.02 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
