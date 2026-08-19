# Hulk DIGEST — 2026-08-19T23:20:18Z

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
| XRPUSDT | IDLE | 2.31 | 7.62 | 2.97 | 0.1 | 42081128.71 | 0.91 | skipped_fast |
| PYTHUSDT | IDLE | 2.43 | 7.21 | 1.52 | 0.09 | 317085.31 | 2.38 | skipped_fast |
| RIZEUSDT | IMPULSE_WAIT — spike en cours, pas chase | 4.12 | 8.37 | 1.65 | -0.0 | 46686.57 | 50.5 | skipped_fast |
| ZBCNUSDT | IDLE | 2.21 | 9.86 | 2.35 | 0.15 | 224100.4 | 17.27 | skipped_fast |
| WUSDT | IDLE | 1.8 | 4.13 | 0.97 | 0.07 | 251172.65 | 13.86 | skipped_fast |
| CCUSDT | IDLE | 1.2 | 3.52 | 1.1 | 0.1 | 342792.4 | 11.09 | skipped_fast |
| HBARUSDT | IDLE | 2.16 | 4.1 | 1.41 | 0.05 | 317139.99 | 1.41 | skipped_fast |
| EDELUSDT | IDLE | 1.73 | 9.7 | 1.1 | 0.19 | 82331.34 | 44.64 | skipped_fast |
| CHIPUSDT | IDLE | 1.16 | 3.54 | 2.62 | 0.06 | 186890.97 | 7.17 | skipped_fast |
| BIOUSDT | IDLE | 1.07 | 5.04 | 3.69 | 0.13 | 153365.18 | 3.61 | skipped_fast |
| REDUSDT | IDLE | 1.08 | 4.7 | 2.93 | 0.02 | 100875.66 | 13.72 | skipped_fast |
| KITEUSDT | IDLE | 1.46 | 2.9 | 1.1 | 0.05 | 59453.59 | 14.54 | skipped_fast |
| FLUIDUSDT | IDLE | 2.23 | 6.09 | 3.05 | 0.06 | 3378.04 | 21.59 | skipped_fast |
| TELUSDT | IDLE | 1.35 | 6.32 | 2.37 | 0.12 | 186853.96 | 49.69 | skipped_fast |
| RWAINCUSDT | IDLE | 0.94 | 2.88 | 0.0 | 0.06 | 16670.11 | 56.56 | skipped_fast |
| QNTUSDT | IDLE | 1.67 | 3.2 | 0.93 | 0.05 | 41266.98 | 5.11 | skipped_fast |
| QAITUSDT | IDLE | 0.8 | 2.03 | 1.69 | 0.02 | 10702.1 | 62.16 | skipped_fast |
| RWAUSDT | IDLE | 0.79 | 1.57 | 0.09 | 0.01 | 53716.55 | 17.24 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
