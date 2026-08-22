# Hulk DIGEST — 2026-08-22T11:33:19Z

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
| PYTHUSDT | IDLE | 2.18 | 9.66 | 7.58 | 0.0 | 51632579.76 | 2.07 | tvl≈110,752,782 |
| XRPUSDT | IDLE | 2.33 | 14.26 | 8.27 | 0.07 | 217479439.9 | 0.67 | n/a |
| CCUSDT | IDLE | 2.04 | 10.24 | 7.37 | 0.11 | 808215.0 | 7.76 | no_map |
| HBARUSDT | IDLE | 1.46 | 5.26 | 3.26 | 0.01 | 1259826.21 | 9.04 | empty_tvl |
| WUSDT | IDLE | 1.56 | 6.27 | 3.96 | 0.01 | 590470.6 | 12.76 | tvl≈1,560,017,487 |
| ZBCNUSDT | IDLE | 2.3 | 5.93 | 4.5 | -0.03 | 393977.12 | 42.36 | n/a |
| CHIPUSDT | IDLE | 0.73 | 4.16 | 2.08 | -0.1 | 636335.14 | 6.74 | no_map |
| BIOUSDT | IDLE | 0.94 | 6.64 | 2.83 | -0.05 | 237331.57 | 3.23 | n/a |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.66 | 6.75 | 5.76 | -0.04 | 167924.19 | 32.17 | no_map |
| KITEUSDT | IDLE | 1.82 | 4.3 | 0.72 | 0.03 | 73553.98 | 13.51 | no_map |
| QAITUSDT | IDLE | 2.16 | 4.16 | 1.12 | 0.01 | 2502.14 | 67.45 | no_map |
| REDUSDT | IDLE | 0.48 | 6.02 | 4.33 | 0.04 | 155196.44 | 12.58 | tvl≈2,031,082 |
| RIZEUSDT | IDLE | 0.67 | 2.89 | 0.95 | -0.03 | 48705.06 | 46.44 | no_map |
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
