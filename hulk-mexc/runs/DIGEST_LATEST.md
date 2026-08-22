# Hulk DIGEST — 2026-08-22T05:31:19Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : XRPUSDT, HBARUSDT, QAITUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT
- Watch only : QNTUSDT, FLUIDUSDT, RWAUSDT

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.17 | 19.14 | 10.01 | 0.08 | 16570109.34 | 5.97 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.3 | 23.87 | 10.99 | 0.15 | 200318256.61 | 9.26 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.28 | 15.8 | 9.74 | 0.05 | 1354619.98 | 33.21 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.29 | 24.54 | 12.12 | -0.09 | 690794.99 | 16.78 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.3 | 17.58 | 8.66 | 0.06 | 590815.4 | 24.0 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.38 | 45.06 | 12.69 | 0.12 | 164331.6 | 10.45 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.24 | 29.98 | 12.18 | -0.03 | 218783.33 | 32.96 | skipped_fast |
| CCUSDT | IDLE | 2.19 | 11.56 | 2.83 | 0.19 | 759539.93 | 12.47 | skipped_fast |
| ZBCNUSDT | IDLE | 3.14 | 8.47 | 4.62 | 0.07 | 545574.04 | 84.85 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.28 | 13.91 | 9.35 | 0.04 | 195250.62 | 6.24 | skipped_fast |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.88 | 9.68 | 6.03 | 0.08 | 73249.91 | 12.04 | skipped_fast |
| EDELUSDT | IDLE | 2.15 | 4.52 | 1.51 | -0.02 | 88529.69 | 43.76 | skipped_fast |
| RWAINCUSDT | IDLE | 2.5 | 4.48 | 3.4 | 0.01 | 11525.01 | 64.66 | skipped_fast |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.22 | 7.9 | 5.34 | 0.05 | 5400.57 | 42.37 | skipped_fast |
| RIZEUSDT | IDLE | 1.23 | 4.9 | 4.62 | 0.08 | 58751.34 | 22.39 | skipped_fast |
| TELUSDT | IDLE | 2.09 | 5.52 | 2.96 | 0.07 | 194928.26 | 30.5 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3288.58 | 35.86 | skipped_fast |
| RWAUSDT | IDLE | 1.85 | 3.38 | 2.07 | 0.05 | 57534.06 | 16.3 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
