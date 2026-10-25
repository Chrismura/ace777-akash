# Hulk DIGEST — 2026-10-25T15:03:56Z

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
| ETHUSDT | IDLE | 0.55 | 1.08 | 0.1 | 0.0 | 121625981.83 | 0.17 | no_map |
| XRPUSDT | IDLE | 0.46 | 0.9 | 0.14 | 0.02 | 19571697.72 | 0.77 | n/a |
| BTCUSDT | IDLE | 0.36 | 0.71 | 0.03 | 0.01 | 181063782.47 | 0.09 | no_map |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 4.26 | 21.0 | 9.02 | -0.01 | 23450.21 | 21.26 | tvl≈2,178,819,407 |
| WUSDT | IDLE | 1.09 | 2.09 | 0.66 | -0.02 | 693528.56 | 23.42 | tvl≈1,502,914,601 |
| PYTHUSDT | IDLE | 1.66 | 3.27 | 0.37 | 0.06 | 466015.12 | 2.76 | tvl≈157,602,157 |
| EDELUSDT | IDLE | 1.48 | 2.96 | 0.03 | -0.02 | 453980.87 | 16.74 | no_map |
| QNTUSDT | IDLE | 2.2 | 4.31 | 0.62 | 0.06 | 423096.28 | 2.68 | n/a |
| ZBCNUSDT | IDLE | 1.59 | 3.55 | 0.54 | 0.06 | 224956.58 | 17.75 | n/a |
| CHIPUSDT | IDLE | 1.68 | 4.83 | 3.36 | 0.06 | 99990.04 | 18.11 | no_map |
| CCUSDT | IDLE | 0.93 | 1.85 | 0.05 | 0.01 | 173112.62 | 10.84 | no_map |
| REDUSDT | IDLE | 1.32 | 2.42 | 1.46 | -0.01 | 66774.14 | 16.11 | tvl≈3,604,206 |
| KITEUSDT | IDLE | 0.9 | 1.8 | 0.0 | -0.02 | 59068.78 | 11.57 | no_map |
| BIOUSDT | IDLE | 0.83 | 1.67 | 0.0 | -0.01 | 61625.0 | 8.9 | n/a |
| RIZEUSDT | IDLE | 1.14 | 2.61 | 1.67 | -0.04 | 40028.33 | 60.47 | no_map |
| RWAINCUSDT | IDLE | 0.66 | 1.21 | 0.76 | -0.01 | 58390.18 | 16.43 | no_map |
| RWAUSDT | IDLE | 1.19 | 2.17 | 1.34 | -0.0 | 50941.45 | 15.92 | no_map |
| LAUSDT | IDLE | 0.88 | 3.5 | 1.93 | -0.11 | 70858.52 | 19.35 | no_map |
| HBARUSDT | IDLE | 0.43 | 0.85 | 0.04 | 0.01 | 185397.04 | 6.49 | empty_tvl |
| IOTAUSDT | IDLE | 0.66 | 1.29 | 0.14 | 0.0 | 64354.83 | 25.61 | no_map |
| MNSRYUSDT | IDLE | 0.38 | 0.74 | 0.1 | 0.0 | 36927.05 | 77.07 | no_map |
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
