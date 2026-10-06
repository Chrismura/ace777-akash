# Hulk DIGEST — 2026-10-06T05:24:36Z

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
| QNTUSDT | IDLE | 2.64 | 4.61 | 4.41 | 0.01 | 2789346.82 | 6.98 | skipped_fast |
| BTCUSDT | IDLE | 0.85 | 1.62 | 0.54 | 0.0 | 565005117.65 | 0.0 | skipped_fast |
| XRPUSDT | IDLE | 0.75 | 1.41 | 0.56 | 0.0 | 29400071.06 | 1.99 | skipped_fast |
| ETHUSDT | IDLE | 0.59 | 1.08 | 0.7 | 0.0 | 323621052.85 | 0.04 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.74 | 8.26 | 5.24 | 0.01 | 340557.36 | 5.99 | skipped_fast |
| PYTHUSDT | IDLE | 1.9 | 3.55 | 1.7 | 0.01 | 581373.12 | 2.57 | skipped_fast |
| WUSDT | IDLE | 2.53 | 4.59 | 3.18 | -0.03 | 377772.54 | 7.81 | skipped_fast |
| ZBCNUSDT | IDLE | 2.41 | 4.34 | 3.19 | 0.0 | 293778.6 | 7.04 | skipped_fast |
| RIZEUSDT | IDLE | 2.0 | 24.74 | 10.91 | 0.17 | 102852.53 | 121.37 | skipped_fast |
| CCUSDT | IDLE | 1.02 | 1.89 | 0.97 | -0.01 | 463139.81 | 7.89 | skipped_fast |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 2.68 | 16.47 | 13.25 | 0.09 | 95896.78 | 21.41 | skipped_fast |
| BIOUSDT | IDLE | 1.88 | 4.64 | 2.73 | 0.03 | 109805.14 | 3.19 | skipped_fast |
| REDUSDT | IDLE | 2.18 | 3.92 | 2.99 | -0.03 | 63959.75 | 8.39 | skipped_fast |
| CHIPUSDT | IDLE | 1.67 | 5.86 | 2.83 | 0.11 | 121523.32 | 14.82 | skipped_fast |
| KITEUSDT | IDLE | 1.12 | 1.98 | 1.71 | -0.04 | 67129.43 | 8.65 | skipped_fast |
| HBARUSDT | IDLE | 0.84 | 1.48 | 1.29 | -0.02 | 423735.66 | 5.95 | skipped_fast |
| RWAINCUSDT | IDLE | 1.29 | 2.85 | 2.57 | -0.03 | 17885.28 | 63.47 | skipped_fast |
| TELUSDT | IDLE | 1.93 | 3.39 | 3.07 | -0.05 | 131387.35 | 43.1 | skipped_fast |
| RWAUSDT | IDLE | 0.48 | 0.88 | 0.51 | -0.01 | 50918.47 | 7.34 | skipped_fast |
| MNSRYUSDT | IDLE | 0.3 | 0.57 | 0.18 | 0.01 | 45577.35 | 5.13 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
