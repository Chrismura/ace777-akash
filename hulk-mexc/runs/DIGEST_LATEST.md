# Hulk DIGEST — 2026-09-17T06:15:59Z

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
| XRPUSDT | IDLE | 0.82 | 1.49 | 1.06 | 0.0 | 55183627.33 | 3.08 | n/a |
| ETHUSDT | IDLE | 0.68 | 1.33 | 0.2 | 0.02 | 386920871.01 | 0.61 | no_map |
| BTCUSDT | IDLE | 0.47 | 0.89 | 0.38 | 0.01 | 508454835.3 | 0.0 | no_map |
| PYTHUSDT | IDLE | 2.39 | 4.56 | 1.42 | 0.02 | 532388.56 | 3.68 | tvl≈121,075,024 |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.73 | 10.83 | 8.0 | -0.07 | 217706.03 | 36.89 | no_map |
| CCUSDT | IDLE | 1.1 | 4.07 | 1.77 | 0.08 | 575927.51 | 10.18 | no_map |
| ZBCNUSDT | IDLE | 2.29 | 4.35 | 1.53 | 0.03 | 172582.59 | 13.8 | n/a |
| RIZEUSDT | IDLE | 1.72 | 16.51 | 11.58 | -0.03 | 61290.09 | 69.09 | no_map |
| WUSDT | IDLE | 1.63 | 3.06 | 1.43 | 0.03 | 222518.96 | 14.11 | tvl≈1,452,358,498 |
| CHIPUSDT | IDLE | 1.97 | 4.33 | 2.9 | -0.02 | 79302.91 | 16.46 | no_map |
| REDUSDT | IDLE | 1.59 | 2.93 | 1.7 | -0.01 | 60523.64 | 0.76 | tvl≈2,354,127 |
| KITEUSDT | IDLE | 1.27 | 4.65 | 0.86 | 0.07 | 67305.72 | 12.92 | no_map |
| BIOUSDT | IDLE | 0.89 | 1.59 | 1.22 | 0.02 | 77932.34 | 3.97 | n/a |
| HBARUSDT | IDLE | 0.77 | 1.38 | 1.03 | -0.01 | 317891.28 | 1.36 | empty_tvl |
| RWAINCUSDT | IDLE | 0.89 | 1.7 | 0.52 | -0.01 | 16388.57 | 57.87 | no_map |
| TELUSDT | IDLE | 0.87 | 1.53 | 1.44 | -0.03 | 115861.89 | 41.81 | no_map |
| QNTUSDT | IDLE | 0.78 | 1.42 | 1.0 | 0.01 | 37734.54 | 1.65 | n/a |
| MNSRYUSDT | IDLE | 0.48 | 0.95 | 0.03 | 0.01 | 36228.03 | 9.83 | no_map |
| RWAUSDT | IDLE | 0.51 | 0.98 | 0.22 | 0.02 | 55659.74 | 44.88 | no_map |
| FLUIDUSDT | IDLE | 0.0 | 0.0 | 0.0 | -0.02 | 1571.52 | 21.96 | tvl≈2,645,899,710 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
