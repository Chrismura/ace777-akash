# Hulk DIGEST — 2026-10-16T17:45:31Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 2.68 | 9.62 | 6.54 | -0.08 | 2239393.07 | 5.84 | skipped_fast |
| WUSDT | IDLE | 3.0 | 7.35 | 4.87 | -0.04 | 1665481.57 | 17.48 | skipped_fast |
| XRPUSDT | IDLE | 2.35 | 4.27 | 2.84 | -0.03 | 25522398.28 | 1.53 | skipped_fast |
| ETHUSDT | IDLE | 1.97 | 3.61 | 2.21 | -0.01 | 210561486.67 | 0.08 | skipped_fast |
| BTCUSDT | IDLE | 1.24 | 2.28 | 1.37 | -0.01 | 356728253.9 | 0.0 | skipped_fast |
| QNTUSDT | IDLE | 3.2 | 5.76 | 4.33 | -0.04 | 927167.72 | 1.98 | skipped_fast |
| CCUSDT | IDLE | 2.4 | 4.35 | 3.05 | -0.05 | 389621.07 | 6.78 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 2.77 | 10.0 | 7.17 | -0.03 | 153209.98 | 10.88 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 3.27 | 10.33 | 7.58 | -0.07 | 24700.76 | 5.36 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 2.99 | 7.29 | 5.06 | -0.08 | 97362.43 | 7.53 | skipped_fast |
| HBARUSDT | IDLE | 3.38 | 6.08 | 4.59 | -0.01 | 312832.21 | 8.42 | skipped_fast |
| ZBCNUSDT | IDLE | 2.57 | 4.66 | 3.17 | -0.01 | 216087.3 | 11.84 | skipped_fast |
| BIOUSDT | IDLE | 2.98 | 5.41 | 3.6 | -0.03 | 62133.44 | 7.95 | skipped_fast |
| EDELUSDT | IDLE | 2.4 | 4.3 | 3.38 | 0.02 | 182600.9 | 20.15 | skipped_fast |
| KITEUSDT | IDLE | 2.29 | 4.2 | 2.55 | -0.03 | 56635.43 | 2.47 | skipped_fast |
| RIZEUSDT | IDLE | 2.35 | 5.54 | 0.53 | 0.05 | 34877.4 | 59.01 | skipped_fast |
| RWAUSDT | IDLE | 2.07 | 3.9 | 1.56 | 0.0 | 53928.83 | 55.58 | skipped_fast |
| TELUSDT | IDLE | 1.27 | 2.26 | 1.82 | 0.0 | 90499.06 | 16.9 | skipped_fast |
| FLUIDUSDT | IDLE | 1.56 | 2.87 | 1.61 | -0.03 | 6135.25 | 21.25 | skipped_fast |
| MNSRYUSDT | IDLE | 0.36 | 0.7 | 0.18 | -0.0 | 36048.02 | 51.06 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
