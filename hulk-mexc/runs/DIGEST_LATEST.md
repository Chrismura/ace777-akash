# Hulk DIGEST — 2026-09-28T20:30:58Z

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
| HBARUSDT | IDLE | 1.61 | 14.78 | 8.16 | 0.27 | 11394449.2 | 1.66 | skipped_fast |
| WUSDT | IDLE | 1.0 | 4.77 | 2.54 | -0.15 | 2186791.23 | 11.75 | skipped_fast |
| QNTUSDT | IDLE | 0.86 | 18.61 | 6.44 | 0.3 | 21868724.58 | 8.66 | skipped_fast |
| XRPUSDT | IDLE | 1.73 | 3.16 | 1.97 | -0.02 | 68482972.82 | 2.01 | skipped_fast |
| ETHUSDT | IDLE | 1.34 | 2.45 | 1.48 | -0.0 | 405758051.21 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 1.02 | 1.88 | 1.05 | -0.01 | 846107258.68 | 0.09 | skipped_fast |
| CCUSDT | IDLE | 1.58 | 5.9 | 3.58 | -0.06 | 1341161.52 | 7.74 | skipped_fast |
| PYTHUSDT | IDLE | 1.88 | 3.93 | 2.05 | -0.07 | 1283963.91 | 3.78 | skipped_fast |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.59 | 27.82 | 5.3 | 0.2 | 291758.59 | 49.76 | skipped_fast |
| RWAINCUSDT | IDLE | 3.48 | 9.08 | 2.42 | 0.0 | 16200.26 | 91.87 | skipped_fast |
| KITEUSDT | IDLE | 1.69 | 6.35 | 3.11 | -0.09 | 101018.71 | 8.04 | skipped_fast |
| RIZEUSDT | IDLE | 1.98 | 6.81 | 0.54 | 0.05 | 52084.05 | 39.87 | skipped_fast |
| CHIPUSDT | IDLE | 1.64 | 3.9 | 1.93 | -0.07 | 74861.13 | 11.45 | skipped_fast |
| ZBCNUSDT | IDLE | 0.96 | 1.88 | 0.27 | -0.05 | 233976.48 | 14.89 | skipped_fast |
| REDUSDT | IDLE | 1.54 | 3.05 | 1.45 | -0.06 | 60024.24 | 8.09 | skipped_fast |
| BIOUSDT | IDLE | 1.19 | 3.62 | 1.14 | -0.07 | 115105.25 | 3.39 | skipped_fast |
| EDELUSDT | IDLE | 0.5 | 3.12 | 1.93 | 0.11 | 169755.91 | 17.29 | skipped_fast |
| FLUIDUSDT | IDLE | 1.54 | 3.66 | 2.11 | -0.06 | 5202.95 | 22.09 | skipped_fast |
| RWAUSDT | IDLE | 0.81 | 1.52 | 0.71 | -0.01 | 60104.73 | 28.72 | skipped_fast |
| MNSRYUSDT | IDLE | 0.42 | 0.76 | 0.47 | -0.02 | 34766.67 | 16.76 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
