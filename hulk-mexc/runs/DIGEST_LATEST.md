# Hulk DIGEST — 2026-10-08T16:17:31Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 3.7 | 17.67 | 13.57 | 0.03 | 1714944.54 | 2.69 | tvl≈172,440,163 |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 3.88 | 11.7 | 8.59 | -0.06 | 2301780.95 | 0.87 | n/a |
| WUSDT | IDLE | 1.76 | 12.43 | 9.98 | 0.05 | 4901558.86 | 9.88 | tvl≈1,895,183,033 |
| ETHUSDT | IDLE | 3.14 | 5.54 | 4.97 | -0.06 | 475504684.28 | 0.25 | no_map |
| XRPUSDT | IDLE | 3.0 | 5.37 | 4.2 | -0.06 | 48088043.76 | 2.22 | n/a |
| BTCUSDT | IDLE | 1.35 | 2.39 | 2.1 | -0.03 | 491701598.69 | 0.39 | no_map |
| CCUSDT | WATCH_PULLBACK — tension haute + reflux | 3.94 | 6.96 | 6.13 | -0.05 | 503099.84 | 9.66 | no_map |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 3.49 | 8.29 | 5.48 | -0.04 | 642015.03 | 13.38 | empty_tvl |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 4.19 | 7.4 | 6.58 | -0.06 | 67632.02 | 10.92 | no_map |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 2.93 | 8.22 | 5.66 | -0.08 | 262879.74 | 46.44 | n/a |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.38 | 6.38 | 5.3 | -0.05 | 60835.32 | 9.08 | tvl≈3,761,571 |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 2.9 | 8.78 | 7.15 | -0.07 | 74373.15 | 14.66 | n/a |
| CHIPUSDT | IDLE | 2.25 | 9.96 | 8.47 | -0.07 | 158009.02 | 12.82 | no_map |
| RIZEUSDT | IDLE | 1.65 | 15.64 | 6.09 | 0.04 | 62096.03 | 11.17 | no_map |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.62 | 9.0 | 8.15 | -0.1 | 186184.85 | 16.65 | no_map |
| EDELUSDT | IDLE | 0.77 | 5.42 | 4.61 | -0.15 | 287344.0 | 17.61 | no_map |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 2.84 | 9.49 | 8.67 | -0.05 | 21568.88 | 33.49 | tvl≈2,464,076,388 |
| RWAINCUSDT | IDLE | 1.87 | 6.36 | 4.88 | -0.11 | 41409.48 | 80.08 | no_map |
| RWAUSDT | IDLE | 2.78 | 4.89 | 4.51 | -0.04 | 49511.48 | 23.61 | no_map |
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
