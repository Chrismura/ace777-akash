# Hulk DIGEST — 2026-09-02T02:30:32Z

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
| XRPUSDT | IDLE | 1.15 | 2.16 | 0.94 | -0.02 | 36944999.13 | 2.23 | n/a |
| ETHUSDT | IDLE | 0.94 | 1.78 | 0.71 | -0.02 | 358027743.16 | 0.91 | no_map |
| BTCUSDT | IDLE | 0.61 | 1.16 | 0.38 | -0.01 | 530302539.46 | 0.0 | no_map |
| PYTHUSDT | IDLE | 2.8 | 8.04 | 3.24 | 0.06 | 663864.8 | 1.9 | tvl≈118,462,197 |
| CHIPUSDT | IDLE | 1.5 | 7.22 | 4.24 | 0.13 | 807999.35 | 2.29 | no_map |
| WUSDT | IDLE | 2.92 | 5.36 | 3.26 | 0.03 | 417319.08 | 10.4 | tvl≈1,495,658,493 |
| ZBCNUSDT | IDLE | 2.22 | 4.69 | 2.24 | -0.02 | 197975.49 | 41.6 | n/a |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.56 | 7.4 | 5.88 | -0.06 | 42688.52 | 78.33 | no_map |
| EDELUSDT | IDLE | 1.03 | 9.32 | 2.09 | -0.01 | 171193.93 | 8.88 | no_map |
| REDUSDT | IDLE | 1.44 | 3.8 | 2.73 | 0.07 | 143711.09 | 21.24 | tvl≈2,106,717 |
| CCUSDT | IDLE | 0.48 | 1.17 | 0.17 | -0.07 | 311615.56 | 8.79 | no_map |
| KITEUSDT | IDLE | 1.25 | 2.37 | 0.83 | 0.04 | 69048.24 | 8.9 | no_map |
| BIOUSDT | IDLE | 1.06 | 1.99 | 0.86 | -0.04 | 70321.55 | 3.94 | n/a |
| RWAINCUSDT | IDLE | 1.33 | 2.48 | 1.21 | 0.01 | 5760.07 | 40.69 | no_map |
| HBARUSDT | IDLE | 1.06 | 1.94 | 1.19 | -0.0 | 255461.73 | 1.36 | empty_tvl |
| QNTUSDT | IDLE | 1.45 | 2.8 | 0.7 | 0.04 | 46927.25 | 4.7 | n/a |
| TELUSDT | IDLE | 1.84 | 3.54 | 1.0 | -0.01 | 92655.55 | 95.12 | no_map |
| FLUIDUSDT | IDLE | 1.17 | 2.04 | 2.0 | -0.06 | 328.66 | 20.42 | tvl≈2,564,851,234 |
| RWAUSDT | IDLE | 0.43 | 1.01 | 0.54 | -0.03 | 58162.48 | 15.4 | no_map |
| MNSRYUSDT | IDLE | 0.39 | 0.7 | 0.49 | -0.02 | 35666.72 | 33.0 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
