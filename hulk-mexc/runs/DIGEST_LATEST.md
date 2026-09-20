# Hulk DIGEST — 2026-09-20T02:00:42Z

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
| XRPUSDT | IDLE | 1.47 | 2.61 | 2.24 | -0.01 | 56186980.95 | 2.86 | skipped_fast |
| ETHUSDT | IDLE | 0.54 | 0.97 | 0.73 | 0.0 | 211806703.06 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.3 | 0.55 | 0.31 | -0.0 | 425288831.05 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.99 | 3.88 | 0.71 | 0.02 | 662669.08 | 4.86 | skipped_fast |
| WUSDT | IDLE | 1.88 | 3.73 | 0.19 | 0.02 | 499891.33 | 4.47 | skipped_fast |
| HBARUSDT | IDLE | 2.53 | 4.71 | 2.35 | 0.03 | 623114.55 | 1.22 | skipped_fast |
| CCUSDT | IDLE | 2.09 | 3.7 | 3.19 | -0.03 | 310603.41 | 8.34 | skipped_fast |
| ZBCNUSDT | IDLE | 1.42 | 5.28 | 4.39 | 0.07 | 215283.84 | 22.64 | skipped_fast |
| EDELUSDT | IDLE | 1.66 | 5.77 | 5.11 | -0.1 | 112395.77 | 45.15 | skipped_fast |
| CHIPUSDT | IDLE | 1.45 | 3.98 | 3.02 | -0.06 | 110533.77 | 13.99 | skipped_fast |
| BIOUSDT | IDLE | 1.35 | 2.47 | 1.52 | 0.02 | 90336.16 | 3.59 | skipped_fast |
| REDUSDT | IDLE | 1.23 | 2.21 | 1.73 | 0.03 | 108911.75 | 15.58 | skipped_fast |
| KITEUSDT | IDLE | 1.02 | 1.86 | 1.24 | 0.01 | 80413.73 | 14.05 | skipped_fast |
| RWAINCUSDT | IDLE | 0.64 | 1.37 | 1.35 | -0.04 | 7651.63 | 5.96 | skipped_fast |
| TELUSDT | IDLE | 1.56 | 3.14 | 2.32 | -0.07 | 103162.52 | 54.02 | skipped_fast |
| QNTUSDT | IDLE | 1.36 | 2.53 | 1.31 | 0.04 | 54896.68 | 7.62 | skipped_fast |
| FLUIDUSDT | IDLE | 1.31 | 2.3 | 2.16 | 0.02 | 8204.33 | 21.37 | skipped_fast |
| RIZEUSDT | IDLE | 1.2 | 4.68 | 2.95 | 0.0 | 40174.44 | 212.51 | skipped_fast |
| RWAUSDT | IDLE | 0.63 | 1.11 | 0.95 | 0.01 | 52750.39 | 51.6 | skipped_fast |
| MNSRYUSDT | IDLE | 0.39 | 0.72 | 0.4 | -0.01 | 34582.79 | 41.16 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
