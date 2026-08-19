# Hulk DIGEST — 2026-08-19T22:12:06Z

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
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.33 | 8.01 | 0.85 | 0.13 | 37885965.54 | 1.78 | skipped_fast |
| RIZEUSDT | IMPULSE_WAIT — spike en cours, pas chase | 4.14 | 8.37 | 1.95 | 0.0 | 46689.67 | 50.62 | skipped_fast |
| PYTHUSDT | IDLE | 2.43 | 7.21 | 1.55 | 0.09 | 303990.46 | 2.38 | skipped_fast |
| CCUSDT | IDLE | 2.19 | 6.61 | 0.59 | 0.1 | 322031.92 | 8.02 | skipped_fast |
| ZBCNUSDT | IDLE | 2.34 | 10.52 | 2.19 | 0.15 | 222959.95 | 28.9 | skipped_fast |
| REDUSDT | IDLE | 2.42 | 10.48 | 6.6 | 0.02 | 105103.7 | 21.85 | skipped_fast |
| WUSDT | IDLE | 1.81 | 4.13 | 1.14 | 0.07 | 241515.37 | 11.57 | skipped_fast |
| EDELUSDT | IDLE | 1.95 | 10.91 | 1.44 | 0.2 | 82184.1 | 33.69 | skipped_fast |
| HBARUSDT | IDLE | 2.09 | 4.1 | 0.53 | 0.06 | 312337.34 | 1.4 | skipped_fast |
| CHIPUSDT | IDLE | 1.1 | 3.32 | 2.58 | 0.07 | 183110.11 | 10.75 | skipped_fast |
| BIOUSDT | IDLE | 1.06 | 5.1 | 3.02 | 0.14 | 147331.61 | 7.15 | skipped_fast |
| KITEUSDT | IDLE | 1.46 | 2.9 | 1.04 | 0.05 | 58898.26 | 14.54 | skipped_fast |
| TELUSDT | IDLE | 1.64 | 7.85 | 1.64 | 0.12 | 186044.78 | 36.92 | skipped_fast |
| FLUIDUSDT | IDLE | 2.08 | 6.09 | 0.26 | 0.09 | 2878.05 | 19.63 | skipped_fast |
| QAITUSDT | IDLE | 1.11 | 2.92 | 1.69 | 0.03 | 11144.08 | 62.16 | skipped_fast |
| QNTUSDT | IDLE | 1.82 | 3.49 | 0.94 | 0.05 | 40963.82 | 6.81 | skipped_fast |
| RWAINCUSDT | IDLE | 0.96 | 2.82 | 0.95 | 0.04 | 16748.39 | 96.45 | skipped_fast |
| RWAUSDT | IDLE | 0.8 | 1.57 | 0.26 | 0.01 | 54064.51 | 25.85 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
