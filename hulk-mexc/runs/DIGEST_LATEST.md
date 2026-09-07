# Hulk DIGEST — 2026-09-07T17:36:46Z

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
| XRPUSDT | IDLE | 1.36 | 2.55 | 1.2 | -0.01 | 36186185.09 | 0.72 | n/a |
| ETHUSDT | IDLE | 0.97 | 1.79 | 0.96 | -0.0 | 340983029.83 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.64 | 1.18 | 0.67 | -0.01 | 453328825.8 | 0.0 | no_map |
| PYTHUSDT | IDLE | 2.77 | 5.01 | 3.59 | 0.01 | 575073.1 | 1.83 | tvl≈123,730,070 |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 4.14 | 8.56 | 5.27 | -0.04 | 206408.19 | 12.82 | n/a |
| CCUSDT | IDLE | 1.98 | 3.58 | 2.57 | -0.03 | 436682.0 | 9.43 | no_map |
| CHIPUSDT | IDLE | 2.19 | 8.22 | 6.46 | -0.12 | 244003.45 | 13.53 | no_map |
| WUSDT | IDLE | 1.93 | 3.62 | 1.66 | -0.02 | 390351.89 | 3.9 | tvl≈1,582,476,040 |
| HBARUSDT | IDLE | 1.76 | 3.34 | 1.21 | 0.02 | 564627.64 | 1.22 | empty_tvl |
| RIZEUSDT | IDLE | 2.15 | 9.74 | 7.7 | -0.09 | 69893.67 | 66.11 | no_map |
| REDUSDT | IDLE | 2.21 | 4.06 | 2.35 | 0.04 | 64090.36 | 8.33 | tvl≈2,459,669 |
| EDELUSDT | IDLE | 1.98 | 6.26 | 5.02 | -0.05 | 87192.18 | 40.61 | no_map |
| KITEUSDT | IDLE | 2.04 | 3.65 | 2.8 | -0.05 | 59992.91 | 9.19 | no_map |
| BIOUSDT | IDLE | 1.82 | 3.39 | 1.69 | -0.01 | 68128.69 | 7.34 | n/a |
| RWAINCUSDT | IDLE | 1.36 | 4.06 | 3.85 | 0.04 | 5172.42 | 132.65 | no_map |
| QNTUSDT | IDLE | 0.88 | 1.62 | 0.95 | 0.0 | 46630.75 | 3.04 | n/a |
| TELUSDT | IDLE | 0.92 | 1.71 | 0.93 | -0.01 | 114441.21 | 52.8 | no_map |
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
