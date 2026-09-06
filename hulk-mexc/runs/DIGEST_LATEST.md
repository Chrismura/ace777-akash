# Hulk DIGEST — 2026-09-06T08:31:07Z

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
| XRPUSDT | IDLE | 0.91 | 1.65 | 1.15 | 0.01 | 25246090.77 | 1.41 | n/a |
| ETHUSDT | IDLE | 0.89 | 1.61 | 1.12 | 0.02 | 225904372.18 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.35 | 0.65 | 0.38 | 0.0 | 391710735.86 | 0.0 | no_map |
| PYTHUSDT | IDLE | 2.72 | 4.86 | 3.9 | 0.03 | 428704.67 | 1.82 | tvl≈123,301,040 |
| CHIPUSDT | IDLE | 1.69 | 3.78 | 1.78 | 0.01 | 372881.88 | 10.26 | no_map |
| ZBCNUSDT | IDLE | 1.84 | 3.64 | 0.31 | 0.01 | 228559.82 | 10.51 | n/a |
| CCUSDT | IDLE | 0.94 | 1.72 | 1.04 | 0.02 | 296534.3 | 6.38 | no_map |
| BIOUSDT | IDLE | 1.54 | 2.76 | 2.19 | 0.0 | 94838.75 | 3.62 | n/a |
| RWAINCUSDT | IDLE | 2.1 | 4.06 | 0.94 | 0.02 | 9468.41 | 21.01 | no_map |
| RIZEUSDT | IDLE | 1.4 | 7.62 | 6.74 | 0.03 | 95175.3 | 65.04 | no_map |
| HBARUSDT | IDLE | 1.17 | 2.1 | 1.54 | 0.02 | 441866.89 | 1.23 | empty_tvl |
| WUSDT | IDLE | 1.12 | 2.13 | 0.76 | 0.02 | 174730.55 | 9.88 | tvl≈1,663,427,099 |
| KITEUSDT | IDLE | 1.53 | 2.68 | 2.54 | -0.03 | 63944.11 | 12.55 | no_map |
| REDUSDT | IDLE | 1.28 | 2.55 | 0.07 | 0.01 | 63719.21 | 12.48 | tvl≈2,329,432 |
| TELUSDT | IDLE | 0.73 | 1.29 | 1.1 | 0.0 | 72422.75 | 40.97 | no_map |
| EDELUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| QNTUSDT | ERR | — | — | — | — | — | — | scan_deadline |
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
