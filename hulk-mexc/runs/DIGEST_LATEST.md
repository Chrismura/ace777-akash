# Hulk DIGEST — 2026-08-21T23:08:40Z

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
| PYTHUSDT | IDLE | 1.72 | 6.39 | 0.32 | 0.12 | 5979172.83 | 2.02 | skipped_fast |
| XRPUSDT | IDLE | 1.76 | 6.77 | 0.43 | 0.15 | 138452770.51 | 2.07 | skipped_fast |
| CCUSDT | IDLE | 1.91 | 7.42 | 1.1 | 0.13 | 666551.7 | 6.23 | skipped_fast |
| HBARUSDT | IDLE | 2.38 | 5.24 | 0.0 | 0.09 | 890083.71 | 1.25 | skipped_fast |
| ZBCNUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.51 | 10.14 | 0.05 | 0.15 | 511412.06 | 32.86 | skipped_fast |
| WUSDT | IDLE | 2.75 | 6.91 | 1.41 | 0.08 | 376805.74 | 13.33 | skipped_fast |
| CHIPUSDT | IDLE | 1.17 | 3.56 | 1.09 | 0.05 | 544899.02 | 6.15 | skipped_fast |
| BIOUSDT | IDLE | 2.3 | 5.04 | 1.23 | 0.02 | 187365.86 | 6.23 | skipped_fast |
| EDELUSDT | IDLE | 2.51 | 5.5 | 0.33 | -0.03 | 82492.95 | 32.7 | skipped_fast |
| RWAINCUSDT | IDLE | 2.18 | 4.07 | 1.96 | 0.02 | 10220.57 | 16.16 | skipped_fast |
| QAITUSDT | IDLE | 2.27 | 4.22 | 2.14 | -0.02 | 3921.68 | 43.69 | skipped_fast |
| REDUSDT | IDLE | 0.87 | 7.3 | 5.09 | 0.18 | 157324.44 | 20.26 | skipped_fast |
| TELUSDT | IDLE | 2.67 | 6.51 | 0.31 | 0.07 | 185014.57 | 46.36 | skipped_fast |
| QNTUSDT | IDLE | 2.51 | 5.22 | 0.01 | 0.07 | 102405.07 | 1.5 | skipped_fast |
| KITEUSDT | IDLE | 1.11 | 3.12 | 1.21 | 0.09 | 61550.26 | 12.98 | skipped_fast |
| RIZEUSDT | IDLE | 1.15 | 5.32 | 1.2 | 0.08 | 57688.53 | 46.34 | skipped_fast |
| RWAUSDT | IDLE | 1.03 | 2.0 | 0.41 | 0.04 | 54404.48 | 24.58 | skipped_fast |
| FLUIDUSDT | IDLE | 0.51 | 1.15 | 0.08 | 0.09 | 4171.26 | 21.83 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
