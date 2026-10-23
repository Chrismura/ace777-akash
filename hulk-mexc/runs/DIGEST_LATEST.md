# Hulk DIGEST — 2026-10-23T09:46:08Z

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
| XRPUSDT | IDLE | 0.59 | 1.06 | 0.85 | -0.0 | 25686478.26 | 1.52 | n/a |
| ETHUSDT | IDLE | 0.49 | 0.89 | 0.55 | -0.0 | 231943617.03 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.28 | 0.51 | 0.35 | -0.0 | 346567215.34 | 0.0 | no_map |
| WUSDT | IDLE | 2.41 | 4.27 | 3.68 | -0.01 | 687177.78 | 13.41 | tvl≈1,552,016,052 |
| PYTHUSDT | IDLE | 1.96 | 3.51 | 2.74 | -0.03 | 652711.01 | 4.18 | tvl≈162,477,830 |
| ZBCNUSDT | IDLE | 3.63 | 8.19 | 3.99 | -0.01 | 172890.16 | 4.5 | n/a |
| EDELUSDT | IDLE | 1.58 | 2.99 | 2.56 | -0.06 | 403236.9 | 22.14 | no_map |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.75 | 11.91 | 8.92 | -0.1 | 45204.9 | 65.33 | no_map |
| QNTUSDT | IDLE | 1.98 | 3.52 | 2.89 | -0.05 | 535219.12 | 2.7 | n/a |
| CHIPUSDT | IDLE | 2.16 | 4.25 | 2.26 | 0.05 | 130484.52 | 17.65 | no_map |
| HBARUSDT | IDLE | 1.84 | 3.25 | 2.9 | -0.02 | 309361.0 | 13.87 | empty_tvl |
| CCUSDT | IDLE | 0.83 | 1.46 | 1.36 | -0.02 | 211282.37 | 8.78 | no_map |
| RWAINCUSDT | IDLE | 1.25 | 2.3 | 1.32 | 0.02 | 50235.66 | 16.68 | no_map |
| REDUSDT | IDLE | 0.98 | 1.73 | 1.59 | -0.01 | 82575.82 | 7.85 | tvl≈3,537,570 |
| BIOUSDT | IDLE | 0.68 | 1.22 | 0.91 | 0.01 | 59226.4 | 4.19 | n/a |
| KITEUSDT | IDLE | 0.56 | 1.05 | 0.41 | 0.0 | 57442.1 | 9.16 | no_map |
| WAXLUSDT | IDLE | 1.76 | 3.13 | 2.54 | -0.03 | 56937.3 | 61.16 | no_map |
| LAUSDT | IDLE | 0.9 | 1.7 | 0.72 | -0.0 | 53853.3 | 19.91 | no_map |
| FLUIDUSDT | IDLE | 1.04 | 1.95 | 1.91 | -0.05 | 9555.94 | 21.14 | tvl≈2,210,434,474 |
| IOTAUSDT | IDLE | 0.73 | 1.3 | 1.02 | -0.01 | 66057.59 | 24.58 | no_map |
| RWAUSDT | IDLE | 0.8 | 1.51 | 0.63 | 0.0 | 52596.15 | 55.14 | no_map |
| MNSRYUSDT | IDLE | 0.32 | 0.63 | 0.0 | 0.0 | 38064.7 | 65.78 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
