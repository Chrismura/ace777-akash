# Hulk DIGEST — 2026-09-02T22:01:01Z

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
| XRPUSDT | IDLE | 1.15 | 2.2 | 0.6 | -0.0 | 36245002.09 | 0.74 | n/a |
| ETHUSDT | IDLE | 0.71 | 1.33 | 0.6 | -0.01 | 356483606.59 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.42 | 0.79 | 0.37 | 0.0 | 508159029.01 | 0.0 | no_map |
| PYTHUSDT | IDLE | 0.71 | 2.49 | 1.14 | 0.13 | 1342232.42 | 6.92 | tvl≈129,737,310 |
| CHIPUSDT | IDLE | 1.55 | 6.16 | 0.94 | -0.05 | 984550.73 | 4.72 | no_map |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.01 | 29.91 | 15.72 | 0.09 | 49463.6 | 95.08 | no_map |
| ZBCNUSDT | IDLE | 2.89 | 6.93 | 0.78 | -0.03 | 184328.98 | 3.89 | n/a |
| WUSDT | IDLE | 2.12 | 4.07 | 1.13 | 0.0 | 248821.29 | 19.47 | tvl≈1,495,758,034 |
| CCUSDT | IDLE | 1.1 | 2.02 | 1.16 | -0.03 | 410126.45 | 9.1 | no_map |
| KITEUSDT | IDLE | 1.67 | 7.81 | 2.07 | 0.18 | 140229.65 | 9.08 | no_map |
| BIOUSDT | IDLE | 1.98 | 3.59 | 2.46 | 0.0 | 68741.66 | 7.89 | n/a |
| RWAINCUSDT | IDLE | 2.1 | 6.05 | 0.79 | 0.1 | 10828.71 | 26.57 | no_map |
| EDELUSDT | IDLE | 1.12 | 5.93 | 4.36 | 0.07 | 161615.14 | 34.42 | no_map |
| REDUSDT | IDLE | 1.04 | 1.85 | 1.57 | 0.0 | 113438.44 | 20.11 | tvl≈2,123,536 |
| QNTUSDT | IDLE | 1.95 | 3.44 | 3.13 | 0.0 | 61623.89 | 14.09 | n/a |
| HBARUSDT | IDLE | 0.74 | 1.46 | 0.19 | -0.0 | 181665.92 | 1.35 | empty_tvl |
| TELUSDT | IDLE | 1.45 | 2.66 | 1.61 | 0.03 | 75641.83 | 41.02 | no_map |
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
