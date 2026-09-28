# Hulk DIGEST — 2026-09-28T00:14:18Z

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
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 3.08 | 103.66 | 17.11 | 1.05 | 14739645.86 | 15.56 | skipped_fast |
| PYTHUSDT | IDLE | 2.18 | 4.8 | 3.15 | 0.03 | 2279813.03 | 14.3 | skipped_fast |
| WUSDT | IDLE | 1.24 | 6.47 | 2.83 | 0.2 | 5162641.36 | 9.53 | skipped_fast |
| XRPUSDT | IDLE | 1.31 | 2.38 | 1.66 | -0.01 | 42972595.0 | 1.98 | skipped_fast |
| ETHUSDT | IDLE | 0.57 | 1.07 | 0.5 | -0.0 | 209500686.83 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.46 | 0.83 | 0.55 | 0.0 | 414715418.83 | 0.0 | skipped_fast |
| CCUSDT | IDLE | 1.61 | 2.98 | 1.58 | 0.01 | 639322.85 | 9.5 | skipped_fast |
| ZBCNUSDT | IDLE | 2.84 | 5.08 | 4.01 | -0.02 | 217185.57 | 22.87 | skipped_fast |
| HBARUSDT | IDLE | 1.41 | 2.76 | 0.34 | 0.03 | 808751.53 | 1.04 | skipped_fast |
| RIZEUSDT | IDLE | 1.82 | 17.0 | 9.62 | -0.21 | 58467.47 | 42.57 | skipped_fast |
| EDELUSDT | IDLE | 1.83 | 8.75 | 6.15 | -0.15 | 144560.19 | 51.41 | skipped_fast |
| CHIPUSDT | IDLE | 1.88 | 3.74 | 1.74 | -0.04 | 98667.06 | 12.81 | skipped_fast |
| RWAINCUSDT | IDLE | 1.15 | 11.59 | 3.96 | 0.22 | 29875.27 | 4.0 | skipped_fast |
| KITEUSDT | IDLE | 1.42 | 2.57 | 2.42 | -0.01 | 110945.85 | 9.96 | skipped_fast |
| REDUSDT | IDLE | 1.59 | 2.87 | 2.08 | 0.01 | 66161.87 | 7.06 | skipped_fast |
| BIOUSDT | IDLE | 1.18 | 2.26 | 0.62 | -0.0 | 82380.21 | 3.14 | skipped_fast |
| TELUSDT | IDLE | 0.84 | 2.8 | 0.69 | 0.11 | 176400.71 | 32.28 | skipped_fast |
| FLUIDUSDT | IDLE | 1.5 | 2.99 | 0.0 | 0.05 | 2779.76 | 21.21 | skipped_fast |
| RWAUSDT | IDLE | 0.44 | 0.78 | 0.71 | 0.01 | 59704.23 | 14.23 | skipped_fast |
| MNSRYUSDT | IDLE | 0.21 | 0.41 | 0.09 | 0.01 | 39716.26 | 3.79 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
