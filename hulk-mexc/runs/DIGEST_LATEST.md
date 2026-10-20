# Hulk DIGEST — 2026-10-20T03:08:26Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| XRPUSDT | IDLE | 0.99 | 1.9 | 0.57 | -0.01 | 20371151.05 | 1.53 | skipped_fast |
| ETHUSDT | IDLE | 0.96 | 1.85 | 0.52 | -0.01 | 122197040.41 | 0.21 | skipped_fast |
| BTCUSDT | IDLE | 0.69 | 1.31 | 0.47 | -0.01 | 305098218.42 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.01 | 3.71 | 2.11 | -0.03 | 1061339.2 | 4.12 | skipped_fast |
| WUSDT | IDLE | 2.97 | 5.57 | 2.43 | 0.01 | 713497.06 | 15.16 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.59 | 13.3 | 11.01 | -0.07 | 66788.15 | 39.99 | skipped_fast |
| EDELUSDT | IDLE | 3.38 | 6.61 | 0.99 | 0.04 | 166406.08 | 35.8 | skipped_fast |
| CCUSDT | IDLE | 2.06 | 4.01 | 0.73 | 0.05 | 394946.78 | 6.55 | skipped_fast |
| QNTUSDT | IDLE | 1.55 | 3.09 | 0.13 | 0.02 | 711458.96 | 2.54 | skipped_fast |
| CHIPUSDT | IDLE | 1.72 | 3.33 | 0.78 | -0.01 | 75729.92 | 14.22 | skipped_fast |
| REDUSDT | IDLE | 1.59 | 3.0 | 1.22 | -0.01 | 58108.05 | 16.02 | skipped_fast |
| KITEUSDT | IDLE | 1.42 | 2.86 | 1.22 | 0.06 | 76857.75 | 10.59 | skipped_fast |
| BIOUSDT | IDLE | 1.25 | 2.46 | 0.25 | -0.01 | 67282.98 | 4.23 | skipped_fast |
| ZBCNUSDT | IDLE | 1.12 | 2.11 | 0.88 | -0.02 | 165322.59 | 49.62 | skipped_fast |
| HBARUSDT | IDLE | 0.9 | 1.73 | 0.4 | -0.02 | 394251.04 | 3.61 | skipped_fast |
| RWAINCUSDT | IDLE | 1.26 | 2.61 | 1.53 | 0.02 | 69223.14 | 57.01 | skipped_fast |
| WAXLUSDT | IDLE | 1.71 | 3.98 | 1.86 | -0.05 | 57227.34 | 54.76 | skipped_fast |
| LAUSDT | IDLE | 1.51 | 2.95 | 0.49 | -0.0 | 55309.67 | 24.65 | skipped_fast |
| IOTAUSDT | IDLE | 1.19 | 2.31 | 0.42 | 0.01 | 90246.45 | 28.66 | skipped_fast |
| FLUIDUSDT | IDLE | 1.15 | 2.25 | 0.28 | 0.02 | 4732.18 | 21.53 | skipped_fast |
| RWAUSDT | IDLE | 0.25 | 0.47 | 0.23 | -0.0 | 52817.97 | 23.54 | skipped_fast |
| MNSRYUSDT | IDLE | 0.14 | 0.27 | 0.04 | -0.0 | 40128.56 | 5.7 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
