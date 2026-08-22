# Hulk DIGEST — 2026-08-22T02:20:00Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.4 | 8.42 | 0.7 | 0.14 | 6942928.54 | 1.95 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.31 | 10.26 | 0.39 | 0.17 | 154260090.39 | 1.99 | skipped_fast |
| ZBCNUSDT | IDLE | 2.49 | 9.63 | 2.78 | 0.09 | 544870.97 | 11.61 | skipped_fast |
| HBARUSDT | IDLE | 2.28 | 4.9 | 0.06 | 0.08 | 961835.5 | 1.24 | skipped_fast |
| CCUSDT | IDLE | 1.69 | 6.24 | 0.0 | 0.15 | 654573.9 | 0.87 | skipped_fast |
| CHIPUSDT | IDLE | 2.22 | 5.07 | 0.42 | -0.0 | 514669.26 | 3.01 | skipped_fast |
| BIOUSDT | IDLE | 3.06 | 7.64 | 0.27 | 0.09 | 192695.13 | 5.91 | skipped_fast |
| WUSDT | IDLE | 1.81 | 4.91 | 0.0 | 0.1 | 401119.26 | 12.03 | skipped_fast |
| RIZEUSDT | IDLE | 1.98 | 8.52 | 3.9 | 0.11 | 61266.03 | 45.71 | skipped_fast |
| EDELUSDT | IDLE | 2.4 | 5.02 | 1.85 | -0.02 | 79698.93 | 66.59 | skipped_fast |
| REDUSDT | IDLE | 1.01 | 8.27 | 6.89 | 0.17 | 157090.61 | 17.14 | skipped_fast |
| QNTUSDT | IDLE | 2.26 | 4.89 | 0.54 | 0.07 | 171159.85 | 7.5 | skipped_fast |
| KITEUSDT | IDLE | 1.35 | 4.09 | 0.7 | 0.12 | 61650.74 | 11.72 | skipped_fast |
| QAITUSDT | IDLE | 1.86 | 3.57 | 0.94 | 0.0 | 3916.13 | 39.49 | skipped_fast |
| RWAINCUSDT | IDLE | 1.82 | 3.27 | 2.48 | 0.0 | 9406.34 | 59.6 | skipped_fast |
| TELUSDT | IDLE | 2.15 | 5.11 | 1.13 | 0.04 | 179438.51 | 41.39 | skipped_fast |
| FLUIDUSDT | IDLE | 1.44 | 3.69 | 2.03 | 0.07 | 4710.05 | 18.99 | skipped_fast |
| RWAUSDT | IDLE | 1.05 | 2.08 | 0.16 | 0.04 | 54807.25 | 16.37 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
