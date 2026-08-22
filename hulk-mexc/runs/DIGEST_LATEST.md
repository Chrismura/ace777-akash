# Hulk DIGEST — 2026-08-22T01:59:09Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.87 | 10.86 | 0.91 | 0.14 | 6868901.17 | 1.95 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.42 | 10.52 | 1.75 | 0.15 | 153863041.55 | 4.05 | skipped_fast |
| HBARUSDT | IDLE | 3.02 | 6.36 | 0.88 | 0.07 | 950589.37 | 1.25 | skipped_fast |
| ZBCNUSDT | IDLE | 2.6 | 10.08 | 2.84 | 0.09 | 549528.54 | 14.52 | skipped_fast |
| CCUSDT | IDLE | 1.81 | 7.36 | 0.88 | 0.15 | 662283.11 | 8.8 | skipped_fast |
| WUSDT | IDLE | 2.66 | 6.7 | 0.0 | 0.09 | 399216.03 | 8.08 | skipped_fast |
| CHIPUSDT | IDLE | 1.57 | 3.56 | 0.46 | 0.02 | 510456.7 | 3.05 | skipped_fast |
| BIOUSDT | IDLE | 2.59 | 5.86 | 0.12 | 0.06 | 184809.39 | 6.08 | skipped_fast |
| EDELUSDT | IDLE | 2.63 | 5.5 | 2.06 | -0.02 | 79546.09 | 22.15 | skipped_fast |
| RIZEUSDT | IDLE | 1.97 | 8.52 | 3.87 | 0.11 | 61079.73 | 45.71 | skipped_fast |
| REDUSDT | IDLE | 1.0 | 8.27 | 6.22 | 0.16 | 156931.22 | 17.82 | skipped_fast |
| QNTUSDT | IDLE | 2.42 | 5.18 | 1.02 | 0.07 | 171326.53 | 1.51 | skipped_fast |
| KITEUSDT | IDLE | 1.6 | 5.17 | 0.1 | 0.13 | 61244.07 | 11.63 | skipped_fast |
| TELUSDT | IDLE | 2.58 | 6.19 | 1.02 | 0.05 | 180991.22 | 36.2 | skipped_fast |
| QAITUSDT | IDLE | 2.04 | 4.02 | 0.43 | 0.01 | 3870.41 | 31.31 | skipped_fast |
| RWAINCUSDT | IDLE | 1.77 | 3.27 | 1.79 | 0.03 | 9181.85 | 80.36 | skipped_fast |
| FLUIDUSDT | IDLE | 1.46 | 3.74 | 2.03 | 0.07 | 4710.05 | 21.23 | skipped_fast |
| RWAUSDT | IDLE | 1.08 | 2.08 | 0.49 | 0.03 | 54607.19 | 8.21 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
