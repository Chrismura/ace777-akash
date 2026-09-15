# Hulk DIGEST — 2026-09-15T02:44:05Z

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
| XRPUSDT | IDLE | 1.7 | 3.46 | 2.59 | 0.05 | 75185017.6 | 2.8 | n/a |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.2 | 49.04 | 28.97 | 0.19 | 428018.1 | 6.29 | no_map |
| ETHUSDT | IDLE | 1.46 | 2.58 | 2.32 | 0.0 | 447246744.05 | 0.16 | no_map |
| BTCUSDT | IDLE | 0.97 | 1.71 | 1.57 | 0.01 | 549024629.96 | 0.0 | no_map |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 4.0 | 40.02 | 24.41 | -0.12 | 56097.47 | 177.56 | no_map |
| ZBCNUSDT | IDLE | 2.55 | 4.51 | 3.92 | 0.0 | 198779.71 | 19.52 | n/a |
| CCUSDT | IDLE | 2.01 | 3.6 | 2.74 | -0.01 | 312917.44 | 10.41 | no_map |
| PYTHUSDT | IDLE | 1.47 | 2.77 | 1.08 | -0.01 | 375052.62 | 3.54 | tvl≈126,453,821 |
| REDUSDT | IDLE | 2.02 | 7.64 | 0.17 | 0.08 | 167134.52 | 21.89 | tvl≈2,543,172 |
| WUSDT | IDLE | 1.41 | 2.47 | 2.38 | -0.01 | 204805.49 | 17.1 | tvl≈1,474,728,221 |
| KITEUSDT | IDLE | 1.75 | 3.07 | 2.88 | -0.02 | 65743.87 | 12.29 | no_map |
| BIOUSDT | IDLE | 1.41 | 2.46 | 2.36 | 0.01 | 95443.01 | 11.7 | n/a |
| CHIPUSDT | IDLE | 1.45 | 2.9 | 0.71 | -0.01 | 74272.06 | 16.57 | no_map |
| HBARUSDT | IDLE | 1.12 | 2.07 | 1.2 | 0.03 | 363461.42 | 1.28 | empty_tvl |
| TELUSDT | IDLE | 1.7 | 3.81 | 3.55 | 0.03 | 104967.85 | 30.7 | no_map |
| RWAINCUSDT | IDLE | 0.74 | 1.39 | 0.6 | -0.0 | 5751.22 | 5.5 | no_map |
| QNTUSDT | IDLE | 0.8 | 1.58 | 0.17 | 0.02 | 40462.53 | 4.64 | n/a |
| FLUIDUSDT | IDLE | 1.02 | 1.97 | 0.47 | 0.02 | 1473.91 | 21.72 | tvl≈2,672,791,915 |
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
