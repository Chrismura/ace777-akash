# Hulk DIGEST — 2026-08-22T01:44:16Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.85 | 10.86 | 0.46 | 0.16 | 6813316.02 | 11.65 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.28 | 9.57 | 0.05 | 0.16 | 151707239.05 | 3.34 | skipped_fast |
| HBARUSDT | IDLE | 3.0 | 6.36 | 0.57 | 0.08 | 960029.21 | 1.24 | skipped_fast |
| ZBCNUSDT | IDLE | 2.6 | 10.08 | 2.89 | 0.08 | 549496.0 | 13.56 | skipped_fast |
| CCUSDT | IDLE | 1.79 | 7.36 | 0.24 | 0.16 | 661219.25 | 9.61 | skipped_fast |
| WUSDT | IDLE | 2.68 | 6.65 | 0.33 | 0.09 | 390771.97 | 11.15 | skipped_fast |
| CHIPUSDT | IDLE | 1.62 | 3.56 | 1.19 | 0.02 | 512325.03 | 6.17 | skipped_fast |
| BIOUSDT | IDLE | 2.47 | 5.57 | 0.21 | 0.05 | 186874.96 | 3.06 | skipped_fast |
| EDELUSDT | IDLE | 2.62 | 5.5 | 1.95 | -0.02 | 79516.18 | 22.12 | skipped_fast |
| RIZEUSDT | IDLE | 1.97 | 8.52 | 3.8 | 0.11 | 60903.05 | 45.71 | skipped_fast |
| REDUSDT | IDLE | 0.98 | 8.27 | 4.92 | 0.17 | 158210.96 | 9.59 | skipped_fast |
| KITEUSDT | IDLE | 1.61 | 5.17 | 0.44 | 0.13 | 61574.39 | 10.78 | skipped_fast |
| TELUSDT | IDLE | 2.61 | 6.19 | 1.53 | 0.05 | 182231.87 | 41.58 | skipped_fast |
| QNTUSDT | IDLE | 2.44 | 5.18 | 1.24 | 0.07 | 171661.19 | 10.57 | skipped_fast |
| QAITUSDT | IDLE | 2.04 | 4.02 | 0.43 | 0.01 | 3870.41 | 31.31 | skipped_fast |
| RWAINCUSDT | IDLE | 1.77 | 3.27 | 1.79 | 0.03 | 9235.4 | 85.56 | skipped_fast |
| FLUIDUSDT | IDLE | 1.35 | 3.74 | 0.0 | 0.1 | 4798.05 | 21.99 | skipped_fast |
| RWAUSDT | IDLE | 1.08 | 2.08 | 0.57 | 0.03 | 54673.14 | 24.6 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
