# Hulk DIGEST — 2026-08-29T14:07:36Z

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
| XRPUSDT | IDLE | 0.37 | 0.73 | 0.12 | -0.01 | 35341399.42 | 2.88 | skipped_fast |
| CHIPUSDT | IDLE | 1.5 | 6.99 | 3.65 | -0.09 | 1094920.04 | 2.46 | skipped_fast |
| EDELUSDT | IDLE | 2.79 | 10.29 | 3.86 | -0.07 | 102697.22 | 37.21 | skipped_fast |
| PYTHUSDT | IDLE | 1.32 | 2.57 | 0.5 | 0.01 | 393467.47 | 4.2 | skipped_fast |
| REDUSDT | IDLE | 1.85 | 5.15 | 4.25 | 0.03 | 76514.7 | 12.78 | skipped_fast |
| CCUSDT | IDLE | 1.42 | 2.79 | 0.35 | 0.03 | 212478.39 | 5.23 | skipped_fast |
| ZBCNUSDT | IDLE | 1.12 | 2.71 | 2.05 | -0.07 | 187833.28 | 4.64 | skipped_fast |
| KITEUSDT | IDLE | 1.7 | 3.4 | 0.02 | 0.05 | 63242.58 | 11.41 | skipped_fast |
| WUSDT | IDLE | 0.82 | 1.63 | 0.03 | -0.02 | 212157.6 | 12.03 | skipped_fast |
| RIZEUSDT | IDLE | 1.66 | 3.64 | 0.02 | -0.01 | 26981.03 | 55.08 | skipped_fast |
| BIOUSDT | IDLE | 0.41 | 0.8 | 0.14 | -0.02 | 82598.26 | 3.63 | skipped_fast |
| HBARUSDT | IDLE | 0.35 | 0.68 | 0.08 | -0.02 | 366862.39 | 2.66 | skipped_fast |
| TELUSDT | IDLE | 0.83 | 1.5 | 1.03 | -0.04 | 77718.31 | 34.58 | skipped_fast |
| RWAINCUSDT | IDLE | 0.53 | 1.0 | 0.39 | -0.03 | 4402.82 | 111.3 | skipped_fast |
| QNTUSDT | IDLE | 0.54 | 0.97 | 0.67 | -0.01 | 33500.4 | 6.56 | skipped_fast |
| RWAUSDT | IDLE | 0.27 | 0.5 | 0.33 | 0.02 | 56656.04 | 16.47 | skipped_fast |
| FLUIDUSDT | IDLE | 0.54 | 1.06 | 0.09 | -0.01 | 1919.89 | 21.45 | skipped_fast |
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
