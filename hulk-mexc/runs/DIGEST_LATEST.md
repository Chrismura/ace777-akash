# Hulk DIGEST — 2026-10-18T22:10:20Z

> ⚠️ **SCAN DÉGRADÉ (réseau)** — données partielles, veille hors délai.

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
| XRPUSDT | IDLE | 1.53 | 3.02 | 0.31 | 0.0 | 26911276.71 | 1.55 | n/a |
| ETHUSDT | IDLE | 1.45 | 2.87 | 0.26 | 0.0 | 115301309.87 | 0.13 | no_map |
| PYTHUSDT | IDLE | 2.06 | 5.76 | 2.76 | -0.1 | 1492270.5 | 4.09 | tvl≈166,595,289 |
| BTCUSDT | IDLE | 0.61 | 1.21 | 0.09 | 0.0 | 227620292.26 | 0.0 | no_map |
| WUSDT | IDLE | 1.57 | 4.1 | 1.14 | -0.06 | 878407.97 | 15.47 | tvl≈1,511,937,507 |
| HBARUSDT | IDLE | 2.37 | 5.75 | 1.71 | 0.01 | 804283.33 | 7.08 | empty_tvl |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 3.38 | 9.75 | 7.34 | -0.03 | 61812.31 | 10.73 | no_map |
| QNTUSDT | IDLE | 2.06 | 4.8 | 1.64 | -0.04 | 597721.91 | 9.05 | n/a |
| EDELUSDT | IDLE | 1.87 | 4.42 | 2.66 | -0.07 | 248850.33 | 11.55 | no_map |
| CCUSDT | IDLE | 1.61 | 3.11 | 0.79 | -0.04 | 234814.17 | 5.06 | no_map |
| REDUSDT | IDLE | 1.96 | 3.91 | 0.11 | -0.01 | 95647.74 | 16.12 | tvl≈3,355,171 |
| ZBCNUSDT | IDLE | 1.34 | 2.53 | 0.96 | -0.05 | 218679.02 | 22.06 | n/a |
| BIOUSDT | IDLE | 1.5 | 3.05 | 0.3 | -0.04 | 82103.13 | 12.95 | n/a |
| CHIPUSDT | IDLE | 1.3 | 4.12 | 0.49 | -0.06 | 76916.22 | 9.95 | no_map |
| KITEUSDT | IDLE | 1.23 | 2.45 | 0.08 | -0.02 | 65172.12 | 14.1 | no_map |
| RIZEUSDT | IDLE | 0.92 | 4.56 | 4.13 | -0.05 | 58456.38 | 61.82 | no_map |
| FLUIDUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| RWAUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| MNSRYUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| IOTAUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| LAUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| WAXLUSDT | ERR | — | — | — | — | — | — | scan_deadline |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
