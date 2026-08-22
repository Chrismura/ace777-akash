# Hulk DIGEST — 2026-08-22T10:20:27Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 3.74 | 16.77 | 11.62 | -0.0 | 51606774.77 | 10.34 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.91 | 23.87 | 14.26 | 0.05 | 216141181.45 | 2.06 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.45 | 15.8 | 11.85 | 0.0 | 1249408.28 | 1.31 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.05 | 22.93 | 13.11 | -0.12 | 664482.75 | 3.43 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.2 | 16.84 | 10.63 | -0.0 | 594639.75 | 9.65 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.23 | 29.98 | 11.84 | -0.05 | 236192.59 | 3.27 | skipped_fast |
| CCUSDT | IDLE | 2.25 | 11.25 | 8.45 | 0.11 | 818799.16 | 9.6 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 2.86 | 37.92 | 11.85 | 0.03 | 155617.33 | 13.6 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.49 | 8.8 | 8.09 | -0.03 | 428537.34 | 18.49 | skipped_fast |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 4.21 | 9.28 | 5.99 | 0.02 | 73071.91 | 9.29 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 3.12 | 9.75 | 7.29 | -0.01 | 189374.02 | 7.89 | skipped_fast |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.17 | 7.96 | 7.37 | -0.04 | 168696.63 | 26.69 | skipped_fast |
| EDELUSDT | IDLE | 2.69 | 4.76 | 4.11 | -0.03 | 79021.07 | 45.15 | skipped_fast |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.89 | 7.38 | 5.83 | -0.01 | 5825.49 | 19.42 | skipped_fast |
| QAITUSDT | IDLE | 1.66 | 2.91 | 2.68 | -0.02 | 3175.19 | 67.05 | skipped_fast |
| RIZEUSDT | IDLE | 0.76 | 3.18 | 1.84 | -0.01 | 49214.36 | 45.14 | skipped_fast |
| RWAUSDT | IDLE | 1.82 | 3.29 | 2.31 | 0.02 | 57539.3 | 16.31 | skipped_fast |
| RWAINCUSDT | IDLE | 1.21 | 2.11 | 2.07 | 0.01 | 11402.57 | 81.15 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
