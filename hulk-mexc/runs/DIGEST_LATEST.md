# Hulk DIGEST — 2026-08-31T21:19:38Z

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
| XRPUSDT | IDLE | 1.11 | 2.05 | 1.07 | -0.01 | 37643038.51 | 1.45 | n/a |
| ETHUSDT | IDLE | 0.62 | 1.14 | 0.71 | -0.0 | 421049519.93 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.5 | 0.93 | 0.53 | 0.0 | 616428308.41 | 0.0 | no_map |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.52 | 23.11 | 16.02 | -0.03 | 172326.33 | 42.11 | no_map |
| PYTHUSDT | IDLE | 2.9 | 5.95 | 0.91 | 0.01 | 429533.31 | 2.04 | tvl≈106,417,148 |
| CCUSDT | IDLE | 3.04 | 7.08 | 1.38 | 0.04 | 351443.26 | 9.71 | no_map |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.06 | 7.3 | 5.17 | -0.08 | 32395.69 | 66.4 | no_map |
| CHIPUSDT | IDLE | 1.03 | 2.82 | 1.58 | -0.01 | 384296.73 | 2.58 | no_map |
| ZBCNUSDT | IDLE | 1.67 | 3.25 | 0.66 | 0.0 | 206781.43 | 16.36 | n/a |
| WUSDT | IDLE | 0.71 | 1.31 | 0.7 | -0.02 | 210357.91 | 2.19 | tvl≈1,522,253,737 |
| KITEUSDT | IDLE | 1.1 | 2.08 | 0.86 | -0.04 | 97374.12 | 13.49 | no_map |
| TELUSDT | IDLE | 2.7 | 5.25 | 1.02 | 0.01 | 88523.71 | 51.5 | no_map |
| BIOUSDT | IDLE | 0.91 | 1.64 | 1.2 | -0.03 | 67299.58 | 3.79 | n/a |
| REDUSDT | IDLE | 0.89 | 1.57 | 1.42 | -0.03 | 64949.72 | 12.37 | tvl≈1,971,683 |
| HBARUSDT | IDLE | 0.83 | 1.5 | 1.09 | -0.02 | 271822.89 | 1.36 | empty_tvl |
| RWAINCUSDT | IDLE | 1.34 | 2.49 | 1.3 | -0.02 | 2921.26 | 97.67 | no_map |
| RWAUSDT | IDLE | 1.52 | 3.37 | 2.52 | 0.06 | 57869.08 | 30.46 | no_map |
| FLUIDUSDT | IDLE | 1.26 | 2.23 | 1.87 | -0.01 | 1900.26 | 16.14 | tvl≈2,616,991,103 |
| QNTUSDT | IDLE | 0.65 | 1.2 | 0.68 | 0.01 | 52775.89 | 4.89 | n/a |
| MNSRYUSDT | IDLE | 0.52 | 1.04 | 0.01 | 0.0 | 25512.93 | 4.02 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
