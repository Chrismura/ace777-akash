# Hulk DIGEST — 2026-08-16T20:08:19Z

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
| XRPUSDT | IDLE | 0.31 | 0.58 | 0.27 | -0.0 | 5648291.68 | 1.0 | skipped_fast |
| CHIPUSDT | IDLE | 2.32 | 10.74 | 6.44 | 0.08 | 277035.85 | 17.17 | skipped_fast |
| CCUSDT | IDLE | 1.44 | 2.74 | 2.21 | -0.03 | 340759.98 | 4.2 | skipped_fast |
| ZBCNUSDT | IDLE | 1.56 | 2.89 | 1.57 | 0.01 | 192792.22 | 19.06 | skipped_fast |
| WUSDT | IDLE | 1.46 | 2.57 | 2.32 | 0.01 | 170347.4 | 15.29 | skipped_fast |
| PYTHUSDT | IDLE | 1.01 | 1.79 | 1.49 | -0.02 | 130018.19 | 2.56 | skipped_fast |
| RIZEUSDT | IDLE | 1.83 | 3.52 | 0.99 | -0.0 | 35874.05 | 61.81 | skipped_fast |
| BIOUSDT | IDLE | 1.04 | 1.84 | 1.57 | -0.01 | 64280.93 | 4.08 | skipped_fast |
| EDELUSDT | IDLE | 1.46 | 2.67 | 1.69 | 0.04 | 60227.17 | 78.84 | skipped_fast |
| KITEUSDT | IDLE | 0.68 | 1.19 | 1.18 | -0.03 | 56569.17 | 14.93 | skipped_fast |
| QAITUSDT | IDLE | 0.99 | 3.07 | 0.87 | -0.05 | 2446.22 | 61.48 | skipped_fast |
| REDUSDT | IDLE | 0.17 | 1.4 | 1.27 | -0.06 | 87473.16 | 14.95 | skipped_fast |
| RWAINCUSDT | IDLE | 0.86 | 2.38 | 0.51 | 0.08 | 9825.35 | 50.98 | skipped_fast |
| TELUSDT | IDLE | 0.79 | 1.46 | 0.82 | -0.03 | 93871.73 | 48.26 | skipped_fast |
| QNTUSDT | IDLE | 0.5 | 0.88 | 0.78 | -0.01 | 32743.23 | 3.51 | skipped_fast |
| HBARUSDT | IDLE | 0.27 | 0.49 | 0.34 | -0.01 | 72042.99 | 1.53 | skipped_fast |
| RWAUSDT | IDLE | 0.32 | 0.61 | 0.17 | 0.0 | 52329.54 | 8.71 | skipped_fast |
| FLUIDUSDT | IDLE | 0.32 | 0.62 | 0.11 | 0.02 | 219.43 | 21.8 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
