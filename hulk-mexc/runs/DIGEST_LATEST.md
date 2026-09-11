# Hulk DIGEST — 2026-09-11T16:21:28Z

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
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.7 | 128.05 | 28.25 | 0.4 | 156981.4 | 35.15 | skipped_fast |
| ETHUSDT | IDLE | 4.24 | 9.44 | 4.35 | 0.05 | 603814512.91 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 4.28 | 8.82 | 4.26 | 0.02 | 52870742.53 | 4.37 | skipped_fast |
| BTCUSDT | IDLE | 2.68 | 4.93 | 2.92 | 0.01 | 535109802.04 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 4.23 | 8.34 | 3.08 | 0.03 | 379801.42 | 1.9 | skipped_fast |
| CCUSDT | IDLE | 3.65 | 6.77 | 3.52 | -0.01 | 483618.28 | 7.12 | skipped_fast |
| WUSDT | IDLE | 4.16 | 8.47 | 2.26 | 0.03 | 192190.33 | 11.21 | skipped_fast |
| EDELUSDT | IDLE | 4.1 | 7.66 | 3.64 | -0.02 | 157948.2 | 27.71 | skipped_fast |
| CHIPUSDT | IDLE | 3.76 | 11.97 | 2.08 | 0.06 | 147868.58 | 14.31 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 4.28 | 8.51 | 5.77 | 0.03 | 10237.99 | 5.51 | skipped_fast |
| REDUSDT | IDLE | 3.84 | 7.49 | 1.24 | 0.04 | 61981.1 | 10.34 | skipped_fast |
| ZBCNUSDT | IDLE | 3.05 | 5.61 | 3.29 | -0.01 | 180916.86 | 16.31 | skipped_fast |
| BIOUSDT | IDLE | 3.43 | 6.49 | 2.43 | 0.01 | 81095.55 | 7.9 | skipped_fast |
| TELUSDT | IDLE | 4.29 | 8.79 | 4.26 | -0.0 | 103490.08 | 50.69 | skipped_fast |
| KITEUSDT | IDLE | 2.22 | 4.0 | 2.96 | -0.01 | 60098.09 | 0.93 | skipped_fast |
| HBARUSDT | IDLE | 2.69 | 5.04 | 2.21 | 0.01 | 218393.09 | 1.33 | skipped_fast |
| QNTUSDT | IDLE | 2.88 | 5.19 | 3.77 | -0.01 | 40982.0 | 3.1 | skipped_fast |
| FLUIDUSDT | IDLE | 2.47 | 4.94 | 0.0 | 0.03 | 1301.56 | 21.52 | skipped_fast |
| RWAUSDT | IDLE | 1.65 | 3.2 | 0.67 | 0.02 | 51595.5 | 22.35 | skipped_fast |
| MNSRYUSDT | IDLE | 1.66 | 3.1 | 1.46 | 0.01 | 37864.26 | 46.99 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
