# Hulk DIGEST — 2026-09-27T21:12:57Z

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
| PYTHUSDT | IDLE | 1.85 | 4.97 | 2.71 | 0.07 | 2312709.08 | 4.74 | skipped_fast |
| WUSDT | IDLE | 1.27 | 7.72 | 4.66 | 0.21 | 4829081.32 | 9.06 | skipped_fast |
| QNTUSDT | IDLE | 0.81 | 12.83 | 0.31 | 0.63 | 7499398.84 | 14.6 | skipped_fast |
| XRPUSDT | IDLE | 0.97 | 1.78 | 1.12 | 0.01 | 40514328.34 | 3.28 | skipped_fast |
| BTCUSDT | IDLE | 0.32 | 0.6 | 0.26 | 0.01 | 435376542.44 | 0.0 | skipped_fast |
| ETHUSDT | IDLE | 0.31 | 0.55 | 0.4 | 0.0 | 195652853.05 | 0.04 | skipped_fast |
| CCUSDT | IDLE | 2.67 | 5.22 | 0.74 | 0.03 | 625404.46 | 7.97 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.68 | 24.25 | 19.49 | -0.23 | 48341.42 | 60.89 | skipped_fast |
| HBARUSDT | IDLE | 1.21 | 2.33 | 0.61 | 0.02 | 708620.58 | 1.05 | skipped_fast |
| KITEUSDT | IDLE | 2.24 | 4.37 | 1.66 | 0.03 | 139630.68 | 8.59 | skipped_fast |
| EDELUSDT | IDLE | 1.65 | 7.33 | 4.8 | -0.13 | 136970.61 | 41.91 | skipped_fast |
| CHIPUSDT | IDLE | 1.85 | 3.5 | 2.18 | -0.03 | 98113.26 | 12.87 | skipped_fast |
| RWAINCUSDT | IDLE | 1.72 | 17.91 | 1.67 | 0.21 | 28696.97 | 92.43 | skipped_fast |
| ZBCNUSDT | IDLE | 1.31 | 2.35 | 1.86 | -0.0 | 210657.72 | 29.52 | skipped_fast |
| REDUSDT | IDLE | 1.39 | 2.55 | 1.54 | 0.02 | 64090.39 | 12.87 | skipped_fast |
| BIOUSDT | IDLE | 1.04 | 1.95 | 0.88 | -0.0 | 84493.76 | 6.31 | skipped_fast |
| TELUSDT | IDLE | 0.97 | 3.83 | 2.53 | 0.14 | 170866.7 | 27.05 | skipped_fast |
| FLUIDUSDT | IDLE | 0.84 | 1.47 | 1.45 | 0.04 | 2168.54 | 21.57 | skipped_fast |
| RWAUSDT | IDLE | 0.29 | 0.5 | 0.49 | 0.01 | 57595.08 | 7.07 | skipped_fast |
| MNSRYUSDT | IDLE | 0.2 | 0.38 | 0.11 | 0.01 | 40043.36 | 12.64 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
