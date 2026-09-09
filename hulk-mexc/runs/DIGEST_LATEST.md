# Hulk DIGEST — 2026-09-09T22:14:40Z

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
| XRPUSDT | IDLE | 1.87 | 3.37 | 2.49 | -0.02 | 42405857.15 | 2.16 | skipped_fast |
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.49 | 11.52 | 9.47 | -0.03 | 981627.24 | 9.69 | skipped_fast |
| ETHUSDT | IDLE | 1.27 | 2.23 | 2.05 | -0.01 | 373553805.14 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.82 | 1.44 | 1.32 | -0.01 | 536191488.8 | 0.22 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.46 | 8.4 | 6.42 | -0.03 | 202650.57 | 10.16 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.52 | 19.09 | 14.53 | -0.06 | 122554.75 | 16.12 | skipped_fast |
| REDUSDT | IDLE | 3.87 | 7.07 | 4.47 | -0.0 | 62558.55 | 18.84 | skipped_fast |
| CCUSDT | IDLE | 1.27 | 2.25 | 1.92 | -0.03 | 611245.9 | 8.71 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 3.05 | 8.64 | 6.56 | -0.09 | 99412.35 | 3.94 | skipped_fast |
| EDELUSDT | IDLE | 2.8 | 4.99 | 4.09 | -0.03 | 176441.24 | 19.84 | skipped_fast |
| HBARUSDT | IDLE | 2.02 | 3.61 | 2.85 | -0.04 | 448036.18 | 1.31 | skipped_fast |
| KITEUSDT | IDLE | 2.23 | 4.1 | 2.42 | -0.01 | 59902.51 | 13.31 | skipped_fast |
| RWAINCUSDT | IDLE | 2.3 | 4.1 | 3.39 | -0.0 | 6800.93 | 28.29 | skipped_fast |
| ZBCNUSDT | IDLE | 1.17 | 2.22 | 0.75 | 0.03 | 198635.47 | 12.01 | skipped_fast |
| RWAUSDT | IDLE | 2.74 | 4.85 | 4.2 | -0.03 | 55471.46 | 52.03 | skipped_fast |
| FLUIDUSDT | IDLE | 2.2 | 3.92 | 3.77 | -0.08 | 951.16 | 22.16 | skipped_fast |
| RIZEUSDT | IDLE | 0.6 | 7.16 | 1.6 | 0.02 | 72460.79 | 111.85 | skipped_fast |
| QNTUSDT | IDLE | 1.2 | 2.16 | 1.58 | -0.0 | 44862.11 | 15.02 | skipped_fast |
| TELUSDT | IDLE | 1.22 | 2.18 | 1.69 | 0.02 | 102013.98 | 72.28 | skipped_fast |
| MNSRYUSDT | IDLE | 1.1 | 1.94 | 1.79 | -0.01 | 25060.53 | 56.52 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
