# Hulk DIGEST — 2026-09-13T04:37:54Z

> ⚠️ **SCAN DÉGRADÉ (réseau)** — données partielles, veille hors délai.

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
| XRPUSDT | IDLE | 0.3 | 0.54 | 0.39 | 0.0 | 14141652.85 | 1.47 | n/a |
| ETHUSDT | IDLE | 0.18 | 0.32 | 0.23 | 0.0 | 196222164.29 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.12 | 0.22 | 0.14 | -0.0 | 314309793.93 | 0.0 | no_map |
| RIZEUSDT | IDLE | 2.35 | 40.81 | 23.21 | 0.07 | 95734.9 | 131.8 | no_map |
| PYTHUSDT | IDLE | 1.36 | 2.49 | 1.51 | 0.04 | 419089.17 | 1.82 | tvl≈123,235,422 |
| WUSDT | IDLE | 2.22 | 4.05 | 2.59 | 0.03 | 215493.2 | 12.96 | tvl≈1,463,317,039 |
| RWAINCUSDT | IDLE | 2.46 | 4.7 | 3.28 | 0.03 | 9808.97 | 27.3 | no_map |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 3.29 | 5.83 | 5.03 | -0.0 | 41070.34 | 1.56 | n/a |
| EDELUSDT | IDLE | 1.46 | 3.93 | 0.97 | 0.08 | 175808.09 | 16.23 | no_map |
| REDUSDT | IDLE | 2.05 | 3.97 | 0.85 | 0.05 | 55952.95 | 17.97 | tvl≈2,385,775 |
| ZBCNUSDT | IDLE | 1.18 | 3.73 | 0.04 | 0.0 | 225314.2 | 11.72 | n/a |
| CCUSDT | IDLE | 0.79 | 1.46 | 0.78 | -0.01 | 185855.2 | 8.18 | no_map |
| RWAUSDT | IDLE | 2.68 | 4.77 | 3.91 | 0.0 | 55841.89 | 29.63 | no_map |
| KITEUSDT | IDLE | 1.21 | 2.41 | 0.01 | 0.01 | 64815.05 | 11.96 | no_map |
| CHIPUSDT | IDLE | 1.04 | 1.99 | 1.72 | 0.0 | 78185.26 | 14.76 | no_map |
| BIOUSDT | IDLE | 0.92 | 1.74 | 0.66 | 0.01 | 71228.63 | 7.81 | n/a |
| FLUIDUSDT | IDLE | 2.07 | 4.13 | 0.08 | 0.03 | 536.22 | 21.47 | tvl≈2,678,720,657 |
| HBARUSDT | IDLE | 0.43 | 0.86 | 0.04 | 0.01 | 134286.73 | 1.33 | empty_tvl |
| TELUSDT | IDLE | 0.71 | 1.29 | 0.91 | -0.03 | 91493.34 | 36.63 | no_map |
| MNSRYUSDT | ERR | — | — | — | — | — | — | scan_deadline |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
