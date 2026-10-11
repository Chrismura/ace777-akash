# Hulk DIGEST — 2026-10-11T18:21:35Z

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
| WUSDT | IDLE | 3.72 | 16.04 | 4.02 | 0.09 | 1355414.31 | 11.96 | skipped_fast |
| XRPUSDT | IDLE | 1.25 | 2.38 | 0.76 | 0.01 | 14172276.16 | 2.12 | skipped_fast |
| ETHUSDT | IDLE | 1.11 | 2.14 | 0.5 | 0.01 | 212543209.33 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.72 | 1.38 | 0.35 | 0.01 | 152099013.12 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.31 | 2.51 | 0.79 | -0.03 | 791083.26 | 2.58 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.61 | 23.17 | 6.22 | 0.07 | 38682.08 | 53.99 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 4.33 | 11.9 | 6.7 | 0.01 | 28075.2 | 53.41 | skipped_fast |
| CHIPUSDT | IDLE | 2.25 | 9.0 | 4.43 | 0.11 | 383491.7 | 17.78 | skipped_fast |
| EDELUSDT | IDLE | 1.96 | 3.5 | 2.85 | -0.01 | 408758.93 | 7.85 | skipped_fast |
| ZBCNUSDT | IDLE | 2.82 | 5.42 | 1.41 | 0.03 | 195714.14 | 8.06 | skipped_fast |
| QNTUSDT | IDLE | 1.09 | 2.06 | 0.81 | 0.02 | 831000.57 | 3.69 | skipped_fast |
| CCUSDT | IDLE | 1.82 | 3.67 | 0.35 | 0.07 | 313395.66 | 10.25 | skipped_fast |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 4.01 | 7.23 | 5.25 | -0.03 | 156455.98 | 52.49 | skipped_fast |
| REDUSDT | IDLE | 1.84 | 3.58 | 0.64 | 0.01 | 58108.09 | 14.43 | skipped_fast |
| BIOUSDT | IDLE | 1.17 | 2.3 | 0.33 | 0.04 | 86440.73 | 3.32 | skipped_fast |
| KITEUSDT | IDLE | 1.11 | 2.17 | 0.36 | -0.02 | 72623.16 | 10.16 | skipped_fast |
| HBARUSDT | IDLE | 1.43 | 2.7 | 1.04 | 0.01 | 252240.33 | 6.45 | skipped_fast |
| RWAUSDT | IDLE | 1.09 | 2.13 | 0.39 | 0.01 | 50979.5 | 15.53 | skipped_fast |
| FLUIDUSDT | IDLE | 0.75 | 5.76 | 0.99 | 0.08 | 55740.94 | 21.69 | skipped_fast |
| MNSRYUSDT | IDLE | 0.91 | 1.75 | 0.47 | -0.01 | 30841.18 | 8.17 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
