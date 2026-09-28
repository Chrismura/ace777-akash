# Hulk DIGEST — 2026-09-28T09:20:55Z

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
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 2.63 | 10.62 | 8.56 | -0.12 | 4109275.73 | 16.58 | skipped_fast |
| HBARUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.68 | 20.84 | 0.11 | 0.2 | 3668725.06 | 14.96 | skipped_fast |
| QNTUSDT | IDLE | 1.01 | 31.69 | 21.96 | 0.28 | 18227166.16 | 20.41 | skipped_fast |
| PYTHUSDT | IDLE | 2.07 | 5.64 | 2.95 | -0.03 | 1689072.14 | 1.24 | skipped_fast |
| XRPUSDT | IDLE | 1.08 | 2.0 | 1.02 | -0.03 | 51396549.48 | 0.67 | skipped_fast |
| BTCUSDT | IDLE | 0.6 | 1.09 | 0.73 | -0.02 | 642651547.34 | 0.0 | skipped_fast |
| ETHUSDT | IDLE | 0.48 | 0.91 | 0.31 | -0.02 | 300010393.53 | 0.94 | skipped_fast |
| CCUSDT | IDLE | 3.24 | 7.77 | 2.58 | 0.02 | 983934.29 | 3.57 | skipped_fast |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.56 | 8.04 | 5.52 | -0.09 | 106191.65 | 7.94 | skipped_fast |
| BIOUSDT | IDLE | 2.11 | 5.16 | 3.48 | -0.07 | 102767.51 | 6.73 | skipped_fast |
| TELUSDT | IDLE | 3.06 | 5.74 | 4.51 | 0.02 | 175076.93 | 39.36 | skipped_fast |
| REDUSDT | IDLE | 1.97 | 3.69 | 2.8 | -0.06 | 62926.03 | 14.87 | skipped_fast |
| ZBCNUSDT | IDLE | 1.34 | 2.43 | 1.72 | -0.05 | 206103.39 | 27.41 | skipped_fast |
| EDELUSDT | IDLE | 1.18 | 5.59 | 2.05 | -0.12 | 181245.41 | 51.45 | skipped_fast |
| CHIPUSDT | IDLE | 1.22 | 3.8 | 1.92 | -0.1 | 89635.7 | 15.76 | skipped_fast |
| FLUIDUSDT | IDLE | 2.02 | 4.02 | 3.86 | -0.05 | 3627.16 | 20.03 | skipped_fast |
| RWAINCUSDT | IDLE | 0.66 | 6.09 | 5.7 | 0.14 | 31916.21 | 86.01 | skipped_fast |
| RIZEUSDT | IDLE | 0.23 | 1.34 | 0.84 | -0.15 | 59323.55 | 54.55 | skipped_fast |
| RWAUSDT | IDLE | 0.98 | 1.74 | 1.42 | -0.03 | 59215.98 | 43.32 | skipped_fast |
| MNSRYUSDT | IDLE | 0.4 | 0.75 | 0.28 | -0.02 | 36477.86 | 35.99 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
