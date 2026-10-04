# Hulk DIGEST — 2026-10-04T20:58:10Z

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
| QNTUSDT | IDLE | 2.26 | 8.54 | 3.54 | -0.06 | 3409070.83 | 7.56 | n/a |
| BTCUSDT | IDLE | 0.39 | 0.78 | 0.0 | 0.01 | 305225751.7 | 0.0 | no_map |
| XRPUSDT | IDLE | 0.39 | 0.73 | 0.28 | 0.01 | 16533064.85 | 1.99 | n/a |
| ETHUSDT | IDLE | 0.2 | 0.39 | 0.01 | 0.01 | 96759206.11 | 0.04 | no_map |
| WUSDT | IDLE | 1.28 | 3.61 | 3.15 | 0.05 | 1010589.47 | 14.51 | tvl≈1,894,255,419 |
| EDELUSDT | IDLE | 2.68 | 5.62 | 0.4 | 0.06 | 544765.91 | 44.34 | no_map |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 4.55 | 8.68 | 7.98 | -0.05 | 6776.07 | 42.11 | no_map |
| CCUSDT | IDLE | 1.32 | 2.54 | 0.64 | 0.05 | 360260.99 | 10.15 | no_map |
| CHIPUSDT | IDLE | 2.34 | 7.46 | 0.53 | 0.11 | 64968.04 | 12.23 | no_map |
| ZBCNUSDT | IDLE | 1.65 | 3.24 | 0.43 | 0.02 | 223281.93 | 30.14 | n/a |
| PYTHUSDT | IDLE | 0.76 | 1.41 | 0.78 | -0.0 | 328535.68 | 3.86 | tvl≈174,844,306 |
| RIZEUSDT | IDLE | 1.69 | 7.92 | 4.06 | 0.1 | 51389.04 | 32.75 | no_map |
| HBARUSDT | IDLE | 1.14 | 2.15 | 0.85 | 0.01 | 461412.02 | 4.84 | empty_tvl |
| KITEUSDT | IDLE | 0.93 | 1.82 | 1.02 | -0.05 | 84622.15 | 10.2 | no_map |
| BIOUSDT | IDLE | 0.89 | 1.57 | 1.39 | -0.03 | 71073.09 | 3.27 | n/a |
| REDUSDT | IDLE | 0.71 | 1.36 | 0.41 | -0.04 | 66964.99 | 13.29 | tvl≈4,297,958 |
| TELUSDT | IDLE | 1.4 | 2.7 | 0.67 | 0.02 | 143733.47 | 10.37 | no_map |
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
