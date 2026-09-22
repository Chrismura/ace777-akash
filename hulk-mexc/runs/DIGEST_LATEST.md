# Hulk DIGEST — 2026-09-22T22:16:19Z

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
| XRPUSDT | IDLE | 1.96 | 3.48 | 2.94 | -0.01 | 110161377.04 | 1.92 | skipped_fast |
| HBARUSDT | IDLE | 2.23 | 5.46 | 2.29 | 0.06 | 1677311.04 | 1.02 | skipped_fast |
| PYTHUSDT | IDLE | 0.85 | 3.79 | 3.07 | 0.04 | 1674752.48 | 6.1 | skipped_fast |
| ETHUSDT | IDLE | 0.57 | 1.02 | 0.83 | -0.01 | 416906834.8 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.44 | 0.77 | 0.68 | -0.01 | 914038095.97 | 0.0 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.57 | 11.13 | 9.77 | -0.02 | 234979.54 | 61.22 | skipped_fast |
| ZBCNUSDT | IDLE | 2.48 | 4.41 | 3.63 | -0.03 | 217695.16 | 15.0 | skipped_fast |
| CCUSDT | IDLE | 1.22 | 2.33 | 0.79 | -0.01 | 488873.98 | 5.28 | skipped_fast |
| RWAINCUSDT | IDLE | 3.5 | 9.03 | 3.23 | 0.03 | 18881.84 | 104.82 | skipped_fast |
| WUSDT | IDLE | 1.3 | 2.42 | 1.22 | 0.02 | 323928.79 | 7.49 | skipped_fast |
| RIZEUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.1 | 22.49 | 0.41 | 0.04 | 46428.63 | 111.73 | skipped_fast |
| CHIPUSDT | IDLE | 1.74 | 3.39 | 1.92 | -0.01 | 138766.12 | 19.77 | skipped_fast |
| BIOUSDT | IDLE | 1.07 | 2.02 | 0.84 | 0.02 | 135768.46 | 13.55 | skipped_fast |
| KITEUSDT | IDLE | 0.8 | 3.45 | 1.05 | 0.17 | 112413.62 | 7.94 | skipped_fast |
| QNTUSDT | IDLE | 1.48 | 4.82 | 1.97 | 0.1 | 204226.29 | 1.36 | skipped_fast |
| REDUSDT | IDLE | 0.7 | 1.29 | 0.68 | 0.05 | 63415.77 | 14.57 | skipped_fast |
| TELUSDT | IDLE | 1.4 | 5.5 | 0.92 | 0.1 | 103854.67 | 38.26 | skipped_fast |
| RWAUSDT | IDLE | 0.66 | 1.24 | 0.51 | -0.01 | 53114.17 | 7.25 | skipped_fast |
| FLUIDUSDT | IDLE | 0.44 | 0.86 | 0.13 | 0.01 | 5966.82 | 22.61 | skipped_fast |
| MNSRYUSDT | IDLE | 0.03 | 0.06 | 0.01 | -0.01 | 39911.97 | 9.02 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
