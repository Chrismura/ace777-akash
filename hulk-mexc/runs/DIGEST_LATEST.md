# Hulk DIGEST — 2026-09-23T17:09:00Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 3.92 | 12.25 | 8.74 | -0.07 | 1398143.03 | 3.25 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 2.59 | 6.67 | 6.06 | -0.05 | 122690802.41 | 2.69 | skipped_fast |
| ETHUSDT | IDLE | 1.99 | 3.56 | 2.8 | -0.03 | 514113292.93 | 0.6 | skipped_fast |
| BTCUSDT | IDLE | 1.62 | 2.87 | 2.41 | -0.03 | 887107726.53 | 0.05 | skipped_fast |
| HBARUSDT | IDLE | 2.34 | 7.25 | 5.84 | -0.07 | 1570654.3 | 2.23 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 3.55 | 9.16 | 6.92 | -0.06 | 400975.0 | 2.64 | skipped_fast |
| CCUSDT | WATCH_PULLBACK — tension haute + reflux | 3.09 | 6.94 | 5.49 | -0.05 | 494991.61 | 3.73 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.61 | 10.94 | 8.17 | -0.07 | 221546.51 | 16.47 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 3.97 | 10.05 | 6.82 | -0.04 | 108794.19 | 10.62 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.55 | 11.06 | 8.56 | -0.09 | 213393.66 | 42.57 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.7 | 6.68 | 5.53 | -0.03 | 59422.51 | 10.48 | skipped_fast |
| ZBCNUSDT | IDLE | 2.24 | 5.11 | 4.7 | -0.02 | 258121.64 | 14.56 | skipped_fast |
| KITEUSDT | IDLE | 2.66 | 4.9 | 3.11 | -0.04 | 165140.57 | 10.53 | skipped_fast |
| QNTUSDT | IDLE | 2.97 | 6.98 | 4.02 | -0.03 | 198401.57 | 2.81 | skipped_fast |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.55 | 7.2 | 6.72 | -0.06 | 4102.2 | 18.62 | skipped_fast |
| RIZEUSDT | IDLE | 1.26 | 16.52 | 13.83 | 0.34 | 69985.91 | 106.99 | skipped_fast |
| TELUSDT | IDLE | 2.39 | 6.14 | 5.4 | -0.03 | 155898.95 | 52.99 | skipped_fast |
| RWAINCUSDT | IDLE | 0.8 | 1.69 | 0.75 | 0.02 | 21375.56 | 21.7 | skipped_fast |
| RWAUSDT | IDLE | 1.71 | 3.05 | 2.53 | -0.02 | 55581.39 | 14.85 | skipped_fast |
| MNSRYUSDT | IDLE | 1.1 | 1.93 | 1.77 | -0.01 | 40859.8 | 71.61 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
