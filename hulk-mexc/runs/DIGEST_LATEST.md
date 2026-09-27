# Hulk DIGEST — 2026-09-27T10:07:12Z

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
| WUSDT | IDLE | 2.25 | 14.4 | 3.4 | 0.21 | 2877223.11 | 18.86 | skipped_fast |
| PYTHUSDT | IDLE | 1.82 | 7.12 | 3.49 | 0.14 | 1999294.68 | 1.17 | skipped_fast |
| QNTUSDT | IDLE | 0.78 | 15.7 | 10.52 | 0.58 | 5077145.93 | 13.25 | skipped_fast |
| XRPUSDT | IDLE | 1.22 | 2.38 | 0.37 | -0.0 | 41481202.28 | 0.65 | skipped_fast |
| ETHUSDT | IDLE | 0.69 | 1.3 | 0.48 | 0.01 | 156256281.2 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.36 | 0.72 | 0.04 | 0.01 | 419081137.61 | 0.0 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 4.42 | 16.11 | 11.43 | -0.01 | 49634.57 | 61.68 | skipped_fast |
| CCUSDT | IDLE | 1.46 | 2.86 | 0.35 | 0.01 | 619448.51 | 9.48 | skipped_fast |
| HBARUSDT | IDLE | 1.91 | 3.63 | 1.22 | 0.01 | 629066.38 | 1.06 | skipped_fast |
| EDELUSDT | IDLE | 2.42 | 5.84 | 4.38 | -0.05 | 152009.99 | 24.45 | skipped_fast |
| REDUSDT | IDLE | 2.54 | 4.59 | 3.24 | 0.02 | 64613.47 | 13.94 | skipped_fast |
| ZBCNUSDT | IDLE | 1.53 | 2.93 | 0.9 | 0.0 | 222538.25 | 13.66 | skipped_fast |
| KITEUSDT | IDLE | 1.01 | 3.96 | 3.55 | 0.12 | 168862.46 | 8.67 | skipped_fast |
| BIOUSDT | IDLE | 1.47 | 2.84 | 0.68 | -0.03 | 101088.14 | 3.12 | skipped_fast |
| CHIPUSDT | IDLE | 1.4 | 3.47 | 0.96 | 0.02 | 117181.91 | 18.24 | skipped_fast |
| RWAINCUSDT | IDLE | 1.29 | 5.15 | 1.25 | 0.07 | 8871.06 | 65.18 | skipped_fast |
| RWAUSDT | IDLE | 1.19 | 2.29 | 0.56 | 0.05 | 58307.95 | 7.04 | skipped_fast |
| MNSRYUSDT | IDLE | 0.97 | 1.89 | 0.35 | 0.01 | 39301.57 | 5.05 | skipped_fast |
| TELUSDT | IDLE | 0.8 | 2.78 | 0.79 | 0.09 | 127262.22 | 51.15 | skipped_fast |
| FLUIDUSDT | IDLE | 1.05 | 2.1 | 0.0 | 0.03 | 924.28 | 22.25 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
