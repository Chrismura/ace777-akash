# Hulk DIGEST — 2026-08-21T23:12:53Z

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
| PYTHUSDT | IDLE | 1.72 | 6.39 | 0.52 | 0.12 | 6001677.61 | 2.03 | skipped_fast |
| XRPUSDT | IDLE | 1.76 | 6.77 | 0.45 | 0.14 | 138589772.79 | 2.76 | skipped_fast |
| CCUSDT | IDLE | 1.91 | 7.42 | 1.0 | 0.13 | 666423.41 | 10.67 | skipped_fast |
| HBARUSDT | IDLE | 2.39 | 5.24 | 0.09 | 0.09 | 890639.19 | 1.25 | skipped_fast |
| ZBCNUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.52 | 10.14 | 0.14 | 0.15 | 511356.33 | 27.12 | skipped_fast |
| WUSDT | IDLE | 2.74 | 6.91 | 1.25 | 0.08 | 375163.03 | 10.24 | skipped_fast |
| CHIPUSDT | IDLE | 1.16 | 3.56 | 1.0 | 0.05 | 547406.88 | 3.07 | skipped_fast |
| BIOUSDT | IDLE | 2.32 | 5.04 | 1.54 | 0.02 | 187502.18 | 3.12 | skipped_fast |
| EDELUSDT | IDLE | 2.53 | 5.5 | 0.65 | -0.03 | 82514.66 | 21.83 | skipped_fast |
| RWAINCUSDT | IDLE | 2.18 | 4.07 | 1.96 | 0.01 | 10186.51 | 16.16 | skipped_fast |
| REDUSDT | IDLE | 0.88 | 7.3 | 5.25 | 0.18 | 157436.49 | 8.92 | skipped_fast |
| QAITUSDT | IDLE | 2.27 | 4.22 | 2.14 | -0.02 | 3921.68 | 43.69 | skipped_fast |
| TELUSDT | IDLE | 2.66 | 6.51 | 0.15 | 0.07 | 184964.85 | 46.36 | skipped_fast |
| QNTUSDT | IDLE | 2.52 | 5.22 | 0.09 | 0.07 | 116477.45 | 1.5 | skipped_fast |
| RIZEUSDT | IDLE | 1.53 | 7.18 | 0.75 | 0.11 | 58709.56 | 43.62 | skipped_fast |
| KITEUSDT | IDLE | 1.11 | 3.12 | 1.12 | 0.1 | 61579.31 | 12.98 | skipped_fast |
| RWAUSDT | IDLE | 1.02 | 2.0 | 0.33 | 0.04 | 54377.66 | 24.58 | skipped_fast |
| FLUIDUSDT | IDLE | 0.92 | 2.35 | 0.18 | 0.1 | 4226.13 | 21.23 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
