# Hulk DIGEST — 2026-08-22T16:16:41Z

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
| PYTHUSDT | IDLE | 1.51 | 7.24 | 1.44 | 0.05 | 51448069.67 | 1.97 | skipped_fast |
| XRPUSDT | IDLE | 1.37 | 7.64 | 5.26 | 0.04 | 215369266.42 | 1.38 | skipped_fast |
| HBARUSDT | IDLE | 0.84 | 3.03 | 2.04 | -0.01 | 1140894.01 | 2.61 | skipped_fast |
| CCUSDT | IDLE | 0.99 | 4.14 | 2.68 | 0.09 | 769138.38 | 5.99 | skipped_fast |
| CHIPUSDT | IDLE | 0.58 | 3.36 | 1.2 | -0.1 | 623789.01 | 3.36 | skipped_fast |
| WUSDT | IDLE | 0.66 | 2.58 | 2.01 | -0.02 | 545971.26 | 14.98 | skipped_fast |
| ZBCNUSDT | IDLE | 1.35 | 3.49 | 2.65 | -0.05 | 316425.76 | 14.5 | skipped_fast |
| BIOUSDT | IDLE | 0.97 | 6.58 | 4.85 | -0.07 | 219765.45 | 6.62 | skipped_fast |
| KITEUSDT | IDLE | 1.87 | 4.35 | 1.15 | 0.04 | 85471.73 | 12.43 | skipped_fast |
| EDELUSDT | IDLE | 1.44 | 2.52 | 2.35 | -0.03 | 74865.2 | 22.88 | skipped_fast |
| REDUSDT | IDLE | 0.53 | 5.67 | 4.54 | -0.12 | 133935.74 | 10.07 | skipped_fast |
| RIZEUSDT | IDLE | 1.32 | 3.23 | 0.05 | 0.03 | 56544.27 | 45.5 | skipped_fast |
| QAITUSDT | IDLE | 1.67 | 3.19 | 0.94 | 0.01 | 2320.37 | 67.45 | skipped_fast |
| QNTUSDT | IDLE | 0.87 | 2.69 | 2.36 | -0.02 | 183794.76 | 1.58 | skipped_fast |
| RWAINCUSDT | IDLE | 0.77 | 1.53 | 0.0 | 0.01 | 8954.22 | 86.02 | skipped_fast |
| TELUSDT | IDLE | 0.96 | 2.37 | 1.47 | 0.0 | 137339.99 | 58.65 | skipped_fast |
| RWAUSDT | IDLE | 0.57 | 1.06 | 0.49 | 0.02 | 56298.36 | 16.26 | skipped_fast |
| FLUIDUSDT | IDLE | 0.0 | 0.0 | 0.0 | -0.03 | 4618.58 | 22.42 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
