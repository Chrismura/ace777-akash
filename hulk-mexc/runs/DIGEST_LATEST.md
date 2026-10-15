# Hulk DIGEST — 2026-10-15T04:33:08Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.9 | 8.73 | 0.3 | 0.08 | 2414967.03 | 12.53 | skipped_fast |
| WUSDT | IDLE | 2.4 | 8.91 | 3.97 | -0.08 | 2801966.95 | 15.92 | skipped_fast |
| ETHUSDT | IDLE | 2.2 | 4.62 | 1.93 | -0.05 | 308059027.3 | 0.55 | skipped_fast |
| XRPUSDT | IDLE | 2.07 | 3.98 | 1.1 | -0.04 | 54476723.79 | 1.51 | skipped_fast |
| BTCUSDT | IDLE | 1.04 | 2.01 | 0.5 | -0.03 | 515719269.02 | 0.1 | skipped_fast |
| QNTUSDT | IDLE | 2.74 | 8.39 | 4.65 | -0.08 | 1183087.09 | 6.59 | skipped_fast |
| CCUSDT | IDLE | 1.97 | 7.12 | 4.56 | -0.12 | 449069.72 | 6.33 | skipped_fast |
| HBARUSDT | IDLE | 2.68 | 5.9 | 2.67 | -0.05 | 589898.03 | 2.42 | skipped_fast |
| EDELUSDT | IDLE | 2.85 | 5.28 | 3.95 | -0.06 | 190576.67 | 12.35 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 2.86 | 9.92 | 5.3 | -0.09 | 77726.0 | 7.94 | skipped_fast |
| CHIPUSDT | IDLE | 1.96 | 11.3 | 8.31 | -0.18 | 113771.86 | 10.59 | skipped_fast |
| ZBCNUSDT | IDLE | 1.79 | 4.67 | 2.56 | -0.06 | 217587.6 | 12.63 | skipped_fast |
| REDUSDT | IDLE | 2.18 | 4.29 | 0.48 | 0.0 | 64919.02 | 9.43 | skipped_fast |
| KITEUSDT | IDLE | 1.41 | 5.84 | 4.47 | -0.09 | 88111.46 | 9.07 | skipped_fast |
| RWAINCUSDT | IDLE | 1.42 | 2.98 | 2.35 | 0.0 | 26801.7 | 30.72 | skipped_fast |
| RIZEUSDT | IDLE | 0.97 | 7.12 | 0.23 | 0.01 | 57275.94 | 55.0 | skipped_fast |
| TELUSDT | IDLE | 2.11 | 3.89 | 2.21 | -0.05 | 97998.72 | 29.03 | skipped_fast |
| FLUIDUSDT | IDLE | 1.8 | 5.24 | 4.46 | -0.02 | 21440.04 | 21.23 | skipped_fast |
| RWAUSDT | IDLE | 0.9 | 1.62 | 1.19 | -0.03 | 54770.14 | 16.12 | skipped_fast |
| MNSRYUSDT | IDLE | 0.64 | 1.14 | 0.87 | -0.02 | 31891.95 | 24.12 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
