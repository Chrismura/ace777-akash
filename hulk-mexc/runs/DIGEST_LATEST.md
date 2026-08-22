# Hulk DIGEST — 2026-08-22T03:32:09Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.4 | 11.15 | 0.32 | 0.18 | 7853968.1 | 1.87 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.47 | 14.16 | 0.93 | 0.21 | 164691607.1 | 5.05 | skipped_fast |
| HBARUSDT | IDLE | 2.36 | 6.74 | 0.0 | 0.12 | 1021598.0 | 1.2 | skipped_fast |
| CCUSDT | IDLE | 1.99 | 8.96 | 2.07 | 0.16 | 682108.19 | 7.68 | skipped_fast |
| BIOUSDT | IDLE | 3.0 | 7.36 | 2.14 | 0.08 | 198231.34 | 3.0 | skipped_fast |
| CHIPUSDT | IDLE | 1.98 | 4.43 | 0.0 | -0.02 | 452630.13 | 2.97 | skipped_fast |
| WUSDT | IDLE | 1.8 | 5.79 | 0.23 | 0.12 | 423651.58 | 7.88 | skipped_fast |
| ZBCNUSDT | IDLE | 1.42 | 5.16 | 1.65 | 0.12 | 537826.75 | 37.77 | skipped_fast |
| EDELUSDT | IDLE | 2.02 | 3.95 | 3.37 | -0.03 | 80005.09 | 22.47 | skipped_fast |
| REDUSDT | IDLE | 0.93 | 7.96 | 4.3 | 0.21 | 157697.03 | 0.79 | skipped_fast |
| RIZEUSDT | IDLE | 1.82 | 7.71 | 4.26 | 0.1 | 59553.19 | 44.22 | skipped_fast |
| RWAINCUSDT | IDLE | 1.87 | 3.44 | 2.06 | 0.01 | 9365.21 | 21.62 | skipped_fast |
| KITEUSDT | IDLE | 1.39 | 4.5 | 0.09 | 0.12 | 67723.84 | 14.25 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | 0.0 | 3808.79 | 63.67 | skipped_fast |
| QNTUSDT | IDLE | 1.76 | 4.31 | 0.0 | 0.09 | 174225.15 | 7.4 | skipped_fast |
| RWAUSDT | IDLE | 1.37 | 2.72 | 0.08 | 0.05 | 56311.69 | 8.04 | skipped_fast |
| TELUSDT | IDLE | 1.01 | 2.45 | 0.15 | 0.08 | 173554.25 | 56.08 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.07 | 4710.05 | 15.98 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
