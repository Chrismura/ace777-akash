# Hulk DIGEST — 2026-09-01T09:23:37Z

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
| XRPUSDT | IDLE | 1.45 | 2.56 | 2.2 | -0.01 | 29246279.12 | 2.2 | skipped_fast |
| BTCUSDT | IDLE | 1.04 | 1.83 | 1.6 | -0.01 | 560209427.13 | 0.0 | skipped_fast |
| ETHUSDT | IDLE | 1.03 | 1.85 | 1.46 | 0.0 | 300370355.37 | 0.04 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 4.22 | 27.96 | 18.26 | -0.02 | 174798.43 | 109.29 | skipped_fast |
| PYTHUSDT | IDLE | 2.36 | 5.72 | 3.93 | 0.04 | 555167.5 | 2.03 | skipped_fast |
| CHIPUSDT | IDLE | 2.8 | 6.71 | 2.76 | -0.02 | 338428.44 | 2.53 | skipped_fast |
| CCUSDT | IDLE | 2.06 | 3.63 | 3.32 | 0.01 | 383754.4 | 7.51 | skipped_fast |
| REDUSDT | IDLE | 3.31 | 6.17 | 2.95 | -0.0 | 59498.22 | 10.03 | skipped_fast |
| WUSDT | IDLE | 1.81 | 3.35 | 1.78 | 0.03 | 237313.26 | 11.56 | skipped_fast |
| RWAUSDT | WATCH_PULLBACK — tension haute + reflux | 2.9 | 8.68 | 7.77 | 0.05 | 64449.05 | 15.35 | skipped_fast |
| ZBCNUSDT | IDLE | 1.45 | 2.59 | 2.12 | 0.02 | 189699.65 | 14.08 | skipped_fast |
| BIOUSDT | IDLE | 1.68 | 2.97 | 2.58 | -0.03 | 62594.52 | 7.69 | skipped_fast |
| KITEUSDT | IDLE | 1.47 | 2.66 | 1.89 | -0.02 | 61401.88 | 12.73 | skipped_fast |
| RIZEUSDT | IDLE | 1.54 | 5.19 | 2.11 | -0.07 | 37825.1 | 71.63 | skipped_fast |
| RWAINCUSDT | IDLE | 1.43 | 2.62 | 1.62 | -0.04 | 5056.65 | 41.16 | skipped_fast |
| HBARUSDT | IDLE | 1.12 | 1.99 | 1.65 | -0.0 | 221716.58 | 1.35 | skipped_fast |
| TELUSDT | IDLE | 1.43 | 2.52 | 2.23 | -0.01 | 84132.26 | 17.55 | skipped_fast |
| QNTUSDT | IDLE | 0.79 | 1.41 | 1.2 | 0.0 | 49847.96 | 3.28 | skipped_fast |
| MNSRYUSDT | IDLE | 0.4 | 0.72 | 0.57 | 0.0 | 28974.01 | 36.57 | skipped_fast |
| FLUIDUSDT | IDLE | 0.0 | 0.0 | 0.0 | -0.01 | 1146.31 | 21.39 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
