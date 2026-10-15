# Hulk DIGEST — 2026-10-15T20:16:50Z

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
| PYTHUSDT | IDLE | 2.22 | 13.12 | 5.78 | 0.12 | 4512779.58 | 3.15 | skipped_fast |
| WUSDT | IDLE | 1.44 | 4.13 | 2.57 | -0.04 | 2667919.93 | 17.66 | skipped_fast |
| ETHUSDT | IDLE | 1.43 | 2.83 | 0.25 | 0.01 | 338751007.15 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 1.0 | 1.94 | 0.45 | 0.01 | 49932575.59 | 2.24 | skipped_fast |
| BTCUSDT | IDLE | 0.83 | 1.6 | 0.35 | 0.0 | 502321310.92 | 0.0 | skipped_fast |
| QNTUSDT | IDLE | 1.67 | 4.93 | 3.85 | 0.0 | 1368304.08 | 2.89 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.75 | 10.86 | 7.88 | -0.12 | 244903.29 | 17.03 | skipped_fast |
| ZBCNUSDT | IDLE | 2.83 | 5.93 | 2.17 | 0.02 | 220642.28 | 38.1 | skipped_fast |
| CCUSDT | IDLE | 1.51 | 3.47 | 3.27 | -0.08 | 432806.67 | 6.55 | skipped_fast |
| RIZEUSDT | IDLE | 2.91 | 11.39 | 4.12 | 0.04 | 82890.27 | 42.64 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 2.91 | 6.12 | 5.72 | 0.03 | 28060.18 | 5.01 | skipped_fast |
| REDUSDT | IDLE | 2.42 | 7.37 | 4.34 | -0.0 | 73039.44 | 5.08 | skipped_fast |
| KITEUSDT | IDLE | 1.57 | 3.14 | 1.71 | -0.02 | 70509.32 | 12.07 | skipped_fast |
| HBARUSDT | IDLE | 1.77 | 3.47 | 0.41 | 0.01 | 306707.85 | 5.87 | skipped_fast |
| CHIPUSDT | IDLE | 0.83 | 4.55 | 2.98 | -0.12 | 151643.59 | 15.06 | skipped_fast |
| BIOUSDT | IDLE | 1.02 | 2.44 | 0.62 | -0.02 | 84944.99 | 7.74 | skipped_fast |
| TELUSDT | IDLE | 1.77 | 3.47 | 0.5 | 0.0 | 89283.59 | 11.24 | skipped_fast |
| MNSRYUSDT | IDLE | 1.21 | 2.27 | 1.06 | -0.0 | 33462.85 | 32.45 | skipped_fast |
| RWAUSDT | IDLE | 1.02 | 1.92 | 0.86 | 0.0 | 55148.95 | 31.7 | skipped_fast |
| FLUIDUSDT | IDLE | 1.02 | 2.38 | 2.09 | -0.05 | 9614.35 | 21.48 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
