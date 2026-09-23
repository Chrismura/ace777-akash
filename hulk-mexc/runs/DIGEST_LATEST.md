# Hulk DIGEST — 2026-09-23T14:08:26Z

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
| PYTHUSDT | IDLE | 2.32 | 4.12 | 3.45 | -0.04 | 1637406.5 | 3.02 | tvl≈150,045,080 |
| XRPUSDT | IDLE | 1.72 | 3.15 | 1.88 | 0.0 | 116838046.77 | 2.54 | n/a |
| HBARUSDT | IDLE | 2.59 | 4.6 | 4.19 | -0.03 | 1644554.7 | 1.07 | empty_tvl |
| ETHUSDT | IDLE | 0.76 | 1.34 | 1.16 | -0.01 | 417994645.19 | 1.55 | no_map |
| BTCUSDT | IDLE | 0.46 | 0.85 | 0.44 | -0.01 | 837476972.33 | 0.11 | no_map |
| WUSDT | IDLE | 2.15 | 3.75 | 3.61 | 0.0 | 383990.29 | 5.85 | tvl≈1,769,454,895 |
| ZBCNUSDT | IDLE | 2.36 | 5.63 | 3.45 | 0.01 | 241188.15 | 10.73 | n/a |
| CCUSDT | IDLE | 1.4 | 2.46 | 2.24 | -0.05 | 418183.43 | 5.41 | no_map |
| EDELUSDT | IDLE | 1.52 | 5.57 | 4.46 | -0.11 | 218467.1 | 23.81 | no_map |
| KITEUSDT | IDLE | 1.64 | 3.03 | 1.62 | 0.03 | 151347.93 | 11.01 | no_map |
| CHIPUSDT | IDLE | 1.61 | 3.05 | 1.1 | -0.01 | 190707.04 | 28.52 | no_map |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.72 | 7.77 | 6.5 | 0.03 | 157098.58 | 57.94 | no_map |
| REDUSDT | IDLE | 1.78 | 3.12 | 2.98 | 0.03 | 59593.13 | 15.11 | tvl≈2,919,731 |
| BIOUSDT | IDLE | 1.34 | 2.5 | 1.15 | 0.03 | 124155.43 | 10.02 | n/a |
| QNTUSDT | IDLE | 2.14 | 3.88 | 2.69 | 0.02 | 183108.3 | 5.44 | n/a |
| RWAINCUSDT | IDLE | 0.62 | 1.36 | 0.91 | 0.02 | 19475.93 | 5.37 | no_map |
| RIZEUSDT | IDLE | 0.19 | 2.79 | 2.36 | 0.54 | 62275.43 | 32.31 | no_map |
| FLUIDUSDT | IDLE | 1.06 | 1.85 | 1.82 | -0.0 | 4400.09 | 22.12 | tvl≈2,635,729,572 |
| RWAUSDT | IDLE | 0.46 | 0.8 | 0.79 | 0.0 | 54451.18 | 7.26 | no_map |
| MNSRYUSDT | IDLE | 0.68 | 1.24 | 0.77 | -0.0 | 40731.65 | 50.31 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
