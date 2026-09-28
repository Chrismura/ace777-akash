# Hulk DIGEST — 2026-09-28T04:15:58Z

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
| QNTUSDT | IDLE | 1.44 | 45.68 | 25.29 | 0.46 | 15271314.85 | 12.56 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 2.86 | 10.77 | 7.2 | 0.05 | 5200988.21 | 9.45 | skipped_fast |
| PYTHUSDT | IDLE | 2.24 | 4.69 | 3.35 | -0.01 | 2021848.36 | 2.44 | skipped_fast |
| XRPUSDT | IDLE | 1.89 | 3.38 | 2.61 | -0.02 | 49789090.46 | 3.35 | skipped_fast |
| ETHUSDT | IDLE | 1.29 | 2.32 | 1.77 | -0.02 | 257599550.49 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 1.19 | 2.11 | 1.83 | -0.01 | 506492958.74 | 0.0 | skipped_fast |
| CCUSDT | IDLE | 3.23 | 7.73 | 2.68 | 0.04 | 765028.59 | 7.07 | skipped_fast |
| HBARUSDT | IDLE | 2.06 | 3.76 | 2.43 | 0.02 | 992317.85 | 1.05 | skipped_fast |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 4.11 | 7.74 | 6.01 | -0.05 | 105199.09 | 7.57 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.09 | 7.32 | 5.77 | -0.03 | 90086.04 | 3.28 | skipped_fast |
| REDUSDT | IDLE | 2.53 | 5.3 | 4.41 | -0.05 | 66554.41 | 9.15 | skipped_fast |
| CHIPUSDT | IDLE | 2.31 | 6.25 | 4.93 | -0.07 | 92740.34 | 15.57 | skipped_fast |
| ZBCNUSDT | IDLE | 1.54 | 2.76 | 2.11 | -0.03 | 246436.54 | 8.36 | skipped_fast |
| RIZEUSDT | IDLE | 1.4 | 13.55 | 6.42 | -0.2 | 64986.9 | 60.72 | skipped_fast |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.38 | 5.92 | 5.59 | -0.01 | 3571.59 | 21.54 | skipped_fast |
| EDELUSDT | IDLE | 1.2 | 6.39 | 4.3 | -0.13 | 164744.03 | 60.64 | skipped_fast |
| RWAINCUSDT | IDLE | 0.61 | 5.95 | 3.56 | 0.21 | 31548.8 | 31.92 | skipped_fast |
| TELUSDT | IDLE | 0.82 | 1.79 | 1.6 | 0.03 | 170199.89 | 21.7 | skipped_fast |
| MNSRYUSDT | IDLE | 1.12 | 1.97 | 1.76 | -0.01 | 39212.89 | 64.21 | skipped_fast |
| RWAUSDT | IDLE | 0.62 | 1.14 | 0.64 | 0.01 | 59453.9 | 64.13 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
