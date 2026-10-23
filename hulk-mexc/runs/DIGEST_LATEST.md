# Hulk DIGEST — 2026-10-23T14:48:39Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| XRPUSDT | IDLE | 1.0 | 1.88 | 0.77 | -0.01 | 27649201.58 | 2.28 | n/a |
| ETHUSDT | IDLE | 0.82 | 1.6 | 0.33 | -0.0 | 226644341.84 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.6 | 1.15 | 0.32 | -0.0 | 315362780.02 | 0.0 | no_map |
| QNTUSDT | IDLE | 2.61 | 5.34 | 2.33 | -0.05 | 1165744.96 | 2.74 | n/a |
| PYTHUSDT | IDLE | 1.98 | 3.7 | 1.75 | -0.04 | 704607.9 | 2.78 | tvl≈159,559,718 |
| EDELUSDT | IDLE | 2.78 | 5.36 | 1.27 | 0.0 | 468415.93 | 33.85 | no_map |
| WUSDT | IDLE | 1.62 | 3.2 | 0.24 | 0.02 | 620576.41 | 15.53 | tvl≈1,543,023,636 |
| CHIPUSDT | IDLE | 3.1 | 5.95 | 4.14 | 0.01 | 116947.13 | 18.12 | no_map |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.53 | 10.85 | 6.32 | -0.08 | 48562.82 | 63.22 | no_map |
| ZBCNUSDT | IDLE | 1.78 | 3.34 | 2.05 | -0.03 | 178866.62 | 21.91 | n/a |
| RWAINCUSDT | IDLE | 1.9 | 3.48 | 2.11 | 0.01 | 52792.57 | 16.62 | no_map |
| CCUSDT | IDLE | 1.1 | 2.2 | 0.03 | 0.02 | 186230.22 | 8.62 | no_map |
| REDUSDT | IDLE | 1.09 | 2.17 | 0.11 | -0.01 | 76433.13 | 7.81 | tvl≈3,495,614 |
| KITEUSDT | IDLE | 1.1 | 2.02 | 1.24 | 0.0 | 57571.21 | 9.16 | no_map |
| BIOUSDT | IDLE | 1.1 | 2.16 | 0.33 | 0.01 | 59843.32 | 8.34 | n/a |
| HBARUSDT | IDLE | 1.1 | 2.06 | 0.97 | -0.01 | 345418.2 | 6.28 | empty_tvl |
| LAUSDT | IDLE | 1.74 | 3.34 | 0.98 | 0.03 | 57275.96 | 39.01 | no_map |
| WAXLUSDT | IDLE | 1.39 | 2.71 | 0.41 | 0.0 | 57888.52 | 35.15 | no_map |
| FLUIDUSDT | IDLE | 1.42 | 2.57 | 1.77 | -0.03 | 8788.51 | 21.56 | tvl≈2,206,145,802 |
| IOTAUSDT | IDLE | 1.07 | 2.08 | 0.35 | 0.0 | 70789.97 | 19.99 | no_map |
| RWAUSDT | IDLE | 0.4 | 0.79 | 0.08 | 0.01 | 51658.96 | 7.85 | no_map |
| MNSRYUSDT | IDLE | 0.73 | 1.32 | 0.92 | -0.01 | 36571.65 | 74.39 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
