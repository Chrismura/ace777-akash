# Hulk DIGEST — 2026-09-10T10:17:50Z

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
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 4.08 | 209.6 | 53.36 | -0.55 | 86104.52 | 530.81 | skipped_fast |
| XRPUSDT | IDLE | 0.75 | 1.33 | 1.1 | -0.03 | 41075439.31 | 2.18 | skipped_fast |
| BTCUSDT | IDLE | 0.45 | 0.79 | 0.72 | -0.01 | 516359904.23 | 0.0 | skipped_fast |
| ETHUSDT | IDLE | 0.46 | 0.82 | 0.62 | -0.01 | 330375668.16 | 0.53 | skipped_fast |
| PYTHUSDT | IDLE | 1.32 | 3.38 | 2.82 | -0.05 | 998720.59 | 1.93 | skipped_fast |
| CCUSDT | IDLE | 2.28 | 4.0 | 3.69 | -0.05 | 665987.59 | 3.95 | skipped_fast |
| KITEUSDT | IDLE | 3.06 | 6.55 | 4.28 | -0.05 | 57471.94 | 12.02 | skipped_fast |
| EDELUSDT | IDLE | 1.43 | 5.35 | 2.84 | 0.08 | 240772.44 | 17.71 | skipped_fast |
| ZBCNUSDT | IDLE | 1.82 | 3.24 | 2.62 | 0.02 | 160762.64 | 16.17 | skipped_fast |
| WUSDT | IDLE | 1.43 | 3.38 | 2.16 | -0.06 | 229670.05 | 19.71 | skipped_fast |
| REDUSDT | IDLE | 1.44 | 3.08 | 2.0 | -0.06 | 65145.96 | 9.7 | skipped_fast |
| BIOUSDT | IDLE | 1.08 | 2.35 | 1.55 | -0.06 | 99235.19 | 7.9 | skipped_fast |
| HBARUSDT | IDLE | 0.95 | 1.67 | 1.57 | -0.04 | 377394.11 | 1.32 | skipped_fast |
| CHIPUSDT | IDLE | 0.7 | 3.96 | 2.84 | -0.19 | 102985.41 | 14.52 | skipped_fast |
| RWAINCUSDT | IDLE | 1.29 | 2.27 | 2.11 | -0.02 | 5918.39 | 33.94 | skipped_fast |
| FLUIDUSDT | IDLE | 1.27 | 2.61 | 2.55 | -0.08 | 1430.23 | 21.43 | skipped_fast |
| TELUSDT | IDLE | 1.04 | 1.96 | 0.77 | 0.01 | 85652.38 | 60.86 | skipped_fast |
| QNTUSDT | IDLE | 0.72 | 1.27 | 1.07 | -0.02 | 38697.86 | 4.52 | skipped_fast |
| MNSRYUSDT | IDLE | 0.39 | 0.72 | 0.34 | -0.02 | 25289.43 | 4.14 | skipped_fast |
| RWAUSDT | IDLE | 0.27 | 0.52 | 0.15 | -0.03 | 53798.22 | 14.94 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
