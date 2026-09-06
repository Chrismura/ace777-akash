# Hulk DIGEST — 2026-09-06T08:46:00Z

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
| XRPUSDT | IDLE | 0.92 | 1.65 | 1.23 | 0.01 | 25224141.18 | 1.41 | n/a |
| ETHUSDT | IDLE | 0.89 | 1.61 | 1.16 | 0.02 | 225910865.47 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.35 | 0.65 | 0.4 | 0.0 | 397843572.1 | 0.0 | no_map |
| PYTHUSDT | IDLE | 2.72 | 4.86 | 3.85 | 0.03 | 426766.0 | 1.82 | tvl≈123,301,040 |
| ZBCNUSDT | IDLE | 2.1 | 4.19 | 0.03 | 0.02 | 229150.26 | 37.09 | n/a |
| CCUSDT | IDLE | 0.95 | 1.72 | 1.26 | 0.01 | 294830.89 | 9.13 | no_map |
| BIOUSDT | IDLE | 1.54 | 2.76 | 2.12 | 0.0 | 93959.24 | 3.62 | n/a |
| WUSDT | IDLE | 1.17 | 2.13 | 1.43 | 0.02 | 174603.8 | 9.95 | tvl≈1,663,427,099 |
| HBARUSDT | IDLE | 1.17 | 2.1 | 1.59 | 0.02 | 454323.97 | 1.24 | empty_tvl |
| RIZEUSDT | IDLE | 1.39 | 7.62 | 6.44 | 0.03 | 95148.46 | 60.59 | no_map |
| REDUSDT | IDLE | 1.28 | 2.55 | 0.13 | 0.01 | 63968.06 | 10.92 | tvl≈2,329,432 |
| KITEUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| TELUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| CHIPUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| RWAINCUSDT | ERR | — | — | — | — | — | — | scan_deadline |
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
