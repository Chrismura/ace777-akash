# Hulk DIGEST — 2026-10-15T17:15:46Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.14 | 25.14 | 6.17 | 0.16 | 4260391.42 | 4.22 | skipped_fast |
| WUSDT | IDLE | 2.57 | 7.78 | 1.92 | -0.05 | 2672010.44 | 13.51 | skipped_fast |
| ETHUSDT | IDLE | 2.66 | 5.29 | 0.25 | -0.0 | 342938254.34 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 2.41 | 4.76 | 0.41 | 0.0 | 52847489.27 | 0.75 | skipped_fast |
| BTCUSDT | IDLE | 1.77 | 3.48 | 0.39 | 0.0 | 499617190.49 | 0.0 | skipped_fast |
| QNTUSDT | IDLE | 3.71 | 11.92 | 2.25 | 0.02 | 1236590.97 | 2.37 | skipped_fast |
| REDUSDT | IDLE | 4.13 | 13.25 | 2.88 | 0.02 | 72692.4 | 8.76 | skipped_fast |
| ZBCNUSDT | IDLE | 3.51 | 6.84 | 1.16 | -0.0 | 197199.64 | 14.36 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.12 | 11.39 | 9.74 | -0.02 | 82711.09 | 60.31 | skipped_fast |
| CCUSDT | IDLE | 1.76 | 4.95 | 1.41 | -0.09 | 423131.62 | 8.26 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.66 | 9.68 | 7.57 | -0.12 | 243774.15 | 75.14 | skipped_fast |
| KITEUSDT | IDLE | 3.28 | 7.56 | 1.65 | -0.05 | 69593.7 | 16.9 | skipped_fast |
| CHIPUSDT | IDLE | 2.07 | 12.89 | 3.04 | -0.13 | 149778.84 | 15.05 | skipped_fast |
| BIOUSDT | IDLE | 2.8 | 6.87 | 0.73 | -0.03 | 86760.3 | 7.75 | skipped_fast |
| HBARUSDT | IDLE | 2.16 | 4.27 | 0.33 | -0.01 | 344190.56 | 3.59 | skipped_fast |
| RWAINCUSDT | IDLE | 2.18 | 5.54 | 4.21 | 0.09 | 27953.95 | 39.51 | skipped_fast |
| TELUSDT | IDLE | 2.7 | 6.61 | 0.39 | -0.02 | 96085.37 | 22.66 | skipped_fast |
| FLUIDUSDT | IDLE | 1.98 | 5.11 | 1.0 | -0.02 | 9319.36 | 21.39 | skipped_fast |
| MNSRYUSDT | IDLE | 1.46 | 2.77 | 1.06 | -0.01 | 32196.98 | 35.25 | skipped_fast |
| RWAUSDT | IDLE | 0.93 | 1.78 | 0.48 | -0.0 | 54744.01 | 15.95 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
