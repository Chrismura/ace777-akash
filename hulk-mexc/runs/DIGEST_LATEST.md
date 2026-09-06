# Hulk DIGEST — 2026-09-06T17:46:08Z

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
| XRPUSDT | IDLE | 1.08 | 2.0 | 1.11 | -0.01 | 25626517.3 | 1.42 | n/a |
| ETHUSDT | IDLE | 0.9 | 1.72 | 0.49 | 0.01 | 245195440.4 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.53 | 1.02 | 0.33 | -0.0 | 369374273.37 | 0.0 | no_map |
| PYTHUSDT | IDLE | 2.63 | 4.73 | 3.56 | -0.01 | 517750.56 | 3.69 | tvl≈123,271,808 |
| CHIPUSDT | IDLE | 2.82 | 5.94 | 2.91 | -0.01 | 426111.78 | 1.72 | no_map |
| WUSDT | IDLE | 2.97 | 6.24 | 0.12 | 0.08 | 291961.25 | 11.26 | tvl≈1,663,589,288 |
| EDELUSDT | IDLE | 2.97 | 5.34 | 3.96 | -0.02 | 62265.71 | 38.42 | no_map |
| CCUSDT | IDLE | 1.2 | 2.2 | 1.39 | -0.01 | 323346.71 | 9.14 | no_map |
| BIOUSDT | IDLE | 1.94 | 3.71 | 1.07 | -0.01 | 93194.45 | 14.45 | n/a |
| RWAINCUSDT | IDLE | 2.05 | 4.5 | 2.1 | 0.07 | 6030.34 | 5.13 | no_map |
| RIZEUSDT | IDLE | 1.74 | 13.25 | 10.14 | -0.19 | 74070.96 | 127.69 | no_map |
| ZBCNUSDT | IDLE | 1.32 | 2.41 | 1.59 | 0.0 | 196140.47 | 30.02 | n/a |
| REDUSDT | IDLE | 1.58 | 2.94 | 1.48 | 0.02 | 63757.22 | 12.55 | tvl≈2,357,164 |
| HBARUSDT | IDLE | 0.96 | 1.73 | 1.3 | -0.01 | 423227.51 | 1.24 | empty_tvl |
| KITEUSDT | IDLE | 0.77 | 1.41 | 0.85 | 0.0 | 60237.72 | 10.27 | no_map |
| TELUSDT | IDLE | 0.77 | 1.53 | 0.12 | 0.0 | 65936.04 | 5.81 | no_map |
| QNTUSDT | IDLE | 0.82 | 1.65 | 0.0 | 0.02 | 37468.73 | 4.55 | n/a |
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
