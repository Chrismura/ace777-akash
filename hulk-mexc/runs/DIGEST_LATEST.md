# Hulk DIGEST — 2026-10-28T23:37:34Z

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
| XRPUSDT | IDLE | 1.29 | 2.4 | 1.21 | 0.0 | 22742147.7 | 1.51 | n/a |
| ETHUSDT | IDLE | 1.18 | 2.18 | 1.23 | 0.01 | 205657714.93 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.71 | 1.33 | 0.55 | 0.01 | 324794920.47 | 0.06 | no_map |
| PYTHUSDT | IDLE | 3.03 | 5.82 | 1.62 | 0.01 | 445801.7 | 1.36 | tvl≈164,828,368 |
| WUSDT | IDLE | 1.91 | 3.46 | 2.37 | -0.01 | 397308.71 | 16.54 | tvl≈1,537,539,483 |
| CCUSDT | IDLE | 1.61 | 3.76 | 0.96 | 0.03 | 429733.77 | 5.93 | no_map |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.23 | 5.69 | 5.09 | -0.03 | 39311.31 | 35.66 | no_map |
| QNTUSDT | IDLE | 2.55 | 4.96 | 0.92 | 0.01 | 411865.15 | 2.98 | n/a |
| HBARUSDT | IDLE | 1.76 | 3.13 | 2.6 | -0.01 | 551666.32 | 1.33 | empty_tvl |
| ZBCNUSDT | IDLE | 1.44 | 2.72 | 1.04 | 0.02 | 291186.37 | 18.69 | n/a |
| BIOUSDT | IDLE | 2.08 | 3.88 | 1.89 | 0.01 | 88716.3 | 8.75 | n/a |
| CHIPUSDT | IDLE | 0.93 | 4.24 | 1.79 | -0.09 | 235548.96 | 16.23 | no_map |
| RWAINCUSDT | IDLE | 1.49 | 5.17 | 4.92 | -0.07 | 33898.0 | 21.59 | no_map |
| EDELUSDT | IDLE | 1.2 | 2.16 | 1.59 | -0.02 | 174422.4 | 24.85 | no_map |
| KITEUSDT | IDLE | 1.47 | 2.77 | 1.14 | -0.02 | 61615.7 | 12.01 | no_map |
| REDUSDT | IDLE | 1.42 | 2.55 | 1.89 | -0.03 | 56095.92 | 14.54 | tvl≈3,770,013 |
| FLUIDUSDT | IDLE | 1.59 | 2.88 | 2.04 | -0.01 | 9267.8 | 21.45 | tvl≈2,238,378,456 |
| RWAUSDT | IDLE | 0.74 | 1.37 | 0.71 | 0.0 | 54641.7 | 7.99 | no_map |
| MNSRYUSDT | IDLE | 0.26 | 0.51 | 0.0 | 0.01 | 35814.22 | 39.4 | no_map |
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
