# Hulk DIGEST — 2026-10-14T18:24:44Z

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
| PYTHUSDT | IDLE | 3.74 | 8.72 | 4.37 | 0.04 | 2099871.24 | 8.56 | skipped_fast |
| WUSDT | IDLE | 1.08 | 4.62 | 2.99 | -0.06 | 2865221.65 | 4.62 | skipped_fast |
| XRPUSDT | IDLE | 1.73 | 3.06 | 2.73 | -0.03 | 42818197.06 | 1.5 | skipped_fast |
| ETHUSDT | IDLE | 1.6 | 2.86 | 2.25 | -0.03 | 192826719.84 | 0.37 | skipped_fast |
| BTCUSDT | IDLE | 1.08 | 1.9 | 1.7 | -0.02 | 425110173.09 | 0.24 | skipped_fast |
| QNTUSDT | IDLE | 2.13 | 4.8 | 3.44 | -0.02 | 1360357.34 | 2.44 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 4.15 | 22.88 | 16.59 | 0.02 | 50965.42 | 56.6 | skipped_fast |
| ZBCNUSDT | IDLE | 2.74 | 4.94 | 3.62 | -0.03 | 185656.58 | 10.01 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 2.5 | 7.3 | 5.5 | -0.07 | 105581.86 | 5.67 | skipped_fast |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.8 | 13.1 | 7.64 | 0.06 | 18060.42 | 22.17 | skipped_fast |
| CCUSDT | IDLE | 0.99 | 2.19 | 1.84 | -0.08 | 423366.5 | 9.38 | skipped_fast |
| REDUSDT | IDLE | 2.58 | 4.95 | 1.45 | 0.01 | 62585.68 | 16.09 | skipped_fast |
| HBARUSDT | IDLE | 1.52 | 2.75 | 1.95 | -0.04 | 520946.92 | 4.75 | skipped_fast |
| KITEUSDT | IDLE | 1.94 | 4.93 | 4.48 | 0.01 | 86780.52 | 10.18 | skipped_fast |
| EDELUSDT | IDLE | 1.86 | 3.27 | 2.96 | -0.03 | 168920.67 | 33.15 | skipped_fast |
| BIOUSDT | IDLE | 1.65 | 2.92 | 2.55 | -0.04 | 70669.88 | 3.79 | skipped_fast |
| RWAINCUSDT | IDLE | 2.01 | 6.57 | 0.61 | -0.06 | 30849.11 | 45.98 | skipped_fast |
| TELUSDT | IDLE | 2.21 | 4.34 | 0.55 | 0.02 | 99769.45 | 27.88 | skipped_fast |
| RWAUSDT | IDLE | 1.23 | 2.15 | 2.02 | -0.02 | 56027.84 | 7.95 | skipped_fast |
| MNSRYUSDT | IDLE | 0.38 | 0.68 | 0.52 | -0.01 | 37753.33 | 52.03 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
