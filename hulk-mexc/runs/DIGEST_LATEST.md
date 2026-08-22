# Hulk DIGEST — 2026-08-22T11:04:03Z

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
| PYTHUSDT | IDLE | 2.2 | 9.66 | 8.23 | -0.0 | 51655472.92 | 4.16 | tvl≈113,478,518 |
| XRPUSDT | IDLE | 2.35 | 14.26 | 8.91 | 0.07 | 218267586.39 | 2.7 | n/a |
| CCUSDT | IDLE | 2.05 | 10.24 | 7.71 | 0.11 | 816725.98 | 6.92 | no_map |
| HBARUSDT | IDLE | 1.47 | 5.26 | 3.76 | 0.0 | 1247791.06 | 3.89 | empty_tvl |
| WUSDT | IDLE | 1.57 | 6.27 | 4.01 | 0.01 | 595008.26 | 9.56 | tvl≈1,583,490,295 |
| ZBCNUSDT | IDLE | 1.99 | 5.08 | 4.18 | -0.03 | 424449.54 | 19.06 | n/a |
| CHIPUSDT | IDLE | 0.74 | 4.16 | 2.48 | -0.1 | 647173.81 | 3.38 | no_map |
| EDELUSDT | IDLE | 2.76 | 4.93 | 3.93 | -0.04 | 78989.53 | 45.4 | no_map |
| BIOUSDT | IDLE | 0.96 | 6.64 | 3.81 | -0.06 | 240740.64 | 6.54 | n/a |
| KITEUSDT | IDLE | 1.91 | 4.3 | 2.18 | 0.03 | 73277.52 | 11.89 | no_map |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.64 | 6.75 | 5.41 | -0.04 | 169154.51 | 58.81 | no_map |
| REDUSDT | IDLE | 0.48 | 6.02 | 4.15 | 0.03 | 153985.73 | 9.89 | tvl≈2,031,082 |
| QAITUSDT | IDLE | 1.82 | 3.41 | 1.47 | 0.01 | 2418.23 | 67.45 | no_map |
| RWAINCUSDT | IDLE | 1.31 | 2.29 | 2.24 | 0.0 | 11326.93 | 59.83 | no_map |
| QNTUSDT | IDLE | 1.1 | 3.47 | 2.45 | -0.01 | 189171.98 | 6.28 | n/a |
| RIZEUSDT | IDLE | 0.68 | 2.89 | 1.33 | -0.0 | 49225.43 | 46.66 | no_map |
| FLUIDUSDT | IDLE | 1.87 | 3.68 | 1.96 | -0.01 | 5711.25 | 22.43 | tvl≈2,553,890,177 |
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
