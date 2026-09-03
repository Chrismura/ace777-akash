# Hulk DIGEST — 2026-09-03T00:04:12Z

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
| XRPUSDT | IDLE | 0.62 | 1.21 | 0.16 | 0.0 | 35512135.22 | 0.74 | n/a |
| ETHUSDT | IDLE | 0.46 | 0.88 | 0.2 | -0.01 | 345777929.81 | 0.21 | no_map |
| BTCUSDT | IDLE | 0.34 | 0.65 | 0.18 | -0.0 | 496288556.9 | 0.67 | no_map |
| PYTHUSDT | IDLE | 0.85 | 2.78 | 1.47 | 0.11 | 1360672.66 | 1.74 | tvl≈130,283,075 |
| CHIPUSDT | IDLE | 1.08 | 4.27 | 0.75 | -0.03 | 919587.92 | 7.03 | no_map |
| ZBCNUSDT | IDLE | 2.88 | 6.9 | 0.87 | -0.01 | 179075.32 | 21.11 | n/a |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.54 | 25.82 | 9.42 | 0.18 | 55233.36 | 154.87 | no_map |
| CCUSDT | IDLE | 1.17 | 2.1 | 1.6 | -0.04 | 433646.47 | 9.15 | no_map |
| WUSDT | IDLE | 1.74 | 3.2 | 1.85 | 0.01 | 227863.78 | 6.19 | tvl≈1,490,908,476 |
| BIOUSDT | IDLE | 1.88 | 3.59 | 1.15 | 0.01 | 70730.95 | 7.78 | n/a |
| EDELUSDT | IDLE | 1.44 | 5.58 | 3.8 | 0.09 | 148813.12 | 34.42 | no_map |
| KITEUSDT | IDLE | 1.2 | 5.59 | 1.13 | 0.15 | 141017.99 | 10.56 | no_map |
| RWAINCUSDT | IDLE | 2.17 | 6.33 | 1.37 | 0.1 | 11608.2 | 53.08 | no_map |
| REDUSDT | IDLE | 0.88 | 1.61 | 0.95 | -0.0 | 112836.45 | 12.19 | tvl≈2,119,727 |
| QNTUSDT | IDLE | 1.15 | 2.2 | 0.72 | 0.01 | 60619.92 | 4.65 | n/a |
| HBARUSDT | IDLE | 0.57 | 1.15 | 0.0 | 0.01 | 191927.5 | 1.34 | empty_tvl |
| TELUSDT | IDLE | 0.84 | 1.6 | 0.52 | 0.03 | 75027.61 | 40.92 | no_map |
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
