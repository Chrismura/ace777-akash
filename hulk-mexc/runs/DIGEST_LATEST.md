# Hulk DIGEST — 2026-08-22T03:34:53Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.41 | 11.15 | 0.47 | 0.18 | 7906995.4 | 3.74 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.47 | 14.16 | 1.0 | 0.21 | 164200442.01 | 5.06 | skipped_fast |
| HBARUSDT | IDLE | 2.39 | 6.93 | 0.18 | 0.12 | 1025662.0 | 3.6 | skipped_fast |
| CCUSDT | IDLE | 1.97 | 8.96 | 1.48 | 0.17 | 687038.93 | 9.34 | skipped_fast |
| CHIPUSDT | IDLE | 2.25 | 5.05 | 0.0 | -0.01 | 452425.89 | 14.73 | skipped_fast |
| BIOUSDT | IDLE | 3.0 | 7.36 | 2.08 | 0.08 | 198696.67 | 2.99 | skipped_fast |
| ZBCNUSDT | IDLE | 1.41 | 5.16 | 1.37 | 0.12 | 537766.96 | 23.36 | skipped_fast |
| WUSDT | IDLE | 1.81 | 5.79 | 0.34 | 0.12 | 423418.16 | 10.82 | skipped_fast |
| EDELUSDT | IDLE | 2.02 | 3.95 | 3.47 | -0.03 | 79955.1 | 22.47 | skipped_fast |
| REDUSDT | IDLE | 0.94 | 7.96 | 4.93 | 0.2 | 158002.86 | 8.78 | skipped_fast |
| RIZEUSDT | IDLE | 1.82 | 7.71 | 4.44 | 0.1 | 59565.38 | 44.22 | skipped_fast |
| RWAINCUSDT | IDLE | 1.87 | 3.44 | 2.06 | 0.01 | 9331.12 | 21.56 | skipped_fast |
| KITEUSDT | IDLE | 1.4 | 4.5 | 0.22 | 0.12 | 67750.01 | 11.61 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | 0.0 | 3808.79 | 63.67 | skipped_fast |
| QNTUSDT | IDLE | 1.84 | 4.68 | 0.04 | 0.1 | 174306.22 | 8.85 | skipped_fast |
| RWAUSDT | IDLE | 1.49 | 2.97 | 0.08 | 0.06 | 56331.38 | 24.07 | skipped_fast |
| TELUSDT | IDLE | 1.02 | 2.45 | 0.41 | 0.07 | 173582.57 | 40.86 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.07 | 4710.05 | 18.09 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
