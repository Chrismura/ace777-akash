# Hulk DIGEST — 2026-09-15T03:35:04Z

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
| XRPUSDT | IDLE | 1.45 | 2.87 | 2.2 | 0.03 | 75233517.99 | 2.82 | skipped_fast |
| ETHUSDT | IDLE | 1.35 | 2.4 | 2.04 | -0.0 | 449981776.54 | 0.04 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.26 | 49.04 | 25.09 | 0.21 | 443613.82 | 53.36 | skipped_fast |
| BTCUSDT | IDLE | 0.82 | 1.46 | 1.26 | 0.0 | 505768390.78 | 0.0 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.96 | 40.02 | 20.87 | -0.08 | 58547.94 | 53.67 | skipped_fast |
| ZBCNUSDT | IDLE | 2.55 | 4.51 | 3.97 | 0.02 | 196074.09 | 11.72 | skipped_fast |
| REDUSDT | IDLE | 2.24 | 8.27 | 4.18 | 0.05 | 171023.37 | 15.22 | skipped_fast |
| PYTHUSDT | IDLE | 1.52 | 2.77 | 1.82 | -0.01 | 353175.37 | 3.56 | skipped_fast |
| CCUSDT | IDLE | 1.64 | 2.98 | 1.98 | -0.0 | 307987.17 | 1.04 | skipped_fast |
| WUSDT | IDLE | 1.62 | 2.88 | 2.34 | -0.02 | 206577.96 | 15.2 | skipped_fast |
| KITEUSDT | IDLE | 1.77 | 3.16 | 2.56 | -0.02 | 65635.82 | 14.17 | skipped_fast |
| BIOUSDT | IDLE | 1.42 | 2.51 | 2.18 | -0.01 | 97729.08 | 11.74 | skipped_fast |
| CHIPUSDT | IDLE | 1.45 | 2.8 | 1.43 | -0.02 | 73658.04 | 14.32 | skipped_fast |
| HBARUSDT | IDLE | 0.98 | 1.75 | 1.37 | 0.02 | 364874.06 | 1.29 | skipped_fast |
| RWAINCUSDT | IDLE | 0.74 | 1.39 | 0.6 | -0.0 | 5610.91 | 5.5 | skipped_fast |
| TELUSDT | IDLE | 1.34 | 3.03 | 2.52 | 0.03 | 104687.96 | 55.44 | skipped_fast |
| FLUIDUSDT | IDLE | 1.18 | 2.06 | 1.94 | 0.0 | 1691.35 | 21.75 | skipped_fast |
| RWAUSDT | IDLE | 0.51 | 0.9 | 0.81 | -0.01 | 54783.3 | 22.36 | skipped_fast |
| QNTUSDT | IDLE | 0.4 | 0.79 | 0.05 | 0.02 | 40247.21 | 4.63 | skipped_fast |
| MNSRYUSDT | IDLE | 0.53 | 0.97 | 0.62 | 0.01 | 33503.72 | 35.95 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
