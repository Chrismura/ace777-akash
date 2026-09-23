# Hulk DIGEST — 2026-09-23T20:23:46Z

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
| XRPUSDT | IDLE | 1.33 | 3.46 | 2.89 | -0.05 | 112961330.36 | 1.34 | n/a |
| ETHUSDT | IDLE | 0.95 | 1.85 | 0.39 | -0.03 | 501147060.48 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.79 | 1.5 | 0.49 | -0.02 | 844134071.54 | 0.0 | no_map |
| PYTHUSDT | IDLE | 1.98 | 6.48 | 2.48 | -0.05 | 1329816.43 | 3.2 | tvl≈140,236,528 |
| HBARUSDT | IDLE | 1.13 | 3.63 | 1.95 | -0.1 | 1418447.81 | 1.11 | empty_tvl |
| CCUSDT | IDLE | 1.35 | 3.32 | 0.51 | -0.04 | 534649.61 | 5.51 | no_map |
| WUSDT | IDLE | 1.74 | 4.4 | 4.02 | -0.06 | 395444.72 | 6.25 | tvl≈1,705,410,028 |
| REDUSDT | IDLE | 2.29 | 4.34 | 4.1 | -0.04 | 58999.34 | 14.58 | tvl≈2,756,399 |
| BIOUSDT | IDLE | 1.96 | 5.04 | 2.8 | -0.04 | 95693.98 | 10.66 | n/a |
| ZBCNUSDT | IDLE | 1.44 | 3.75 | 1.1 | 0.01 | 230083.98 | 19.69 | n/a |
| RIZEUSDT | IDLE | 1.3 | 11.55 | 9.3 | 0.27 | 73488.97 | 97.05 | no_map |
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
