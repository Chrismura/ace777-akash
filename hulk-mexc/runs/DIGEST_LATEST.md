# Hulk DIGEST — 2026-09-29T00:33:01Z

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
| QNTUSDT | IDLE | 1.39 | 15.02 | 12.23 | -0.25 | 13930413.97 | 7.59 | skipped_fast |
| HBARUSDT | IDLE | 1.47 | 13.25 | 6.9 | 0.25 | 11753976.59 | 3.33 | skipped_fast |
| WUSDT | IDLE | 1.12 | 4.77 | 0.37 | -0.11 | 1720369.32 | 5.75 | skipped_fast |
| XRPUSDT | IDLE | 1.29 | 2.42 | 1.03 | -0.02 | 64604224.55 | 0.67 | skipped_fast |
| ETHUSDT | IDLE | 0.68 | 1.29 | 0.47 | 0.0 | 391744900.27 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.62 | 1.14 | 0.68 | -0.01 | 825383703.62 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.87 | 4.0 | 1.14 | -0.05 | 1165794.58 | 1.24 | skipped_fast |
| CCUSDT | IDLE | 0.99 | 3.87 | 1.15 | -0.06 | 1340108.67 | 6.9 | skipped_fast |
| ZBCNUSDT | IDLE | 3.72 | 7.35 | 0.57 | 0.03 | 230110.03 | 27.35 | skipped_fast |
| EDELUSDT | IDLE | 1.86 | 11.33 | 8.98 | 0.05 | 157309.16 | 22.46 | skipped_fast |
| REDUSDT | IDLE | 2.97 | 5.43 | 3.39 | -0.05 | 58579.37 | 14.85 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 3.01 | 6.54 | 6.14 | -0.05 | 16481.45 | 20.82 | skipped_fast |
| TELUSDT | IDLE | 1.81 | 17.99 | 4.95 | 0.27 | 364060.7 | 42.34 | skipped_fast |
| RIZEUSDT | IDLE | 1.91 | 8.95 | 2.19 | 0.1 | 44964.68 | 71.98 | skipped_fast |
| CHIPUSDT | IDLE | 1.51 | 2.87 | 1.36 | -0.07 | 75921.07 | 20.68 | skipped_fast |
| BIOUSDT | IDLE | 1.14 | 3.07 | 0.27 | -0.07 | 114530.39 | 10.04 | skipped_fast |
| KITEUSDT | IDLE | 1.04 | 3.31 | 1.31 | -0.08 | 98789.69 | 9.45 | skipped_fast |
| FLUIDUSDT | IDLE | 1.16 | 2.23 | 1.51 | -0.07 | 3383.39 | 21.32 | skipped_fast |
| RWAUSDT | IDLE | 0.37 | 0.65 | 0.57 | -0.01 | 57566.42 | 7.2 | skipped_fast |
| MNSRYUSDT | IDLE | 0.7 | 1.25 | 1.03 | -0.03 | 33244.2 | 44.18 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
