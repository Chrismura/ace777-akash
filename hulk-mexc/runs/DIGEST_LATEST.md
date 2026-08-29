# Hulk DIGEST — 2026-08-29T20:07:15Z

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
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.87 | 70.44 | 38.01 | -0.02 | 136777.75 | 17.86 | skipped_fast |
| XRPUSDT | IDLE | 0.57 | 1.13 | 0.12 | 0.02 | 17973751.52 | 2.14 | skipped_fast |
| CHIPUSDT | IDLE | 1.25 | 3.63 | 2.71 | -0.02 | 952276.03 | 2.45 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.6 | 9.92 | 6.68 | -0.08 | 39100.22 | 61.18 | skipped_fast |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.79 | 7.11 | 6.43 | 0.01 | 67606.44 | 8.59 | skipped_fast |
| PYTHUSDT | IDLE | 1.86 | 3.52 | 1.36 | 0.04 | 321930.58 | 4.13 | skipped_fast |
| ZBCNUSDT | IDLE | 2.18 | 3.87 | 3.21 | -0.03 | 193967.56 | 7.79 | skipped_fast |
| CCUSDT | IDLE | 1.61 | 3.18 | 0.71 | 0.08 | 206967.99 | 4.23 | skipped_fast |
| WUSDT | IDLE | 0.93 | 1.73 | 0.8 | 0.01 | 180884.33 | 11.99 | skipped_fast |
| REDUSDT | IDLE | 1.03 | 1.83 | 1.5 | 0.02 | 76223.91 | 12.04 | skipped_fast |
| BIOUSDT | IDLE | 0.59 | 1.06 | 0.79 | -0.0 | 65161.22 | 7.26 | skipped_fast |
| RWAINCUSDT | IDLE | 0.98 | 1.8 | 1.11 | -0.05 | 2885.56 | 106.89 | skipped_fast |
| TELUSDT | IDLE | 1.19 | 2.21 | 1.08 | -0.01 | 68950.78 | 46.06 | skipped_fast |
| HBARUSDT | IDLE | 0.29 | 0.57 | 0.13 | -0.01 | 184690.41 | 1.32 | skipped_fast |
| QNTUSDT | IDLE | 0.58 | 1.05 | 0.71 | 0.0 | 28885.61 | 4.9 | skipped_fast |
| RWAUSDT | IDLE | 0.3 | 0.58 | 0.16 | 0.01 | 54131.39 | 24.68 | skipped_fast |
| FLUIDUSDT | IDLE | 0.12 | 0.24 | 0.0 | 0.0 | 1985.37 | 21.47 | skipped_fast |
| QAITUSDT | ERR | — | — | — | — | — | — | HTTP Error 400: Bad Request |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
