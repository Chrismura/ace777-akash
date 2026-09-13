# Hulk DIGEST — 2026-09-13T00:38:02Z

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
| ETHUSDT | IDLE | 0.27 | 0.52 | 0.09 | 0.01 | 199367719.31 | 0.04 | no_map |
| XRPUSDT | IDLE | 0.24 | 0.46 | 0.07 | 0.01 | 14557661.31 | 2.2 | n/a |
| BTCUSDT | IDLE | 0.16 | 0.31 | 0.04 | 0.0 | 310605240.95 | 0.0 | no_map |
| PYTHUSDT | IDLE | 1.2 | 2.59 | 1.72 | 0.08 | 414113.97 | 3.64 | tvl≈123,388,794 |
| ZBCNUSDT | IDLE | 1.85 | 5.39 | 3.06 | -0.02 | 227702.15 | 12.47 | n/a |
| WUSDT | IDLE | 1.83 | 3.27 | 2.64 | 0.03 | 175855.41 | 7.03 | tvl≈1,470,326,377 |
| EDELUSDT | IDLE | 1.81 | 4.25 | 1.14 | 0.07 | 167856.43 | 8.25 | no_map |
| RWAINCUSDT | IDLE | 2.12 | 4.25 | 1.55 | 0.02 | 9686.01 | 32.79 | no_map |
| CCUSDT | IDLE | 1.04 | 1.97 | 0.68 | 0.0 | 213030.32 | 9.19 | no_map |
| CHIPUSDT | IDLE | 1.23 | 2.42 | 1.54 | 0.01 | 76844.93 | 14.6 | no_map |
| RIZEUSDT | IDLE | 0.63 | 10.39 | 9.2 | 0.37 | 92116.52 | 69.88 | no_map |
| KITEUSDT | IDLE | 0.98 | 1.88 | 0.56 | -0.01 | 62258.24 | 14.89 | no_map |
| REDUSDT | IDLE | 0.86 | 1.71 | 0.05 | 0.03 | 56471.12 | 18.24 | tvl≈2,353,648 |
| BIOUSDT | IDLE | 0.52 | 0.95 | 0.55 | 0.01 | 65488.45 | 3.93 | n/a |
| HBARUSDT | IDLE | 0.51 | 1.01 | 0.07 | 0.0 | 129900.97 | 1.34 | empty_tvl |
| TELUSDT | IDLE | 0.74 | 1.34 | 0.96 | -0.04 | 89027.23 | 36.41 | no_map |
| QNTUSDT | IDLE | 0.61 | 1.2 | 0.16 | 0.01 | 35078.61 | 4.67 | n/a |
| FLUIDUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| RWAUSDT | ERR | — | — | — | — | — | — | scan_deadline |
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
