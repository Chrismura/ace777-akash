# Hulk DIGEST — 2026-09-12T17:38:00Z

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
| ETHUSDT | IDLE | 0.49 | 0.86 | 0.77 | -0.02 | 276783950.94 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.34 | 0.6 | 0.47 | -0.0 | 21623015.78 | 2.19 | skipped_fast |
| BTCUSDT | IDLE | 0.18 | 0.31 | 0.31 | -0.01 | 373711762.11 | 0.0 | skipped_fast |
| RIZEUSDT | IDLE | 2.15 | 56.23 | 14.14 | 0.61 | 113552.2 | 50.28 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 4.03 | 9.61 | 7.17 | -0.03 | 208577.59 | 17.31 | skipped_fast |
| CHIPUSDT | IDLE | 2.91 | 7.31 | 4.23 | 0.01 | 74563.61 | 26.44 | skipped_fast |
| PYTHUSDT | IDLE | 1.65 | 3.93 | 0.69 | 0.04 | 346808.86 | 3.66 | skipped_fast |
| RWAINCUSDT | IDLE | 2.69 | 5.11 | 3.8 | -0.02 | 10494.82 | 5.49 | skipped_fast |
| EDELUSDT | IDLE | 2.0 | 5.14 | 0.84 | 0.09 | 170251.9 | 33.9 | skipped_fast |
| WUSDT | IDLE | 1.48 | 2.84 | 0.77 | 0.0 | 119456.53 | 10.1 | skipped_fast |
| CCUSDT | IDLE | 0.77 | 1.37 | 1.13 | -0.0 | 244608.95 | 7.16 | skipped_fast |
| REDUSDT | IDLE | 1.01 | 1.98 | 0.28 | 0.02 | 61167.35 | 19.95 | skipped_fast |
| KITEUSDT | IDLE | 0.79 | 1.47 | 0.75 | -0.02 | 59221.01 | 10.33 | skipped_fast |
| BIOUSDT | IDLE | 0.61 | 1.09 | 0.93 | 0.01 | 72739.24 | 7.8 | skipped_fast |
| TELUSDT | IDLE | 1.2 | 2.3 | 1.13 | -0.06 | 97990.35 | 6.0 | skipped_fast |
| RWAUSDT | IDLE | 1.1 | 1.93 | 1.82 | 0.0 | 53399.35 | 14.84 | skipped_fast |
| HBARUSDT | IDLE | 0.45 | 0.83 | 0.49 | -0.01 | 162585.83 | 1.34 | skipped_fast |
| QNTUSDT | IDLE | 0.69 | 1.23 | 0.99 | -0.01 | 41329.42 | 7.8 | skipped_fast |
| MNSRYUSDT | IDLE | 0.36 | 0.68 | 0.31 | -0.01 | 24730.4 | 36.15 | skipped_fast |
| FLUIDUSDT | IDLE | 0.27 | 0.54 | 0.0 | 0.01 | 1430.19 | 22.18 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
