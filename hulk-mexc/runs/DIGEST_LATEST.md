# Hulk DIGEST — 2026-08-22T07:52:27Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.13 | 19.14 | 8.76 | 0.01 | 23889137.37 | 5.89 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.4 | 23.87 | 7.07 | 0.2 | 222838018.13 | 2.53 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.3 | 15.8 | 9.52 | 0.04 | 1352511.67 | 5.09 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.29 | 24.54 | 12.0 | -0.1 | 692854.86 | 6.69 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.28 | 17.58 | 8.16 | 0.04 | 616037.14 | 14.53 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.19 | 29.98 | 9.53 | -0.04 | 247997.1 | 3.19 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.15 | 42.01 | 11.2 | 0.06 | 160596.19 | 20.98 | skipped_fast |
| CCUSDT | IDLE | 2.04 | 11.25 | 3.02 | 0.2 | 806637.97 | 5.77 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.27 | 8.47 | 6.04 | 0.04 | 538146.76 | 27.5 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.37 | 13.91 | 8.76 | 0.04 | 194802.36 | 4.64 | skipped_fast |
| KITEUSDT | IDLE | 3.42 | 9.68 | 3.5 | 0.08 | 74131.3 | 12.65 | skipped_fast |
| EDELUSDT | IDLE | 2.27 | 4.52 | 3.35 | -0.04 | 87136.02 | 33.46 | skipped_fast |
| FLUIDUSDT | IDLE | 3.33 | 7.38 | 4.01 | 0.04 | 6888.1 | 19.69 | skipped_fast |
| RWAINCUSDT | IDLE | 2.48 | 4.48 | 3.24 | 0.01 | 11302.57 | 112.81 | skipped_fast |
| TELUSDT | IDLE | 2.08 | 5.36 | 4.0 | -0.01 | 176274.72 | 30.93 | skipped_fast |
| QAITUSDT | IDLE | 1.66 | 3.32 | 0.0 | -0.0 | 3309.3 | 63.29 | skipped_fast |
| RIZEUSDT | IDLE | 0.91 | 3.99 | 1.18 | 0.01 | 52378.21 | 41.01 | skipped_fast |
| RWAUSDT | IDLE | 1.75 | 3.29 | 1.35 | 0.04 | 58329.28 | 8.07 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
