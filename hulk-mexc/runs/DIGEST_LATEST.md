# Hulk DIGEST — 2026-09-25T20:47:47Z

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
| XRPUSDT | IDLE | 1.47 | 2.71 | 1.56 | 0.02 | 116379914.07 | 1.91 | n/a |
| ETHUSDT | IDLE | 0.57 | 1.1 | 0.3 | 0.0 | 333691057.48 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.49 | 0.97 | 0.1 | -0.0 | 703334948.4 | 0.0 | no_map |
| PYTHUSDT | IDLE | 1.7 | 4.66 | 1.05 | 0.09 | 1220802.07 | 5.44 | tvl≈162,005,824 |
| CCUSDT | IDLE | 1.82 | 8.06 | 2.32 | 0.13 | 827892.71 | 10.05 | no_map |
| HBARUSDT | IDLE | 1.83 | 3.62 | 0.32 | 0.03 | 922393.63 | 1.05 | empty_tvl |
| WUSDT | IDLE | 2.18 | 4.31 | 0.32 | 0.05 | 395167.09 | 5.69 | tvl≈1,825,720,930 |
| ZBCNUSDT | IDLE | 1.62 | 3.73 | 2.23 | 0.06 | 248232.45 | 16.02 | n/a |
| QNTUSDT | IDLE | 1.04 | 5.1 | 1.7 | 0.12 | 574650.43 | 3.08 | n/a |
| CHIPUSDT | IDLE | 1.66 | 4.27 | 0.28 | 0.04 | 159451.47 | 10.11 | no_map |
| BIOUSDT | IDLE | 1.47 | 4.42 | 1.17 | 0.06 | 114587.17 | 6.08 | n/a |
| KITEUSDT | IDLE | 1.78 | 3.49 | 0.52 | -0.0 | 79693.07 | 9.75 | no_map |
| EDELUSDT | IDLE | 0.54 | 4.68 | 3.56 | 0.04 | 230238.09 | 6.77 | no_map |
| REDUSDT | IDLE | 1.21 | 3.08 | 0.6 | 0.09 | 136184.32 | 13.17 | tvl≈3,166,960 |
| RIZEUSDT | IDLE | 1.47 | 21.84 | 14.95 | 0.06 | 118658.51 | 250.98 | no_map |
| RWAINCUSDT | IDLE | 0.49 | 1.85 | 0.51 | -0.08 | 17173.74 | 70.81 | no_map |
| FLUIDUSDT | IDLE | 1.24 | 2.46 | 0.16 | 0.03 | 3384.99 | 22.05 | tvl≈2,582,407,344 |
| TELUSDT | IDLE | 1.0 | 1.77 | 1.5 | 0.01 | 115423.3 | 66.81 | no_map |
| MNSRYUSDT | IDLE | 0.75 | 1.37 | 0.81 | 0.02 | 41284.68 | 10.18 | no_map |
| RWAUSDT | IDLE | 0.72 | 1.33 | 0.73 | -0.01 | 54908.37 | 29.43 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
