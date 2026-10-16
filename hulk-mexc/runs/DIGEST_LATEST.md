# Hulk DIGEST — 2026-10-16T20:46:34Z

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
| PYTHUSDT | IDLE | 1.91 | 6.8 | 4.76 | -0.11 | 2008538.84 | 4.73 | skipped_fast |
| WUSDT | IDLE | 2.41 | 6.27 | 3.68 | -0.03 | 1769919.91 | 11.2 | skipped_fast |
| XRPUSDT | IDLE | 1.67 | 3.07 | 1.84 | -0.03 | 28592850.62 | 2.3 | skipped_fast |
| ETHUSDT | IDLE | 1.53 | 2.78 | 1.92 | -0.02 | 211555224.56 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.74 | 1.43 | 0.38 | -0.01 | 360264617.85 | 0.0 | skipped_fast |
| QNTUSDT | IDLE | 1.79 | 3.33 | 1.68 | -0.03 | 752971.27 | 2.47 | skipped_fast |
| EDELUSDT | IDLE | 3.02 | 5.45 | 3.93 | 0.0 | 189912.97 | 30.44 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 2.61 | 6.96 | 5.05 | -0.09 | 96721.22 | 16.67 | skipped_fast |
| ZBCNUSDT | IDLE | 2.32 | 4.27 | 2.5 | -0.01 | 189384.15 | 2.28 | skipped_fast |
| CCUSDT | IDLE | 1.37 | 2.49 | 1.7 | -0.04 | 377716.03 | 8.75 | skipped_fast |
| RWAINCUSDT | IDLE | 1.9 | 9.03 | 5.57 | -0.11 | 28081.66 | 5.6 | skipped_fast |
| HBARUSDT | IDLE | 2.34 | 4.2 | 3.14 | -0.03 | 309639.4 | 3.62 | skipped_fast |
| CHIPUSDT | IDLE | 1.47 | 5.31 | 3.74 | -0.03 | 152829.93 | 10.97 | skipped_fast |
| BIOUSDT | IDLE | 1.92 | 3.52 | 2.19 | -0.03 | 61852.75 | 3.99 | skipped_fast |
| KITEUSDT | IDLE | 1.36 | 2.52 | 1.35 | -0.04 | 56405.65 | 12.43 | skipped_fast |
| RWAUSDT | IDLE | 2.08 | 3.9 | 1.8 | -0.01 | 53230.72 | 15.91 | skipped_fast |
| FLUIDUSDT | IDLE | 2.35 | 4.69 | 0.06 | -0.0 | 7182.33 | 17.59 | skipped_fast |
| RIZEUSDT | IDLE | 1.02 | 2.4 | 0.28 | -0.0 | 45878.94 | 44.67 | skipped_fast |
| TELUSDT | IDLE | 1.88 | 3.33 | 2.89 | -0.01 | 92413.74 | 40.01 | skipped_fast |
| MNSRYUSDT | IDLE | 0.49 | 0.88 | 0.69 | -0.01 | 34041.73 | 24.19 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
