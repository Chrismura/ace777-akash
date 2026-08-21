# Hulk DIGEST — 2026-08-21T23:15:58Z

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
| PYTHUSDT | IDLE | 1.72 | 6.39 | 0.52 | 0.12 | 6016610.18 | 2.03 | skipped_fast |
| XRPUSDT | IDLE | 1.75 | 6.77 | 0.27 | 0.15 | 138505360.46 | 2.07 | skipped_fast |
| HBARUSDT | IDLE | 2.48 | 5.81 | 0.0 | 0.1 | 892037.93 | 2.49 | skipped_fast |
| CCUSDT | IDLE | 1.91 | 7.42 | 1.21 | 0.13 | 656931.21 | 8.91 | skipped_fast |
| ZBCNUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.52 | 10.14 | 0.24 | 0.15 | 511413.24 | 20.46 | skipped_fast |
| WUSDT | IDLE | 2.74 | 6.91 | 1.32 | 0.08 | 377021.75 | 13.33 | skipped_fast |
| CHIPUSDT | IDLE | 1.16 | 3.56 | 0.91 | 0.05 | 547417.89 | 3.07 | skipped_fast |
| BIOUSDT | IDLE | 2.29 | 5.04 | 1.11 | 0.02 | 187893.24 | 3.11 | skipped_fast |
| EDELUSDT | IDLE | 2.53 | 5.5 | 0.54 | -0.03 | 82514.7 | 10.91 | skipped_fast |
| REDUSDT | IDLE | 0.88 | 7.3 | 5.13 | 0.18 | 157448.17 | 8.9 | skipped_fast |
| RWAINCUSDT | IDLE | 2.2 | 4.07 | 2.22 | 0.02 | 10178.81 | 32.38 | skipped_fast |
| TELUSDT | IDLE | 2.67 | 6.51 | 0.31 | 0.07 | 184906.55 | 46.38 | skipped_fast |
| QAITUSDT | IDLE | 2.27 | 4.22 | 2.14 | -0.02 | 3921.68 | 67.45 | skipped_fast |
| QNTUSDT | IDLE | 2.51 | 5.22 | 0.06 | 0.07 | 117907.97 | 1.5 | skipped_fast |
| KITEUSDT | IDLE | 1.12 | 3.12 | 1.29 | 0.09 | 61570.83 | 12.07 | skipped_fast |
| RIZEUSDT | IDLE | 1.81 | 8.64 | 0.0 | 0.12 | 58807.69 | 218.04 | skipped_fast |
| RWAUSDT | IDLE | 1.02 | 2.0 | 0.25 | 0.04 | 54405.68 | 16.39 | skipped_fast |
| FLUIDUSDT | IDLE | 0.92 | 2.35 | 0.18 | 0.1 | 4226.13 | 21.9 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
