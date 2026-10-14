# Hulk DIGEST — 2026-10-14T12:18:01Z

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
| PYTHUSDT | IDLE | 2.93 | 7.43 | 0.68 | 0.02 | 1764410.86 | 1.18 | tvl≈181,249,525 |
| WUSDT | IDLE | 1.56 | 6.53 | 5.53 | -0.14 | 3361299.83 | 11.4 | tvl≈1,650,517,136 |
| ETHUSDT | IDLE | 1.01 | 1.94 | 0.59 | 0.01 | 114097602.54 | 0.04 | no_map |
| XRPUSDT | IDLE | 0.94 | 1.8 | 0.59 | 0.01 | 26495867.28 | 2.9 | n/a |
| BTCUSDT | IDLE | 0.69 | 1.31 | 0.4 | 0.01 | 311559781.42 | 0.0 | no_map |
| QNTUSDT | IDLE | 2.4 | 5.57 | 5.01 | 0.01 | 1469652.44 | 8.29 | n/a |
| CCUSDT | IDLE | 1.34 | 2.45 | 1.85 | -0.05 | 520140.7 | 8.26 | no_map |
| CHIPUSDT | IDLE | 2.66 | 4.99 | 2.15 | -0.02 | 82224.14 | 12.36 | no_map |
| KITEUSDT | IDLE | 2.28 | 6.7 | 4.64 | 0.08 | 79829.22 | 11.07 | no_map |
| REDUSDT | IDLE | 1.73 | 3.17 | 1.92 | 0.03 | 61608.55 | 9.62 | tvl≈3,916,642 |
| EDELUSDT | IDLE | 1.14 | 2.12 | 1.1 | 0.0 | 169778.83 | 14.59 | no_map |
| RIZEUSDT | IDLE | 1.73 | 4.98 | 3.08 | -0.0 | 48113.87 | 56.49 | no_map |
| BIOUSDT | IDLE | 1.33 | 2.47 | 1.33 | 0.02 | 67523.93 | 3.64 | n/a |
| ZBCNUSDT | IDLE | 0.73 | 1.44 | 0.09 | 0.01 | 195668.39 | 18.73 | n/a |
| RWAINCUSDT | IDLE | 1.1 | 2.51 | 2.04 | -0.04 | 34279.71 | 20.83 | no_map |
| HBARUSDT | IDLE | 1.1 | 2.06 | 0.91 | 0.01 | 306998.57 | 2.3 | empty_tvl |
| TELUSDT | IDLE | 0.73 | 1.4 | 0.44 | 0.04 | 108515.48 | 22.23 | no_map |
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
