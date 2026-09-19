# Hulk DIGEST — 2026-09-19T13:58:39Z

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
| XRPUSDT | IDLE | 1.5 | 2.9 | 0.68 | 0.06 | 68575635.97 | 1.39 | skipped_fast |
| ETHUSDT | IDLE | 0.75 | 1.37 | 0.8 | 0.04 | 505705127.76 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.28 | 0.53 | 0.21 | 0.02 | 596845644.54 | 0.0 | skipped_fast |
| WUSDT | IDLE | 2.15 | 5.97 | 0.69 | 0.11 | 1051565.71 | 11.46 | skipped_fast |
| PYTHUSDT | IDLE | 1.53 | 2.93 | 0.83 | 0.02 | 683516.98 | 8.25 | skipped_fast |
| BIOUSDT | IDLE | 3.8 | 7.26 | 2.26 | 0.05 | 87459.67 | 17.75 | skipped_fast |
| HBARUSDT | IDLE | 2.24 | 4.39 | 0.55 | 0.04 | 582227.83 | 1.23 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 3.24 | 5.68 | 5.38 | -0.0 | 5193.19 | 35.91 | skipped_fast |
| EDELUSDT | IDLE | 1.67 | 9.85 | 3.87 | -0.1 | 194571.14 | 37.88 | skipped_fast |
| CCUSDT | IDLE | 1.12 | 2.17 | 0.49 | 0.03 | 381842.16 | 6.29 | skipped_fast |
| CHIPUSDT | IDLE | 1.84 | 4.85 | 3.31 | 0.03 | 141576.15 | 11.33 | skipped_fast |
| ZBCNUSDT | IDLE | 1.7 | 3.28 | 0.78 | 0.01 | 184596.21 | 21.97 | skipped_fast |
| REDUSDT | IDLE | 1.01 | 4.58 | 2.45 | 0.06 | 131818.08 | 8.66 | skipped_fast |
| KITEUSDT | IDLE | 1.41 | 2.57 | 1.64 | 0.04 | 71882.69 | 26.85 | skipped_fast |
| TELUSDT | IDLE | 1.8 | 5.11 | 4.61 | -0.02 | 125561.61 | 39.68 | skipped_fast |
| QNTUSDT | IDLE | 1.73 | 3.4 | 0.4 | 0.03 | 73784.36 | 3.06 | skipped_fast |
| FLUIDUSDT | IDLE | 1.3 | 5.0 | 0.0 | 0.15 | 10856.93 | 21.46 | skipped_fast |
| RIZEUSDT | IDLE | 0.31 | 2.55 | 1.53 | -0.07 | 41279.03 | 94.72 | skipped_fast |
| RWAUSDT | IDLE | 0.6 | 1.18 | 0.07 | 0.0 | 55368.34 | 21.95 | skipped_fast |
| MNSRYUSDT | IDLE | 0.84 | 1.52 | 1.01 | 0.02 | 38008.35 | 49.03 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
