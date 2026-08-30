# Hulk DIGEST — 2026-08-21T22:52:24Z

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
| PYTHUSDT | IDLE | 1.35 | 5.17 | 0.02 | 0.11 | 5895710.23 | 2.04 | skipped_fast |
| XRPUSDT | IDLE | 1.65 | 6.41 | 0.17 | 0.15 | 136161396.13 | 2.76 | skipped_fast |
| CCUSDT | IDLE | 1.89 | 7.44 | 0.24 | 0.14 | 659185.56 | 9.7 | skipped_fast |
| HBARUSDT | IDLE | 2.19 | 4.73 | 0.41 | 0.08 | 876019.9 | 2.52 | skipped_fast |
| ZBCNUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.07 | 8.93 | 0.01 | 0.15 | 508481.61 | 36.02 | skipped_fast |
| WUSDT | IDLE | 2.62 | 6.46 | 0.06 | 0.09 | 371406.0 | 12.18 | skipped_fast |
| CHIPUSDT | IDLE | 1.54 | 4.54 | 2.41 | 0.05 | 541604.7 | 12.33 | skipped_fast |
| BIOUSDT | IDLE | 2.28 | 5.04 | 0.95 | 0.03 | 187969.59 | 3.11 | skipped_fast |
| REDUSDT | IDLE | 1.32 | 11.01 | 7.64 | 0.19 | 157339.32 | 19.37 | skipped_fast |
| EDELUSDT | IDLE | 2.3 | 5.04 | 0.22 | -0.03 | 82568.56 | 21.83 | skipped_fast |
| RWAINCUSDT | IDLE | 2.18 | 4.07 | 1.96 | 0.02 | 10244.46 | 16.16 | skipped_fast |
| TELUSDT | IDLE | 2.53 | 6.45 | 0.82 | 0.05 | 186850.29 | 25.89 | skipped_fast |
| QAITUSDT | IDLE | 2.31 | 4.38 | 1.63 | -0.01 | 3896.16 | 63.29 | skipped_fast |
| KITEUSDT | IDLE | 1.21 | 3.58 | 1.03 | 0.11 | 61360.63 | 11.98 | skipped_fast |
| QNTUSDT | IDLE | 2.28 | 4.56 | 0.03 | 0.06 | 88141.5 | 7.55 | skipped_fast |
| RIZEUSDT | IDLE | 0.96 | 4.7 | 1.94 | 0.06 | 56396.62 | 46.99 | skipped_fast |
| RWAUSDT | IDLE | 0.92 | 1.83 | 0.0 | 0.04 | 54111.09 | 16.38 | skipped_fast |
| FLUIDUSDT | IDLE | 0.51 | 1.15 | 0.08 | 0.09 | 4171.26 | 26.04 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
