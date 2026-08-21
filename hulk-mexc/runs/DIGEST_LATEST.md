# Hulk DIGEST — 2026-08-21T23:36:23Z

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
| PYTHUSDT | IDLE | 1.75 | 6.39 | 1.19 | 0.1 | 6116492.71 | 4.08 | skipped_fast |
| XRPUSDT | IDLE | 1.94 | 8.23 | 0.51 | 0.16 | 140989551.1 | 4.77 | skipped_fast |
| HBARUSDT | IDLE | 2.57 | 6.36 | 0.2 | 0.1 | 906796.19 | 1.24 | skipped_fast |
| ZBCNUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.84 | 11.25 | 1.57 | 0.13 | 513137.03 | 35.35 | skipped_fast |
| CCUSDT | IDLE | 1.91 | 7.42 | 1.01 | 0.13 | 645457.3 | 8.0 | skipped_fast |
| WUSDT | IDLE | 2.75 | 6.91 | 1.39 | 0.08 | 380089.52 | 12.3 | skipped_fast |
| CHIPUSDT | IDLE | 1.18 | 3.56 | 1.4 | 0.03 | 549164.43 | 6.17 | skipped_fast |
| BIOUSDT | IDLE | 2.28 | 5.04 | 0.92 | 0.02 | 186420.7 | 6.21 | skipped_fast |
| EDELUSDT | IDLE | 2.53 | 5.5 | 0.54 | -0.03 | 82459.49 | 21.83 | skipped_fast |
| RIZEUSDT | IDLE | 2.19 | 9.82 | 4.16 | 0.12 | 58911.29 | 44.11 | skipped_fast |
| TELUSDT | IDLE | 2.7 | 6.62 | 0.21 | 0.07 | 187444.48 | 20.53 | skipped_fast |
| RWAINCUSDT | IDLE | 2.25 | 4.07 | 2.85 | 0.01 | 10202.52 | 38.03 | skipped_fast |
| REDUSDT | IDLE | 0.87 | 7.3 | 4.52 | 0.19 | 157732.31 | 18.55 | skipped_fast |
| QNTUSDT | IDLE | 2.59 | 5.68 | 0.06 | 0.07 | 138607.23 | 1.49 | skipped_fast |
| QAITUSDT | IDLE | 2.27 | 4.22 | 2.14 | -0.02 | 3921.68 | 67.45 | skipped_fast |
| KITEUSDT | IDLE | 1.1 | 3.12 | 0.93 | 0.09 | 61424.22 | 11.1 | skipped_fast |
| RWAUSDT | IDLE | 1.06 | 2.08 | 0.33 | 0.04 | 54580.1 | 16.38 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 2.87 | 0.0 | 0.11 | 4903.8 | 23.35 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
