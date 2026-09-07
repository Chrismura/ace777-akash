# Hulk DIGEST — 2026-09-07T07:34:30Z

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
| XRPUSDT | IDLE | 1.24 | 2.17 | 2.03 | -0.01 | 29316622.92 | 1.43 | n/a |
| ETHUSDT | IDLE | 1.15 | 2.02 | 1.93 | -0.0 | 290049298.79 | 1.53 | no_map |
| BTCUSDT | IDLE | 0.73 | 1.28 | 1.17 | -0.0 | 410267945.69 | 0.0 | no_map |
| PYTHUSDT | IDLE | 2.84 | 5.0 | 4.55 | -0.0 | 598714.02 | 12.78 | tvl≈125,195,492 |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 2.61 | 6.59 | 5.95 | -0.04 | 414708.59 | 12.66 | no_map |
| WUSDT | IDLE | 2.27 | 3.98 | 3.78 | 0.01 | 436435.74 | 25.44 | tvl≈1,576,734,545 |
| EDELUSDT | IDLE | 3.82 | 6.92 | 4.77 | -0.01 | 63088.98 | 47.19 | no_map |
| CCUSDT | IDLE | 1.01 | 1.77 | 1.61 | -0.0 | 390696.29 | 10.06 | no_map |
| BIOUSDT | IDLE | 1.43 | 2.49 | 2.42 | -0.02 | 74719.11 | 14.83 | n/a |
| HBARUSDT | IDLE | 1.28 | 2.23 | 2.18 | -0.0 | 381916.73 | 6.22 | empty_tvl |
| RIZEUSDT | IDLE | 1.27 | 8.69 | 2.21 | -0.16 | 70940.39 | 57.53 | no_map |
| KITEUSDT | IDLE | 1.25 | 2.24 | 1.68 | -0.02 | 55916.52 | 12.75 | no_map |
| ZBCNUSDT | IDLE | 0.73 | 1.35 | 0.74 | -0.01 | 141749.4 | 6.46 | n/a |
| RWAINCUSDT | IDLE | 1.76 | 5.5 | 4.51 | 0.07 | 6818.43 | 98.23 | no_map |
| REDUSDT | IDLE | 0.68 | 1.28 | 0.49 | 0.01 | 63005.41 | 10.24 | tvl≈2,349,078 |
| TELUSDT | IDLE | 1.34 | 2.33 | 2.28 | 0.01 | 97256.81 | 29.08 | no_map |
| QNTUSDT | IDLE | 1.01 | 1.77 | 1.73 | 0.0 | 35223.62 | 10.61 | n/a |
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
