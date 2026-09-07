# Hulk DIGEST — 2026-09-07T09:34:09Z

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
| XRPUSDT | IDLE | 1.02 | 1.92 | 0.84 | -0.01 | 31716447.32 | 1.42 | n/a |
| ETHUSDT | IDLE | 0.82 | 1.52 | 0.8 | -0.0 | 308382489.32 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.62 | 1.16 | 0.58 | -0.01 | 415101852.87 | 0.0 | no_map |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 4.53 | 11.2 | 9.89 | -0.07 | 71558.24 | 39.92 | no_map |
| CHIPUSDT | IDLE | 2.49 | 8.18 | 4.49 | -0.07 | 389134.75 | 9.08 | no_map |
| PYTHUSDT | IDLE | 1.6 | 3.07 | 0.87 | 0.01 | 594323.72 | 3.6 | tvl≈123,271,808 |
| WUSDT | IDLE | 1.69 | 3.3 | 0.51 | 0.04 | 457869.12 | 10.53 | tvl≈1,663,589,288 |
| CCUSDT | IDLE | 1.14 | 1.99 | 1.94 | -0.02 | 416322.13 | 6.44 | no_map |
| KITEUSDT | IDLE | 2.32 | 4.14 | 3.37 | -0.05 | 56531.48 | 9.01 | no_map |
| RWAINCUSDT | IDLE | 1.62 | 4.91 | 4.25 | 0.06 | 6671.28 | 9.85 | no_map |
| RIZEUSDT | IDLE | 1.38 | 8.45 | 2.66 | -0.14 | 72408.16 | 38.39 | no_map |
| ZBCNUSDT | IDLE | 0.99 | 1.89 | 0.61 | -0.02 | 158257.4 | 9.64 | n/a |
| REDUSDT | IDLE | 1.41 | 2.76 | 0.44 | 0.01 | 63682.33 | 10.07 | tvl≈2,331,573 |
| BIOUSDT | IDLE | 1.23 | 2.39 | 0.47 | -0.02 | 73749.86 | 3.66 | n/a |
| HBARUSDT | IDLE | 0.97 | 1.81 | 0.9 | -0.01 | 357024.26 | 1.24 | empty_tvl |
| TELUSDT | IDLE | 1.32 | 2.46 | 1.26 | 0.01 | 100322.24 | 58.0 | no_map |
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
