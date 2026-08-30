# Hulk DIGEST — 2026-08-30T02:07:13Z

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
| XRPUSDT | IDLE | 0.41 | 0.76 | 0.41 | 0.01 | 16490531.04 | 2.15 | skipped_fast |
| CHIPUSDT | IDLE | 1.2 | 3.48 | 2.56 | -0.04 | 818941.01 | 12.5 | skipped_fast |
| RIZEUSDT | IDLE | 2.68 | 8.3 | 2.78 | -0.01 | 42408.18 | 60.45 | skipped_fast |
| PYTHUSDT | IDLE | 0.88 | 1.55 | 1.37 | 0.0 | 317753.32 | 2.1 | skipped_fast |
| ZBCNUSDT | IDLE | 1.39 | 2.57 | 1.45 | -0.03 | 201956.21 | 18.94 | skipped_fast |
| CCUSDT | IDLE | 0.84 | 1.62 | 0.93 | 0.07 | 239794.69 | 3.38 | skipped_fast |
| BIOUSDT | IDLE | 0.92 | 1.76 | 0.5 | -0.01 | 67455.29 | 3.62 | skipped_fast |
| WUSDT | IDLE | 0.52 | 0.98 | 0.4 | -0.0 | 177511.06 | 18.65 | skipped_fast |
| KITEUSDT | IDLE | 0.79 | 2.04 | 1.55 | 0.02 | 67470.78 | 7.76 | skipped_fast |
| REDUSDT | IDLE | 0.84 | 1.52 | 1.05 | 0.02 | 76358.34 | 13.75 | skipped_fast |
| TELUSDT | IDLE | 2.37 | 4.4 | 2.31 | -0.05 | 71345.66 | 47.31 | skipped_fast |
| EDELUSDT | IDLE | 0.2 | 3.82 | 1.23 | 0.08 | 121742.64 | 17.73 | skipped_fast |
| RWAINCUSDT | IDLE | 0.84 | 1.47 | 1.45 | -0.04 | 1577.44 | 107.37 | skipped_fast |
| HBARUSDT | IDLE | 0.34 | 0.61 | 0.52 | -0.0 | 131814.02 | 1.33 | skipped_fast |
| QNTUSDT | IDLE | 0.76 | 1.46 | 0.45 | 0.01 | 31501.42 | 4.86 | skipped_fast |
| FLUIDUSDT | IDLE | 0.9 | 1.61 | 1.24 | -0.01 | 2078.48 | 21.5 | skipped_fast |
| RWAUSDT | IDLE | 0.63 | 1.24 | 0.16 | 0.01 | 53885.42 | 16.31 | skipped_fast |
| QAITUSDT | ERR | — | — | — | — | — | — | HTTP Error 400: Bad Request |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
