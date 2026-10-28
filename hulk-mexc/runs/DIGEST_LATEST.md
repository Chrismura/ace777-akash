# Hulk DIGEST — 2026-10-28T15:40:05Z

> ⚠️ **SCAN DÉGRADÉ (réseau)** — données partielles, veille hors délai.

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| ETHUSDT | IDLE | 1.24 | 2.21 | 1.78 | -0.01 | 223246950.18 | 0.04 | no_map |
| XRPUSDT | IDLE | 0.99 | 1.76 | 1.49 | -0.01 | 19225905.27 | 2.29 | n/a |
| BTCUSDT | IDLE | 0.82 | 1.46 | 1.23 | 0.0 | 294672057.35 | 0.0 | no_map |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.45 | 13.96 | 10.38 | -0.06 | 185406.51 | 17.55 | no_map |
| CCUSDT | IDLE | 4.2 | 9.68 | 3.3 | 0.01 | 375579.1 | 21.69 | no_map |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 3.4 | 7.89 | 7.32 | 0.01 | 41043.34 | 6.7 | no_map |
| WUSDT | IDLE | 1.44 | 2.74 | 0.99 | -0.04 | 506515.16 | 17.25 | tvl≈1,497,982,251 |
| QNTUSDT | IDLE | 2.87 | 5.16 | 3.82 | -0.01 | 422555.43 | 2.57 | n/a |
| PYTHUSDT | IDLE | 1.52 | 2.78 | 1.73 | -0.02 | 399443.6 | 2.79 | tvl≈158,727,627 |
| ZBCNUSDT | IDLE | 2.05 | 3.94 | 2.16 | -0.04 | 225616.37 | 30.97 | n/a |
| EDELUSDT | IDLE | 1.54 | 2.83 | 1.63 | 0.0 | 214626.05 | 24.65 | no_map |
| HBARUSDT | IDLE | 1.26 | 2.32 | 1.32 | -0.0 | 517008.47 | 6.6 | empty_tvl |
| BIOUSDT | IDLE | 1.78 | 3.29 | 1.74 | 0.01 | 87986.9 | 8.87 | n/a |
| KITEUSDT | IDLE | 1.23 | 2.24 | 1.41 | -0.03 | 58942.24 | 11.29 | no_map |
| REDUSDT | IDLE | 1.13 | 2.13 | 0.86 | -0.02 | 53726.19 | 9.88 | tvl≈3,765,901 |
| RIZEUSDT | IDLE | 0.97 | 1.79 | 1.06 | 0.03 | 37110.35 | 61.57 | no_map |
| FLUIDUSDT | IDLE | 1.16 | 3.48 | 2.88 | -0.0 | 6664.52 | 21.66 | tvl≈2,224,246,347 |
| RWAUSDT | IDLE | 0.63 | 1.12 | 0.87 | -0.0 | 55022.41 | 24.01 | no_map |
| MNSRYUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| IOTAUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| LAUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| WAXLUSDT | ERR | — | — | — | — | — | — | scan_deadline |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
