# Hulk DIGEST — 2026-08-22T10:19:07Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 3.74 | 16.77 | 11.53 | 0.0 | 51600516.77 | 4.13 | tvl≈113,478,518 |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.9 | 23.87 | 13.71 | 0.05 | 216020272.17 | 3.41 | n/a |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.43 | 15.8 | 11.36 | 0.01 | 1246330.64 | 1.3 | empty_tvl |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.06 | 22.93 | 13.17 | -0.12 | 664523.01 | 13.72 | no_map |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.19 | 16.84 | 10.31 | 0.01 | 594981.83 | 13.91 | tvl≈1,583,490,295 |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.23 | 29.98 | 11.61 | -0.04 | 236141.41 | 13.09 | n/a |
| CCUSDT | IDLE | 2.25 | 11.25 | 8.45 | 0.11 | 820311.14 | 8.74 | no_map |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 2.86 | 37.92 | 11.58 | 0.04 | 155602.0 | 11.78 | tvl≈2,081,438 |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.39 | 8.58 | 7.73 | -0.02 | 429104.21 | 14.33 | n/a |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 4.21 | 9.28 | 6.05 | 0.03 | 73005.83 | 12.11 | no_map |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 3.1 | 9.75 | 7.01 | -0.01 | 189389.06 | 7.89 | n/a |
| EDELUSDT | IDLE | 2.71 | 4.76 | 4.43 | -0.04 | 79046.03 | 33.92 | no_map |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.16 | 7.96 | 7.27 | -0.04 | 168734.28 | 26.69 | no_map |
| QAITUSDT | IDLE | 1.66 | 2.91 | 2.68 | -0.02 | 3175.19 | 67.05 | no_map |
| RIZEUSDT | IDLE | 0.76 | 3.18 | 1.84 | -0.0 | 49218.9 | 45.14 | no_map |
| RWAINCUSDT | IDLE | 1.21 | 2.11 | 2.07 | 0.01 | 11436.39 | 75.72 | no_map |
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
