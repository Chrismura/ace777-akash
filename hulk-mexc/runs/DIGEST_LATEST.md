# Hulk DIGEST — 2026-08-21T23:57:30Z

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
| PYTHUSDT | IDLE | 1.77 | 6.39 | 1.61 | 0.1 | 6221838.06 | 4.1 | skipped_fast |
| XRPUSDT | IDLE | 1.98 | 8.23 | 1.67 | 0.14 | 142043666.81 | 2.07 | skipped_fast |
| HBARUSDT | IDLE | 2.64 | 6.36 | 1.39 | 0.08 | 908339.88 | 1.25 | skipped_fast |
| ZBCNUSDT | IDLE | 2.9 | 11.25 | 3.06 | 0.12 | 515116.6 | 53.4 | skipped_fast |
| CCUSDT | IDLE | 1.91 | 7.42 | 1.05 | 0.13 | 644182.33 | 8.01 | skipped_fast |
| WUSDT | IDLE | 2.78 | 6.91 | 1.9 | 0.08 | 379020.19 | 14.42 | skipped_fast |
| CHIPUSDT | IDLE | 1.19 | 3.56 | 1.64 | 0.04 | 545135.32 | 6.19 | skipped_fast |
| BIOUSDT | IDLE | 2.3 | 5.04 | 1.14 | 0.02 | 187235.51 | 3.11 | skipped_fast |
| EDELUSDT | IDLE | 2.58 | 5.5 | 1.3 | -0.01 | 80067.28 | 11.0 | skipped_fast |
| RIZEUSDT | IDLE | 2.19 | 9.82 | 4.18 | 0.12 | 58870.53 | 44.22 | skipped_fast |
| TELUSDT | IDLE | 2.83 | 6.89 | 0.41 | 0.06 | 189898.14 | 10.27 | skipped_fast |
| REDUSDT | IDLE | 0.87 | 7.3 | 4.93 | 0.18 | 157753.08 | 8.9 | skipped_fast |
| QNTUSDT | IDLE | 2.59 | 5.68 | 0.06 | 0.07 | 155171.37 | 1.49 | skipped_fast |
| QAITUSDT | IDLE | 2.27 | 4.22 | 2.14 | -0.01 | 3715.41 | 67.45 | skipped_fast |
| RWAINCUSDT | IDLE | 2.13 | 4.07 | 1.27 | 0.02 | 10291.37 | 69.69 | skipped_fast |
| KITEUSDT | IDLE | 1.1 | 3.12 | 0.93 | 0.09 | 61534.25 | 12.02 | skipped_fast |
| RWAUSDT | IDLE | 1.06 | 2.08 | 0.24 | 0.04 | 54487.77 | 24.56 | skipped_fast |
| FLUIDUSDT | IDLE | 1.09 | 2.87 | 0.66 | 0.1 | 4934.79 | 20.55 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
