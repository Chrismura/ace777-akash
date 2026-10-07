# Hulk DIGEST — 2026-10-07T10:07:51Z

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
| QNTUSDT | IDLE | 2.29 | 5.82 | 5.12 | -0.04 | 2651703.97 | 12.74 | skipped_fast |
| XRPUSDT | IDLE | 1.08 | 1.91 | 1.62 | -0.03 | 41069778.37 | 2.06 | skipped_fast |
| ETHUSDT | IDLE | 0.67 | 1.17 | 1.1 | -0.04 | 499826794.2 | 0.15 | skipped_fast |
| BTCUSDT | IDLE | 0.48 | 0.86 | 0.7 | -0.03 | 759079161.21 | 0.0 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 3.44 | 6.06 | 5.48 | -0.05 | 498651.57 | 9.38 | skipped_fast |
| PYTHUSDT | IDLE | 0.65 | 2.02 | 1.43 | -0.08 | 1119869.82 | 1.38 | skipped_fast |
| KITEUSDT | IDLE | 3.04 | 5.58 | 3.36 | -0.03 | 63308.89 | 9.56 | skipped_fast |
| HBARUSDT | IDLE | 1.3 | 2.35 | 1.69 | -0.06 | 717187.49 | 4.22 | skipped_fast |
| ZBCNUSDT | IDLE | 2.08 | 4.39 | 4.14 | -0.04 | 234227.47 | 22.51 | skipped_fast |
| CCUSDT | IDLE | 1.0 | 2.23 | 2.14 | -0.08 | 453713.74 | 9.34 | skipped_fast |
| CHIPUSDT | IDLE | 1.51 | 4.42 | 3.32 | -0.07 | 201634.9 | 14.25 | skipped_fast |
| EDELUSDT | IDLE | 0.52 | 2.9 | 2.15 | -0.19 | 454961.12 | 29.49 | skipped_fast |
| RWAINCUSDT | IDLE | 2.35 | 7.28 | 2.23 | -0.02 | 50006.26 | 52.82 | skipped_fast |
| REDUSDT | IDLE | 0.88 | 2.46 | 1.34 | -0.09 | 61739.61 | 7.33 | skipped_fast |
| BIOUSDT | IDLE | 0.66 | 2.47 | 2.18 | -0.11 | 88392.74 | 3.48 | skipped_fast |
| RIZEUSDT | IDLE | 0.63 | 3.74 | 3.28 | 0.04 | 81182.99 | 36.06 | skipped_fast |
| TELUSDT | IDLE | 0.83 | 3.5 | 1.81 | 0.1 | 197709.54 | 33.97 | skipped_fast |
| RWAUSDT | IDLE | 0.82 | 1.43 | 1.34 | -0.03 | 52340.86 | 7.53 | skipped_fast |
| FLUIDUSDT | IDLE | 0.65 | 2.04 | 0.48 | -0.06 | 31112.5 | 58.34 | skipped_fast |
| MNSRYUSDT | IDLE | 0.42 | 0.73 | 0.73 | -0.01 | 39519.61 | 66.45 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
