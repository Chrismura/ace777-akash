# Hulk DIGEST — 2026-10-11T01:43:59Z

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
| XRPUSDT | IDLE | 0.51 | 0.93 | 0.61 | -0.0 | 12456633.08 | 2.14 | skipped_fast |
| ETHUSDT | IDLE | 0.24 | 0.46 | 0.2 | 0.01 | 130340353.88 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.11 | 0.2 | 0.11 | 0.0 | 144354564.14 | 0.0 | skipped_fast |
| WUSDT | IDLE | 1.19 | 4.02 | 1.0 | 0.02 | 1247067.39 | 9.51 | skipped_fast |
| QNTUSDT | IDLE | 1.05 | 1.88 | 1.46 | -0.03 | 1274620.78 | 1.68 | skipped_fast |
| PYTHUSDT | IDLE | 1.6 | 3.03 | 1.12 | -0.03 | 753451.95 | 2.54 | skipped_fast |
| EDELUSDT | IDLE | 2.48 | 4.54 | 2.8 | -0.04 | 268673.76 | 54.52 | skipped_fast |
| CHIPUSDT | IDLE | 1.29 | 12.6 | 1.46 | 0.35 | 275722.86 | 12.69 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.64 | 7.24 | 6.41 | -0.1 | 33812.28 | 46.7 | skipped_fast |
| BIOUSDT | IDLE | 1.58 | 2.91 | 1.71 | 0.02 | 88040.29 | 6.84 | skipped_fast |
| TELUSDT | IDLE | 2.62 | 5.07 | 4.23 | -0.07 | 145008.67 | 45.85 | skipped_fast |
| CCUSDT | IDLE | 0.56 | 1.09 | 0.16 | -0.02 | 236916.27 | 8.38 | skipped_fast |
| ZBCNUSDT | IDLE | 0.81 | 1.48 | 0.88 | 0.02 | 169515.42 | 14.8 | skipped_fast |
| KITEUSDT | IDLE | 0.76 | 1.69 | 0.73 | 0.05 | 75482.99 | 10.18 | skipped_fast |
| REDUSDT | IDLE | 0.64 | 1.21 | 0.47 | 0.01 | 56677.52 | 14.62 | skipped_fast |
| HBARUSDT | IDLE | 0.54 | 1.07 | 0.06 | 0.01 | 315357.84 | 3.24 | skipped_fast |
| RWAINCUSDT | IDLE | 0.69 | 1.29 | 0.64 | -0.02 | 11889.39 | 24.55 | skipped_fast |
| FLUIDUSDT | IDLE | 0.71 | 1.36 | 0.43 | 0.02 | 7768.97 | 22.4 | skipped_fast |
| MNSRYUSDT | IDLE | 0.96 | 1.8 | 0.85 | -0.01 | 36578.58 | 68.32 | skipped_fast |
| RWAUSDT | IDLE | 0.18 | 0.32 | 0.24 | 0.0 | 53615.77 | 15.75 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
