# Hulk DIGEST — 2026-09-12T04:22:03Z

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
| XRPUSDT | IDLE | 0.58 | 1.25 | 0.2 | 0.01 | 52441114.1 | 2.2 | n/a |
| BTCUSDT | IDLE | 0.18 | 0.34 | 0.2 | 0.0 | 544192042.68 | 0.0 | no_map |
| ETHUSDT | IDLE | 0.16 | 0.34 | 0.29 | 0.02 | 631056853.23 | 1.47 | no_map |
| PYTHUSDT | IDLE | 2.14 | 4.44 | 0.08 | 0.03 | 423357.51 | 1.9 | tvl≈114,190,097 |
| CCUSDT | IDLE | 1.96 | 3.68 | 1.63 | -0.0 | 413908.92 | 9.13 | no_map |
| WUSDT | IDLE | 1.5 | 3.08 | 0.65 | 0.01 | 198514.24 | 8.18 | tvl≈1,482,838,769 |
| ZBCNUSDT | IDLE | 1.4 | 2.64 | 1.1 | -0.01 | 191572.19 | 12.85 | n/a |
| REDUSDT | IDLE | 1.69 | 4.21 | 3.44 | 0.04 | 65144.14 | 18.84 | tvl≈2,375,899 |
| BIOUSDT | IDLE | 1.52 | 2.94 | 0.7 | 0.01 | 81581.13 | 7.88 | n/a |
| KITEUSDT | IDLE | 0.8 | 1.4 | 1.38 | -0.01 | 58889.64 | 7.44 | no_map |
| RIZEUSDT | IDLE | 0.08 | 5.87 | 0.98 | 0.7 | 196419.72 | 98.98 | no_map |
| HBARUSDT | IDLE | 0.51 | 0.97 | 0.33 | -0.01 | 254998.65 | 1.34 | empty_tvl |
| TELUSDT | IDLE | 1.1 | 2.3 | 2.02 | -0.02 | 100861.44 | 17.66 | no_map |
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
