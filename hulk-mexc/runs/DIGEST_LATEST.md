# Hulk DIGEST — 2026-08-22T17:03:25Z

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
| PYTHUSDT | IDLE | 1.71 | 8.33 | 0.78 | 0.09 | 49194283.45 | 1.91 | skipped_fast |
| XRPUSDT | IDLE | 1.31 | 7.64 | 3.03 | 0.06 | 214570605.57 | 2.7 | skipped_fast |
| HBARUSDT | IDLE | 0.8 | 3.03 | 0.79 | -0.0 | 1125026.92 | 2.58 | skipped_fast |
| CCUSDT | IDLE | 0.93 | 4.14 | 0.74 | 0.1 | 770285.02 | 8.4 | skipped_fast |
| CHIPUSDT | IDLE | 0.57 | 3.36 | 0.83 | -0.1 | 631090.26 | 3.35 | skipped_fast |
| WUSDT | IDLE | 0.6 | 2.58 | 0.28 | -0.0 | 544005.59 | 13.69 | skipped_fast |
| ZBCNUSDT | IDLE | 1.27 | 3.45 | 1.33 | -0.02 | 312694.25 | 5.62 | skipped_fast |
| BIOUSDT | IDLE | 1.03 | 6.91 | 5.58 | -0.07 | 226150.83 | 3.34 | skipped_fast |
| KITEUSDT | IDLE | 1.4 | 3.22 | 1.15 | 0.03 | 87632.69 | 12.42 | skipped_fast |
| EDELUSDT | IDLE | 1.64 | 3.0 | 1.9 | -0.02 | 74794.37 | 34.23 | skipped_fast |
| REDUSDT | IDLE | 0.55 | 5.67 | 3.77 | -0.13 | 125398.31 | 14.57 | skipped_fast |
| RIZEUSDT | IDLE | 1.1 | 2.63 | 0.5 | 0.05 | 46180.7 | 45.5 | skipped_fast |
| QAITUSDT | IDLE | 1.39 | 2.71 | 0.47 | -0.01 | 2322.14 | 67.45 | skipped_fast |
| QNTUSDT | IDLE | 0.85 | 2.69 | 1.8 | -0.01 | 181174.22 | 4.72 | skipped_fast |
| RWAINCUSDT | IDLE | 0.8 | 1.53 | 0.43 | 0.01 | 7571.75 | 91.62 | skipped_fast |
| TELUSDT | IDLE | 1.0 | 2.37 | 2.15 | -0.0 | 136204.23 | 59.0 | skipped_fast |
| RWAUSDT | IDLE | 0.57 | 1.14 | 0.0 | 0.03 | 56307.92 | 16.16 | skipped_fast |
| FLUIDUSDT | IDLE | 0.1 | 0.19 | 0.19 | -0.03 | 4628.58 | 17.87 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
