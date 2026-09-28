# Hulk DIGEST — 2026-09-28T05:37:45Z

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
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 3.43 | 11.01 | 9.67 | -0.0 | 5077507.31 | 6.98 | skipped_fast |
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 2.64 | 6.64 | 5.49 | -0.06 | 2003782.67 | 2.49 | skipped_fast |
| QNTUSDT | IDLE | 1.03 | 32.28 | 20.7 | 0.38 | 15912942.23 | 12.61 | skipped_fast |
| XRPUSDT | IDLE | 2.35 | 4.11 | 3.89 | -0.03 | 51222949.62 | 2.04 | skipped_fast |
| BTCUSDT | IDLE | 1.43 | 2.49 | 2.43 | -0.02 | 553721056.22 | 0.0 | skipped_fast |
| ETHUSDT | IDLE | 1.36 | 2.38 | 2.31 | -0.02 | 270540868.44 | 0.15 | skipped_fast |
| CCUSDT | WATCH_PULLBACK — tension haute + reflux | 4.06 | 9.05 | 7.92 | -0.02 | 804602.11 | 17.94 | skipped_fast |
| HBARUSDT | IDLE | 2.07 | 3.74 | 2.7 | 0.02 | 1103341.77 | 1.05 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.53 | 8.43 | 7.5 | -0.05 | 89355.91 | 10.02 | skipped_fast |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 4.03 | 7.47 | 6.68 | -0.06 | 106474.84 | 9.06 | skipped_fast |
| CHIPUSDT | IDLE | 2.36 | 6.28 | 5.86 | -0.08 | 88685.46 | 13.51 | skipped_fast |
| REDUSDT | IDLE | 2.55 | 5.3 | 4.83 | -0.04 | 65666.79 | 13.49 | skipped_fast |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 4.14 | 7.26 | 6.77 | -0.03 | 3563.99 | 16.94 | skipped_fast |
| RIZEUSDT | IDLE | 2.18 | 13.55 | 6.08 | -0.2 | 62010.62 | 63.51 | skipped_fast |
| ZBCNUSDT | IDLE | 1.55 | 2.74 | 2.34 | -0.03 | 245029.3 | 20.71 | skipped_fast |
| EDELUSDT | IDLE | 1.24 | 6.77 | 3.17 | -0.12 | 173082.38 | 43.78 | skipped_fast |
| TELUSDT | IDLE | 1.23 | 2.69 | 2.36 | 0.05 | 173861.79 | 38.39 | skipped_fast |
| RWAINCUSDT | IDLE | 0.53 | 5.61 | 0.0 | 0.25 | 31818.84 | 89.44 | skipped_fast |
| MNSRYUSDT | IDLE | 1.16 | 2.02 | 1.98 | -0.01 | 38724.72 | 68.07 | skipped_fast |
| RWAUSDT | IDLE | 0.83 | 1.44 | 1.42 | 0.0 | 60396.14 | 57.27 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
