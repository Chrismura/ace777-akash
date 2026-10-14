# Hulk DIGEST — 2026-10-14T15:21:44Z

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
| PYTHUSDT | IDLE | 2.37 | 5.34 | 4.09 | 0.01 | 2117726.57 | 6.09 | tvl≈189,914,482 |
| WUSDT | IDLE | 1.92 | 7.54 | 5.66 | -0.14 | 3345971.04 | 8.48 | tvl≈1,606,189,286 |
| XRPUSDT | IDLE | 2.37 | 4.24 | 3.35 | -0.02 | 40277710.74 | 1.5 | n/a |
| ETHUSDT | IDLE | 2.35 | 4.22 | 3.14 | -0.03 | 183858695.8 | 0.37 | no_map |
| BTCUSDT | IDLE | 1.53 | 2.71 | 2.27 | -0.02 | 409026796.12 | 0.22 | no_map |
| QNTUSDT | IDLE | 1.94 | 4.8 | 2.06 | 0.01 | 1515449.56 | 6.74 | n/a |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.86 | 22.88 | 17.4 | -0.04 | 64171.31 | 50.78 | no_map |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 4.0 | 7.17 | 5.48 | -0.05 | 187945.25 | 12.7 | n/a |
| CCUSDT | IDLE | 1.54 | 3.9 | 3.36 | -0.09 | 467055.56 | 7.66 | no_map |
| CHIPUSDT | IDLE | 2.88 | 5.67 | 4.65 | -0.06 | 80913.54 | 14.68 | no_map |
| HBARUSDT | IDLE | 2.3 | 4.11 | 3.21 | -0.03 | 460709.73 | 7.11 | empty_tvl |
| BIOUSDT | IDLE | 2.63 | 4.67 | 3.92 | -0.03 | 68631.66 | 3.78 | n/a |
| KITEUSDT | IDLE | 2.28 | 6.33 | 5.23 | 0.03 | 85786.39 | 10.76 | no_map |
| EDELUSDT | IDLE | 1.98 | 3.57 | 2.64 | -0.02 | 150751.61 | 14.87 | no_map |
| REDUSDT | IDLE | 2.12 | 3.88 | 2.41 | 0.01 | 59886.33 | 7.22 | tvl≈3,792,735 |
| RWAINCUSDT | IDLE | 1.61 | 5.32 | 3.51 | -0.08 | 32440.6 | 48.17 | no_map |
| FLUIDUSDT | IDLE | 2.49 | 7.33 | 4.76 | 0.05 | 16099.48 | 17.08 | tvl≈2,361,823,346 |
| TELUSDT | IDLE | 2.41 | 4.39 | 2.82 | -0.0 | 111964.75 | 57.01 | no_map |
| RWAUSDT | IDLE | 1.31 | 2.31 | 2.02 | -0.03 | 56548.26 | 7.93 | no_map |
| MNSRYUSDT | IDLE | 0.63 | 1.13 | 0.82 | -0.01 | 39348.2 | 54.83 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
