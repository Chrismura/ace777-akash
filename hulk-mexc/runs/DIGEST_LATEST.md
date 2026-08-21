# Hulk DIGEST — 2026-08-21T23:16:31Z

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
| PYTHUSDT | IDLE | 1.73 | 6.39 | 0.58 | 0.12 | 6020761.62 | 4.06 | skipped_fast |
| XRPUSDT | IDLE | 1.76 | 6.77 | 0.56 | 0.14 | 138574199.81 | 1.38 | skipped_fast |
| HBARUSDT | IDLE | 2.48 | 5.82 | 0.02 | 0.1 | 892800.86 | 1.24 | skipped_fast |
| CCUSDT | IDLE | 1.92 | 7.42 | 1.29 | 0.13 | 656939.11 | 6.24 | skipped_fast |
| ZBCNUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.51 | 10.14 | 0.04 | 0.15 | 511483.86 | 17.59 | skipped_fast |
| WUSDT | IDLE | 2.75 | 6.91 | 1.46 | 0.08 | 377021.75 | 10.26 | skipped_fast |
| CHIPUSDT | IDLE | 1.16 | 3.56 | 0.91 | 0.05 | 547417.89 | 3.07 | skipped_fast |
| BIOUSDT | IDLE | 2.29 | 5.04 | 1.11 | 0.02 | 187893.24 | 3.12 | skipped_fast |
| EDELUSDT | IDLE | 2.53 | 5.5 | 0.65 | -0.03 | 82514.65 | 21.83 | skipped_fast |
| RWAINCUSDT | IDLE | 2.2 | 4.07 | 2.22 | 0.02 | 10178.81 | 26.99 | skipped_fast |
| REDUSDT | IDLE | 0.87 | 7.3 | 4.88 | 0.18 | 157456.83 | 11.31 | skipped_fast |
| TELUSDT | IDLE | 2.66 | 6.51 | 0.21 | 0.07 | 184929.77 | 51.49 | skipped_fast |
| QAITUSDT | IDLE | 2.27 | 4.22 | 2.14 | -0.02 | 3921.68 | 67.45 | skipped_fast |
| QNTUSDT | IDLE | 2.51 | 5.22 | 0.06 | 0.07 | 118385.16 | 1.5 | skipped_fast |
| KITEUSDT | IDLE | 1.12 | 3.12 | 1.47 | 0.09 | 61606.98 | 12.07 | skipped_fast |
| RIZEUSDT | IDLE | 1.95 | 9.29 | 0.0 | 0.13 | 58956.12 | 263.72 | skipped_fast |
| RWAUSDT | IDLE | 1.02 | 2.0 | 0.25 | 0.04 | 54450.21 | 8.19 | skipped_fast |
| FLUIDUSDT | IDLE | 0.92 | 2.35 | 0.18 | 0.1 | 4226.13 | 21.21 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
