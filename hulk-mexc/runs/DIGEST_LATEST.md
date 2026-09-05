# Hulk DIGEST — 2026-09-05T17:45:28Z

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
| ETHUSDT | IDLE | 0.72 | 1.39 | 0.3 | 0.01 | 172340713.28 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.71 | 1.4 | 0.18 | 0.02 | 21374618.25 | 2.82 | skipped_fast |
| BTCUSDT | IDLE | 0.42 | 0.81 | 0.2 | 0.01 | 345414116.74 | 0.12 | skipped_fast |
| CHIPUSDT | IDLE | 2.5 | 8.91 | 2.75 | 0.11 | 472132.32 | 18.74 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.5 | 23.03 | 5.03 | 0.3 | 146135.48 | 56.7 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 3.03 | 5.31 | 5.04 | -0.03 | 7928.33 | 16.42 | skipped_fast |
| PYTHUSDT | IDLE | 1.28 | 2.38 | 1.21 | 0.01 | 331015.85 | 3.65 | skipped_fast |
| KITEUSDT | IDLE | 2.31 | 5.35 | 4.17 | -0.06 | 61613.0 | 10.32 | skipped_fast |
| CCUSDT | IDLE | 1.48 | 2.8 | 1.03 | 0.03 | 281297.75 | 7.25 | skipped_fast |
| ZBCNUSDT | IDLE | 1.83 | 3.19 | 3.08 | -0.01 | 169931.16 | 4.3 | skipped_fast |
| WUSDT | IDLE | 1.47 | 2.65 | 1.91 | 0.01 | 148744.7 | 15.14 | skipped_fast |
| BIOUSDT | IDLE | 1.56 | 3.0 | 0.85 | 0.04 | 78718.77 | 3.59 | skipped_fast |
| REDUSDT | IDLE | 0.89 | 1.65 | 0.86 | 0.02 | 60529.35 | 8.78 | skipped_fast |
| EDELUSDT | IDLE | 0.26 | 4.79 | 0.84 | 0.0 | 173637.78 | 28.24 | skipped_fast |
| HBARUSDT | IDLE | 0.83 | 1.52 | 0.93 | 0.04 | 322051.75 | 1.24 | skipped_fast |
| RWAUSDT | IDLE | 1.55 | 3.02 | 0.56 | 0.03 | 51970.93 | 14.03 | skipped_fast |
| TELUSDT | IDLE | 1.43 | 2.73 | 0.87 | 0.0 | 66435.89 | 11.66 | skipped_fast |
| QNTUSDT | IDLE | 0.8 | 1.59 | 0.0 | 0.01 | 40282.4 | 3.09 | skipped_fast |
| FLUIDUSDT | IDLE | 0.76 | 1.43 | 0.62 | 0.01 | 897.41 | 21.74 | skipped_fast |
| MNSRYUSDT | IDLE | 0.16 | 0.3 | 0.1 | 0.0 | 38446.56 | 12.28 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
