# Hulk DIGEST — 2026-09-28T12:22:04Z

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
| QNTUSDT | IDLE | 1.44 | 47.4 | 15.59 | 0.49 | 19924196.91 | 12.77 | skipped_fast |
| HBARUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.48 | 29.82 | 0.14 | 0.31 | 5984263.5 | 17.66 | skipped_fast |
| CCUSDT | WATCH_PULLBACK — tension haute + reflux | 4.39 | 14.75 | 9.74 | -0.04 | 1196587.14 | 7.54 | skipped_fast |
| WUSDT | IDLE | 1.27 | 5.62 | 1.09 | -0.02 | 3284289.8 | 7.68 | skipped_fast |
| XRPUSDT | IDLE | 1.67 | 3.33 | 0.07 | -0.02 | 55180967.95 | 1.98 | skipped_fast |
| PYTHUSDT | IDLE | 1.88 | 4.6 | 1.51 | -0.07 | 1561906.82 | 11.06 | skipped_fast |
| ETHUSDT | IDLE | 1.05 | 2.07 | 0.21 | -0.01 | 321022977.2 | 0.15 | skipped_fast |
| BTCUSDT | IDLE | 0.54 | 1.06 | 0.09 | -0.02 | 676431812.25 | 0.61 | skipped_fast |
| EDELUSDT | IDLE | 3.6 | 24.05 | 3.4 | 0.03 | 191451.16 | 23.43 | skipped_fast |
| KITEUSDT | IDLE | 1.96 | 6.31 | 3.29 | -0.08 | 103774.59 | 9.33 | skipped_fast |
| ZBCNUSDT | IDLE | 1.2 | 2.32 | 0.49 | -0.05 | 211957.65 | 15.78 | skipped_fast |
| BIOUSDT | IDLE | 1.23 | 3.28 | 0.4 | -0.06 | 106044.3 | 3.32 | skipped_fast |
| REDUSDT | IDLE | 1.51 | 3.29 | 0.04 | -0.03 | 61117.57 | 13.96 | skipped_fast |
| CHIPUSDT | IDLE | 1.34 | 3.27 | 0.29 | -0.08 | 86202.68 | 15.54 | skipped_fast |
| TELUSDT | IDLE | 2.09 | 3.87 | 2.13 | 0.0 | 162220.3 | 27.94 | skipped_fast |
| RIZEUSDT | IDLE | 0.4 | 2.49 | 0.6 | -0.14 | 59771.88 | 33.13 | skipped_fast |
| RWAINCUSDT | IDLE | 0.38 | 3.96 | 0.04 | 0.14 | 33261.6 | 91.72 | skipped_fast |
| RWAUSDT | IDLE | 0.82 | 1.53 | 0.72 | -0.02 | 59751.96 | 7.21 | skipped_fast |
| FLUIDUSDT | IDLE | 1.02 | 2.38 | 0.86 | -0.06 | 3276.58 | 21.79 | skipped_fast |
| MNSRYUSDT | IDLE | 0.38 | 0.73 | 0.23 | -0.02 | 35197.46 | 57.81 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
