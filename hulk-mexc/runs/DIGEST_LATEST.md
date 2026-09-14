# Hulk DIGEST — 2026-09-14T06:34:20Z

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
| XRPUSDT | IDLE | 1.93 | 3.74 | 0.75 | 0.01 | 26568598.87 | 2.18 | skipped_fast |
| ETHUSDT | IDLE | 1.12 | 2.14 | 0.62 | -0.0 | 325110077.38 | 0.12 | skipped_fast |
| BTCUSDT | IDLE | 0.83 | 1.58 | 0.55 | 0.0 | 388197749.42 | 0.0 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.8 | 49.46 | 13.52 | 0.34 | 81568.52 | 25.31 | skipped_fast |
| REDUSDT | IDLE | 3.66 | 8.4 | 4.93 | 0.01 | 114011.29 | 16.4 | skipped_fast |
| PYTHUSDT | IDLE | 1.87 | 4.2 | 1.93 | 0.05 | 522043.94 | 1.74 | skipped_fast |
| WUSDT | IDLE | 2.39 | 4.7 | 0.47 | 0.02 | 220656.25 | 6.86 | skipped_fast |
| EDELUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.07 | 9.48 | 0.49 | 0.14 | 228860.74 | 21.22 | skipped_fast |
| CHIPUSDT | IDLE | 2.11 | 7.62 | 3.65 | -0.1 | 104062.87 | 18.85 | skipped_fast |
| ZBCNUSDT | IDLE | 1.85 | 3.47 | 1.57 | -0.01 | 204789.63 | 39.47 | skipped_fast |
| CCUSDT | IDLE | 1.07 | 2.0 | 0.99 | -0.02 | 272311.9 | 8.31 | skipped_fast |
| KITEUSDT | IDLE | 1.74 | 3.2 | 1.89 | -0.02 | 61479.94 | 6.51 | skipped_fast |
| BIOUSDT | IDLE | 1.6 | 3.08 | 0.85 | -0.01 | 67767.66 | 3.91 | skipped_fast |
| HBARUSDT | IDLE | 1.14 | 2.18 | 0.73 | 0.01 | 271854.97 | 1.31 | skipped_fast |
| RWAINCUSDT | IDLE | 1.09 | 2.07 | 0.71 | 0.0 | 9612.57 | 16.56 | skipped_fast |
| QNTUSDT | IDLE | 1.34 | 2.64 | 0.25 | -0.0 | 36138.88 | 6.25 | skipped_fast |
| TELUSDT | IDLE | 1.15 | 2.18 | 0.82 | -0.02 | 85096.08 | 25.3 | skipped_fast |
| FLUIDUSDT | IDLE | 1.44 | 2.75 | 0.85 | -0.0 | 813.34 | 21.73 | skipped_fast |
| RWAUSDT | IDLE | 0.39 | 0.74 | 0.3 | 0.0 | 52897.48 | 22.21 | skipped_fast |
| MNSRYUSDT | IDLE | 0.09 | 0.15 | 0.14 | -0.0 | 29927.06 | 4.18 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
