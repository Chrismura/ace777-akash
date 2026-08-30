# Hulk DIGEST — 2026-08-30T11:07:25Z

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
| XRPUSDT | IDLE | 0.84 | 1.53 | 0.94 | 0.0 | 16674927.58 | 2.16 | skipped_fast |
| CHIPUSDT | IDLE | 2.21 | 3.98 | 2.97 | -0.04 | 608159.38 | 2.53 | skipped_fast |
| WUSDT | IDLE | 1.99 | 3.88 | 0.66 | 0.04 | 209184.32 | 11.67 | skipped_fast |
| PYTHUSDT | IDLE | 1.26 | 2.42 | 0.73 | 0.01 | 331292.47 | 4.21 | skipped_fast |
| ZBCNUSDT | IDLE | 1.89 | 3.58 | 1.3 | 0.0 | 156545.16 | 3.59 | skipped_fast |
| CCUSDT | IDLE | 0.79 | 1.41 | 1.17 | 0.05 | 296343.8 | 6.76 | skipped_fast |
| BIOUSDT | IDLE | 1.41 | 2.59 | 1.48 | -0.01 | 67896.42 | 3.66 | skipped_fast |
| KITEUSDT | IDLE | 0.96 | 2.13 | 1.79 | 0.0 | 70629.36 | 11.73 | skipped_fast |
| REDUSDT | IDLE | 0.85 | 1.6 | 0.67 | -0.04 | 66030.81 | 11.87 | skipped_fast |
| RIZEUSDT | IDLE | 1.12 | 4.47 | 2.4 | -0.05 | 47023.44 | 61.55 | skipped_fast |
| RWAINCUSDT | IDLE | 0.91 | 1.59 | 1.57 | -0.02 | 1396.06 | 16.94 | skipped_fast |
| EDELUSDT | IDLE | 0.24 | 4.36 | 1.09 | 0.16 | 121942.86 | 33.78 | skipped_fast |
| FLUIDUSDT | IDLE | 1.18 | 2.3 | 0.34 | 0.03 | 3393.64 | 21.61 | skipped_fast |
| HBARUSDT | IDLE | 0.28 | 0.53 | 0.23 | 0.0 | 145538.52 | 2.66 | skipped_fast |
| TELUSDT | IDLE | 0.61 | 1.13 | 0.65 | -0.03 | 73053.5 | 29.66 | skipped_fast |
| QNTUSDT | IDLE | 0.49 | 0.96 | 0.19 | 0.01 | 36767.94 | 9.73 | skipped_fast |
| RWAUSDT | IDLE | 0.27 | 0.49 | 0.33 | 0.01 | 52180.79 | 32.71 | skipped_fast |
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
