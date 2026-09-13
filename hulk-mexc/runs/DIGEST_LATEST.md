# Hulk DIGEST — 2026-09-13T00:32:35Z

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
| ETHUSDT | IDLE | 0.27 | 0.52 | 0.12 | 0.0 | 199970484.31 | 0.04 | no_map |
| XRPUSDT | IDLE | 0.24 | 0.46 | 0.08 | 0.01 | 14612190.01 | 2.2 | n/a |
| BTCUSDT | IDLE | 0.16 | 0.31 | 0.04 | 0.0 | 311158407.88 | 0.0 | no_map |
| PYTHUSDT | IDLE | 1.2 | 2.59 | 1.83 | 0.08 | 413435.91 | 1.82 | tvl≈123,388,794 |
| ZBCNUSDT | IDLE | 1.85 | 5.39 | 3.02 | -0.02 | 226959.26 | 22.09 | n/a |
| EDELUSDT | IDLE | 1.82 | 4.25 | 1.31 | 0.08 | 167764.88 | 8.26 | no_map |
| WUSDT | IDLE | 1.81 | 3.27 | 2.4 | 0.03 | 175449.4 | 11.04 | tvl≈1,470,326,377 |
| CCUSDT | IDLE | 1.03 | 1.97 | 0.55 | 0.0 | 212227.73 | 6.12 | no_map |
| RWAINCUSDT | IDLE | 2.12 | 4.25 | 1.55 | 0.02 | 9700.96 | 43.72 | no_map |
| CHIPUSDT | IDLE | 1.2 | 2.42 | 1.15 | 0.02 | 76798.93 | 16.61 | no_map |
| RIZEUSDT | IDLE | 0.59 | 9.83 | 8.35 | 0.38 | 92009.54 | 57.7 | no_map |
| KITEUSDT | IDLE | 0.98 | 1.88 | 0.56 | -0.01 | 62322.2 | 12.09 | no_map |
| REDUSDT | IDLE | 0.87 | 1.71 | 0.24 | 0.03 | 56485.73 | 16.73 | tvl≈2,353,648 |
| BIOUSDT | IDLE | 0.5 | 0.95 | 0.35 | 0.01 | 65637.09 | 7.85 | n/a |
| HBARUSDT | IDLE | 0.51 | 1.01 | 0.07 | 0.0 | 133617.09 | 1.34 | empty_tvl |
| TELUSDT | IDLE | 0.75 | 1.34 | 1.02 | -0.04 | 88938.45 | 24.29 | no_map |
| QNTUSDT | IDLE | 0.61 | 1.2 | 0.17 | 0.01 | 35028.63 | 7.78 | n/a |
| FLUIDUSDT | IDLE | 0.74 | 1.34 | 0.91 | 0.02 | 1701.62 | 22.17 | tvl≈2,678,580,809 |
| RWAUSDT | IDLE | 0.25 | 0.45 | 0.3 | 0.0 | 53499.32 | 7.44 | no_map |
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
