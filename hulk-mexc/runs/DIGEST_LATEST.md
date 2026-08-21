# Hulk DIGEST — 2026-08-21T22:29:03Z

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
| PYTHUSDT | IDLE | 1.36 | 5.17 | 0.31 | 0.11 | 5784539.53 | 4.09 | skipped_fast |
| XRPUSDT | IDLE | 1.56 | 5.68 | 0.4 | 0.14 | 134007572.86 | 4.19 | skipped_fast |
| CCUSDT | IDLE | 1.76 | 6.48 | 0.19 | 0.13 | 654461.99 | 11.57 | skipped_fast |
| HBARUSDT | IDLE | 2.21 | 4.71 | 0.75 | 0.08 | 857944.93 | 1.27 | skipped_fast |
| WUSDT | IDLE | 2.46 | 5.3 | 0.24 | 0.08 | 370574.56 | 11.31 | skipped_fast |
| CHIPUSDT | IDLE | 1.48 | 4.54 | 1.18 | 0.06 | 534261.76 | 3.05 | skipped_fast |
| ZBCNUSDT | IDLE | 1.58 | 6.77 | 0.32 | 0.11 | 503402.81 | 11.8 | skipped_fast |
| BIOUSDT | IDLE | 2.29 | 5.04 | 1.08 | 0.02 | 188047.66 | 3.11 | skipped_fast |
| REDUSDT | IDLE | 1.32 | 11.01 | 8.0 | 0.18 | 156086.34 | 11.31 | skipped_fast |
| EDELUSDT | IDLE | 2.3 | 5.04 | 0.33 | -0.03 | 82630.42 | 32.8 | skipped_fast |
| TELUSDT | IDLE | 2.53 | 6.45 | 0.87 | 0.05 | 187103.32 | 15.54 | skipped_fast |
| QAITUSDT | IDLE | 2.37 | 4.38 | 2.37 | -0.02 | 3827.91 | 63.67 | skipped_fast |
| RWAINCUSDT | IDLE | 2.13 | 4.07 | 1.27 | 0.03 | 10212.76 | 70.1 | skipped_fast |
| KITEUSDT | IDLE | 1.22 | 3.58 | 1.09 | 0.11 | 61397.17 | 10.14 | skipped_fast |
| RIZEUSDT | IDLE | 0.95 | 4.7 | 1.69 | 0.06 | 56362.1 | 45.14 | skipped_fast |
| QNTUSDT | IDLE | 1.86 | 3.71 | 0.03 | 0.05 | 65334.04 | 1.52 | skipped_fast |
| RWAUSDT | IDLE | 0.91 | 1.75 | 0.41 | 0.03 | 54169.19 | 16.42 | skipped_fast |
| FLUIDUSDT | IDLE | 0.51 | 1.15 | 0.08 | 0.09 | 4171.26 | 18.24 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
