# Hulk DIGEST — 2026-08-21T21:12:07Z

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
| PYTHUSDT | IDLE | 1.21 | 4.51 | 1.62 | 0.09 | 5596795.51 | 2.09 | skipped_fast |
| XRPUSDT | IDLE | 1.15 | 3.73 | 1.97 | 0.1 | 128075496.56 | 3.61 | skipped_fast |
| CHIPUSDT | IDLE | 1.9 | 5.61 | 4.24 | 0.07 | 514554.97 | 18.68 | skipped_fast |
| ZBCNUSDT | IDLE | 2.0 | 8.19 | 5.14 | 0.09 | 481675.83 | 37.24 | skipped_fast |
| CCUSDT | IDLE | 1.14 | 3.14 | 0.39 | 0.1 | 641914.86 | 5.53 | skipped_fast |
| HBARUSDT | IDLE | 1.62 | 3.04 | 1.32 | 0.06 | 806092.43 | 1.29 | skipped_fast |
| WUSDT | IDLE | 1.97 | 3.83 | 0.76 | 0.06 | 368011.69 | 10.49 | skipped_fast |
| BIOUSDT | IDLE | 2.48 | 5.2 | 2.79 | -0.0 | 187657.8 | 6.32 | skipped_fast |
| REDUSDT | IDLE | 1.35 | 11.01 | 9.46 | 0.16 | 153534.3 | 3.28 | skipped_fast |
| EDELUSDT | IDLE | 2.07 | 4.12 | 3.08 | -0.06 | 82250.03 | 34.07 | skipped_fast |
| RWAINCUSDT | IDLE | 2.27 | 4.3 | 1.64 | 0.02 | 10271.93 | 21.42 | skipped_fast |
| RIZEUSDT | IDLE | 1.87 | 9.54 | 1.42 | 0.01 | 56222.29 | 45.77 | skipped_fast |
| KITEUSDT | IDLE | 1.32 | 4.0 | 2.23 | 0.11 | 61177.26 | 12.98 | skipped_fast |
| TELUSDT | IDLE | 1.38 | 3.39 | 1.37 | 0.01 | 180180.97 | 37.56 | skipped_fast |
| QNTUSDT | IDLE | 1.45 | 2.65 | 1.65 | 0.04 | 60162.32 | 1.56 | skipped_fast |
| QAITUSDT | IDLE | 1.72 | 3.0 | 2.88 | -0.03 | 2646.1 | 175.02 | skipped_fast |
| RWAUSDT | IDLE | 0.64 | 1.17 | 0.74 | 0.03 | 53751.81 | 33.25 | skipped_fast |
| FLUIDUSDT | IDLE | 0.58 | 1.15 | 1.1 | 0.08 | 4161.15 | 39.35 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
