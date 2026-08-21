# Hulk DIGEST — 2026-08-21T19:40:37Z

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
| PYTHUSDT | IDLE | 1.36 | 4.99 | 4.1 | 0.06 | 5420150.27 | 2.13 | skipped_fast |
| XRPUSDT | IDLE | 1.13 | 4.21 | 2.65 | 0.12 | 129151967.36 | 1.45 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.15 | 26.97 | 13.56 | 0.16 | 154008.78 | 17.99 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 2.55 | 11.37 | 9.19 | 0.06 | 481264.51 | 42.95 | skipped_fast |
| CCUSDT | IDLE | 2.05 | 5.44 | 2.01 | 0.06 | 630410.51 | 11.24 | skipped_fast |
| CHIPUSDT | IDLE | 1.24 | 4.81 | 4.09 | 0.09 | 519203.3 | 3.11 | skipped_fast |
| WUSDT | IDLE | 2.16 | 3.92 | 2.95 | 0.04 | 360649.5 | 11.78 | skipped_fast |
| BIOUSDT | IDLE | 2.66 | 5.33 | 4.69 | -0.0 | 190463.72 | 3.22 | skipped_fast |
| HBARUSDT | IDLE | 1.46 | 2.85 | 2.28 | 0.06 | 755046.35 | 1.31 | skipped_fast |
| RIZEUSDT | IDLE | 2.28 | 11.27 | 4.0 | 0.01 | 56486.73 | 47.99 | skipped_fast |
| EDELUSDT | IDLE | 2.43 | 4.29 | 3.79 | -0.04 | 79588.38 | 22.5 | skipped_fast |
| KITEUSDT | IDLE | 1.29 | 4.0 | 3.51 | 0.09 | 60887.72 | 13.18 | skipped_fast |
| RWAINCUSDT | IDLE | 2.25 | 4.3 | 1.27 | 0.05 | 10991.31 | 113.06 | skipped_fast |
| QAITUSDT | IDLE | 1.65 | 3.0 | 1.98 | -0.01 | 2940.34 | 63.29 | skipped_fast |
| TELUSDT | IDLE | 1.83 | 4.46 | 2.0 | 0.02 | 184093.39 | 42.96 | skipped_fast |
| QNTUSDT | IDLE | 1.66 | 3.01 | 2.03 | 0.04 | 59858.05 | 6.28 | skipped_fast |
| RWAUSDT | IDLE | 0.65 | 1.16 | 0.99 | 0.04 | 54220.33 | 16.6 | skipped_fast |
| FLUIDUSDT | IDLE | 0.73 | 1.48 | 1.14 | 0.07 | 4331.26 | 34.82 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
