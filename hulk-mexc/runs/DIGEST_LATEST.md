# Hulk DIGEST — 2026-10-13T10:59:18Z

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
| PYTHUSDT | IDLE | 1.66 | 6.04 | 4.76 | -0.06 | 3197315.86 | 1.2 | skipped_fast |
| WUSDT | IDLE | 0.59 | 7.23 | 5.81 | -0.33 | 7340424.47 | 10.52 | skipped_fast |
| XRPUSDT | IDLE | 1.06 | 1.86 | 1.67 | -0.03 | 37074601.91 | 0.74 | skipped_fast |
| ETHUSDT | IDLE | 1.03 | 1.82 | 1.58 | -0.02 | 243011667.44 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.8 | 1.46 | 1.0 | -0.0 | 384067044.49 | 0.0 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 3.34 | 5.99 | 5.44 | -0.07 | 885266.07 | 4.57 | skipped_fast |
| CCUSDT | IDLE | 1.93 | 3.75 | 2.09 | -0.03 | 439362.84 | 9.8 | skipped_fast |
| REDUSDT | IDLE | 1.31 | 4.48 | 4.21 | -0.07 | 225838.65 | 14.37 | skipped_fast |
| HBARUSDT | IDLE | 1.19 | 2.79 | 2.61 | -0.07 | 522817.05 | 6.94 | skipped_fast |
| ZBCNUSDT | IDLE | 1.29 | 2.27 | 2.05 | -0.04 | 217139.58 | 16.07 | skipped_fast |
| EDELUSDT | IDLE | 0.79 | 2.94 | 2.15 | -0.13 | 274504.86 | 15.23 | skipped_fast |
| CHIPUSDT | IDLE | 1.17 | 4.62 | 4.07 | -0.11 | 139462.06 | 13.7 | skipped_fast |
| BIOUSDT | IDLE | 1.41 | 4.18 | 3.55 | -0.07 | 73076.46 | 3.64 | skipped_fast |
| KITEUSDT | IDLE | 1.41 | 3.43 | 2.75 | -0.04 | 66526.57 | 8.72 | skipped_fast |
| RWAINCUSDT | IDLE | 1.15 | 2.93 | 1.61 | 0.05 | 42957.09 | 9.65 | skipped_fast |
| RIZEUSDT | IDLE | 1.24 | 7.45 | 5.05 | -0.11 | 63928.39 | 87.9 | skipped_fast |
| TELUSDT | IDLE | 1.61 | 2.82 | 2.63 | -0.02 | 102517.5 | 22.98 | skipped_fast |
| FLUIDUSDT | IDLE | 1.49 | 2.97 | 2.58 | 0.02 | 14754.65 | 21.63 | skipped_fast |
| MNSRYUSDT | IDLE | 1.03 | 2.0 | 0.44 | -0.01 | 38749.89 | 18.01 | skipped_fast |
| RWAUSDT | IDLE | 0.16 | 0.31 | 0.08 | 0.0 | 53261.6 | 7.71 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
