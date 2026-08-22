# Hulk DIGEST — 2026-08-22T03:42:14Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.48 | 11.77 | 1.11 | 0.18 | 8115125.46 | 14.97 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.48 | 14.16 | 1.45 | 0.2 | 164830196.13 | 3.18 | skipped_fast |
| HBARUSDT | IDLE | 2.43 | 6.93 | 0.89 | 0.11 | 1033202.31 | 3.63 | skipped_fast |
| CCUSDT | IDLE | 1.96 | 9.22 | 0.06 | 0.19 | 692080.94 | 9.17 | skipped_fast |
| CHIPUSDT | IDLE | 2.49 | 5.36 | 1.5 | -0.03 | 452591.3 | 3.0 | skipped_fast |
| BIOUSDT | IDLE | 3.02 | 7.36 | 2.52 | 0.07 | 199001.45 | 3.0 | skipped_fast |
| ZBCNUSDT | IDLE | 1.41 | 5.16 | 1.38 | 0.14 | 536275.3 | 15.76 | skipped_fast |
| WUSDT | IDLE | 1.81 | 5.83 | 0.3 | 0.12 | 424065.9 | 8.87 | skipped_fast |
| RIZEUSDT | IDLE | 1.82 | 7.71 | 4.33 | 0.1 | 59540.07 | 44.22 | skipped_fast |
| EDELUSDT | IDLE | 1.96 | 3.95 | 2.5 | -0.03 | 80455.94 | 33.35 | skipped_fast |
| REDUSDT | IDLE | 0.93 | 7.96 | 4.31 | 0.21 | 157894.23 | 11.92 | skipped_fast |
| RWAINCUSDT | IDLE | 2.02 | 3.6 | 2.95 | 0.01 | 9351.15 | 38.1 | skipped_fast |
| KITEUSDT | IDLE | 1.45 | 4.71 | 0.34 | 0.12 | 67790.06 | 14.25 | skipped_fast |
| QNTUSDT | IDLE | 1.89 | 4.68 | 0.74 | 0.09 | 174978.66 | 7.42 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | 0.0 | 3808.79 | 63.67 | skipped_fast |
| TELUSDT | IDLE | 1.04 | 2.45 | 0.66 | 0.07 | 173587.05 | 25.6 | skipped_fast |
| RWAUSDT | IDLE | 1.49 | 2.97 | 0.0 | 0.06 | 56317.04 | 16.04 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.07 | 4710.05 | 22.29 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
