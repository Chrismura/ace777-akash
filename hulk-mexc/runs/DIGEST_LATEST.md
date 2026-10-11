# Hulk DIGEST — 2026-10-11T14:18:02Z

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
| XRPUSDT | IDLE | 0.34 | 0.66 | 0.17 | -0.0 | 10075321.39 | 1.43 | skipped_fast |
| ETHUSDT | IDLE | 0.25 | 0.46 | 0.28 | 0.0 | 172719987.75 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.18 | 0.34 | 0.18 | 0.0 | 124073782.84 | 0.0 | skipped_fast |
| WUSDT | IDLE | 0.87 | 2.42 | 0.54 | -0.0 | 1104584.56 | 6.28 | skipped_fast |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 4.32 | 31.62 | 16.61 | 0.04 | 59494.23 | 21.6 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 4.36 | 11.9 | 7.38 | -0.01 | 28288.31 | 4.89 | skipped_fast |
| QNTUSDT | IDLE | 1.59 | 3.03 | 0.99 | -0.03 | 1022872.68 | 1.64 | skipped_fast |
| PYTHUSDT | IDLE | 1.43 | 2.56 | 1.97 | -0.02 | 723448.85 | 3.92 | skipped_fast |
| CCUSDT | IDLE | 1.92 | 3.8 | 0.33 | 0.03 | 306042.26 | 8.07 | skipped_fast |
| CHIPUSDT | IDLE | 0.92 | 9.04 | 0.59 | 0.34 | 391710.43 | 15.91 | skipped_fast |
| EDELUSDT | IDLE | 1.22 | 2.3 | 0.97 | 0.01 | 382858.07 | 36.12 | skipped_fast |
| RIZEUSDT | IDLE | 2.35 | 6.54 | 2.55 | -0.07 | 35571.26 | 59.57 | skipped_fast |
| ZBCNUSDT | IDLE | 1.34 | 2.54 | 0.96 | 0.0 | 160874.97 | 13.58 | skipped_fast |
| BIOUSDT | IDLE | 1.4 | 2.71 | 0.54 | 0.03 | 76212.77 | 3.36 | skipped_fast |
| TELUSDT | IDLE | 2.17 | 3.85 | 3.42 | -0.07 | 147858.52 | 23.6 | skipped_fast |
| REDUSDT | IDLE | 0.85 | 1.58 | 0.85 | -0.01 | 58007.42 | 17.48 | skipped_fast |
| KITEUSDT | IDLE | 0.68 | 1.24 | 0.76 | -0.03 | 74454.52 | 10.32 | skipped_fast |
| HBARUSDT | IDLE | 0.86 | 1.65 | 0.47 | -0.01 | 243677.54 | 6.53 | skipped_fast |
| RWAUSDT | IDLE | 0.77 | 1.51 | 0.16 | 0.0 | 52174.19 | 15.66 | skipped_fast |
| MNSRYUSDT | IDLE | 0.39 | 0.74 | 0.27 | -0.01 | 31702.65 | 28.73 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
