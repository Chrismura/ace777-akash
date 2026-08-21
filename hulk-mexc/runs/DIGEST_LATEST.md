# Hulk DIGEST — 2026-08-21T23:40:30Z

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
| PYTHUSDT | IDLE | 1.76 | 6.39 | 1.39 | 0.1 | 6140950.92 | 2.05 | skipped_fast |
| XRPUSDT | IDLE | 1.95 | 8.23 | 1.03 | 0.15 | 141076575.81 | 6.17 | skipped_fast |
| HBARUSDT | IDLE | 2.61 | 6.36 | 0.87 | 0.09 | 909236.01 | 1.25 | skipped_fast |
| ZBCNUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.85 | 11.25 | 1.86 | 0.12 | 513874.95 | 30.18 | skipped_fast |
| CCUSDT | IDLE | 1.91 | 7.42 | 0.99 | 0.13 | 644458.97 | 6.22 | skipped_fast |
| WUSDT | IDLE | 2.77 | 6.91 | 1.76 | 0.08 | 379870.86 | 16.44 | skipped_fast |
| CHIPUSDT | IDLE | 1.18 | 3.56 | 1.28 | 0.03 | 547860.02 | 6.17 | skipped_fast |
| BIOUSDT | IDLE | 2.3 | 5.04 | 1.14 | 0.02 | 186448.84 | 6.21 | skipped_fast |
| EDELUSDT | IDLE | 2.53 | 5.5 | 0.54 | -0.03 | 82417.01 | 21.81 | skipped_fast |
| RIZEUSDT | IDLE | 2.2 | 9.82 | 4.6 | 0.12 | 59402.69 | 46.13 | skipped_fast |
| TELUSDT | IDLE | 2.82 | 6.89 | 0.31 | 0.07 | 189893.6 | 30.77 | skipped_fast |
| RWAINCUSDT | IDLE | 2.13 | 4.07 | 1.27 | 0.02 | 10344.85 | 21.39 | skipped_fast |
| REDUSDT | IDLE | 0.87 | 7.3 | 4.78 | 0.19 | 157720.47 | 11.31 | skipped_fast |
| QNTUSDT | IDLE | 2.59 | 5.68 | 0.07 | 0.08 | 143895.66 | 1.49 | skipped_fast |
| QAITUSDT | IDLE | 2.27 | 4.22 | 2.14 | -0.02 | 3921.68 | 67.45 | skipped_fast |
| KITEUSDT | IDLE | 1.1 | 3.12 | 0.98 | 0.09 | 61476.55 | 9.25 | skipped_fast |
| RWAUSDT | IDLE | 1.05 | 2.08 | 0.08 | 0.04 | 54570.89 | 8.18 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 2.87 | 0.0 | 0.11 | 4903.8 | 41.1 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
