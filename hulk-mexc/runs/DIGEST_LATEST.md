# Hulk DIGEST — 2026-09-11T02:17:33Z

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
| XRPUSDT | IDLE | 1.11 | 2.07 | 0.99 | -0.03 | 41242176.01 | 1.49 | n/a |
| ETHUSDT | IDLE | 0.63 | 1.2 | 0.43 | -0.0 | 420189685.81 | 0.33 | no_map |
| BTCUSDT | IDLE | 0.56 | 1.05 | 0.48 | -0.01 | 533191301.59 | 0.0 | no_map |
| CHIPUSDT | IDLE | 4.01 | 9.46 | 3.69 | -0.01 | 99983.16 | 26.96 | no_map |
| PYTHUSDT | IDLE | 1.66 | 2.94 | 2.55 | -0.01 | 418544.1 | 1.95 | tvl≈115,944,061 |
| CCUSDT | IDLE | 1.24 | 2.24 | 2.12 | -0.06 | 471853.06 | 8.21 | no_map |
| ZBCNUSDT | IDLE | 2.06 | 3.79 | 2.16 | -0.01 | 205400.25 | 25.54 | n/a |
| RIZEUSDT | IDLE | 0.96 | 53.98 | 6.25 | -0.33 | 142394.41 | 296.4 | no_map |
| EDELUSDT | IDLE | 1.39 | 5.24 | 4.44 | -0.06 | 219496.73 | 27.89 | no_map |
| WUSDT | IDLE | 1.17 | 2.17 | 1.16 | -0.03 | 166939.09 | 13.61 | tvl≈1,478,466,089 |
| KITEUSDT | IDLE | 1.11 | 2.08 | 0.87 | -0.02 | 57261.29 | 11.93 | no_map |
| BIOUSDT | IDLE | 1.01 | 1.91 | 0.76 | -0.01 | 77781.36 | 28.13 | n/a |
| REDUSDT | IDLE | 0.74 | 1.32 | 1.07 | -0.05 | 60096.19 | 19.04 | tvl≈2,196,395 |
| RWAINCUSDT | IDLE | 0.64 | 1.24 | 0.28 | 0.0 | 4220.66 | 11.18 | no_map |
| TELUSDT | IDLE | 1.73 | 3.08 | 2.55 | -0.02 | 88488.99 | 51.18 | no_map |
| HBARUSDT | IDLE | 0.9 | 1.67 | 0.91 | -0.01 | 185217.12 | 1.33 | empty_tvl |
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
