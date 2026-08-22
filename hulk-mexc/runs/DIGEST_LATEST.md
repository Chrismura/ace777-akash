# Hulk DIGEST — 2026-08-22T09:39:41Z

> ⚠️ **SCAN DÉGRADÉ (réseau)** — données partielles, veille hors délai.

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : XRPUSDT, HBARUSDT, QAITUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT
- Watch only : QNTUSDT, FLUIDUSDT, RWAUSDT

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.19 | 19.14 | 10.82 | 0.03 | 44014083.32 | 6.02 | tvl≈113,478,518 |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.84 | 23.87 | 11.14 | 0.1 | 218570215.15 | 3.31 | n/a |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.38 | 15.8 | 9.99 | 0.03 | 1292907.6 | 1.28 | empty_tvl |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.31 | 17.58 | 8.84 | 0.03 | 591434.69 | 10.45 | tvl≈1,583,490,295 |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.21 | 29.98 | 10.62 | -0.03 | 237621.41 | 3.23 | n/a |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.09 | 41.27 | 11.14 | 0.06 | 154574.3 | 11.45 | tvl≈2,081,438 |
| CCUSDT | IDLE | 2.22 | 11.25 | 7.45 | 0.13 | 801562.92 | 9.51 | no_map |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.13 | 8.0 | 6.59 | -0.01 | 439708.77 | 17.65 | n/a |
| RIZEUSDT | IDLE | 0.8 | 3.36 | 2.07 | -0.01 | 49370.04 | 22.54 | no_map |
| QAITUSDT | IDLE | 1.54 | 2.91 | 1.09 | 0.01 | 3209.57 | 66.45 | no_map |
| KITEUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| TELUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| CHIPUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| RWAINCUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| EDELUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| QNTUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| FLUIDUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| RWAUSDT | ERR | — | — | — | — | — | — | scan_deadline |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
