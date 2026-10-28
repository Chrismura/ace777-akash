# Hulk DIGEST — 2026-10-28T14:34:21Z

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
| ETHUSDT | IDLE | 1.25 | 2.21 | 1.88 | 0.0 | 237244548.36 | 0.26 | no_map |
| XRPUSDT | IDLE | 1.04 | 1.83 | 1.63 | -0.0 | 19956425.55 | 2.29 | n/a |
| BTCUSDT | IDLE | 0.83 | 1.46 | 1.31 | 0.0 | 311657361.59 | 0.0 | no_map |
| CCUSDT | WATCH_PULLBACK — tension haute + reflux | 4.44 | 9.68 | 7.09 | -0.02 | 371376.07 | 8.21 | no_map |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.52 | 12.9 | 11.38 | -0.04 | 184447.56 | 13.8 | no_map |
| RWAINCUSDT | IDLE | 4.2 | 10.56 | 3.6 | 0.06 | 44472.92 | 6.43 | no_map |
| QNTUSDT | IDLE | 3.12 | 5.52 | 4.75 | -0.03 | 465260.75 | 1.55 | n/a |
| WUSDT | IDLE | 1.53 | 2.74 | 2.16 | -0.04 | 546133.6 | 18.24 | tvl≈1,502,087,702 |
| PYTHUSDT | IDLE | 1.56 | 2.78 | 2.28 | -0.03 | 437691.17 | 5.62 | tvl≈158,727,627 |
| ZBCNUSDT | IDLE | 2.11 | 3.94 | 2.98 | -0.05 | 231886.01 | 22.92 | n/a |
| EDELUSDT | IDLE | 1.59 | 2.83 | 2.39 | -0.0 | 240688.54 | 21.7 | no_map |
| BIOUSDT | IDLE | 1.85 | 3.29 | 2.79 | 0.01 | 88142.43 | 8.97 | n/a |
| HBARUSDT | IDLE | 1.3 | 2.32 | 1.81 | -0.01 | 516070.64 | 6.64 | empty_tvl |
| KITEUSDT | IDLE | 1.27 | 2.24 | 2.03 | -0.04 | 58352.14 | 11.37 | no_map |
| REDUSDT | IDLE | 1.21 | 2.15 | 1.78 | -0.02 | 53140.04 | 15.96 | tvl≈3,765,901 |
| RIZEUSDT | IDLE | 1.01 | 1.79 | 1.53 | 0.02 | 36432.27 | 25.21 | no_map |
| FLUIDUSDT | IDLE | 1.16 | 3.48 | 2.83 | -0.0 | 6563.17 | 21.15 | tvl≈2,224,246,347 |
| RWAUSDT | ERR | — | — | — | — | — | — | scan_deadline |
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
