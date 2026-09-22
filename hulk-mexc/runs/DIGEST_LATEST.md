# Hulk DIGEST — 2026-09-22T08:05:09Z

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
| XRPUSDT | IDLE | 1.15 | 2.2 | 0.64 | 0.05 | 119042889.38 | 1.98 | skipped_fast |
| ETHUSDT | IDLE | 0.55 | 1.01 | 0.58 | 0.02 | 706691432.36 | 1.43 | skipped_fast |
| BTCUSDT | IDLE | 0.4 | 0.74 | 0.39 | 0.04 | 1162160172.68 | 0.0 | skipped_fast |
| HBARUSDT | IDLE | 2.18 | 4.47 | 0.17 | 0.09 | 1314392.51 | 2.1 | skipped_fast |
| PYTHUSDT | IDLE | 2.33 | 4.22 | 2.99 | 0.02 | 856396.32 | 1.58 | skipped_fast |
| CCUSDT | IDLE | 1.48 | 2.92 | 0.31 | 0.05 | 667258.38 | 5.02 | skipped_fast |
| WUSDT | IDLE | 1.6 | 2.97 | 1.55 | -0.01 | 450734.91 | 5.93 | skipped_fast |
| KITEUSDT | IDLE | 3.09 | 6.12 | 0.36 | 0.08 | 82278.49 | 8.73 | skipped_fast |
| ZBCNUSDT | IDLE | 1.71 | 3.17 | 1.66 | 0.02 | 274828.92 | 38.41 | skipped_fast |
| EDELUSDT | IDLE | 1.18 | 6.79 | 2.15 | 0.1 | 232982.23 | 25.15 | skipped_fast |
| CHIPUSDT | IDLE | 1.61 | 4.76 | 0.39 | 0.08 | 177586.11 | 18.64 | skipped_fast |
| REDUSDT | IDLE | 1.97 | 3.83 | 0.74 | 0.04 | 97809.25 | 15.13 | skipped_fast |
| BIOUSDT | IDLE | 1.41 | 2.56 | 1.71 | 0.01 | 130360.82 | 6.95 | skipped_fast |
| RIZEUSDT | IDLE | 1.55 | 15.97 | 1.0 | -0.15 | 50869.88 | 86.71 | skipped_fast |
| RWAINCUSDT | IDLE | 0.76 | 1.79 | 1.16 | 0.07 | 25416.35 | 11.18 | skipped_fast |
| TELUSDT | IDLE | 1.78 | 3.15 | 2.75 | 0.06 | 118511.0 | 56.48 | skipped_fast |
| QNTUSDT | IDLE | 1.29 | 2.46 | 0.75 | 0.02 | 125466.3 | 8.88 | skipped_fast |
| RWAUSDT | IDLE | 0.55 | 1.02 | 0.58 | 0.01 | 57093.65 | 14.6 | skipped_fast |
| FLUIDUSDT | IDLE | 0.48 | 0.85 | 0.79 | 0.07 | 12465.48 | 21.29 | skipped_fast |
| MNSRYUSDT | IDLE | 0.2 | 0.36 | 0.23 | 0.02 | 41717.09 | 18.07 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
