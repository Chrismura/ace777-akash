# Hulk DIGEST — 2026-08-21T23:34:37Z

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
| PYTHUSDT | IDLE | 1.74 | 6.39 | 0.89 | 0.11 | 6106780.47 | 2.03 | skipped_fast |
| XRPUSDT | IDLE | 1.93 | 8.23 | 0.2 | 0.15 | 140818311.8 | 3.4 | skipped_fast |
| HBARUSDT | IDLE | 2.56 | 6.29 | 0.16 | 0.1 | 905262.63 | 3.72 | skipped_fast |
| ZBCNUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.83 | 11.25 | 1.11 | 0.14 | 513264.09 | 49.65 | skipped_fast |
| CCUSDT | IDLE | 1.91 | 7.42 | 1.13 | 0.13 | 645450.83 | 0.89 | skipped_fast |
| WUSDT | IDLE | 2.74 | 6.91 | 1.32 | 0.08 | 379663.21 | 18.44 | skipped_fast |
| CHIPUSDT | IDLE | 1.18 | 3.56 | 1.43 | 0.03 | 549132.93 | 3.09 | skipped_fast |
| BIOUSDT | IDLE | 2.25 | 5.04 | 0.46 | 0.02 | 186476.66 | 3.1 | skipped_fast |
| EDELUSDT | IDLE | 2.53 | 5.5 | 0.65 | -0.03 | 82459.42 | 21.83 | skipped_fast |
| RIZEUSDT | IDLE | 2.2 | 9.82 | 4.39 | 0.12 | 58920.23 | 45.81 | skipped_fast |
| TELUSDT | IDLE | 2.7 | 6.62 | 0.1 | 0.07 | 186971.28 | 20.53 | skipped_fast |
| REDUSDT | IDLE | 0.87 | 7.3 | 4.7 | 0.18 | 157752.94 | 8.87 | skipped_fast |
| QNTUSDT | IDLE | 2.59 | 5.68 | 0.07 | 0.07 | 135267.39 | 1.49 | skipped_fast |
| QAITUSDT | IDLE | 2.27 | 4.22 | 2.14 | -0.02 | 3921.68 | 67.45 | skipped_fast |
| RWAINCUSDT | IDLE | 2.25 | 4.07 | 2.85 | 0.01 | 10124.73 | 75.92 | skipped_fast |
| KITEUSDT | IDLE | 1.1 | 3.12 | 0.93 | 0.09 | 61400.67 | 11.1 | skipped_fast |
| RWAUSDT | IDLE | 1.06 | 2.08 | 0.33 | 0.04 | 54589.22 | 24.56 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 2.87 | 0.0 | 0.11 | 4903.8 | 21.93 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
