# Hulk DIGEST — 2026-08-21T12:24:28Z

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
| PYTHUSDT | IDLE | 1.77 | 6.82 | 5.65 | 0.11 | 3045930.22 | 2.09 | skipped_fast |
| XRPUSDT | IDLE | 2.14 | 10.14 | 4.77 | 0.15 | 151272164.33 | 0.73 | skipped_fast |
| CCUSDT | IDLE | 1.88 | 3.67 | 0.66 | 0.01 | 532602.54 | 10.54 | skipped_fast |
| ZBCNUSDT | IDLE | 1.38 | 6.51 | 1.48 | 0.11 | 463649.81 | 17.98 | skipped_fast |
| CHIPUSDT | IDLE | 0.9 | 3.96 | 2.08 | 0.08 | 547224.14 | 3.04 | skipped_fast |
| BIOUSDT | IDLE | 2.56 | 5.85 | 2.84 | 0.05 | 168023.32 | 3.11 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.23 | 5.67 | 5.26 | -0.0 | 82781.01 | 44.35 | skipped_fast |
| HBARUSDT | IDLE | 1.84 | 3.41 | 1.85 | 0.04 | 639294.13 | 1.32 | skipped_fast |
| KITEUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.8 | 9.82 | 1.49 | 0.12 | 62666.9 | 12.04 | skipped_fast |
| WUSDT | IDLE | 1.75 | 3.67 | 1.33 | 0.07 | 333450.77 | 16.09 | skipped_fast |
| QAITUSDT | IDLE | 3.53 | 6.82 | 1.62 | -0.01 | 4013.41 | 67.05 | skipped_fast |
| REDUSDT | IDLE | 2.52 | 5.04 | 0.0 | 0.03 | 98120.04 | 11.7 | skipped_fast |
| RIZEUSDT | IDLE | 2.91 | 14.84 | 2.11 | 0.12 | 43598.95 | 222.48 | skipped_fast |
| TELUSDT | IDLE | 1.94 | 8.66 | 3.06 | 0.16 | 216248.43 | 25.85 | skipped_fast |
| RWAINCUSDT | IDLE | 1.74 | 3.31 | 1.12 | 0.04 | 9461.94 | 27.05 | skipped_fast |
| QNTUSDT | IDLE | 1.83 | 3.58 | 0.51 | 0.05 | 59179.94 | 6.25 | skipped_fast |
| FLUIDUSDT | IDLE | 2.17 | 4.54 | 0.05 | 0.07 | 3328.57 | 26.85 | skipped_fast |
| RWAUSDT | IDLE | 1.26 | 2.45 | 0.41 | 0.04 | 56020.2 | 16.56 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
