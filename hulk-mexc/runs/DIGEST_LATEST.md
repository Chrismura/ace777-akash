# Hulk DIGEST — 2026-08-22T12:11:56Z

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
| PYTHUSDT | IDLE | 1.72 | 7.83 | 4.58 | 0.02 | 51609644.36 | 4.07 | tvl≈110,752,782 |
| XRPUSDT | IDLE | 2.49 | 14.26 | 7.1 | 0.11 | 215114502.88 | 2.65 | n/a |
| HBARUSDT | IDLE | 1.27 | 4.63 | 2.46 | 0.02 | 1251315.89 | 5.15 | empty_tvl |
| CCUSDT | IDLE | 1.63 | 8.38 | 4.47 | 0.13 | 774979.58 | 9.35 | no_map |
| WUSDT | IDLE | 1.53 | 6.27 | 3.08 | 0.02 | 578299.74 | 21.03 | tvl≈1,560,017,487 |
| ZBCNUSDT | IDLE | 2.23 | 5.77 | 4.13 | -0.03 | 379150.41 | 37.09 | n/a |
| BIOUSDT | IDLE | 0.77 | 5.65 | 0.82 | -0.02 | 240828.74 | 6.35 | n/a |
| QAITUSDT | IDLE | 2.2 | 4.16 | 1.63 | -0.0 | 2384.15 | 63.29 | no_map |
| REDUSDT | IDLE | 0.47 | 6.02 | 3.1 | 0.02 | 153526.98 | 13.31 | tvl≈2,031,082 |
| RIZEUSDT | IDLE | 0.47 | 1.91 | 0.43 | -0.05 | 48032.53 | 20.52 | no_map |
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
