# Hulk DIGEST — 2026-09-24T23:40:27Z

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
| XRPUSDT | IDLE | 1.11 | 2.12 | 0.67 | 0.03 | 68747713.37 | 1.95 | skipped_fast |
| ETHUSDT | IDLE | 0.79 | 1.52 | 0.34 | 0.0 | 353837064.38 | 0.19 | skipped_fast |
| BTCUSDT | IDLE | 0.47 | 0.9 | 0.27 | -0.0 | 724291981.69 | 0.0 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.77 | 41.19 | 25.33 | 0.04 | 197227.33 | 27.32 | skipped_fast |
| PYTHUSDT | IDLE | 0.73 | 2.68 | 0.8 | 0.09 | 1020378.75 | 5.88 | skipped_fast |
| CCUSDT | IDLE | 2.07 | 3.91 | 1.59 | 0.03 | 477514.64 | 9.72 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.62 | 31.75 | 6.75 | 0.38 | 71956.7 | 137.08 | skipped_fast |
| HBARUSDT | IDLE | 1.51 | 2.88 | 0.98 | 0.03 | 793054.36 | 1.07 | skipped_fast |
| CHIPUSDT | IDLE | 2.38 | 12.95 | 4.82 | 0.14 | 94853.37 | 16.74 | skipped_fast |
| QNTUSDT | IDLE | 1.96 | 17.26 | 5.3 | 0.27 | 293226.2 | 13.32 | skipped_fast |
| ZBCNUSDT | IDLE | 1.68 | 2.99 | 2.49 | 0.01 | 210361.03 | 12.72 | skipped_fast |
| WUSDT | IDLE | 0.88 | 1.7 | 0.36 | 0.06 | 248795.42 | 3.4 | skipped_fast |
| KITEUSDT | IDLE | 1.61 | 2.93 | 1.98 | -0.01 | 65143.28 | 11.41 | skipped_fast |
| RWAINCUSDT | IDLE | 1.44 | 7.19 | 4.09 | 0.17 | 12846.01 | 78.83 | skipped_fast |
| REDUSDT | IDLE | 0.8 | 2.07 | 1.57 | 0.06 | 100239.5 | 16.22 | skipped_fast |
| BIOUSDT | IDLE | 0.78 | 2.29 | 1.79 | 0.09 | 87736.51 | 13.01 | skipped_fast |
| TELUSDT | IDLE | 1.54 | 2.9 | 1.2 | -0.05 | 105801.03 | 36.54 | skipped_fast |
| RWAUSDT | IDLE | 0.95 | 1.77 | 0.8 | 0.01 | 57564.11 | 21.92 | skipped_fast |
| FLUIDUSDT | IDLE | 0.63 | 1.13 | 0.91 | 0.03 | 1191.45 | 20.69 | skipped_fast |
| MNSRYUSDT | IDLE | 0.38 | 0.72 | 0.28 | 0.0 | 37986.59 | 28.54 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
