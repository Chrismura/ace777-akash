# Hulk DIGEST — 2026-09-11T22:21:42Z

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
| RIZEUSDT | IDLE | 1.81 | 124.7 | 44.77 | 0.75 | 225047.16 | 90.79 | skipped_fast |
| ETHUSDT | IDLE | 1.42 | 3.02 | 2.42 | 0.02 | 651254394.39 | 0.28 | skipped_fast |
| XRPUSDT | IDLE | 1.18 | 2.35 | 1.76 | -0.0 | 55363951.9 | 2.22 | skipped_fast |
| BTCUSDT | IDLE | 0.76 | 1.37 | 1.0 | 0.0 | 566148276.15 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 3.0 | 5.57 | 4.49 | -0.03 | 418109.1 | 3.95 | skipped_fast |
| EDELUSDT | IDLE | 3.75 | 10.48 | 4.87 | -0.0 | 166791.69 | 9.0 | skipped_fast |
| WUSDT | IDLE | 2.48 | 4.63 | 4.2 | -0.01 | 199124.53 | 10.45 | skipped_fast |
| CCUSDT | IDLE | 1.26 | 2.28 | 1.64 | -0.02 | 451920.25 | 5.15 | skipped_fast |
| ZBCNUSDT | IDLE | 2.44 | 4.38 | 3.37 | 0.01 | 198443.85 | 21.74 | skipped_fast |
| CHIPUSDT | IDLE | 2.26 | 6.26 | 4.8 | -0.05 | 141786.69 | 15.03 | skipped_fast |
| BIOUSDT | IDLE | 1.77 | 3.19 | 2.27 | -0.0 | 77543.59 | 12.01 | skipped_fast |
| RWAINCUSDT | IDLE | 1.76 | 3.43 | 2.16 | 0.04 | 13792.37 | 5.39 | skipped_fast |
| REDUSDT | IDLE | 1.18 | 2.27 | 0.95 | 0.04 | 63855.28 | 18.9 | skipped_fast |
| HBARUSDT | IDLE | 1.3 | 2.33 | 1.84 | -0.02 | 260380.36 | 1.35 | skipped_fast |
| KITEUSDT | IDLE | 0.72 | 1.35 | 0.55 | -0.01 | 59095.08 | 10.14 | skipped_fast |
| TELUSDT | IDLE | 1.66 | 3.23 | 2.8 | -0.03 | 103617.09 | 28.76 | skipped_fast |
| QNTUSDT | IDLE | 1.35 | 2.38 | 2.13 | -0.02 | 44090.05 | 1.58 | skipped_fast |
| FLUIDUSDT | IDLE | 1.49 | 2.66 | 2.19 | 0.02 | 1301.43 | 21.82 | skipped_fast |
| RWAUSDT | IDLE | 0.48 | 0.9 | 0.37 | 0.02 | 52992.24 | 29.78 | skipped_fast |
| MNSRYUSDT | IDLE | 0.53 | 0.95 | 0.72 | 0.0 | 35932.9 | 30.53 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
