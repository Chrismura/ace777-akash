# Hulk DIGEST — 2026-08-21T23:12:10Z

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
| PYTHUSDT | IDLE | 1.73 | 6.39 | 0.54 | 0.12 | 5996816.98 | 2.03 | skipped_fast |
| XRPUSDT | IDLE | 1.75 | 6.77 | 0.31 | 0.15 | 138542912.23 | 2.07 | skipped_fast |
| CCUSDT | IDLE | 1.91 | 7.42 | 1.08 | 0.13 | 666444.08 | 9.77 | skipped_fast |
| HBARUSDT | IDLE | 2.39 | 5.24 | 0.05 | 0.09 | 890369.39 | 1.25 | skipped_fast |
| ZBCNUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.52 | 10.14 | 0.22 | 0.15 | 511380.54 | 32.4 | skipped_fast |
| WUSDT | IDLE | 2.74 | 6.91 | 1.28 | 0.08 | 374872.97 | 11.25 | skipped_fast |
| CHIPUSDT | IDLE | 1.16 | 3.56 | 1.03 | 0.05 | 546001.89 | 3.07 | skipped_fast |
| BIOUSDT | IDLE | 2.32 | 5.04 | 1.45 | 0.02 | 187473.23 | 3.12 | skipped_fast |
| EDELUSDT | IDLE | 2.53 | 5.5 | 0.54 | -0.03 | 82514.69 | 21.81 | skipped_fast |
| RWAINCUSDT | IDLE | 2.18 | 4.07 | 1.96 | 0.01 | 10220.57 | 16.16 | skipped_fast |
| REDUSDT | IDLE | 0.88 | 7.3 | 5.28 | 0.18 | 157411.39 | 10.56 | skipped_fast |
| QAITUSDT | IDLE | 2.27 | 4.22 | 2.14 | -0.02 | 3921.68 | 43.69 | skipped_fast |
| TELUSDT | IDLE | 2.66 | 6.51 | 0.26 | 0.07 | 184994.97 | 51.49 | skipped_fast |
| QNTUSDT | IDLE | 2.52 | 5.22 | 0.09 | 0.07 | 113598.96 | 1.5 | skipped_fast |
| RIZEUSDT | IDLE | 1.51 | 7.18 | 0.0 | 0.11 | 58709.56 | 43.62 | skipped_fast |
| KITEUSDT | IDLE | 1.11 | 3.12 | 1.14 | 0.09 | 61573.36 | 11.12 | skipped_fast |
| RWAUSDT | IDLE | 1.01 | 2.0 | 0.16 | 0.04 | 54410.35 | 24.58 | skipped_fast |
| FLUIDUSDT | IDLE | 0.92 | 2.35 | 0.18 | 0.1 | 4226.13 | 21.93 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
