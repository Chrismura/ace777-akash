# Hulk DIGEST — 2026-09-19T14:01:57Z

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
| XRPUSDT | IDLE | 1.48 | 2.87 | 0.58 | 0.06 | 68272097.91 | 0.69 | skipped_fast |
| ETHUSDT | IDLE | 0.65 | 1.18 | 0.81 | 0.03 | 502333109.67 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.22 | 0.4 | 0.22 | 0.01 | 594748627.58 | 0.0 | skipped_fast |
| WUSDT | IDLE | 2.01 | 5.55 | 0.58 | 0.1 | 1050943.41 | 2.64 | skipped_fast |
| PYTHUSDT | IDLE | 1.19 | 2.26 | 0.85 | 0.02 | 681534.48 | 6.61 | skipped_fast |
| BIOUSDT | IDLE | 3.33 | 6.31 | 2.39 | 0.05 | 87550.41 | 10.66 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 3.79 | 6.64 | 6.23 | -0.01 | 5195.72 | 66.61 | skipped_fast |
| HBARUSDT | IDLE | 1.63 | 3.15 | 0.7 | 0.04 | 577777.35 | 1.23 | skipped_fast |
| CCUSDT | IDLE | 0.98 | 1.87 | 0.55 | 0.02 | 381435.03 | 10.78 | skipped_fast |
| CHIPUSDT | IDLE | 1.95 | 4.85 | 2.85 | 0.03 | 141488.42 | 22.56 | skipped_fast |
| EDELUSDT | IDLE | 1.31 | 7.9 | 1.95 | -0.1 | 192951.37 | 9.45 | skipped_fast |
| ZBCNUSDT | IDLE | 1.69 | 3.28 | 0.73 | 0.02 | 184124.82 | 13.39 | skipped_fast |
| KITEUSDT | IDLE | 1.4 | 2.57 | 1.51 | 0.04 | 71833.89 | 11.21 | skipped_fast |
| REDUSDT | IDLE | 0.54 | 2.44 | 0.92 | 0.06 | 131893.13 | 6.0 | skipped_fast |
| TELUSDT | IDLE | 1.78 | 5.11 | 4.36 | -0.02 | 125664.51 | 19.82 | skipped_fast |
| QNTUSDT | IDLE | 1.38 | 2.68 | 0.47 | 0.03 | 69719.35 | 1.53 | skipped_fast |
| FLUIDUSDT | IDLE | 1.2 | 4.33 | 0.18 | 0.15 | 10866.91 | 22.2 | skipped_fast |
| RIZEUSDT | IDLE | 0.31 | 2.55 | 1.86 | -0.08 | 41280.64 | 94.72 | skipped_fast |
| MNSRYUSDT | IDLE | 0.84 | 1.52 | 1.11 | 0.01 | 37971.51 | 49.03 | skipped_fast |
| RWAUSDT | IDLE | 0.58 | 1.11 | 0.29 | 0.0 | 55324.98 | 29.28 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
