# Hulk DIGEST — 2026-08-22T02:04:13Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.4 | 8.42 | 0.75 | 0.14 | 6884441.62 | 3.9 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.34 | 10.03 | 1.68 | 0.15 | 154051203.33 | 3.37 | skipped_fast |
| HBARUSDT | IDLE | 2.32 | 4.9 | 0.54 | 0.07 | 952093.19 | 1.24 | skipped_fast |
| ZBCNUSDT | IDLE | 2.49 | 9.63 | 2.96 | 0.09 | 547783.48 | 16.46 | skipped_fast |
| CCUSDT | IDLE | 1.67 | 6.1 | 0.05 | 0.15 | 657766.76 | 8.72 | skipped_fast |
| CHIPUSDT | IDLE | 1.61 | 3.69 | 0.27 | 0.02 | 516318.4 | 3.04 | skipped_fast |
| BIOUSDT | IDLE | 2.87 | 5.96 | 0.06 | 0.08 | 185049.22 | 8.99 | skipped_fast |
| WUSDT | IDLE | 1.72 | 4.41 | 0.17 | 0.09 | 400308.65 | 15.14 | skipped_fast |
| EDELUSDT | IDLE | 2.38 | 5.02 | 1.63 | -0.01 | 79621.2 | 33.09 | skipped_fast |
| RIZEUSDT | IDLE | 1.98 | 8.52 | 3.98 | 0.11 | 61064.13 | 45.71 | skipped_fast |
| REDUSDT | IDLE | 1.0 | 8.27 | 6.03 | 0.17 | 156772.18 | 17.78 | skipped_fast |
| QNTUSDT | IDLE | 2.28 | 4.89 | 0.82 | 0.07 | 171350.57 | 7.53 | skipped_fast |
| KITEUSDT | IDLE | 1.33 | 4.09 | 0.4 | 0.13 | 61324.48 | 10.78 | skipped_fast |
| QAITUSDT | IDLE | 1.78 | 3.57 | 0.0 | 0.01 | 3870.41 | 31.31 | skipped_fast |
| TELUSDT | IDLE | 2.14 | 5.11 | 1.02 | 0.05 | 178893.4 | 41.37 | skipped_fast |
| RWAINCUSDT | IDLE | 1.75 | 3.27 | 1.58 | 0.03 | 9241.73 | 64.41 | skipped_fast |
| FLUIDUSDT | IDLE | 1.44 | 3.69 | 2.03 | 0.07 | 4710.05 | 21.2 | skipped_fast |
| RWAUSDT | IDLE | 1.07 | 2.08 | 0.41 | 0.04 | 54551.63 | 8.2 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
