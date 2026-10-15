# Hulk DIGEST — 2026-10-15T19:16:47Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 3.73 | 22.41 | 7.01 | 0.13 | 4425260.29 | 3.2 | skipped_fast |
| WUSDT | IDLE | 2.29 | 7.07 | 0.74 | -0.01 | 2669455.77 | 16.03 | skipped_fast |
| ETHUSDT | IDLE | 2.6 | 5.17 | 0.18 | 0.01 | 340601060.09 | 0.49 | skipped_fast |
| XRPUSDT | IDLE | 2.37 | 4.71 | 0.26 | 0.01 | 50339686.51 | 1.49 | skipped_fast |
| BTCUSDT | IDLE | 1.55 | 3.08 | 0.13 | 0.01 | 499951081.56 | 0.0 | skipped_fast |
| QNTUSDT | IDLE | 3.54 | 11.34 | 2.25 | 0.03 | 1344995.81 | 1.42 | skipped_fast |
| REDUSDT | IDLE | 4.17 | 13.25 | 3.73 | 0.01 | 72862.92 | 11.34 | skipped_fast |
| ZBCNUSDT | IDLE | 3.31 | 7.2 | 0.36 | 0.04 | 207128.86 | 3.52 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.77 | 10.86 | 8.57 | -0.12 | 244557.17 | 47.96 | skipped_fast |
| CCUSDT | IDLE | 1.82 | 4.84 | 2.15 | -0.07 | 434934.43 | 5.56 | skipped_fast |
| KITEUSDT | IDLE | 3.28 | 7.05 | 0.46 | -0.01 | 70442.79 | 11.92 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.97 | 11.39 | 5.66 | 0.03 | 82301.47 | 57.82 | skipped_fast |
| CHIPUSDT | IDLE | 2.01 | 12.28 | 2.5 | -0.12 | 150469.61 | 12.83 | skipped_fast |
| BIOUSDT | IDLE | 2.54 | 6.26 | 0.38 | -0.02 | 84793.28 | 7.72 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 2.51 | 6.12 | 5.67 | 0.04 | 28183.07 | 25.06 | skipped_fast |
| HBARUSDT | IDLE | 2.63 | 5.26 | 0.0 | 0.02 | 306212.36 | 2.36 | skipped_fast |
| TELUSDT | IDLE | 3.33 | 6.57 | 0.56 | -0.01 | 91879.95 | 22.52 | skipped_fast |
| FLUIDUSDT | IDLE | 1.67 | 4.42 | 0.0 | -0.02 | 9094.41 | 21.26 | skipped_fast |
| MNSRYUSDT | IDLE | 1.45 | 2.77 | 0.85 | -0.0 | 32933.28 | 32.44 | skipped_fast |
| RWAUSDT | IDLE | 1.05 | 2.02 | 0.48 | -0.0 | 54527.65 | 15.91 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
