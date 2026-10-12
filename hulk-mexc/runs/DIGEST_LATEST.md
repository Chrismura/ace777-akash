# Hulk DIGEST — 2026-10-12T07:17:45Z

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
| WUSDT | IDLE | 1.83 | 35.96 | 4.01 | 0.67 | 11130774.28 | 10.43 | tvl≈1,708,740,074 |
| ETHUSDT | IDLE | 0.78 | 1.51 | 0.27 | 0.03 | 229487838.06 | 0.04 | no_map |
| XRPUSDT | IDLE | 0.71 | 1.35 | 0.41 | 0.01 | 21684975.98 | 2.12 | n/a |
| BTCUSDT | IDLE | 0.5 | 0.98 | 0.17 | 0.01 | 184216230.47 | 0.0 | no_map |
| PYTHUSDT | IDLE | 2.95 | 6.39 | 3.41 | 0.03 | 1030029.82 | 1.24 | tvl≈178,653,493 |
| QNTUSDT | IDLE | 2.11 | 3.95 | 1.75 | 0.01 | 751304.17 | 1.67 | n/a |
| CHIPUSDT | IDLE | 2.61 | 7.92 | 4.96 | -0.01 | 221236.16 | 15.64 | no_map |
| ZBCNUSDT | IDLE | 2.67 | 5.36 | 2.02 | 0.06 | 274843.04 | 26.78 | n/a |
| REDUSDT | IDLE | 3.49 | 7.82 | 1.32 | 0.07 | 55372.24 | 16.43 | tvl≈3,801,937 |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.5 | 16.43 | 5.11 | 0.14 | 46815.64 | 78.39 | no_map |
| CCUSDT | IDLE | 1.19 | 2.28 | 0.7 | 0.06 | 420819.95 | 7.92 | no_map |
| EDELUSDT | IDLE | 1.71 | 3.12 | 1.98 | -0.05 | 287213.42 | 13.29 | no_map |
| HBARUSDT | IDLE | 1.05 | 1.96 | 0.97 | 0.03 | 420905.62 | 5.3 | empty_tvl |
| KITEUSDT | IDLE | 1.19 | 2.14 | 1.64 | 0.01 | 62334.21 | 10.16 | no_map |
| BIOUSDT | IDLE | 0.94 | 1.69 | 1.23 | -0.0 | 99698.57 | 3.36 | n/a |
| RWAINCUSDT | IDLE | 1.05 | 2.95 | 2.03 | -0.01 | 21339.04 | 20.2 | no_map |
| TELUSDT | IDLE | 1.46 | 2.75 | 1.08 | -0.02 | 175666.81 | 17.28 | no_map |
| MNSRYUSDT | IDLE | 0.78 | 1.37 | 1.27 | 0.01 | 36163.5 | 6.83 | no_map |
| FLUIDUSDT | IDLE | 0.27 | 2.09 | 0.43 | 0.05 | 66396.41 | 18.6 | tvl≈2,435,222,347 |
| RWAUSDT | IDLE | 0.16 | 0.31 | 0.08 | 0.03 | 52780.43 | 15.44 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
