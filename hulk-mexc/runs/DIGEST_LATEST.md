# Hulk DIGEST — 2026-08-21T21:51:49Z

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
| PYTHUSDT | IDLE | 1.17 | 4.51 | 0.55 | 0.09 | 5669625.12 | 2.06 | skipped_fast |
| XRPUSDT | IDLE | 1.08 | 3.73 | 0.45 | 0.11 | 129965902.42 | 0.71 | skipped_fast |
| CHIPUSDT | IDLE | 1.88 | 5.61 | 3.64 | 0.05 | 527062.66 | 3.09 | skipped_fast |
| HBARUSDT | IDLE | 2.04 | 4.49 | 0.29 | 0.08 | 826269.36 | 1.26 | skipped_fast |
| CCUSDT | IDLE | 1.3 | 3.89 | 0.0 | 0.11 | 638491.87 | 8.2 | skipped_fast |
| ZBCNUSDT | IDLE | 1.92 | 8.19 | 2.79 | 0.11 | 491332.65 | 52.75 | skipped_fast |
| WUSDT | IDLE | 1.96 | 3.91 | 0.01 | 0.07 | 368650.07 | 15.58 | skipped_fast |
| BIOUSDT | IDLE | 2.38 | 5.2 | 1.38 | 0.03 | 187290.23 | 6.23 | skipped_fast |
| REDUSDT | IDLE | 1.34 | 11.01 | 9.11 | 0.17 | 154051.49 | 10.63 | skipped_fast |
| RIZEUSDT | IDLE | 1.86 | 9.54 | 1.08 | 0.04 | 55836.88 | 31.52 | skipped_fast |
| EDELUSDT | IDLE | 1.9 | 4.12 | 0.55 | -0.04 | 83634.11 | 33.2 | skipped_fast |
| QAITUSDT | IDLE | 2.37 | 4.38 | 2.37 | -0.02 | 3827.91 | 59.7 | skipped_fast |
| RWAINCUSDT | IDLE | 2.22 | 4.3 | 0.95 | 0.02 | 10222.59 | 42.69 | skipped_fast |
| KITEUSDT | IDLE | 1.26 | 4.0 | 1.07 | 0.11 | 61212.01 | 13.77 | skipped_fast |
| TELUSDT | IDLE | 1.9 | 4.81 | 0.89 | 0.03 | 185759.44 | 10.52 | skipped_fast |
| QNTUSDT | IDLE | 1.35 | 2.65 | 0.4 | 0.04 | 62613.16 | 7.72 | skipped_fast |
| RWAUSDT | IDLE | 0.6 | 1.17 | 0.25 | 0.03 | 53991.93 | 24.78 | skipped_fast |
| FLUIDUSDT | IDLE | 0.51 | 1.15 | 0.09 | 0.09 | 4171.26 | 21.9 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
