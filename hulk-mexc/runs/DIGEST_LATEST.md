# Hulk DIGEST — 2026-10-16T14:00:54Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| PYTHUSDT | IDLE | 2.3 | 8.83 | 5.72 | 0.07 | 3723679.0 | 3.38 | skipped_fast |
| WUSDT | IDLE | 1.99 | 3.59 | 2.61 | 0.03 | 1789766.44 | 15.11 | skipped_fast |
| ETHUSDT | IDLE | 1.08 | 1.96 | 1.37 | 0.05 | 231794464.58 | 0.08 | skipped_fast |
| XRPUSDT | IDLE | 1.0 | 1.79 | 1.39 | 0.04 | 25426903.64 | 2.25 | skipped_fast |
| BTCUSDT | IDLE | 0.83 | 1.49 | 1.08 | 0.02 | 386557000.7 | 0.26 | skipped_fast |
| QNTUSDT | IDLE | 2.17 | 3.89 | 3.0 | 0.06 | 1188764.41 | 0.97 | skipped_fast |
| CCUSDT | IDLE | 1.79 | 3.49 | 0.62 | 0.0 | 430488.84 | 8.51 | skipped_fast |
| RIZEUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.09 | 9.55 | 1.66 | 0.04 | 69492.63 | 59.01 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 2.66 | 7.39 | 6.39 | -0.08 | 26362.36 | 31.86 | skipped_fast |
| CHIPUSDT | IDLE | 1.61 | 4.83 | 4.61 | 0.12 | 173135.41 | 14.59 | skipped_fast |
| ZBCNUSDT | IDLE | 1.66 | 2.99 | 2.16 | 0.06 | 193794.49 | 17.37 | skipped_fast |
| REDUSDT | IDLE | 1.65 | 4.67 | 1.96 | 0.04 | 90494.28 | 7.29 | skipped_fast |
| EDELUSDT | IDLE | 0.96 | 2.55 | 0.39 | 0.01 | 213677.4 | 26.2 | skipped_fast |
| BIOUSDT | IDLE | 1.35 | 2.39 | 2.06 | 0.05 | 64642.54 | 3.9 | skipped_fast |
| KITEUSDT | IDLE | 1.18 | 2.07 | 1.99 | 0.03 | 69459.25 | 9.01 | skipped_fast |
| HBARUSDT | IDLE | 0.94 | 1.76 | 0.84 | 0.07 | 291053.9 | 6.94 | skipped_fast |
| TELUSDT | IDLE | 1.1 | 2.03 | 1.16 | 0.06 | 92575.53 | 33.58 | skipped_fast |
| FLUIDUSDT | IDLE | 1.29 | 2.36 | 1.52 | 0.01 | 7601.48 | 21.24 | skipped_fast |
| RWAUSDT | IDLE | 0.26 | 0.47 | 0.31 | 0.02 | 51560.01 | 7.89 | skipped_fast |
| MNSRYUSDT | IDLE | 0.12 | 0.21 | 0.21 | 0.01 | 39383.54 | 16.96 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
