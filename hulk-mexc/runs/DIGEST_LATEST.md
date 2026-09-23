# Hulk DIGEST — 2026-09-23T23:24:15Z

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
| PYTHUSDT | IDLE | 1.26 | 3.93 | 2.88 | -0.07 | 1584528.18 | 1.6 | tvl≈140,680,403 |
| XRPUSDT | IDLE | 0.76 | 2.19 | 0.77 | -0.05 | 110522131.5 | 2.67 | n/a |
| ETHUSDT | IDLE | 0.77 | 1.47 | 0.49 | -0.03 | 467172425.28 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.34 | 0.65 | 0.26 | -0.02 | 830605578.47 | 0.0 | no_map |
| HBARUSDT | IDLE | 0.47 | 1.56 | 0.58 | -0.09 | 1302894.88 | 1.1 | empty_tvl |
| CCUSDT | IDLE | 1.01 | 2.45 | 0.59 | -0.06 | 541541.6 | 5.49 | no_map |
| WUSDT | IDLE | 1.04 | 2.91 | 1.77 | -0.09 | 380816.38 | 5.34 | tvl≈1,705,960,536 |
| EDELUSDT | IDLE | 1.42 | 3.95 | 2.3 | -0.07 | 167439.54 | 21.39 | no_map |
| ZBCNUSDT | IDLE | 1.0 | 2.58 | 1.01 | 0.01 | 239917.94 | 17.78 | n/a |
| KITEUSDT | IDLE | 1.22 | 2.62 | 0.14 | -0.04 | 174074.78 | 9.75 | no_map |
| CHIPUSDT | IDLE | 0.83 | 2.86 | 1.13 | -0.11 | 216633.36 | 19.05 | no_map |
| REDUSDT | IDLE | 1.31 | 2.62 | 2.08 | -0.05 | 59324.81 | 14.54 | tvl≈2,756,399 |
| BIOUSDT | IDLE | 0.77 | 2.04 | 0.81 | -0.06 | 94149.45 | 3.54 | n/a |
| RWAINCUSDT | IDLE | 0.71 | 1.31 | 0.7 | -0.01 | 19061.32 | 54.17 | no_map |
| TELUSDT | IDLE | 1.0 | 2.89 | 0.52 | -0.06 | 155552.75 | 28.83 | no_map |
| RIZEUSDT | IDLE | 0.87 | 4.32 | 1.82 | 0.02 | 65305.06 | 170.62 | no_map |
| QNTUSDT | IDLE | 0.6 | 1.39 | 0.88 | -0.04 | 131305.46 | 1.41 | n/a |
| RWAUSDT | IDLE | 1.01 | 1.96 | 0.37 | -0.03 | 56064.31 | 7.42 | no_map |
| FLUIDUSDT | IDLE | 0.91 | 2.08 | 0.21 | -0.04 | 5789.95 | 21.37 | tvl≈2,617,543,872 |
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
