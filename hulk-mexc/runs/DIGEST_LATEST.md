# Hulk DIGEST — 2026-09-20T20:02:54Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| XRPUSDT | IDLE | 1.43 | 2.78 | 0.49 | -0.01 | 41383414.65 | 2.13 | skipped_fast |
| ETHUSDT | IDLE | 1.28 | 2.48 | 0.56 | -0.0 | 265650662.09 | 0.65 | skipped_fast |
| BTCUSDT | IDLE | 0.52 | 1.0 | 0.33 | -0.0 | 470159791.69 | 0.0 | skipped_fast |
| HBARUSDT | IDLE | 2.08 | 6.02 | 5.26 | 0.04 | 1277385.32 | 4.69 | skipped_fast |
| WUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.57 | 8.05 | 1.48 | 0.04 | 434081.52 | 7.82 | skipped_fast |
| PYTHUSDT | IDLE | 2.39 | 4.8 | 0.89 | 0.0 | 678592.63 | 3.26 | skipped_fast |
| EDELUSDT | IDLE | 3.22 | 26.92 | 2.39 | 0.23 | 104935.01 | 28.24 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.88 | 8.37 | 5.02 | -0.02 | 87003.35 | 18.95 | skipped_fast |
| ZBCNUSDT | IDLE | 2.82 | 5.08 | 3.86 | -0.04 | 204763.42 | 43.28 | skipped_fast |
| CCUSDT | IDLE | 1.32 | 2.67 | 0.41 | -0.03 | 412883.62 | 7.38 | skipped_fast |
| BIOUSDT | IDLE | 2.25 | 4.38 | 0.75 | -0.02 | 80384.87 | 3.61 | skipped_fast |
| RWAINCUSDT | IDLE | 3.45 | 6.62 | 1.87 | -0.04 | 9076.68 | 119.98 | skipped_fast |
| REDUSDT | IDLE | 1.42 | 2.77 | 0.53 | 0.02 | 73271.8 | 8.58 | skipped_fast |
| KITEUSDT | IDLE | 1.26 | 2.52 | 0.01 | 0.0 | 63448.59 | 12.16 | skipped_fast |
| TELUSDT | IDLE | 2.52 | 4.73 | 2.13 | 0.0 | 96034.56 | 46.16 | skipped_fast |
| QNTUSDT | IDLE | 1.51 | 2.85 | 1.13 | -0.01 | 81264.17 | 4.64 | skipped_fast |
| FLUIDUSDT | IDLE | 1.8 | 3.37 | 1.47 | -0.03 | 3772.9 | 22.33 | skipped_fast |
| RIZEUSDT | IDLE | 0.88 | 2.16 | 1.16 | -0.02 | 35100.38 | 96.21 | skipped_fast |
| RWAUSDT | IDLE | 0.72 | 1.41 | 0.15 | -0.0 | 54723.17 | 14.7 | skipped_fast |
| MNSRYUSDT | IDLE | 0.42 | 0.79 | 0.37 | -0.0 | 35927.01 | 54.45 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
