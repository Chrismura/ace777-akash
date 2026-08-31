# Hulk DIGEST — 2026-08-31T00:14:56Z

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
| XRPUSDT | IDLE | 3.67 | 6.64 | 4.63 | -0.03 | 31499459.49 | 2.21 | n/a |
| ETHUSDT | IDLE | 2.9 | 5.24 | 3.69 | -0.01 | 346355026.04 | 0.04 | no_map |
| BTCUSDT | IDLE | 1.45 | 2.65 | 1.68 | -0.01 | 351499309.77 | 0.0 | no_map |
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.42 | 8.82 | 6.1 | -0.02 | 484598.91 | 6.35 | tvl≈109,675,290 |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.18 | 7.77 | 5.09 | -0.0 | 236083.15 | 13.19 | tvl≈1,528,741,183 |
| CHIPUSDT | IDLE | 2.11 | 6.49 | 3.81 | -0.05 | 565796.14 | 7.83 | no_map |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.24 | 7.74 | 5.16 | -0.04 | 88974.69 | 3.81 | n/a |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.35 | 7.97 | 6.88 | -0.09 | 88569.47 | 11.0 | no_map |
| CCUSDT | IDLE | 2.37 | 4.26 | 3.25 | -0.03 | 237020.31 | 7.8 | no_map |
| ZBCNUSDT | IDLE | 1.68 | 3.74 | 2.56 | -0.04 | 213120.58 | 9.9 | n/a |
| EDELUSDT | IDLE | 2.39 | 6.05 | 5.7 | 0.06 | 78277.08 | 51.11 | no_map |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.73 | 6.54 | 6.14 | -0.03 | 3712.45 | 21.81 | tvl≈2,625,574,149 |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.35 | 5.92 | 5.2 | 0.01 | 87548.78 | 41.73 | no_map |
| REDUSDT | IDLE | 1.99 | 3.92 | 0.41 | -0.0 | 62746.64 | 10.03 | tvl≈2,002,827 |
| HBARUSDT | IDLE | 2.3 | 4.15 | 3.01 | -0.02 | 213786.37 | 1.35 | empty_tvl |
| RIZEUSDT | IDLE | 1.8 | 5.01 | 2.75 | -0.06 | 43008.78 | 60.19 | no_map |
| RWAINCUSDT | IDLE | 1.65 | 3.05 | 1.64 | 0.02 | 1751.1 | 16.69 | no_map |
| QNTUSDT | IDLE | 2.18 | 4.0 | 2.42 | -0.02 | 38068.13 | 9.93 | n/a |
| MNSRYUSDT | IDLE | 1.06 | 1.87 | 1.6 | -0.01 | 32084.49 | 39.31 | no_map |
| RWAUSDT | IDLE | 0.77 | 1.39 | 1.05 | 0.01 | 52911.26 | 32.52 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
