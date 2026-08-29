# Hulk DIGEST — 2026-08-29T22:11:50Z

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
| XRPUSDT | IDLE | 0.64 | 1.18 | 0.61 | 0.01 | 17030565.07 | 2.15 | skipped_fast |
| CHIPUSDT | IDLE | 1.64 | 4.63 | 4.4 | -0.0 | 896770.25 | 2.49 | skipped_fast |
| RIZEUSDT | IDLE | 3.44 | 9.39 | 4.33 | -0.05 | 41420.51 | 59.91 | skipped_fast |
| ZBCNUSDT | IDLE | 2.61 | 4.74 | 3.17 | -0.01 | 197434.41 | 17.66 | skipped_fast |
| PYTHUSDT | IDLE | 1.92 | 3.52 | 2.14 | 0.03 | 322728.11 | 6.24 | skipped_fast |
| CCUSDT | IDLE | 1.31 | 2.52 | 0.81 | 0.07 | 226343.05 | 3.39 | skipped_fast |
| KITEUSDT | IDLE | 1.6 | 4.24 | 2.56 | 0.02 | 67574.06 | 10.02 | skipped_fast |
| WUSDT | IDLE | 0.62 | 1.13 | 0.78 | 0.0 | 178285.0 | 9.86 | skipped_fast |
| REDUSDT | IDLE | 1.14 | 2.24 | 0.21 | 0.01 | 75343.1 | 20.05 | skipped_fast |
| EDELUSDT | IDLE | 0.16 | 3.0 | 0.97 | 0.09 | 125026.01 | 8.89 | skipped_fast |
| BIOUSDT | IDLE | 0.49 | 0.88 | 0.69 | -0.01 | 66191.84 | 7.28 | skipped_fast |
| RWAINCUSDT | IDLE | 0.98 | 1.8 | 1.05 | -0.02 | 1671.17 | 84.48 | skipped_fast |
| TELUSDT | IDLE | 1.49 | 2.63 | 2.39 | -0.02 | 68506.3 | 40.88 | skipped_fast |
| HBARUSDT | IDLE | 0.37 | 0.7 | 0.29 | -0.0 | 158381.13 | 1.32 | skipped_fast |
| QNTUSDT | IDLE | 0.85 | 1.56 | 0.94 | 0.01 | 29947.04 | 1.63 | skipped_fast |
| RWAUSDT | IDLE | 0.28 | 0.5 | 0.41 | 0.01 | 54885.89 | 8.24 | skipped_fast |
| FLUIDUSDT | IDLE | 0.06 | 0.11 | 0.11 | -0.0 | 1915.06 | 20.64 | skipped_fast |
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
